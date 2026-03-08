"""疾病映射模組 - 葡萄牙語適應症/治療類別映射至 TxGNN 疾病本體"""

import re
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import pandas as pd


# 葡萄牙語-英語疾病/症狀對照表
DISEASE_DICT = {
    # Sistema Cardiovascular (心血管系統)
    "hipertensão": "hypertension",
    "hipertensao": "hypertension",
    "pressão alta": "hypertension",
    "hipotensão": "hypotension",
    "hipotensao": "hypotension",
    "doença cardíaca": "heart disease",
    "doenca cardiaca": "heart disease",
    "infarto": "myocardial infarction",
    "infarto do miocárdio": "myocardial infarction",
    "angina": "angina",
    "arritmia": "arrhythmia",
    "palpitação": "palpitation",
    "palpitacao": "palpitation",
    "insuficiência cardíaca": "heart failure",
    "insuficiencia cardiaca": "heart failure",
    "aterosclerose": "atherosclerosis",
    "varizes": "varicose veins",
    "trombose": "thrombosis",
    "acidente vascular cerebral": "stroke",
    "avc": "stroke",
    "derrame": "stroke",
    "embolia": "embolism",
    "fibrilação atrial": "atrial fibrillation",
    "fibrilacao atrial": "atrial fibrillation",

    # Sistema Respiratório (呼吸系統)
    "asma": "asthma",
    "bronquite": "bronchitis",
    "pneumonia": "pneumonia",
    "tuberculose": "tuberculosis",
    "tosse": "cough",
    "resfriado": "common cold",
    "gripe": "influenza",
    "influenza": "influenza",
    "rinite": "rhinitis",
    "rinite alérgica": "allergic rhinitis",
    "rinite alergica": "allergic rhinitis",
    "sinusite": "sinusitis",
    "dispneia": "dyspnea",
    "dispnéia": "dyspnea",
    "falta de ar": "dyspnea",
    "enfisema": "emphysema",
    "dpoc": "chronic obstructive pulmonary disease",
    "doença pulmonar obstrutiva crônica": "chronic obstructive pulmonary disease",
    "fibrose pulmonar": "pulmonary fibrosis",

    # Sistema Digestivo (消化系統)
    "gastrite": "gastritis",
    "úlcera gástrica": "gastric ulcer",
    "ulcera gastrica": "gastric ulcer",
    "úlcera duodenal": "duodenal ulcer",
    "ulcera duodenal": "duodenal ulcer",
    "dispepsia": "dyspepsia",
    "indigestão": "dyspepsia",
    "indigestao": "dyspepsia",
    "diarreia": "diarrhea",
    "diarréia": "diarrhea",
    "constipação": "constipation",
    "constipacao": "constipation",
    "prisão de ventre": "constipation",
    "enterite": "enteritis",
    "colite": "colitis",
    "disenteria": "dysentery",
    "hepatite": "hepatitis",
    "cirrose": "cirrhosis",
    "cálculo biliar": "gallstone",
    "calculo biliar": "gallstone",
    "colecistite": "cholecystitis",
    "pancreatite": "pancreatitis",
    "náusea": "nausea",
    "nausea": "nausea",
    "vômito": "vomiting",
    "vomito": "vomiting",
    "refluxo gastroesofágico": "gastroesophageal reflux",
    "refluxo gastroesofagico": "gastroesophageal reflux",
    "azia": "heartburn",
    "doença de crohn": "crohn disease",
    "doenca de crohn": "crohn disease",
    "síndrome do intestino irritável": "irritable bowel syndrome",

    # Sistema Nervoso (神經系統)
    "epilepsia": "epilepsy",
    "convulsão": "seizure",
    "convulsao": "seizure",
    "cefaleia": "headache",
    "dor de cabeça": "headache",
    "dor de cabeca": "headache",
    "enxaqueca": "migraine",
    "vertigem": "vertigo",
    "tontura": "dizziness",
    "insônia": "insomnia",
    "insonia": "insomnia",
    "neuralgia": "neuralgia",
    "ciática": "sciatica",
    "ciatica": "sciatica",
    "doença de parkinson": "parkinson disease",
    "doenca de parkinson": "parkinson disease",
    "parkinson": "parkinson disease",
    "doença de alzheimer": "alzheimer disease",
    "doenca de alzheimer": "alzheimer disease",
    "alzheimer": "alzheimer disease",
    "demência": "dementia",
    "demencia": "dementia",
    "esclerose múltipla": "multiple sclerosis",
    "esclerose multipla": "multiple sclerosis",
    "meningite": "meningitis",
    "neuropatia": "neuropathy",
    "neuropatia periférica": "peripheral neuropathy",

    # Doenças Psiquiátricas (精神疾病)
    "depressão": "depression",
    "depressao": "depression",
    "ansiedade": "anxiety disorder",
    "transtorno de ansiedade": "anxiety disorder",
    "transtorno bipolar": "bipolar disorder",
    "esquizofrenia": "schizophrenia",
    "transtorno de pânico": "panic disorder",
    "transtorno de panico": "panic disorder",
    "transtorno obsessivo-compulsivo": "obsessive-compulsive disorder",
    "toc": "obsessive-compulsive disorder",
    "tdah": "attention deficit hyperactivity disorder",
    "transtorno de déficit de atenção": "attention deficit hyperactivity disorder",
    "psicose": "psychosis",
    "estresse pós-traumático": "post-traumatic stress disorder",

    # Sistema Endócrino (內分泌系統)
    "diabetes": "diabetes",
    "diabetes mellitus": "diabetes mellitus",
    "diabetes tipo 1": "type 1 diabetes",
    "diabetes tipo 2": "type 2 diabetes",
    "hipertireoidismo": "hyperthyroidism",
    "hipotireoidismo": "hypothyroidism",
    "obesidade": "obesity",
    "gota": "gout",
    "hiperlipidemia": "hyperlipidemia",
    "dislipidemia": "dyslipidemia",
    "hipercolesterolemia": "hypercholesterolemia",
    "colesterol alto": "hypercholesterolemia",
    "síndrome metabólica": "metabolic syndrome",
    "sindrome metabolica": "metabolic syndrome",
    "hipoglicemia": "hypoglycemia",
    "hiperglicemia": "hyperglycemia",

    # Sistema Musculoesquelético (肌肉骨骼系統)
    "artrite": "arthritis",
    "artrite reumatoide": "rheumatoid arthritis",
    "artrite reumatóide": "rheumatoid arthritis",
    "osteoartrite": "osteoarthritis",
    "osteoporose": "osteoporosis",
    "fratura": "fracture",
    "mialgia": "myalgia",
    "dor muscular": "myalgia",
    "lombalgia": "back pain",
    "dor nas costas": "back pain",
    "dor lombar": "low back pain",
    "cervicalgia": "neck pain",
    "dor no pescoço": "neck pain",
    "entorse": "sprain",
    "contusão": "contusion",
    "contusao": "contusion",
    "tendinite": "tendinitis",
    "bursite": "bursitis",
    "fibromialgia": "fibromyalgia",
    "espondilite": "spondylitis",
    "hérnia de disco": "herniated disc",
    "hernia de disco": "herniated disc",

    # Doenças de Pele (皮膚疾病)
    "eczema": "eczema",
    "urticária": "urticaria",
    "urticaria": "urticaria",
    "psoríase": "psoriasis",
    "psoriase": "psoriasis",
    "dermatite": "dermatitis",
    "dermatite atópica": "atopic dermatitis",
    "dermatite atopica": "atopic dermatitis",
    "micose": "fungal infection",
    "tinha": "tinea",
    "pé de atleta": "tinea pedis",
    "pe de atleta": "tinea pedis",
    "onicomicose": "onychomycosis",
    "acne": "acne",
    "escabiose": "scabies",
    "sarna": "scabies",
    "herpes zoster": "herpes zoster",
    "herpes simples": "herpes simplex",
    "prurido": "pruritus",
    "coceira": "pruritus",
    "queimadura": "burn",
    "vitiligo": "vitiligo",
    "rosácea": "rosacea",
    "rosacea": "rosacea",
    "alopecia": "alopecia",
    "queda de cabelo": "alopecia",

    # Sistema Urinário (泌尿系統)
    "uretrite": "urethritis",
    "cistite": "cystitis",
    "infecção urinária": "urinary tract infection",
    "infeccao urinaria": "urinary tract infection",
    "nefrite": "nephritis",
    "cálculo renal": "kidney stone",
    "calculo renal": "kidney stone",
    "pedra nos rins": "kidney stone",
    "hiperplasia prostática": "prostatic hyperplasia",
    "hiperplasia prostatica": "prostatic hyperplasia",
    "próstata aumentada": "prostatic hyperplasia",
    "incontinência urinária": "urinary incontinence",
    "incontinencia urinaria": "urinary incontinence",
    "insuficiência renal": "renal failure",
    "insuficiencia renal": "renal failure",
    "doença renal crônica": "chronic kidney disease",
    "doenca renal cronica": "chronic kidney disease",

    # Oftalmologia (眼科)
    "conjuntivite": "conjunctivitis",
    "glaucoma": "glaucoma",
    "catarata": "cataract",
    "olho seco": "dry eye",
    "síndrome do olho seco": "dry eye syndrome",
    "miopia": "myopia",
    "hipermetropia": "hyperopia",
    "retinopatia": "retinopathy",
    "retinopatia diabética": "diabetic retinopathy",
    "degeneração macular": "macular degeneration",
    "degeneracao macular": "macular degeneration",
    "blefarite": "blepharitis",
    "uveíte": "uveitis",
    "uveite": "uveitis",

    # Otorrinolaringologia (耳鼻喉)
    "otite média": "otitis media",
    "otite media": "otitis media",
    "otite externa": "otitis externa",
    "zumbido": "tinnitus",
    "faringite": "pharyngitis",
    "dor de garganta": "pharyngitis",
    "amigdalite": "tonsillitis",
    "laringite": "laryngitis",
    "surdez": "deafness",
    "perda auditiva": "hearing loss",

    # Infecções (感染症)
    "infecção bacteriana": "bacterial infection",
    "infeccao bacteriana": "bacterial infection",
    "infecção viral": "viral infection",
    "infeccao viral": "viral infection",
    "infecção fúngica": "fungal infection",
    "infeccao fungica": "fungal infection",
    "infecção parasitária": "parasitic infection",
    "infeccao parasitaria": "parasitic infection",
    "sepse": "sepsis",
    "septicemia": "sepsis",
    "celulite": "cellulitis",
    "malária": "malaria",
    "malaria": "malaria",
    "dengue": "dengue",
    "febre amarela": "yellow fever",
    "hiv": "hiv infection",
    "aids": "aids",
    "covid-19": "covid-19",
    "coronavirus": "coronavirus infection",
    "zika": "zika virus infection",
    "chikungunya": "chikungunya",
    "leishmaniose": "leishmaniasis",
    "doença de chagas": "chagas disease",
    "doenca de chagas": "chagas disease",
    "hanseníase": "leprosy",
    "hanseniase": "leprosy",

    # Alergias (過敏)
    "alergia": "allergy",
    "reação alérgica": "allergic reaction",
    "reacao alergica": "allergic reaction",
    "febre do feno": "hay fever",
    "alergia alimentar": "food allergy",
    "alergia a medicamentos": "drug allergy",
    "choque anafilático": "anaphylaxis",
    "choque anafilatico": "anaphylaxis",
    "anafilaxia": "anaphylaxis",

    # Ginecologia (婦科)
    "dismenorreia": "dysmenorrhea",
    "dismenorréia": "dysmenorrhea",
    "cólica menstrual": "dysmenorrhea",
    "colica menstrual": "dysmenorrhea",
    "menopausa": "menopause",
    "síndrome da menopausa": "menopause syndrome",
    "endometriose": "endometriosis",
    "vaginite": "vaginitis",
    "candidíase": "candidiasis",
    "candidiase": "candidiasis",
    "mioma uterino": "uterine fibroid",
    "síndrome do ovário policístico": "polycystic ovary syndrome",
    "sop": "polycystic ovary syndrome",
    "infertilidade": "infertility",
    "tpm": "premenstrual syndrome",
    "síndrome pré-menstrual": "premenstrual syndrome",

    # Oncologia/Câncer (腫瘤/癌症)
    "câncer": "cancer",
    "cancer": "cancer",
    "tumor": "tumor",
    "neoplasia": "neoplasm",
    "tumor maligno": "malignant tumor",
    "tumor benigno": "benign tumor",
    "leucemia": "leukemia",
    "linfoma": "lymphoma",
    "câncer de mama": "breast cancer",
    "cancer de mama": "breast cancer",
    "câncer de pulmão": "lung cancer",
    "cancer de pulmao": "lung cancer",
    "câncer de próstata": "prostate cancer",
    "cancer de prostata": "prostate cancer",
    "câncer colorretal": "colorectal cancer",
    "cancer colorretal": "colorectal cancer",
    "melanoma": "melanoma",
    "carcinoma": "carcinoma",

    # Sintomas Gerais (一般症狀)
    "febre": "fever",
    "dor": "pain",
    "inflamação": "inflammation",
    "inflamacao": "inflammation",
    "edema": "edema",
    "inchaço": "swelling",
    "inchaco": "swelling",
    "fadiga": "fatigue",
    "cansaço": "fatigue",
    "cansaco": "fatigue",
    "anemia": "anemia",
    "sangramento": "bleeding",
    "hemorragia": "hemorrhage",
    "espasmo": "spasm",
    "cãibra": "cramp",
    "caibra": "cramp",
    "câimbra": "cramp",

    # Classes Terapêuticas ANVISA (治療分類)
    "antibioticos": "bacterial infection",
    "antibióticos": "bacterial infection",
    "antibioticos sistemicos": "bacterial infection",
    "antiinflamatorios": "inflammation",
    "anti-inflamatórios": "inflammation",
    "analgesicos": "pain",
    "analgésicos": "pain",
    "antihipertensivos": "hypertension",
    "anti-hipertensivos": "hypertension",
    "antidiabeticos": "diabetes",
    "antidiabéticos": "diabetes",
    "hipoglicemiantes": "diabetes",
    "antivirais": "viral infection",
    "antifungicos": "fungal infection",
    "antifúngicos": "fungal infection",
    "antidepressivos": "depression",
    "ansioliticos": "anxiety disorder",
    "ansiolíticos": "anxiety disorder",
    "anticonvulsivantes": "epilepsy",
    "antiepilepticos": "epilepsy",
    "antiepilépticos": "epilepsy",
    "antineoplasicos": "cancer",
    "antineoplásicos": "cancer",
    "imunossupressores": "autoimmune disease",
    "broncodilatadores": "asthma",
    "antihistaminicos": "allergy",
    "anti-histamínicos": "allergy",
    "corticosteroides": "inflammation",
    "corticosteróides": "inflammation",
    "diureticos": "edema",
    "diuréticos": "edema",
    "anticoagulantes": "thrombosis",
    "antiplaquetarios": "thrombosis",
    "antiplaquetários": "thrombosis",
    "cefalosporinas": "bacterial infection",
    "penicilinas": "bacterial infection",
    "quinolonas": "bacterial infection",
    "macrolideos": "bacterial infection",
    "macrolídeos": "bacterial infection",
}


