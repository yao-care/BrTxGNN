# TxGNN 國際化 SOP - 從初始化包建立地區藥品老藥新用預測系統

## 目標

將此初始化包轉換為您國家的藥品老藥新用預測系統。

**使用方式**：
1. 解壓縮 TxGNN_init.zip
2. 閱讀本文件，按照階段化流程執行
3. 將 `.template` 檔案改名並填入當地資訊
4. 執行預測流程

---

## 一、元件分類總覽

### 1.1 通用元件（直接使用，約 60-70%）

| 類別 | 檔案 | 說明 |
|------|------|------|
| **TxGNN 知識圖譜** | `data/node.csv`, `data/kg.csv` | 知識圖譜基礎資料（需下載） |
| **詞彙表提取** | `scripts/prepare_external_data.py` | 從 TxGNN 提取 DrugBank/疾病詞彙 |
| **藥名正規化** | `src/txgnn/mapping/normalizer.py` | 通用藥名標準化 |
| **DrugBank 映射** | `src/txgnn/mapping/drugbank_mapper.py` | 成分 → DrugBank ID |
| **KG 預測** | `src/txgnn/predict/repurposing.py` | 知識圖譜方法 |
| **DL 預測** | `src/txgnn/predict/txgnn_model.py` | 深度學習方法 |
| **通用收集器** | `collectors/clinicaltrials.py`, `pubmed.py`, `drugbank.py`, `ictrp.py` | 全球資料來源 |
| **收集器基類** | `src/txgnn/collectors/base.py` | 收集器介面 |

### 1.2 需在地化元件（約 30-40%）

| 類別 | 模板檔案 | 需修改內容 |
|------|----------|------------|
| **專案設定** | `pyproject.toml.template` | 專案名稱 |
| **欄位映射** | `config/fields.yaml.template` | 藥監局資料欄位對應 |
| **資料載入** | `src/txgnn/data/loader.py.template` | 載入邏輯 |
| **疾病映射** | `src/txgnn/mapping/disease_mapper.py.template` | DISEASE_DICT（當地語言→英文） |
| **資料處理** | `scripts/process_fda_data.py.template` | ZIP/JSON 解析 |
| **預測腳本** | `scripts/run_kg_prediction.py.template` | 微調欄位名稱 |
| **FHIR 生成** | `scripts/generate_fhir_resources.py.template` | URL 和管轄區域 |
| **新聞同義詞** | `data/news/synonyms.json.template` | 疾病/藥物同義詞 |
| **網站設定** | `docs/_config.yml.template` | 標題、URL |
| **SMART App** | `docs/smart/launch.html.template` | Client ID |
| **CI/CD** | `.github/workflows/pages.yml.template` | 部署設定 |

---

## 二、階段化實施流程

### Phase 0：專案初始化

**目標**：設定專案基礎

#### 步驟：

1. **重新命名專案**
   ```bash
   # 建議命名：{Country}TxGNN
   # 例：JpTxGNN, KrTxGNN, ThTxGNN
   mv TxGNN_init {Country}TxGNN
   cd {Country}TxGNN
   ```

2. **設定 pyproject.toml**
   ```bash
   mv pyproject.toml.template pyproject.toml
   # 編輯 pyproject.toml，修改 name 和 description
   ```

3. **下載 TxGNN 資料**
   ```bash
   mkdir -p data
   curl -L -o data/node.csv "https://dataverse.harvard.edu/api/access/datafile/7144482"
   curl -L -o data/kg.csv "https://dataverse.harvard.edu/api/access/datafile/7144484"
   ```

4. **安裝依賴**
   ```bash
   uv sync
   ```

**品質檢查點**：
- [ ] 專案已重新命名
- [ ] `pyproject.toml` 已修改
- [ ] `uv sync` 執行成功
- [ ] TxGNN 資料下載完成（node.csv ~15MB, kg.csv ~500MB）

---

### Phase 1：FDA 資料整合

**目標**：整合當地藥監局資料

#### 1.1 調查資料來源

常見藥監局資料來源：

| 國家 | 藥監局 | 資料來源 |
|------|--------|----------|
| 日本 | PMDA | https://www.pmda.go.jp/ |
| 韓國 | MFDS | https://nedrug.mfds.go.kr/ |
| 泰國 | Thai FDA | https://www.fda.moph.go.th/ |

**產出**：記錄資料來源 URL、格式、欄位說明

#### 1.2 建立欄位映射設定

```bash
mv config/fields.yaml.template config/fields.yaml
# 編輯 fields.yaml，填入欄位對應
```

**fields.yaml 範例（日本 PMDA）**：
```yaml
country_code: JP
language: ja
regulatory_agency: PMDA

field_mapping:
  license_id: "承認番号"
  brand_name_local: "販売名"
  brand_name_en: "一般名"
  ingredients: "有効成分"
  indication: "効能・効果"
  dosage_form: "剤形"
  status: "承認状況"

withdrawn_statuses:
  - "取消"
  - "回収"
```

#### 1.3 實作資料載入器

```bash
mv src/txgnn/data/loader.py.template src/txgnn/data/loader.py
# 編輯 loader.py，實作載入邏輯
```

#### 1.4 實作資料處理腳本

```bash
mv scripts/process_fda_data.py.template scripts/process_fda_data.py
# 編輯並執行
uv run python scripts/process_fda_data.py
```

**品質檢查點**：
- [ ] `config/fields.yaml` 建立完成
- [ ] `loader.py` 能正確載入資料
- [ ] `process_fda_data.py` 執行成功
- [ ] `data/raw/{country}_fda_drugs.json` 產生

---

### Phase 2：疾病映射

**目標**：建立當地語言 → 英文疾病對照

#### 2.1 建立 DISEASE_DICT

