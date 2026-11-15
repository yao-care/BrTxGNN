/**
 * BrTxGNN Drug-Drug Interaction Checker
 *
 * Client-side DDI checking with 15 built-in curated rules (DDInter consulted as a reference; not a full database lookup).
 * Provides real-time interaction alerts for drug repurposing candidates.
 *
 * @author BrTxGNN Team
 * @version 1.0.0
 */
(function(global) {
  'use strict';

  const CONFIG = {
    // This site does not publish /data/ddi-index.json; only the curated rules
    // below are used. Set a URL here once such a file exists.
    ddiDataUrl: null,
    maxAlerts: 10
  };

  // Severity levels with priority (higher = more severe)
  const SEVERITY = {
    'Major': { priority: 3, class: 'ddi-major', label: 'Grave' },
    'Moderate': { priority: 2, class: 'ddi-moderate', label: 'Moderada' },
    'Minor': { priority: 1, class: 'ddi-minor', label: 'Leve' }
  };

  // 15 built-in high-priority DDI rules (hand-curated, DDInter consulted as a reference)
  // Format: { drug1: [synonym list], drug2: [synonym list], severity, summary, detail }
  const CURATED_DDI_RULES = [
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['ibuprofen', 'advil', 'motrin', 'brufen']
      ],
      severity: 'Major',
      summary: 'Varfarina + Ibuprofeno: maior risco de sangramento',
      detail: 'Os AINEs inibem a função plaquetária e podem potencializar o efeito anticoagulante da varfarina, aumentando muito o risco de sangramento gastrointestinal.',
      recommendation: 'Use paracetamol em vez disso ou associe um IBP para proteção gástrica.'
    },
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['aspirin', 'acetylsalicylic acid']
      ],
      severity: 'Major',
      summary: 'Varfarina + Ácido acetilsalicílico: maior risco de sangramento',
      detail: 'Ambos afetam a hemostasia; o uso combinado aumenta muito o risco de sangramento.',
      recommendation: 'Se a associação for necessária, use ácido acetilsalicílico em dose baixa e monitore o INR de perto.'
    },
    {
      drugs: [
        ['warfarin', 'coumadin'],
        ['naproxen', 'aleve', 'naprosyn']
      ],
      severity: 'Major',
      summary: 'Varfarina + Naproxeno: maior risco de sangramento',
      detail: 'Associar naproxeno à varfarina aumenta o risco de sangramento gastrointestinal e de outros sangramentos.',
      recommendation: 'Use paracetamol para alívio da dor em vez disso.'
    },
    {
      drugs: [
        ['metformin', 'glucophage'],
        ['iodixanol', 'visipaque', 'iopamidol', 'isovue', 'contrast']
      ],
      severity: 'Major',
      summary: 'Metformina + contrastes iodados: risco de acidose láctica',
      detail: 'Os contrastes podem causar lesão renal aguda, levando ao acúmulo de metformina e à acidose láctica.',
      recommendation: 'Suspenda a metformina 48 horas antes do procedimento e só retome após confirmar função renal normal.'
    },
    {
      drugs: [
        ['colchicine', 'colcrys'],
        ['clarithromycin', 'biaxin', 'klacid']
      ],
      severity: 'Major',
      summary: 'Colchicina + Claritromicina: risco de toxicidade',
      detail: 'A claritromicina é um inibidor potente do CYP3A4 e aumenta muito os níveis sanguíneos de colchicina.',
      recommendation: 'Evite a associação ou reduza substancialmente a dose de colchicina.'
    },
    {
      drugs: [
        ['colchicine', 'colcrys'],
        ['ritonavir', 'norvir', 'cobicistat', 'tybost']
      ],
      severity: 'Major',
      summary: 'Colchicina + inibidores da protease do HIV: risco de toxicidade grave',
      detail: 'Os inibidores da protease do HIV aumentam acentuadamente os níveis de colchicina e podem causar toxicidade fatal.',
      recommendation: 'Contraindicado em pacientes com insuficiência renal ou hepática.'
    },
    {
      drugs: [
        ['simvastatin', 'zocor'],
        ['amiodarone', 'cordarone']
      ],
      severity: 'Major',
      summary: 'Sinvastatina + Amiodarona: risco de miopatia',
      detail: 'A amiodarona aumenta os níveis de sinvastatina, elevando o risco de rabdomiólise.',
      recommendation: 'Não ultrapasse 20 mg/dia de sinvastatina ou troque por outra estatina.'
    },
    {
      drugs: [
        ['fluoxetine', 'prozac', 'sertraline', 'zoloft', 'paroxetine', 'paxil'],
        ['tramadol', 'ultram']
      ],
      severity: 'Major',
      summary: 'ISRS + Tramadol: risco de síndrome serotoninérgica',
      detail: 'Ambos aumentam a atividade serotoninérgica; o uso combinado pode causar síndrome serotoninérgica potencialmente fatal.',
      recommendation: 'Monitore de perto os sintomas (hipertermia, mioclonia, alteração do estado mental) e considere outro analgésico.'
    },
    {
      drugs: [
        ['fluoxetine', 'prozac', 'sertraline', 'zoloft', 'paroxetine', 'paxil'],
        ['linezolid', 'zyvox']
      ],
      severity: 'Major',
      summary: 'ISRS + Linezolida: risco de síndrome serotoninérgica',
      detail: 'A linezolida é um inibidor da MAO; associá-la a um ISRS é muito perigoso.',
      recommendation: 'Evite a associação. Se a linezolida for necessária, suspenda o ISRS e respeite um período de washout adequado.'
    },
    {
      drugs: [
        ['amiodarone', 'cordarone'],
        ['moxifloxacin', 'avelox']
      ],
      severity: 'Major',
      summary: 'Amiodarona + Moxifloxacino: risco de prolongamento do QT',
      detail: 'Ambos podem prolongar o intervalo QT; o uso combinado aumenta o risco de torsades de pointes.',
      recommendation: 'Evite a associação ou monitore o ECG de perto.'
    },
    {
      drugs: [
        ['digoxin', 'lanoxin'],
        ['amiodarone', 'cordarone']
      ],
      severity: 'Major',
      summary: 'Digoxina + Amiodarona: risco de toxicidade por digoxina',
      detail: 'A amiodarona aumenta os níveis sanguíneos de digoxina em cerca de 70%.',
      recommendation: 'Ao iniciar a amiodarona, reduza a dose de digoxina pela metade e monitore os níveis sanguíneos.'
    },
    {
      drugs: [
        ['clopidogrel', 'plavix'],
        ['omeprazole', 'prilosec', 'esomeprazole', 'nexium']
      ],
      severity: 'Moderate',
      summary: 'Clopidogrel + IBP: redução do efeito antiplaquetário',
      detail: 'O omeprazol inibe o CYP2C19, reduzindo a conversão do clopidogrel em seu metabólito ativo.',
      recommendation: 'Considere pantoprazol ou um antagonista H2 em vez disso.'
    },
    {
      drugs: [
        ['lithium', 'lithobid'],
        ['ibuprofen', 'advil', 'naproxen', 'aleve', 'diclofenac']
      ],
      severity: 'Major',
      summary: 'Lítio + AINEs: risco de toxicidade por lítio',
      detail: 'Os AINEs reduzem a excreção renal do lítio, elevando seus níveis sanguíneos.',
      recommendation: 'Evite a associação ou monitore de perto os níveis de lítio.'
    },
    {
      drugs: [
        ['potassium', 'k-dur', 'klor-con'],
        ['spironolactone', 'aldactone', 'eplerenone', 'inspra']
      ],
      severity: 'Major',
      summary: 'Suplementos de potássio + diuréticos poupadores de potássio: risco de hipercalemia',
      detail: 'Ambos elevam o potássio sérico; o uso combinado pode causar hipercalemia potencialmente fatal.',
      recommendation: 'Monitore regularmente o potássio sérico e evite suplementação de potássio concomitante.'
    },
    {
      drugs: [
        ['methotrexate', 'trexall'],
        ['trimethoprim', 'bactrim', 'septra', 'sulfamethoxazole']
      ],
      severity: 'Major',
      summary: 'Metotrexato + SMX-TMP: risco de supressão da medula óssea',
      detail: 'Ambos inibem o metabolismo do folato; o uso combinado aumenta o risco de supressão da medula óssea e de mucosite.',
      recommendation: 'Evite a associação ou garanta suplementação adequada de folato e monitore de perto o hemograma.'
    }
  ];

  let ddiIndex = null;
  let isLoaded = false;

  /**
   * Load DDI index data
   */
  async function loadDDIIndex() {
    if (isLoaded) return;
    if (!CONFIG.ddiDataUrl) {
      isLoaded = true;
      return;
    }

    try {
      const response = await fetch(CONFIG.ddiDataUrl);
      if (response.ok) {
        ddiIndex = await response.json();
        isLoaded = true;
        console.log('DDI index loaded:', ddiIndex?.count || 0, 'interactions');
      }
    } catch (error) {
      console.warn('DDI index not available, using curated rules only');
      isLoaded = true;
    }
  }

  /**
   * Normalize drug name for comparison
   */
  function normalizeDrugName(name) {
    if (!name) return '';
    return name.toLowerCase()
      .replace(/\s+/g, ' ')
      .replace(/[^a-z0-9\s]/g, '')
      .trim();
  }

  /**
   * Check if a drug name matches any of the synonyms
   */
  function matchesDrug(drugName, synonyms) {
    const normalized = normalizeDrugName(drugName);
    return synonyms.some(syn => {
      const normalizedSyn = normalizeDrugName(syn);
      return normalized.includes(normalizedSyn) || normalizedSyn.includes(normalized);
    });
  }

  /**
   * Check for DDI between two drugs using curated rules
   */
  function checkCuratedDDI(drug1, drug2) {
    const alerts = [];

    for (const rule of CURATED_DDI_RULES) {
      const [drugGroup1, drugGroup2] = rule.drugs;

      // Check if drug1 matches group1 and drug2 matches group2, or vice versa
      if (
        (matchesDrug(drug1, drugGroup1) && matchesDrug(drug2, drugGroup2)) ||
        (matchesDrug(drug1, drugGroup2) && matchesDrug(drug2, drugGroup1))
      ) {
        alerts.push({
          drug1: drug1,
          drug2: drug2,
          severity: rule.severity,
          severityInfo: SEVERITY[rule.severity],
          summary: rule.summary,
          detail: rule.detail,
          recommendation: rule.recommendation,
          source: 'Regras DDI internas do BrTxGNN (15 regras selecionadas; não é uma consulta completa ao DDInter)'
        });
      }
    }

    return alerts;
  }

  /**
   * Check DDI for a list of medications
   * @param {string[]} medications - Array of medication names
   * @returns {Object[]} Array of DDI alerts
   */
  function checkInteractions(medications) {
    if (!medications || medications.length < 2) {
      return [];
    }

    const allAlerts = [];
    const seen = new Set();

    // Check all pairs
    for (let i = 0; i < medications.length; i++) {
      for (let j = i + 1; j < medications.length; j++) {
        const drug1 = medications[i];
        const drug2 = medications[j];
        const pairKey = [drug1, drug2].sort().join('|');

        if (seen.has(pairKey)) continue;
        seen.add(pairKey);

        const alerts = checkCuratedDDI(drug1, drug2);
        allAlerts.push(...alerts);
      }
    }

    // Sort by severity (highest first) and limit
    return allAlerts
      .sort((a, b) => b.severityInfo.priority - a.severityInfo.priority)
      .slice(0, CONFIG.maxAlerts);
  }

  /**
   * Check if a new drug has interactions with existing medications
   * @param {string} newDrug - The new drug to check
   * @param {string[]} currentMeds - Array of current medication names
   * @returns {Object[]} Array of DDI alerts
   */
  function checkNewDrug(newDrug, currentMeds) {
    if (!newDrug || !currentMeds || currentMeds.length === 0) {
      return [];
    }

    const allAlerts = [];

    for (const currentDrug of currentMeds) {
      const alerts = checkCuratedDDI(newDrug, currentDrug);
      allAlerts.push(...alerts);
    }

    return allAlerts
      .sort((a, b) => b.severityInfo.priority - a.severityInfo.priority);
  }

  /**
   * Format alerts as HTML for display
   */
  function formatAlertsHTML(alerts) {
    if (!alerts || alerts.length === 0) {
      return '<div class="ddi-no-alerts">Nenhum alerta de interação medicamentosa encontrado</div>';
    }

    let html = '<div class="ddi-alerts">';

    alerts.forEach((alert, index) => {
      html += `
        <div class="ddi-alert ${alert.severityInfo.class}">
          <div class="ddi-alert-header">
            <span class="ddi-severity-badge">${alert.severityInfo.label}</span>
            <span class="ddi-summary">${escapeHtml(alert.summary)}</span>
          </div>
          <div class="ddi-alert-body">
            <p class="ddi-detail">${escapeHtml(alert.detail)}</p>
            <p class="ddi-recommendation"><strong>Recomendação:</strong> ${escapeHtml(alert.recommendation)}</p>
          </div>
          <div class="ddi-alert-footer">
            <span class="ddi-source">Fonte: ${escapeHtml(alert.source)}</span>
          </div>
        </div>
      `;
    });

    html += '</div>';
    return html;
  }

  /**
   * Format alerts for CDS Hooks response
   */
  function formatForCDSHooks(alerts) {
    return alerts.map((alert, index) => ({
      uuid: `ddi-alert-${index}`,
      summary: alert.summary,
      indicator: alert.severity === 'Major' ? 'critical' : alert.severity === 'Moderate' ? 'warning' : 'info',
      detail: `${alert.detail}\n\nRecomendação: ${alert.recommendation}`,
      source: {
        label: 'BrTxGNN DDI Checker',
        url: 'https://brtxgnn.yao.care/'
      }
    }));
  }

  function escapeHtml(text) {
    if (!text) return '';
    const div = document.createElement('div');
    div.textContent = text;
    return div.innerHTML;
  }

  // Export
  global.BrTxGNN = global.BrTxGNN || {};
  global.BrTxGNN.DDIChecker = {
    load: loadDDIIndex,
    checkInteractions: checkInteractions,
    checkNewDrug: checkNewDrug,
    formatAlertsHTML: formatAlertsHTML,
    formatForCDSHooks: formatForCDSHooks,
    SEVERITY: SEVERITY
  };

  // Auto-load when DOM is ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadDDIIndex);
  } else {
    loadDDIIndex();
  }

})(typeof window !== 'undefined' ? window : this);