def load_disease_vocab(filepath: Optional[Path] = None) -> pd.DataFrame:
    """載入 TxGNN 疾病詞彙表"""
    if filepath is None:
        filepath = Path(__file__).parent.parent.parent.parent / "data" / "external" / "disease_vocab.csv"
    return pd.read_csv(filepath)


def build_disease_index(disease_df: pd.DataFrame) -> Dict[str, Tuple[str, str]]:
    """建立疾病名稱索引（關鍵詞 -> (disease_id, disease_name)）"""
    index = {}

    for _, row in disease_df.iterrows():
        disease_id = row["disease_id"]
        disease_name = row["disease_name"]
        name_upper = row["disease_name_upper"]

        # 完整名稱
        index[name_upper] = (disease_id, disease_name)

        # 提取關鍵詞（按空格和逗號分割）
        keywords = re.split(r"[,\s\-]+", name_upper)
        for kw in keywords:
            kw = kw.strip()
            if len(kw) > 3 and kw not in index:  # 只保留較長的關鍵詞
                index[kw] = (disease_id, disease_name)

    return index


def extract_indications(indication_str: str) -> List[str]:
    """從適應症/治療類別文字提取個別適應症

    使用葡萄牙語常見分隔符分割
    """
    if not indication_str:
        return []

    # 正規化
    text = indication_str.strip().lower()

    # 使用分隔符分割
    parts = re.split(r"[.;]", text)

    indications = []
    for part in parts:
        # 再用逗號細分
        sub_parts = re.split(r"[,/]", part)
        for sub in sub_parts:
            sub = sub.strip()
            # 移除常見前綴
            sub = re.sub(r"^(para |tratamento de |indicado para |usado para )", "", sub)
            # 移除常見後綴
            sub = re.sub(r"( e outros| etc\.?)$", "", sub)
            sub = sub.strip()
            if sub and len(sub) >= 2:
                indications.append(sub)

    return indications