```bash
mv src/txgnn/mapping/disease_mapper.py.template src/txgnn/mapping/disease_mapper.py
# 編輯 disease_mapper.py，填入 DISEASE_DICT
```

**目標數量**：150-200 個疾病詞條

**分類建議**：

| 分類 | 建議數量 |
|------|----------|
| 心血管系統 | 15-20 |
| 呼吸系統 | 10-15 |
| 消化系統 | 15-20 |
| 神經系統 | 10-15 |
| 精神疾病 | 8-12 |
| 內分泌系統 | 10-15 |
| 肌肉骨骼 | 10-15 |
| 皮膚疾病 | 10-15 |
| 泌尿系統 | 8-12 |
| 眼科 | 5-8 |
| 耳鼻喉 | 5-8 |
| 感染症 | 10-15 |
| 過敏 | 5-8 |
| 婦科 | 8-12 |
| 腫瘤/癌症 | 10-15 |
| 一般症狀 | 15-20 |

#### 2.2 建立新聞同義詞

```bash
mv data/news/synonyms.json.template data/news/synonyms.json
# 編輯 synonyms.json，填入當地語言同義詞
```

**品質檢查點**：
- [ ] DISEASE_DICT 有 150+ 詞條
- [ ] 涵蓋所有主要疾病分類
- [ ] `synonyms.json` 建立完成

---

### Phase 3：KG 預測流程

**目標**：執行知識圖譜預測

#### 執行步驟：

```bash
# 1. 準備詞彙表
uv run python scripts/prepare_external_data.py

# 2. 設定預測腳本
mv scripts/run_kg_prediction.py.template scripts/run_kg_prediction.py
# 編輯並執行

# 3. 執行預測
uv run python scripts/run_kg_prediction.py
```

#### 預期產出：

| 檔案 | 預期內容 |
|------|----------|
| `data/external/drugbank_vocab.csv` | ~7,958 個藥物 |
| `data/external/disease_vocab.csv` | ~17,081 個疾病 |
| `data/external/drug_disease_relations.csv` | ~80,127 個關係 |
| `data/processed/repurposing_candidates.csv` | 視藥品數量而定 |

**品質檢查點**：
- [ ] 詞彙表正確產生
- [ ] `repurposing_candidates.csv` 產生
- [ ] DrugBank 映射率 > 30%
- [ ] 疾病映射率 > 20%

---

### Phase 4：網站與 FHIR

**目標**：部署文件網站與 FHIR API

#### 4.1 Jekyll 設定

```bash
mv docs/_config.yml.template docs/_config.yml
# 編輯 _config.yml，修改標題、URL、語言
```

#### 4.2 FHIR 資源設定

```bash
mv scripts/generate_fhir_resources.py.template scripts/generate_fhir_resources.py
# 編輯 BASE_URL 和 JURISDICTION
uv run python scripts/generate_fhir_resources.py
```

#### 4.3 SMART App 設定

```bash
mv docs/smart/launch.html.template docs/smart/launch.html
# 編輯 CLIENT_ID
```

#### 4.4 本地測試

```bash
cd docs
bundle install
bundle exec jekyll serve
# 訪問 http://localhost:4000
```

**品質檢查點**：
- [ ] Jekyll 本地建置成功
- [ ] `/fhir/metadata` 可存取
- [ ] FHIR 資源正確產生

---

### Phase 5：證據收集

**目標**：設定證據收集器

#### 5.1 建立當地 FDA 收集器

建立 `src/txgnn/collectors/{country}fda.py`：

```python
from .base import BaseCollector, CollectorResult

class {Country}FDACollector(BaseCollector):
    source_name = "{country}fda"

    def search(self, drug: str, disease: str | None = None) -> CollectorResult:
        # 實作搜尋邏輯
        pass
```

#### 5.2 區域臨床試驗註冊

ICTRP 涵蓋的區域註冊：
- 日本：JPRN (UMIN-CTR, JapicCTI)
- 韓國：CRIS
- 泰國：TCTR

**品質檢查點**：
- [ ] 當地 FDA 收集器建立
- [ ] ClinicalTrials.gov 收集器正常
- [ ] PubMed 收集器正常

---

### Phase 6：新聞監測

**目標**：設定健康新聞監測

#### 6.1 設定關鍵字模式

建立 `scripts/generate_news_keywords.py`，參考 TwTxGNN 版本。

#### 6.2 新增當地新聞來源

建立 `scripts/fetchers/{country}_news.py`

**品質檢查點**：
- [ ] `keywords.json` 產生
- [ ] 新聞爬蟲正常運作

---

### Phase 7：驗證與部署

**目標**：端對端驗證並部署

#### 7.1 設定 GitHub Actions

```bash
mv .github/workflows/pages.yml.template .github/workflows/pages.yml
# 編輯部署設定
```

#### 7.2 完整流程測試

```bash
uv run python scripts/process_fda_data.py
uv run python scripts/prepare_external_data.py
uv run python scripts/run_kg_prediction.py
uv run python scripts/generate_fhir_resources.py
```

#### 7.3 品質指標

| 指標 | 台灣參考值 | 目標 |
|------|-----------|------|
| FDA 藥品總數 | 71,552 | 記錄 |
| 有效藥品比例 | 33% | > 20% |
| DrugBank 映射率 | 73.87% | > 50% |
| 疾病映射率 | 44.85% | > 30% |
| 預測候選數 | 142,328 | 記錄 |

**品質檢查點**：
- [ ] 端對端流程通過
- [ ] GitHub Pages 部署成功
- [ ] SMART App 可從 SMART Launcher 啟動

---

## 三、關鍵檔案詳解

### 3.1 `config/fields.yaml`

欄位映射設定檔，定義藥監局資料欄位與標準欄位的對應關係。

