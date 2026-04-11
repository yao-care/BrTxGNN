/**
 * BrTxGNN SMART App Main Logic
 *
 * Handles FHIR client initialization, medication retrieval,
 * and UI rendering for drug repurposing candidates.
 */
(function(global) {
  'use strict';

  const CONFIG = {
    searchIndexUrl: '/data/search-index.json',
    drugsBaseUrl: '/drugs/',
    clinicalTrialsApiUrl: 'https://clinicaltrials.gov/api/v2/studies'
  };

  // Clinical trials cache to avoid repeated API calls
  const clinicalTrialsCache = new Map();

  // UI Elements
  let elements = {};

  // State
  let fhirClient = null;
  let drugMapper = null;
  let searchIndex = null;
  let patientMedications = [];
  let mappingResults = [];

  /**
   * Initialize the SMART App
   */
  async function init() {
    elements = {
      loading: document.getElementById('loading'),
      error: document.getElementById('error'),
      content: document.getElementById('content'),
      patientInfo: document.getElementById('patient-info'),
      medList: document.getElementById('medication-list'),
      results: document.getElementById('repurposing-results'),
      queryBtn: document.getElementById('query-btn'),
      selectAllBtn: document.getElementById('select-all-btn')
    };

    try {
      showLoading('Carregando banco de dados de medicamentos...');

      // Load search index
      searchIndex = await loadSearchIndex();

      showLoading('Conectando ao sistema EHR...');

      // Initialize FHIR client
      fhirClient = await FHIR.oauth2.ready();

      // Initialize drug mapper
      drugMapper = new BrTxGNN.DrugMapper(searchIndex);

      showLoading('Carregando dados de medicamentos do paciente...');

      // Load patient info and medications
      await loadPatientData();

      // Show main content
      showContent();

      // Setup event listeners
      setupEventListeners();

    } catch (error) {
      console.error('SMART App initialization error:', error);
      showError('Nao foi possivel inicializar o aplicativo: ' + (error.message || error));
    }
  }

  /**
   * Load BrTxGNN search index
   */
  async function loadSearchIndex() {
    const response = await fetch(CONFIG.searchIndexUrl);
    if (!response.ok) {
      throw new Error('Nao foi possivel carregar o banco de dados de medicamentos');
    }
    return response.json();
  }

  /**
   * Load patient information and medications
   */
  async function loadPatientData() {
    // Get patient info
    const patient = await fhirClient.patient.read();
    renderPatientInfo(patient);

    // Get medications (try MedicationRequest first, then MedicationStatement)
    let medications = [];

    try {
      const medRequests = await fhirClient.request(
        `MedicationRequest?patient=${fhirClient.patient.id}&status=active,completed`,
        { flat: true }
      );
      if (Array.isArray(medRequests)) {
        medications = medications.concat(medRequests);
      }
    } catch (e) {
      console.warn('Could not fetch MedicationRequest:', e);
    }

    try {
      const medStatements = await fhirClient.request(
        `MedicationStatement?patient=${fhirClient.patient.id}&status=active,completed`,
        { flat: true }
      );
      if (Array.isArray(medStatements)) {
        medications = medications.concat(medStatements);
      }
    } catch (e) {
      console.warn('Could not fetch MedicationStatement:', e);
    }

    patientMedications = medications;

    // Map medications to BrTxGNN
    mappingResults = await drugMapper.mapMedications(medications);

    // Render medication list
    renderMedicationList();
  }

  /**
   * Render patient information
   */
  function renderPatientInfo(patient) {
    if (!elements.patientInfo) return;

    const name = patient.name?.[0];
    const displayName = name ?
      `${name.family || ''}, ${name.given?.join(' ') || ''}`.trim() :
      'Desconhecido';

    const birthDate = patient.birthDate || 'Desconhecido';
    const gender = {
      'male': 'Masculino',
      'female': 'Feminino',
      'other': 'Outro',
      'unknown': 'Desconhecido'
    }[patient.gender] || patient.gender || 'Desconhecido';

    elements.patientInfo.innerHTML = `
      <div class="patient-card">
        <div class="patient-name">${escapeHtml(displayName)}</div>
        <div class="patient-details">
          <span>Data de Nascimento: ${escapeHtml(birthDate)}</span>
          <span>Sexo: ${escapeHtml(gender)}</span>
        </div>
      </div>
    `;
  }

  /**
   * Render medication list with checkboxes
   */
  function renderMedicationList() {
    if (!elements.medList) return;

    if (mappingResults.length === 0) {
      elements.medList.innerHTML = `
        <div class="empty-state">
          <p>Nenhum registro de medicamento do paciente encontrado</p>
        </div>
      `;
      return;
    }

    let html = '<div class="med-list">';

    mappingResults.forEach((result, index) => {
      const displayName = result.displayName || result.ingredientName || 'Medicamento desconhecido';
      const matchStatus = result.matched ?
        `<span class="match-badge matched">Dados de previsao disponiveis</span>` :
        `<span class="match-badge unmatched">Sem dados de previsao</span>`;

      const brtxgnnInfo = result.brtxgnnMatch ?
        `<span class="brtxgnn-name">&rarr; ${escapeHtml(result.brtxgnnMatch.name)}</span>
         <span class="level-badge level-${result.brtxgnnMatch.level}">${result.brtxgnnMatch.level}</span>` :
        '';

      html += `
        <div class="med-item ${result.matched ? 'has-match' : 'no-match'}">
          <label class="med-label">
            <input type="checkbox" class="med-checkbox" data-index="${index}"
                   ${result.matched ? 'checked' : 'disabled'}>
            <span class="med-name">${escapeHtml(displayName)}</span>
            ${matchStatus}
          </label>
          <div class="med-mapping">
            ${brtxgnnInfo}
          </div>
        </div>
      `;
    });

    html += '</div>';
    elements.medList.innerHTML = html;
  }

  /**
   * Query repurposing candidates for selected medications
   */
  function queryRepurposingCandidates() {
    const checkboxes = document.querySelectorAll('.med-checkbox:checked');
    const selectedIndices = Array.from(checkboxes).map(cb => parseInt(cb.dataset.index));

    if (selectedIndices.length === 0) {
      elements.results.innerHTML = `
        <div class="empty-state">
          <p>Selecione pelo menos um medicamento</p>
        </div>
      `;
      return;
    }

    let html = '';

    selectedIndices.forEach(index => {
      const result = mappingResults[index];
      if (!result.brtxgnnMatch) return;

      const drug = result.brtxgnnMatch;
      const indications = drug.indications || [];

      html += `
        <div class="drug-result-card">
          <div class="drug-header">
            <h3>
              <a href="${CONFIG.drugsBaseUrl}${drug.slug}/" target="_blank">
                ${escapeHtml(drug.name)}
              </a>
              <span class="level-badge level-${drug.level}">${drug.level}</span>
            </h3>
            <a href="${CONFIG.drugsBaseUrl}${drug.slug}/" target="_blank" class="view-full">
              Ver Detalhes &rarr;
            </a>
          </div>

          <div class="drug-original">
            <strong>Indicacao original:</strong>
            ${escapeHtml(drug.original) || '&mdash;'}
          </div>

          <div class="drug-indications">
            <strong>Nova Indicacao Prevista (Candidatos ao Reposicionamento):</strong>
            <div class="indication-list">
      `;

      if (indications.length > 0) {
        indications.slice(0, 10).forEach((ind, indIndex) => {
          const trialsContainerId = `trials-${drug.slug}-${indIndex}`;
          html += `
            <div class="indication-item">
              <div class="indication-header">
                <span class="level-badge level-${ind.level}">${ind.level}</span>
                <span class="ind-name">${escapeHtml(ind.name)}</span>
                <span class="ind-score">${ind.score}%</span>
                <button class="trials-btn" onclick="BrTxGNN.SmartApp.loadTrials('${escapeHtml(drug.name)}', '${escapeHtml(ind.name)}', '${trialsContainerId}')">
                  Ensaios Clinicos
                </button>
              </div>
              <div class="trials-container" id="${trialsContainerId}"></div>
            </div>
          `;
        });

        if (indications.length > 10) {
          html += `
            <div class="more-indications">
              ...e mais ${indications.length - 10} indicacoes previstas
              <a href="${CONFIG.drugsBaseUrl}${drug.slug}/" target="_blank">Ver todas</a>
            </div>
          `;
        }
      } else {
        html += '<p class="no-indications">Nenhuma nova indicacao prevista</p>';
      }

      html += `
            </div>
          </div>
        </div>
      `;
    });

    if (!html) {
      html = `
        <div class="empty-state">
          <p>Os medicamentos selecionados nao possuem dados de previsao</p>
        </div>
      `;
    }

    elements.results.innerHTML = html;
  }

  /**
   * Setup event listeners
   */
  function setupEventListeners() {
    if (elements.queryBtn) {
      elements.queryBtn.addEventListener('click', queryRepurposingCandidates);
    }

    if (elements.selectAllBtn) {
      elements.selectAllBtn.addEventListener('click', function() {
        const checkboxes = document.querySelectorAll('.med-checkbox:not(:disabled)');
        const allChecked = Array.from(checkboxes).every(cb => cb.checked);

        checkboxes.forEach(cb => {
          cb.checked = !allChecked;
        });
      });
    }
  }

  // UI Helper functions
  function showLoading(message) {
    if (elements.loading) {
      elements.loading.style.display = 'flex';
      elements.loading.querySelector('.loading-text').textContent = message || 'Carregando...';
    }
    if (elements.error) elements.error.style.display = 'none';
    if (elements.content) elements.content.style.display = 'none';
  }

  function showError(message) {
    if (elements.loading) elements.loading.style.display = 'none';
    if (elements.error) {
      elements.error.style.display = 'block';
      elements.error.querySelector('.error-message').textContent = message;
    }
    if (elements.content) elements.content.style.display = 'none';
  }

  function showContent() {
    if (elements.loading) elements.loading.style.display = 'none';
    if (elements.error) elements.error.style.display = 'none';
    if (elements.content) elements.content.style.display = 'block';
  }

  function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  /**
   * Search ClinicalTrials.gov for drug + condition trials
   * @param {string} drugName - Drug name
   * @param {string} condition - Disease/condition name
   * @returns {Promise<Object>} Trial results with count and trials array
   */
  async function searchClinicalTrials(drugName, condition) {
    const cacheKey = `${drugName.toLowerCase()}|${condition.toLowerCase()}`;

    // Return cached result if available
    if (clinicalTrialsCache.has(cacheKey)) {
      return clinicalTrialsCache.get(cacheKey);
    }

    try {
      const params = new URLSearchParams({
        'query.intr': drugName,
        'query.cond': condition,
        'pageSize': '5',
        'format': 'json',
        'countTotal': 'true'
      });

      const response = await fetch(`${CONFIG.clinicalTrialsApiUrl}?${params}`);

      if (!response.ok) {
        console.warn('ClinicalTrials.gov API error:', response.status);
        return { totalCount: 0, trials: [] };
      }

      const data = await response.json();

      const result = {
        totalCount: data.totalCount || 0,
        trials: (data.studies || []).slice(0, 5).map(study => ({
          nctId: study.protocolSection?.identificationModule?.nctId,
          title: study.protocolSection?.identificationModule?.briefTitle,
          status: study.protocolSection?.statusModule?.overallStatus,
          phase: study.protocolSection?.designModule?.phases?.join(', ') || 'N/A',
          enrollment: study.protocolSection?.designModule?.enrollmentInfo?.count,
          url: `https://clinicaltrials.gov/study/${study.protocolSection?.identificationModule?.nctId}`
        }))
      };

      // Cache the result
      clinicalTrialsCache.set(cacheKey, result);

      return result;
    } catch (error) {
      console.warn('Failed to fetch clinical trials:', error);
      return { totalCount: 0, trials: [] };
    }
  }

  /**
   * Render clinical trials section for an indication
   * @param {string} drugName - Drug name
   * @param {string} indicationName - Indication name
   * @param {string} containerId - Container element ID
   */
  async function loadClinicalTrials(drugName, indicationName, containerId) {
    const container = document.getElementById(containerId);
    if (!container) return;

    container.innerHTML = '<span class="trials-loading">Pesquisando ensaios clinicos...</span>';

    const result = await searchClinicalTrials(drugName, indicationName);

    if (result.totalCount === 0) {
      container.innerHTML = '<span class="trials-none">Nenhum ensaio clinico relacionado encontrado</span>';
      return;
    }

    let html = `
      <div class="trials-summary">
        <strong>${result.totalCount}</strong> ensaios clinicos relacionados encontrados
      </div>
      <div class="trials-list">
    `;

    result.trials.forEach(trial => {
      const statusClass = getTrialStatusClass(trial.status);
      html += `
        <div class="trial-item">
          <a href="${trial.url}" target="_blank" class="trial-nct">${trial.nctId}</a>
          <span class="trial-status ${statusClass}">${formatTrialStatus(trial.status)}</span>
          <span class="trial-phase">${trial.phase}</span>
          <div class="trial-title">${escapeHtml(trial.title)}</div>
        </div>
      `;
    });

    if (result.totalCount > 5) {
      const searchUrl = `https://clinicaltrials.gov/search?cond=${encodeURIComponent(indicationName)}&intr=${encodeURIComponent(drugName)}`;
      html += `
        <a href="${searchUrl}" target="_blank" class="trials-more">
          Ver todos os ${result.totalCount} ensaios clinicos &rarr;
        </a>
      `;
    }

    html += '</div>';
    container.innerHTML = html;
  }

  /**
   * Get CSS class for trial status
   */
  function getTrialStatusClass(status) {
    const statusMap = {
      'RECRUITING': 'status-recruiting',
      'ACTIVE_NOT_RECRUITING': 'status-active',
      'COMPLETED': 'status-completed',
      'TERMINATED': 'status-terminated',
      'NOT_YET_RECRUITING': 'status-pending'
    };
    return statusMap[status] || 'status-unknown';
  }

  /**
   * Format trial status for display
   */
  function formatTrialStatus(status) {
    const statusMap = {
      'RECRUITING': 'Recrutando',
      'ACTIVE_NOT_RECRUITING': 'Em andamento',
      'COMPLETED': 'Concluido',
      'TERMINATED': 'Encerrado',
      'NOT_YET_RECRUITING': 'Ainda nao recrutando',
      'SUSPENDED': 'Suspenso',
      'WITHDRAWN': 'Retirado',
      'ENROLLING_BY_INVITATION': 'Por convite'
    };
    return statusMap[status] || status;
  }

  // Export
  global.BrTxGNN = global.BrTxGNN || {};
  global.BrTxGNN.SmartApp = {
    init: init,
    loadTrials: loadClinicalTrials,
    searchTrials: searchClinicalTrials
  };

  // Auto-initialize when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }

})(typeof window !== 'undefined' ? window : this);