def translate_indication(indication: str) -> List[str]:
    """將葡萄牙語適應症翻譯為英文關鍵詞"""
    keywords = []
    indication_lower = indication.lower()

    for pt, en in DISEASE_DICT.items():
        if pt in indication_lower:
            keywords.append(en.upper())

    return keywords


def map_indication_to_disease(
    indication: str,
    disease_index: Dict[str, Tuple[str, str]],
) -> List[Tuple[str, str, float]]:
    """將單一適應症映射到 TxGNN 疾病

    Returns:
        [(disease_id, disease_name, confidence), ...]
    """
    results = []

    # 翻譯為英文關鍵詞
    keywords = translate_indication(indication)

    for kw in keywords:
        # 完全匹配
        if kw in disease_index:
            disease_id, disease_name = disease_index[kw]
            results.append((disease_id, disease_name, 1.0))
            continue

        # 部分匹配
        for index_kw, (disease_id, disease_name) in disease_index.items():
            if kw in index_kw or index_kw in kw:
                results.append((disease_id, disease_name, 0.8))

    # 去重並按信心度排序
    seen = set()
    unique_results = []
    for disease_id, disease_name, conf in sorted(results, key=lambda x: -x[2]):
        if disease_id not in seen:
            seen.add(disease_id)
            unique_results.append((disease_id, disease_name, conf))

    return unique_results[:5]  # 最多返回 5 個匹配