### 3.2 `src/txgnn/data/loader.py`

資料載入器，根據 `fields.yaml` 載入並過濾藥品資料。

### 3.3 `src/txgnn/mapping/disease_mapper.py`

疾病映射模組，包含 `DISEASE_DICT`（當地語言→英文對照表）。

### 3.4 `scripts/process_fda_data.py`

資料處理腳本，將原始資料轉換為標準 JSON 格式。

---

## 四、GitHub Actions 設定

### 需設定的 Workflow：

| Workflow | 功能 | 需修改 |
|----------|------|--------|
| `pages.yml` | Jekyll 部署 | URL |
| `link-check.yml` | 連結檢查 | 無 |
| `check-new-evidence.yml` | 證據檢查 | 無 |

### 需設定的 Secrets：

| Secret | 用途 |
|--------|------|
| `GITHUB_TOKEN` | 自動提供 |
| `NCBI_API_KEY` | PubMed API（可選，提高速率限制） |

---

## 五、驗證清單

### 總體完成檢查

- [ ] Phase 0：專案初始化完成
- [ ] Phase 1：FDA 資料整合完成
- [ ] Phase 2：疾病映射完成
- [ ] Phase 3：KG 預測完成
- [ ] Phase 4：網站與 FHIR 完成
- [ ] Phase 5：證據收集完成
- [ ] Phase 6：新聞監測完成
- [ ] Phase 7：驗證與部署完成

### YMYL 檢查（醫療內容必檢）

- [ ] 免責聲明：「僅供研究參考，不構成醫療建議」
- [ ] 預測結果標註：「需經臨床驗證」
- [ ] 資料來源標註完整

---

## 六、附錄：區域特殊考量

### 日本 (PMDA)
- 資料格式：可能有 Shift-JIS 編碼
- 藥名：漢字/平假名/片假名混用
- 臨床試驗：JPRN (UMIN-CTR, JapicCTI, JMACCT)

### 韓國 (MFDS)
- 資料格式：UTF-8
- 藥名：韓文 + 英文音譯
- 臨床試驗：CRIS

### 泰國 (Thai FDA)
- 資料格式：UTF-8
- 藥名：泰文 + 英文
- 臨床試驗：TCTR

### 常見挑戰

1. **成分名稱變異**：同一藥物可能有不同鹽類形式
2. **品牌名映射**：當地品牌名需對應到國際名稱
3. **適應症文字解析**：不同語言的標點符號慣例不同
4. **日期格式**：各地區日期格式不同
5. **狀態碼**：有效/註銷的術語不同

---

## 常用命令

```bash
# 安裝依賴
uv sync

# 處理 FDA 資料
uv run python scripts/process_fda_data.py

# 準備詞彙表資料
uv run python scripts/prepare_external_data.py

# 執行知識圖譜預測
uv run python scripts/run_kg_prediction.py

# 生成 FHIR 資源
uv run python scripts/generate_fhir_resources.py

# 本地測試網站
cd docs && bundle exec jekyll serve

# 執行測試
uv run pytest tests/ -v
```

---

## 注意事項

- 本專案結果僅供研究參考，不構成醫療建議
- 老藥新用候選需經過臨床驗證才能應用
- 所有網站頁面需包含 YMYL 免責聲明

---

## 藥物頁查核機制（2026-11-12 起）

用戶 2026-11-12 決定：30 站各有自己的查核機制，核心流程比照 TwTxGNN（Tw 的 CLAUDE.md「藥物頁人工查核紀錄」兩節）與 UsTxGNN（第一個試做站）。
本站的規則與程式都在本 repo，頁面上的查核框與查核紀錄表用葡萄牙文，依據是 ANVISA 藥品開放資料（DADOS_ABERTOS_MEDICAMENTOS）；在地字樣集中在 `src/brtxgnn/regulatory/site_config.py`。

| 環節 | 本站檔案 | 說明 |
|------|----------|------|
| 查核紀錄 | `docs/_data/drug_reviews.json` | 單一真實來源，欄位同 Tw（correct／annotate／rereview／rereview_result／header_level／description_level、history、status） |
| 套用 | `scripts/apply_drug_reviews.py` | 套到 `docs/_drugs/*.md`：查核框 `<!-- review:begin id -->`、免責聲明前的查核紀錄表；可重複執行；`--check` 只檢查、`--touch` 連 last_modified_at 一起改 |
| 頁首等級 | `src/brtxgnn/regulatory/page_format.py` | 頁首＝Quick Overview 等級格的**第一個**等級（主預測）；這是本站產線原本的行為（2026-11-12 實測，見 site_config 的 HEADER_RULE_NOTE），不照 Tw 整格取最高。頁首 N/A 且沒有預測的頁不重算 |
| 撤回預測 | `src/brtxgnn/regulatory/withdrawn.py` | verdict=withdraw 的預測不進證據監測（`scripts/extract_drug_list.py`）、搜尋索引與 FHIR（母目錄 `.claude/rebuild_search_index.py`、`.claude/sync_fhir_levels.py` 會讀本站這支） |
| 許可證 | `snapshots/br_licenses.json.gz`、`scripts/build_license_snapshot.py`、`src/brtxgnn/regulatory/licenses.py` | 本站沒有程式產生的許可證表；gate 依快照驗市場段落表格的號碼屬於本藥、狀態列與張數列＝事實層、表格列狀態不跟事實相反 |
| 刪改轉紀錄 | `scripts/reviews_from_edits.py` | 依 git 前後版本（或改寫前後目錄）把正文刪改轉成 correct 紀錄；site_config 的 COMMITS／REGEN_COMMITS 是 2026-10-31～11-06 的刪改與 AI 重產提交 |
| 待查清單 | `docs/_data/drug_reviews_uncertain.json`、`scripts/check_original_indications.py` | 原適應症交叉驗證，只列待查、不改頁面 |
| gate | `scripts/check_seo_docs.py` 第 19–22 項 | 紀錄都已套用、許可證＝快照、頁首＝主預測等級、撤回預測沒有對外發布 |

原則（同 Tw）：基本事實照主管機關資料更正；模型預測原文不刪不改寫，只加註；證據等級與決策只經重審（rereview → rereview_result）變更。

改頁之後要跑：

```bash
python3 scripts/apply_drug_reviews.py          # 重套查核紀錄（sync_notes_to_docs.py、每週許可證排程結尾都會自動跑）
python3 scripts/build_license_snapshot.py --ws <工作目錄>   # 證據包或事實層變了才要（每週排程會自動跑）
python3 scripts/check_seo_docs.py              # 必須 exit 0
```

2026-10-31～11-06 正文裡跟許可證事實矛盾、直接刪掉的子句，2026-11-12 已用 `scripts/reviews_from_edits.py --git` 轉成 587 筆紀錄（346 頁；
其中 2 筆因報告在 11 月經 AI 重產、原句已不在頁面，標 resolved_by_regeneration）。

本站另外三件事（2026-11-12）：
- `config/license_own_extra.json`：15 個登記號 ANVISA 的 PRINCIPIO_ATIVO 欄空白、產品名就是本藥（或其鹽類），證據包依 PRINCIPIO_ATIVO 比對所以沒收，
  但 10-31 依成分全量重建許可證表時進了頁面；`scripts/build_license_snapshot.py` 把它們併進快照的本藥號碼，每筆附依據。要加新的，先在 ANVISA 資料查到同樣的條件。
- ganciclovir 頁的許可證表原本收了 4 筆 valganciclovir（另一個藥）的登記，用 2 筆 correct 紀錄刪掉（`br-lic-20261112-ganciclovir-*`）。
- bedaquilina_fumarate：11-06 的刪句在「2.」處切斷、留下未閉合的粗體「**2.」；紀錄改成整項刪除，前版存在 history。
`site_config.PROGRAM_LINE_RE` 排除程式產生的「A tabela mostra até 30 registros…」一行（轉紀錄與驗證時不當成正文）。
- 2026-11-12 正文許可證張數對事實層掃描：28 頁 30 筆 correct 紀錄（`br-lic-20261112-*`）把 AI 正文依 10-31 前舊證據包（最多 20 筆）寫的市場事實張數改成事實層（例：metamizole「20 張全部有效」→496 張中 171 張有效、mirtazapine「20 張全部註銷」→36 張中 30 張有效）；錨在被更正句上的 6 筆舊紀錄改錨，前版存 history。
  講證據包／流程的句子（「O Evidence Pack retornou N registros」、待辦「Recuperar os detalhes dos N registros」）與「pelo menos／lista parcial／5 de N」之類的顯示說明不改。
- 2026-11-12 許可證表格列狀態對事實層（母目錄 check_drug_page.py --row-status）：26 頁 56 列 ANVISA 現行有效（Ativo）的登記在號碼格、類別格或狀態欄標成 cancelado，以 56 筆 `br-row-20261112-*` correct 紀錄更正（拿掉「(cancelado)」、狀態欄改「Ativo」；依證據包 data-20261105 原始狀態逐列確認）。
- 2026-11-12 顯示說明的列數與總數：12 頁「Principais registros (5 de 20)」「Exibidos os 5 primeiros de N」之類句子的列數／總數是舊證據包的數字（現在程式表列到 30 筆），以 `br-lic-20261112-*` 照表格列數與事實層總數更正；fluconazole、ketoprofen 是 11-06 紀錄同 id 重發（前版存 history）。講證據包／流程的句子不改。

## 同一 DrugBank ID 的重複公開頁改轉址（2026-11-19）