def map_fda_indications_to_diseases(
    fda_df: pd.DataFrame,
    disease_df: Optional[pd.DataFrame] = None,
) -> pd.DataFrame:
    """將巴西 ANVISA 藥品治療類別映射到 TxGNN 疾病"""
    if disease_df is None:
        disease_df = load_disease_vocab()

    disease_index = build_disease_index(disease_df)

    results = []

    for _, row in fda_df.iterrows():
        # ANVISA 使用 CLASSE_TERAPEUTICA 而非適應症
        indication_str = row.get("CLASSE_TERAPEUTICA", "")
        if not indication_str:
            continue

        # 提取個別適應症
        indications = extract_indications(indication_str)

        for ind in indications:
            # 翻譯並映射
            matches = map_indication_to_disease(ind, disease_index)

            if matches:
                for disease_id, disease_name, confidence in matches:
                    results.append({
                        "NUMERO_REGISTRO_PRODUTO": row.get("NUMERO_REGISTRO_PRODUTO", ""),
                        "NOME_PRODUTO": row.get("NOME_PRODUTO", ""),
                        "CLASSE_TERAPEUTICA": indication_str[:100],
                        "extracted_indication": ind,
                        "disease_id": disease_id,
                        "disease_name": disease_name,
                        "confidence": confidence,
                    })
            else:
                results.append({
                    "NUMERO_REGISTRO_PRODUTO": row.get("NUMERO_REGISTRO_PRODUTO", ""),
                    "NOME_PRODUTO": row.get("NOME_PRODUTO", ""),
                    "CLASSE_TERAPEUTICA": indication_str[:100],
                    "extracted_indication": ind,
                    "disease_id": None,
                    "disease_name": None,
                    "confidence": 0,
                })

    return pd.DataFrame(results)


def get_indication_mapping_stats(mapping_df: pd.DataFrame) -> dict:
    """計算適應症映射統計"""
    total = len(mapping_df)
    mapped = mapping_df["disease_id"].notna().sum()
    unique_indications = mapping_df["extracted_indication"].nunique()
    unique_diseases = mapping_df[mapping_df["disease_id"].notna()]["disease_id"].nunique()

    return {
        "total_indications": total,
        "mapped_indications": int(mapped),
        "mapping_rate": mapped / total if total > 0 else 0,
        "unique_indications": unique_indications,
        "unique_diseases": unique_diseases,
    }