用戶 2026-11-19 決定（照 ARTxGNN 同日做法）：公開藥物頁（非 noindex、非轉址）同一 DrugBank ID（front matter drugbank_id，沒有的用證據包 drug.drugbank_id 推斷）、預測相同的，留一頁、另一頁改轉址（layout: id_redirect、permalink 不變、sitemap: false、search_exclude、nav_exclude）。
只轉「被轉址頁的許可證號是保留頁的子集」的組（不丟市場資料）、保留頁等級不低於被轉址頁；保留順序：許可證涵蓋→查核紀錄數→字數（差 5% 內算平手）→葡文 INN 名。
轉了 7 頁：levonorgestrel_micronizado→levonorgestrel（9 張⊂95 張；保留頁 L2）、amlodipina_besylate→amlodipine_besylate、amilorida_hydrochloride→amilorida（5⊂21 張）、albuterol、albuterol_sulfate→salbutamol（15⊂98 張）、levofloxacin→levofloxacina（levofloxacin_hemihydrate 轉址改直接指 levofloxacina）、paliperidona_palmitate→paliperidona。
被轉址頁的查核紀錄（amilorida_hydrochloride 3 筆、albuterol 1、albuterol_sulfate 1，全是 resolved_by_regeneration）照本站慣例留在 drug_reviews.json 當歷史（apply_drug_reviews 跳過轉址頁），保留頁沒有同樣的錯句。
沒轉（許可證不是子集，要人工決定）：DB00125 arginine（73 張、L4）／arginine_aspartate、arginine_glutamate（各 18 張、各有 3 張不在 arginine）；DB00134 levometionina（46 張）／methionine（20 張，10 張不在 levometionina）。
公開藥物頁 575→568；FHIR 被轉址頁自己的 MK 由 sync_fhir_levels 當重複刪（MK 575→568、CUD 3014→2961）；衍生檔、hreflang 照重產。
2026-11-19 同日（用戶決定「合併後轉址」）：上面沒轉的 2 組改成先合併許可證再轉址。判斷：drug_mapping.csv 把 ARGININE ASPARTATE／ARGININE GLUTAMATE（drugbank_synonym）、DL-METIONINA、L-METIONINA、LEVOMETIONINA 都對到同一個 DrugBank ID，預測相同，照本站鹽類頁慣例（amilorida_hydrochloride→amilorida）算同一個藥。
`scripts/merge_duplicate_bundles.py`（MERGES 表）把被轉址頁證據包的登記號＋drug_mapping 同一 ID 的登記號（原收集器 brfda 的規則，不放寬）併進保留頁證據包，新紀錄照依成分重建的格式（欄位取 data/raw/anvisa_medicamentos.csv、狀態取 anvisa_situacao.json），記 source、merged_from、added，total_matches＝紀錄數；只加不刪、可重複執行，license-refresh.yml 在排程前先跑；母目錄 br_rebuild_by_ingredient 重建（會整批換掉 records）後要再跑一次。
arginine 73→76 張（有效 24→27；補 REFORGAN 156510039、NEPHROTECT 100410131、PRIMENE 106830098），arginine_aspartate、arginine_glutamate→arginine；levometionina 46→57 張（有效 10→21；methionine 證據包的 10 張＋兩頁都因 20 筆上限沒收的 100419935 AMINOVEN），methionine→levometionina。
arginine 的許可證表照 br_rebuild_by_ingredient --tables 重排、狀態列／張數列由 sync_market_rows 同步；正文張數以 `br-lic-20261112-arginine-1`、`-2` 同 id 重發（前版存 history）與 `br-lic-20261119-levometionina-1` 更正。被轉址頁沒有查核紀錄。公開藥物頁 568→565；被轉址頁的 MK 由 sync_fhir_levels 當重複刪（MK 568→565、CUD 2961→2949）；衍生檔、hreflang 照重產。
2026-11-19 同日補（用戶決定「補進來」）：沒有藥物頁的證據包 l-arginina、l-metionina、dl-metionina 是 10-31 依成分以「l-arginina」等寫法重建的，保留頁依整詞 arginina／levometionina 重建認不到 l-／dl- 前綴，所以少收；drug_mapping.csv 把 L-ARGININA 對到 DB00125、L-METIONINA 與 DL-METIONINA（外消旋體，本站對照如此，同 methionine）對到 DB00134，只把這 3 個證據包加進 MERGES（不放寬一般成分比對；這 3 個證據包不刪）。arginine 76→94 張（補 18 張，全部 Inativo，有效仍 27；表格照 --tables 重排，重排會重複插一行「A tabela mostra até 30…」，已刪掉多的那行）、levometionina 57→88 張（l-metionina 15、dl-metionina 16，全部 Inativo，有效仍 21）；正文張數以 `br-lic-20261112-arginine-1`、`-2`、`br-lic-20261119-levometionina-1` 同 id 重發（前版存 history）；有效張數沒變，「principalmente soluções de nutrição parenteral…」（講有效登記，21 張中 16 張是靜脈營養）當時判為仍成立、未改；同日用戶決定照實改寫：逐張對照證據包（Release data-20261119-102658），21 張有效登記＝靜脈營養液 16、甲硫胺酸＋膽鹼＋甜菜鹼複方 3（ABCLER ABNAT、EPOCLER、FIGZ）、維生素礦物質（含人參）複方 1（NATUS GERIN）、眼用 1（REGENCEL；開放資料沒有劑型欄），全部複方，以 `br-lic-20261119-levometionina-2` 把括號裡的分類改成實際張數、`-3` 把「下一步」的「os registros ativos são de nutrição parenteral」改成「em sua maioria (16 de 21)」；「nenhum registro … isolada」與開頭「diversas soluções de nutrição parenteral e … associações vitamínicas e hepáticas」仍成立，不改。

## 作用機轉段的資料來源與查核機制（2026-11-19）

用戶 2026-11-19 決定把 NZTxGNN 同日的作法推到各站（seo-ops 轉交：搜「<藥名> mechanism of action」落在藥物頁排名 30–99，因為頁面寫「作用機轉資料不可得」）。
2026-11-19 量測：本站公開藥物頁（排除 noindex、轉址頁）有 493 頁在正文章節寫這種句子（證據包 drugbank.source＝vocab_only、沒有作用機轉文字，AI 照實寫「沒有資料」；本站最常見的寫法：「Atualmente, não há dados detalhados sobre o mecanismo de ação nos dados compilados para este relatório.」）。
作用機轉是藥物本身的基本藥理事實、不是模型預測，所以照查核機制補：每段都節錄官方仿單或資料庫原文、附可點的出處與取用日期，不自己寫。

- 來源（理由同 NZTxGNN/CLAUDE.md 同名一節）：美國 FDA 核准仿單（openFDA drug label，連結到 NLM DailyMed 同一份 SPL setid；FDA 仿單是美國政府公開資料），美國沒有仿單時用 ChEMBL drug mechanism 表（CC BY-SA 3.0）；證據包的 DrugBank 欄位只有 vocab，DrugBank 文字授權也不允許轉載，不用。
  2026-11-19 這次用 openFDA 的 drug label 全量下載檔（download.open.fda.gov，同一批資料，只留 human prescription 仿單；`--fda-bulk <目錄>`），不吃 API 每日 1,000 次配額；之後少量重跑可直接用 API（不給 `--fda-bulk`）。快取目錄各站共用。
- `scripts/build_mechanism_reviews.py --cache <目錄> [--fda-bulk <目錄>]`：掃公開頁正文章節（排除結論／下一步的待辦、安全性、摘要、總覽表、查核紀錄、免責聲明等）裡同時有「作用機轉」「資料」「沒有」字樣的短句（本站語言的字樣在檔內 L 的 KW／DATA／NEG／EXCL）→ 依 front matter monitor_inn（INN 另對 USAN，表在 US_NAME）查 openFDA，選仿單規則同 NZ：只用單一成分、主成分名（去鹽類；酯類要相同）跟本頁相同的處方藥仿單；排序全身給藥→節錄夠長→有 12.1→有品牌名→版本新；美國只有複方仿單的只節錄 12.1 裡講本藥成分的句子並寫明是複方；節錄照原文 2～4 句、不改寫。
  紀錄寫進 `docs/_data/drug_reviews.json`（action＝mechanism，id `br-moa-<日期>-<藥>-1`，sources 附 url、accessed、excerpt、label_version、section、set_id 或 chembl_id）；仿單與 ChEMBL 都沒有的，列進 `docs/_data/drug_reviews_uncertain.json`（source＝mechanism of action，附原因）。已有紀錄或已列待查的頁不重抓。`--list` 只列仍寫「不可得」的頁。
- 替換句格式：本站語言（português）的出處句＋節錄的忠實翻譯（標明「非官方翻譯」）＋英文原文（照引、為準）＋DailyMed 連結、仿單版本、取用日期（用戶 2026-11-19 決定「當地語言摘要＋英文原文」）。只換「不可得」那一句（英文站句首子句後接 so／but 的後半句是 AI 推論，保留），不加框；查核紀錄表列原句與出處。模型預測與其他正文不動。
- 翻譯：節錄的翻譯是 AI 輔助的忠實翻譯（不增不減，藥名、基因與受體符號、數字、「[…]」照原文），2026-11-19 批次產生，存在紀錄 sources 的 translation（translation_lang、translation_note 註明非官方、英文原文為準）；頁面上同時列英文原文。`--translations <檔>` 讀翻譯、`--need <檔>` 列出還沒翻的節錄（這些頁那次不寫紀錄，gate 會擋，翻好再跑）。
- 2026-11-19 結果：412 頁寫入紀錄（美國仿單 363、ChEMBL 49），81 頁列待查（美國沒有單一成分處方藥仿單、仿單段落不是作用機轉，且 ChEMBL 沒有已核准分子的機轉紀錄；多是胺基酸、維生素、礦物質、賦形劑、生物製劑或只在別國上市的藥）。
- `scripts/apply_drug_reviews.py` 支援 mechanism；gate 第 23 項（`scripts/check_seo_docs.py`，函式在 build_mechanism_reviews.gate_errors）：公開頁仍寫「不可得」、既沒有 mechanism 紀錄也沒列待查的，擋下；有紀錄沒套上的由查核紀錄那一項擋。
- 注意：節錄的是美國仿單，劑型與適應症可能跟本站市場的產品不同（例如取到外用仿單）；文字上已寫明是美國 FDA 核准仿單。`sync_notes_to_docs.py` 整頁重寫後會重套紀錄（claim 是頁面原句）；報告重產、原句改寫後要再跑 build_mechanism_reviews.py。
- 2026-11-20 補做：程式更新：同頁不只一句「不可得」時每句各一筆紀錄（-1、-2…）；同頁別筆紀錄的更正文字、錨點與已套上的節錄不再當成「不可得」句；gate 改成公開頁仍寫「不可得」、又沒列待查就擋（不再只看該頁有沒有紀錄）；ChEMBL 譯文（詞組清單）後補句號 49 筆；同 id 重發，前版 replacement 存 history。
- 2026-11-20 試跑母目錄「交付前驗證」規則時補做：偵測改成原條件不動、另加新增寫法（L2，比中的再用 NOT 排除以缺資料為前提的模型推論），字樣用獨立、更寬的偵測全量掃出的候選句逐句標註校準（A 沒有漏、B 沒有誤中）；全量複查沒有漏抓、沒有要重排或重複引用的節錄。程式另加 reorder_src_tail、同頁已引用同一段節錄時改指向上方（產生器 txgnn/.claude/moa_rollout_20261119/fix_20261120/）。

## 說明頁與證據等級頁的在地資料（2026-11-19）

用戶 2026-11-19 決定的第一批改版（母目錄 `.claude/gen_local_pages_20261119.py` 產生，不逐站手改）：說明頁（about／guide／sources／downloads／methodology，自有結構站只有證據等級頁與隱私頁）加本站資料區塊（`<!-- local-facts -->`）、證據等級頁的事實段與藥名表（`<!-- tier-facts -->`、`<!-- tier-table -->`）、隱私頁的適用法律／權利／著作權與資料來源段（`<!-- privacy-law -->`）；en／es／de 樣板站的共用長段落縮成一段（`<!-- local-condensed -->`）。
資料檔 `docs/_data/local_facts.json`、`docs/_data/evidence_tier_facts.json` 由 `scripts/local_facts.py`（＝母目錄 `.claude/local_facts_lib.py`）依藥物頁、許可證快照、查核紀錄、FHIR 算；`apply_drug_reviews.py`、許可證快照程式結尾會自動 `--write`，`check_seo_docs.py` 跑 `--check` 擋過期。跨站欄位（cross：本站獨有預測、30 站中位數）與頁面區塊只由母目錄產生器更新；藥物頁改等級、noindex 或預測後要在母目錄重跑。

## 藥物頁 description 句尾在地化（2026-11-19）

用戶 2026-11-19 決定（「藥物頁簡述在地化」，SEO 工具判定 30 站藥物頁近似重複，原因之一是 description 句尾都是同一句「原適應症：本地資料未記載」）：公開藥物頁（排除 noindex、轉址頁）front matter description 句尾的「Indicação original: Não consta nos dados locais」換成本站許可證快照事實層（`snapshots/*_licenses.json.gz`，經 `src/*/regulatory/licenses.py` 的 snapshot()）的品項數句子，資料名稱照本站口徑：ANVISA 登記。藥名、預測新適應症、等級字樣不動（母目錄 sync_description_levels.py 照舊對得到）；已有原適應症原文的頁不動。
例：abatacepte「Indicação original: Não consta nos dados locais」→「No Brasil, registros na ANVISA: 1 (ativos: 1)」；2026-11-19 改了 155 頁。
由母目錄 `.claude/drug_meta_description.py --apply --site BrTxGNN` 產生（站上複本 `tools/txgnn/.claude/drug_meta_description.py --apply --root .`），改動記在 `docs/_data/description_local_log.json`（pages＝目前句尾與原字樣、entries＝每次改動前後整行，可還原）。快照數字變了重跑會換新數字；`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾會自動 --apply，`check_seo_docs.py` 跑 --check 擋「還是未記載句尾」或「數字跟快照不符」。只改 front matter，lastmod_fix 不算正文改動、last_modified_at 不動。
同日修：`apply_drug_reviews.py`、`build_license_snapshot.py` 結尾重算 local_facts 的 atexit 掛鉤在結束時取不到 `__file__`（NameError，之前其實沒跑成），改成先算好路徑。

## 許可證表與正文張數由程式產生（2026-11-24）

用戶 2026-11-24 決定（各站同日）：每週許可證排程只改程式管得到的格子，AI 寫的自由格式許可證表與正文張數句跟著 ANVISA 資料過期，checker 擋頁、要人處理；改成程式產生、每次自動同步。
- A. 程式許可證表：`scripts/sync_license_tables.py`。「## Informações de Comercialização no Brasil」段落裡的第一張表（AI 表與 known_use_pages 的表 167 頁（含 noindex 1 頁）、10-31 `br_rebuild_by_ingredient_20261031.py --tables` 重建的表 269 頁（含 noindex 3 頁））一律換成程式依證據包產生的表，前後加 `<!-- licenses:begin -->`／`<!-- licenses:end -->`。
  表頭沿用 10-31 重建表「| Registro | Produto | Empresa detentora | Situação |」（證據包是原收集器格式、沒有持有人欄的 143 個藥用三欄 `| Registro | Produto | Situação |`，不放整欄「—」）；最多 30 列、Ativo 在前；狀態 Ativo／Cancelado（license_labels）。
  超過 30 個登記號時表下一句「A tabela mostra até 30 registros (os ativos primeiro), de N registros nos dados. …」；證據包只收了一部分（19 個藥）時加「Os dados contêm apenas parte dos registros; a lista pode estar incompleta.」；沒有紀錄時一句 NONE_LINE。段落裡沒有表的頁（49 頁）不新增表。
  快照 `snapshots/br_licenses.json.gz` 另存 rows（前 30 列）／total／partial；gate 第 20 項（src/brtxgnn/regulatory/licenses.py 的 program_block_problems）擋「段落有表卻不是程式區塊」「程式區塊≠快照重算」。
  接上：`scripts/license_adapter.py` 的 `sync_tables`（每週排程，依證據包全站重排）與 `PAGE_NOTE`（3b 自我檢查認得程式區塊的說明句與標記）、`scripts/apply_drug_reviews.py`（非 --check）結尾與 `scripts/build_license_snapshot.py` 結尾（`--from-snapshot`，不需要 data/）。site_config 的 PROGRAM_LINE_RE 也認得這些程式句。
  被換掉的 AI 表上錨著的 59 筆查核紀錄（`br-row-20261112-*` 等）照 Tw 慣例標 `status: superseded`＋`superseded_by`（紀錄保留、頁面不顯示框，查核紀錄表註明）。
- B. 正文張數程式改寫：`scripts/rewrite_license_counts.py`＋`src/brtxgnn/regulatory/count_prose.py`（照 KrTxGNN／MyTxGNN 移植，規則改成葡萄牙文句型：「N registros válidos de M」「X de Y registros válidos」「Dos N registros, V estão válidos」「V válidos e C cancelados, totalizando T」等）。
  有保留、講證據包或查詢（encontrad／localizad…；「segundo os dados compilados」不算）、相對數、劑型／廠商／單方複方子集、顯示筆數、文字數詞、partial 頁不動；同一行有判斷不了的句子整行不動；跨過 1（單複數要跟著變）列 plural、「Os N registros … estão válidos」而事實不是全部有效列 premise，不改、列進待查清單。
  不寫查核框（同 Tw／Kr／My）；apply_drug_reviews.py（非 --check）結尾、build_license_snapshot.py 結尾自動跑；gate 第 24 項擋「再跑一次會變」。查核紀錄 replacement／anchor 所在的句子程式不改。
- 2026-11-24 第一次套用（資料 data-20261123-132649）：表格 436 頁（AI 表 167 頁換掉、10-31 表 269 頁補標記並依證據包重排，其中 29 頁列有變）；正文改寫 22 頁 25 行（多是「N registros válidos de N」→「de 總數」）；待查清單加 11 句（premise 9、ambiguous 2）；
  查核紀錄 replacement 裡的張數已跟 11-23 資料不符的 6 筆同 id 重發（aztreonam、mometasone、rivastigmine、procaine、calcitriol、spironolactone-2，前版存 history）。
  另寫的寬偵測（正文張數／狀態跟事實層不符）156 句→73 句；剩下多是表格說明句（「a tabela lista os 5 principais」「Principais registros (máximo de 5)」等 42 句，表換成程式表後列數對不上，其中約 25 句是這次換表才變得不符）、「Todos os N registros … válidos」前提句 19 句、相對數 5 句、文字數詞 3 句；表格說明句要不要寫紀錄更正待用戶決定。
  checker 全量前後都是 0；gate exit 0。last_modified_at：正文有變的 285 頁改 2026-11-24，只加標記的 154 頁維持原日期。

## 舊錯句與查核紀錄裡的張數（2026-11-24 第二輪）

用戶 2026-11-24 第二輪決定：第一輪列待查、寬偵測剩下的舊錯句逐句寫紀錄；查核紀錄與說明樣板不再寫死張數（張數只在概覽表與程式表，由排程維護）。
- 說明樣板：`site_config.py` 的 `T["figures"]`（`scripts/reviews_from_edits.py` 寫紀錄說明時用）改成不寫數字「Os números atualizados de registros estão no resumo rápido e nas informações de comercialização.」；既有 476 筆說明裡的「Nos dados … constam N registros …, V válidos」同 id 重發成新句（前版存 history，checked 不動）。
- 更正文字寫死張數：頁面上看得到、含張數的 66 筆（＋2 筆外層紀錄）同 id 重發，改成不寫數字的寫法（「há registros válidos e cancelados (números atualizados no resumo rápido)」、表格說明「Principais registros (30 de N)」→「Principais registros:」、只講舊表筆數的整句刪掉，錨點改到 `<!-- licenses:end -->`）；錨在被刪句上的 2 筆舊紀錄改錨。例外：`br-lic-20261119-levometionina-2` 的分類張數（16 靜脈營養、3 複方…）是 11-19 用戶指定照實寫的分類，不是總數／有效數，保留。
- 舊錯句：112 筆新紀錄 `br-lic-20261124b-*`（102 頁；表格說明 55、張數或全部有效 21、partial 15、前提 9、現行品項被寫成註銷 7、單方／範圍 5），逐句對照證據包 tfda.records 與快照事實層（data-20261123-132649）：表格說明句（「a tabela mostra os 5 primeiros」「Os cinco principais:」「Há mais 4 registros além dos cinco listados」等，程式表最多 30 列）刪掉；「Todos os N registros … válidos」而事實不是全部有效的、張數不符的改成不寫數字；「lista parcial／pelo menos 20」而事實層不是 partial 的刪掉；說「另有 N 張已註銷（品名…）」而其中有現行 Ativo 的 7 句刪掉（loperamide 100470525 等 3 張、oxcarbazepine 3 張、ropivacaine NAROPIN／HYROVI／ROPI、topiramate Toduze／Têmpora／Vidmax、hydroquinone Suavicid／Hormoskin、insulin_human Afrezza／Novolin N／Humulin N、perindopril TRIPLIXAM 都是 Ativo）；說「表上只列單方」而程式表也列複方的改寫；結論／下一步的錯誤前提只拿掉前提（doxorubicin「já que não há registro vigente」、olanzapine「20 registros vigentes」、azacitidina「11 registros」等），建議內容不動。
- 待查清單 11 句（premise 9、ambiguous 2）全部寫紀錄，標 resolved（附 record_ids）。劑型說法（「apenas injetável」等）掃到 3 句，對照證據包都成立，不改。
- 驗證：第一輪同一支寬偵測 73 句→1 句（benralizumab 的「IL-5Rα」誤中）；市場段落含張數／列表字樣的行另掃 212 行→108 行，剩下的都是跟事實層一致、由 count_prose 維護的張數句或 partial 頁的保留語；checker 全量前後 0；gate exit 0；`rewrite_license_counts.py` 再跑 0 頁。last_modified_at：368 頁正文（含查核框說明）有變，改 2026-11-24。

## 缺市場段落／段落沒有表的公開頁補程式表（2026-11-24 第三輪）

用戶 2026-11-24 決定（比照 JpTxGNN 第二輪 `add_section`）：公開頁（非 noindex、非轉址）證據包有紀錄，卻整頁沒有「## Informações de Comercialização no Brasil」、或段落在而表不在的，由 `scripts/sync_license_tables.py` 補程式表：
整頁沒有段落的，`add_section` 在「## Considerações de Segurança」之前（沒有就結論、查核紀錄、免責聲明段之前）補段落；段落沒有表的，程式區塊放在段落開頭。noindex 頁、證據包沒有紀錄的頁照舊不補。
gate（`src/brtxgnn/regulatory/licenses.py` 第 5 項）擋「公開頁快照有程式表列，卻沒有市場段落或段落沒有程式表」；`license_adapter.PAGE_NOTE` 放行新標題行。
- 2026-11-24 全量量測：整頁沒有段落 84 頁、段落沒有表 49 頁（第二輪回報的 49 頁），共 133 頁補上（last_modified_at 改 2026-11-24）。
- 正文跟新表矛盾的句子以 49 筆 `br-lic-20261124c-*` 更正：段落裡「A lista detalhada de registros não está disponível」「por isso a tabela não é apresentada」「Os detalhes dos registros serão adicionados pelo programa」等 33 句刪除或改寫（資料確實沒有的劑型、適應症文字照實保留），
  非 partial 頁的「a lista pode estar incompleta／parcial」一併刪；tamoxifen 10 月刪句後留下的殘句「Essa informação diverge…」刪；新補段落頁以「não há registros／nenhum registro na ANVISA／zero licenças／ausência de registros ativos／não está registrado nem comercializado」或「lista parcial」為前提的句子 14 句（多是下一步待辦）只拿掉錯的前提。
  錨在被刪句上的 16 筆 11-06 紀錄改錨到程式表下方（前版存 history，reanchored）。
- 驗證：checker 全量前後都是 0、gate exit 0；另寫的寬偵測（否定＋註冊／清單字樣）掃 133 頁，剩下的都是 partial 頁的保留語、不講註冊的句子、或成立的（nitrogen、selenium 確實沒有有效登記）。
