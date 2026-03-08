"""主成分名稱標準化 - 支援葡萄牙語/英文藥名"""

import re
from typing import List, Tuple, Optional


# 葡萄牙語 → 英文 鹽類形式對照表
PT_TO_EN_SALT_PREFIX = {
    # "CLORIDRATO DE X" → "X HYDROCHLORIDE"
    "CLORIDRATO DE": "HYDROCHLORIDE",
    "DICLORIDRATO DE": "DIHYDROCHLORIDE",
    "SULFATO DE": "SULFATE",
    "BISSULFATO DE": "BISULFATE",
    "MALEATO DE": "MALEATE",
    "CITRATO DE": "CITRATE",
    "FOSFATO DE": "PHOSPHATE",
    "ACETATO DE": "ACETATE",
    "TARTARATO DE": "TARTRATE",
    "HEMITARTARATO DE": "HEMITARTRATE",
    "BITARTARATO DE": "BITARTRATE",
    "NITRATO DE": "NITRATE",
    "BROMETO DE": "BROMIDE",
    "CLORETO DE": "CHLORIDE",
    "IODETO DE": "IODIDE",
    "LACTATO DE": "LACTATE",
    "SUCCINATO DE": "SUCCINATE",
    "FUMARATO DE": "FUMARATE",
    "MESILATO DE": "MESYLATE",
    "BESILATO DE": "BESYLATE",
    "TOSILATO DE": "TOSYLATE",
    "GLUCONATO DE": "GLUCONATE",
    "BENZOATO DE": "BENZOATE",
    "OLEATO DE": "OLEATE",
    "ESTEARATO DE": "STEARATE",
    "PALMITATO DE": "PALMITATE",
    "LAURILSULFATO DE": "LAURYL SULFATE",
    "VALERATO DE": "VALERATE",
    "PROPIONATO DE": "PROPIONATE",
    "DIPROPIONATO DE": "DIPROPIONATE",
    "BUTIRATO DE": "BUTYRATE",
    "ACETONIDO DE": "ACETONIDE",
    "FUROATO DE": "FUROATE",
    "PIVALATO DE": "PIVALATE",
    "HEXANOATO DE": "HEXANOATE",
    "UNDECANOATO DE": "UNDECANOATE",
    "DECANOATO DE": "DECANOATE",
    "ENANTATO DE": "ENANTHATE",
    "CIPIONATO DE": "CYPIONATE",
    "EMBONATO DE": "EMBONATE",
    "PAMOATO DE": "PAMOATE",
    "XINAFOATO DE": "XINAFOATE",
    "OROTATO DE": "OROTATE",
    "ASPARTATO DE": "ASPARTATE",
    "GLUTAMATO DE": "GLUTAMATE",
    "CARBONATO DE": "CARBONATE",
    "BICARBONATO DE": "BICARBONATE",
    "OXALATO DE": "OXALATE",
    "HIDRÓXIDO DE": "HYDROXIDE",
    "ÓXIDO DE": "OXIDE",
}

# 葡萄牙語後綴 → 英文
PT_TO_EN_SALT_SUFFIX = {
    "SÓDICA": "SODIUM",
    "SÓDICO": "SODIUM",
    "DISSÓDICA": "DISODIUM",
    "DISSÓDICO": "DISODIUM",
    "TRISSÓDICO": "TRISODIUM",
    "POTÁSSICA": "POTASSIUM",
    "POTÁSSICO": "POTASSIUM",
    "CÁLCICA": "CALCIUM",
    "CÁLCICO": "CALCIUM",
    "MAGNÉSICA": "MAGNESIUM",
    "MAGNÉSICO": "MAGNESIUM",
    "FÉRRICA": "FERRIC",
    "FÉRRICO": "FERRIC",
    "FERROSA": "FERROUS",
    "FERROSO": "FERROUS",
    "ZINCO": "ZINC",
    "ALUMÍNIO": "ALUMINUM",
    "AMÔNICA": "AMMONIUM",
    "AMÔNIO": "AMMONIUM",
    "MEGLUMINA": "MEGLUMINE",
}

# 水合物形式
PT_TO_EN_HYDRATE = {
    "ANIDRO": "ANHYDROUS",
    "ANIDRA": "ANHYDROUS",
    "MONO-HIDRATADO": "MONOHYDRATE",
    "MONO-HIDRATADA": "MONOHYDRATE",
    "MONOIDRATADO": "MONOHYDRATE",
    "MONOIDRATADA": "MONOHYDRATE",
    "HEMI-HIDRATADO": "HEMIHYDRATE",
    "HEMI-HIDRATADA": "HEMIHYDRATE",
    "HEMIHIDRATADO": "HEMIHYDRATE",
    "DI-HIDRATADO": "DIHYDRATE",
    "DI-HIDRATADA": "DIHYDRATE",
    "DIIDRATADO": "DIHYDRATE",
    "TRI-HIDRATADO": "TRIHYDRATE",
    "TRI-HIDRATADA": "TRIHYDRATE",
    "TRIIDRATADO": "TRIHYDRATE",
    "HEXA-HIDRATADO": "HEXAHYDRATE",
    "HEXA-HIDRATADA": "HEXAHYDRATE",
    "HEXAIDRATADO": "HEXAHYDRATE",
    "SESQUI-HIDRATADO": "SESQUIHYDRATE",
}

# 葡萄牙語藥名 → 英文藥名對照表
PT_TO_EN_DRUG_NAMES = {
    # 電解質/礦物質
    "SÓDIO": "SODIUM",
    "POTÁSSIO": "POTASSIUM",
    "CÁLCIO": "CALCIUM",
    "MAGNÉSIO": "MAGNESIUM",
    "ZINCO": "ZINC",
    "FERRO": "IRON",
    "COBRE": "COPPER",
    "MANGANÊS": "MANGANESE",
    "SELÊNIO": "SELENIUM",
    "CROMO": "CHROMIUM",
    "IODO": "IODINE",
    "FÓSFORO": "PHOSPHORUS",
    "ENXOFRE": "SULFUR",

    # 維生素
    "ÁCIDO ASCÓRBICO": "ASCORBIC ACID",
    "COLECALCIFEROL": "CHOLECALCIFEROL",
    "ERGOCALCIFEROL": "ERGOCALCIFEROL",
    "TIAMINA": "THIAMINE",
    "RIBOFLAVINA": "RIBOFLAVIN",
    "NIACINA": "NIACIN",
    "NICOTINAMIDA": "NICOTINAMIDE",
    "PIRIDOXINA": "PYRIDOXINE",
    "CIANOCOBALAMINA": "CYANOCOBALAMIN",
    "ÁCIDO FÓLICO": "FOLIC ACID",
    "BIOTINA": "BIOTIN",
    "ÁCIDO PANTOTÊNICO": "PANTOTHENIC ACID",
    "TOCOFEROL": "TOCOPHEROL",
    "RETINOL": "RETINOL",
    "FILOQUINONA": "PHYLLOQUINONE",
    "FITOMENADIONA": "PHYTONADIONE",
    "MENADIONA": "MENADIONE",

    # 止痛/解熱/抗炎
    "PARACETAMOL": "ACETAMINOPHEN",
    "DIPIRONA": "METAMIZOLE",
    "IBUPROFENO": "IBUPROFEN",
    "NAPROXENO": "NAPROXEN",
    "DICLOFENACO": "DICLOFENAC",
    "CETOPROFENO": "KETOPROFEN",
    "PIROXICAM": "PIROXICAM",
    "MELOXICAM": "MELOXICAM",
    "NIMESULIDA": "NIMESULIDE",
    "INDOMETACINA": "INDOMETHACIN",
    "ÁCIDO ACETILSALICÍLICO": "ASPIRIN",
    "ASPIRINA": "ASPIRIN",
    "CELECOXIBE": "CELECOXIB",
    "ETORICOXIBE": "ETORICOXIB",

    # 抗生素
    "AMOXICILINA": "AMOXICILLIN",
    "AMPICILINA": "AMPICILLIN",
    "PENICILINA": "PENICILLIN",
    "CEFALEXINA": "CEPHALEXIN",
    "CEFAZOLINA": "CEFAZOLIN",
    "CEFTRIAXONA": "CEFTRIAXONE",
    "AZITROMICINA": "AZITHROMYCIN",
    "ERITROMICINA": "ERYTHROMYCIN",
    "CLARITROMICINA": "CLARITHROMYCIN",
    "CIPROFLOXACINO": "CIPROFLOXACIN",
    "LEVOFLOXACINO": "LEVOFLOXACIN",
    "NORFLOXACINO": "NORFLOXACIN",
    "METRONIDAZOL": "METRONIDAZOLE",
    "VANCOMICINA": "VANCOMYCIN",
    "GENTAMICINA": "GENTAMICIN",
    "NEOMICINA": "NEOMYCIN",
    "TOBRAMICINA": "TOBRAMYCIN",
    "AMICACINA": "AMIKACIN",
    "CLINDAMICINA": "CLINDAMYCIN",
    "DOXICICLINA": "DOXYCYCLINE",
    "TETRACICLINA": "TETRACYCLINE",
    "SULFAMETOXAZOL": "SULFAMETHOXAZOLE",
    "TRIMETOPRIMA": "TRIMETHOPRIM",
    "NISTATINA": "NYSTATIN",
    "FLUCONAZOL": "FLUCONAZOLE",
    "ITRACONAZOL": "ITRACONAZOLE",
    "CETOCONAZOL": "KETOCONAZOLE",
    "MICONAZOL": "MICONAZOLE",
    "CLOTRIMAZOL": "CLOTRIMAZOLE",
    "TERBINAFINA": "TERBINAFINE",
    "ACICLOVIR": "ACYCLOVIR",
    "VALACICLOVIR": "VALACYCLOVIR",

    # 心血管
    "ATENOLOL": "ATENOLOL",
    "METOPROLOL": "METOPROLOL",
    "PROPRANOLOL": "PROPRANOLOL",
    "CARVEDILOL": "CARVEDILOL",
    "ANLODIPINO": "AMLODIPINE",
    "NIFEDIPINO": "NIFEDIPINE",
    "VERAPAMIL": "VERAPAMIL",
    "DILTIAZEM": "DILTIAZEM",
    "LOSARTANA": "LOSARTAN",
    "VALSARTANA": "VALSARTAN",
    "CANDESARTANA": "CANDESARTAN",
    "IRBESARTANA": "IRBESARTAN",
    "TELMISARTANA": "TELMISARTAN",
    "OLMESARTANA": "OLMESARTAN",
    "ENALAPRIL": "ENALAPRIL",
    "CAPTOPRIL": "CAPTOPRIL",
    "LISINOPRIL": "LISINOPRIL",
    "RAMIPRIL": "RAMIPRIL",
    "PERINDOPRIL": "PERINDOPRIL",
    "HIDROCLOROTIAZIDA": "HYDROCHLOROTHIAZIDE",
    "FUROSEMIDA": "FUROSEMIDE",
    "ESPIRONOLACTONA": "SPIRONOLACTONE",
    "INDAPAMIDA": "INDAPAMIDE",
    "CLORTALIDONA": "CHLORTHALIDONE",
    "SINVASTATINA": "SIMVASTATIN",
    "ATORVASTATINA": "ATORVASTATIN",
    "ROSUVASTATINA": "ROSUVASTATIN",
    "PRAVASTATINA": "PRAVASTATIN",
    "EZETIMIBA": "EZETIMIBE",
    "VARFARINA": "WARFARIN",
    "RIVAROXABANA": "RIVAROXABAN",
    "APIXABANA": "APIXABAN",
    "DABIGATRANA": "DABIGATRAN",
    "ENOXAPARINA": "ENOXAPARIN",
    "HEPARINA": "HEPARIN",
    "CLOPIDOGREL": "CLOPIDOGREL",
    "TICAGRELOR": "TICAGRELOR",
    "DIGOXINA": "DIGOXIN",
    "AMIODARONA": "AMIODARONE",

    # 消化系統
    "OMEPRAZOL": "OMEPRAZOLE",
    "PANTOPRAZOL": "PANTOPRAZOLE",
    "ESOMEPRAZOL": "ESOMEPRAZOLE",
    "LANSOPRAZOL": "LANSOPRAZOLE",
    "RABEPRAZOL": "RABEPRAZOLE",
    "RANITIDINA": "RANITIDINE",
    "FAMOTIDINA": "FAMOTIDINE",
    "METOCLOPRAMIDA": "METOCLOPRAMIDE",
    "DOMPERIDONA": "DOMPERIDONE",
    "ONDANSETRONA": "ONDANSETRON",
    "LOPERAMIDA": "LOPERAMIDE",
    "SIMETICONA": "SIMETHICONE",
    "LACTULOSE": "LACTULOSE",
    "BISACODIL": "BISACODYL",

    # 神經/精神
    "DIAZEPAM": "DIAZEPAM",
    "CLONAZEPAM": "CLONAZEPAM",
    "LORAZEPAM": "LORAZEPAM",
    "ALPRAZOLAM": "ALPRAZOLAM",
    "BROMAZEPAM": "BROMAZEPAM",
    "MIDAZOLAM": "MIDAZOLAM",
    "ZOLPIDEM": "ZOLPIDEM",
    "FLUOXETINA": "FLUOXETINE",
    "SERTRALINA": "SERTRALINE",
    "PAROXETINA": "PAROXETINE",
    "ESCITALOPRAM": "ESCITALOPRAM",
    "CITALOPRAM": "CITALOPRAM",
    "VENLAFAXINA": "VENLAFAXINE",
    "DULOXETINA": "DULOXETINE",
    "AMITRIPTILINA": "AMITRIPTYLINE",
    "NORTRIPTILINA": "NORTRIPTYLINE",
    "IMIPRAMINA": "IMIPRAMINE",
    "CLOMIPRAMINA": "CLOMIPRAMINE",
    "MIRTAZAPINA": "MIRTAZAPINE",
    "BUPROPIONA": "BUPROPION",
    "TRAZODONA": "TRAZODONE",
    "HALOPERIDOL": "HALOPERIDOL",
    "RISPERIDONA": "RISPERIDONE",
    "OLANZAPINA": "OLANZAPINE",
    "QUETIAPINA": "QUETIAPINE",
    "ARIPIPRAZOL": "ARIPIPRAZOLE",
    "CLOZAPINA": "CLOZAPINE",
    "LÍTIO": "LITHIUM",
    "CARBAMAZEPINA": "CARBAMAZEPINE",
    "OXCARBAZEPINA": "OXCARBAZEPINE",
    "VALPROATO": "VALPROATE",
    "ÁCIDO VALPROICO": "VALPROIC ACID",
    "LAMOTRIGINA": "LAMOTRIGINE",
    "TOPIRAMATO": "TOPIRAMATE",
    "GABAPENTINA": "GABAPENTIN",
    "PREGABALINA": "PREGABALIN",
    "FENITOÍNA": "PHENYTOIN",
    "FENOBARBITAL": "PHENOBARBITAL",
    "LEVETIRACETAM": "LEVETIRACETAM",
    "DONEPEZILA": "DONEPEZIL",
    "RIVASTIGMINA": "RIVASTIGMINE",
    "MEMANTINA": "MEMANTINE",
    "LEVODOPA": "LEVODOPA",
    "CARBIDOPA": "CARBIDOPA",
    "PRAMIPEXOL": "PRAMIPEXOLE",
    "ROPINIROL": "ROPINIROLE",
    "SELEGILINA": "SELEGILINE",
    "RASAGILINA": "RASAGILINE",
    "ENTACAPONA": "ENTACAPONE",
    "BIPERIDENO": "BIPERIDEN",
    "TRIEXIFENIDIL": "TRIHEXYPHENIDYL",
    "SUMATRIPTANO": "SUMATRIPTAN",
    "RIZATRIPTANO": "RIZATRIPTAN",

    # 內分泌/糖尿病
    "METFORMINA": "METFORMIN",
    "GLIBENCLAMIDA": "GLYBURIDE",
    "GLICAZIDA": "GLICLAZIDE",
    "GLIMEPIRIDA": "GLIMEPIRIDE",
    "PIOGLITAZONA": "PIOGLITAZONE",
    "SITAGLIPTINA": "SITAGLIPTIN",
    "VILDAGLIPTINA": "VILDAGLIPTIN",
    "LINAGLIPTINA": "LINAGLIPTIN",
    "SAXAGLIPTINA": "SAXAGLIPTIN",
    "EMPAGLIFLOZINA": "EMPAGLIFLOZIN",
    "DAPAGLIFLOZINA": "DAPAGLIFLOZIN",
    "CANAGLIFLOZINA": "CANAGLIFLOZIN",
    "LIRAGLUTIDA": "LIRAGLUTIDE",
    "SEMAGLUTIDA": "SEMAGLUTIDE",
    "DULAGLUTIDA": "DULAGLUTIDE",
    "ACARBOSE": "ACARBOSE",
    "LEVOTIROXINA": "LEVOTHYROXINE",
    "LIOTIRONINA": "LIOTHYRONINE",
    "METIMAZOL": "METHIMAZOLE",
    "PROPILTIOURACIL": "PROPYLTHIOURACIL",
    "PREDNISONA": "PREDNISONE",
    "PREDNISOLONA": "PREDNISOLONE",
    "DEXAMETASONA": "DEXAMETHASONE",
    "BETAMETASONA": "BETAMETHASONE",
    "HIDROCORTISONA": "HYDROCORTISONE",
    "METILPREDNISOLONA": "METHYLPREDNISOLONE",
    "TRIANCINOLONA": "TRIAMCINOLONE",
    "BUDESONIDA": "BUDESONIDE",
    "FLUTICASONA": "FLUTICASONE",
    "BECLOMETASONA": "BECLOMETHASONE",
    "MOMETASONA": "MOMETASONE",

    # 呼吸系統
    "SALBUTAMOL": "ALBUTEROL",
    "FENOTEROL": "FENOTEROL",
    "FORMOTEROL": "FORMOTEROL",
    "SALMETEROL": "SALMETEROL",
    "BROMETO DE IPRATRÓPIO": "IPRATROPIUM BROMIDE",
    "IPRATRÓPIO": "IPRATROPIUM",
    "TIOTRÓPIO": "TIOTROPIUM",
    "MONTELUCASTE": "MONTELUKAST",
    "TEOFILINA": "THEOPHYLLINE",
    "AMINOFILINA": "AMINOPHYLLINE",
    "DEXTROMETORFANO": "DEXTROMETHORPHAN",
    "CODEÍNA": "CODEINE",
    "DROPROPIZINA": "DROPROPIZINE",
    "BROMEXINA": "BROMHEXINE",
    "AMBROXOL": "AMBROXOL",
    "ACETILCISTEÍNA": "ACETYLCYSTEINE",
    "CARBOCISTEÍNA": "CARBOCISTEINE",

    # 抗過敏/抗組織胺
    "LORATADINA": "LORATADINE",
    "DESLORATADINA": "DESLORATADINE",
    "CETIRIZINA": "CETIRIZINE",
    "LEVOCETIRIZINA": "LEVOCETIRIZINE",
    "FEXOFENADINA": "FEXOFENADINE",
    "DIFENIDRAMINA": "DIPHENHYDRAMINE",
    "PROMETAZINA": "PROMETHAZINE",
    "DEXCLORFENIRAMINA": "DEXCHLORPHENIRAMINE",
    "CLORFENIRAMINA": "CHLORPHENIRAMINE",
    "HIDROXIZINA": "HYDROXYZINE",
    "MECLIZINA": "MECLIZINE",
    "DIMENIDRINATO": "DIMENHYDRINATE",

    # 麻醉/止痛
    "LIDOCAÍNA": "LIDOCAINE",
    "LIDOCAINA": "LIDOCAINE",
    "BUPIVACAÍNA": "BUPIVACAINE",
    "ROPIVACAÍNA": "ROPIVACAINE",
    "PRILOCAÍNA": "PRILOCAINE",
    "BENZOCAÍNA": "BENZOCAINE",
    "TETRACAÍNA": "TETRACAINE",
    "PROCAÍNA": "PROCAINE",
    "MORFINA": "MORPHINE",
    "FENTANILA": "FENTANYL",
    "TRAMADOL": "TRAMADOL",
    "OXICODONA": "OXYCODONE",
    "HIDROCODONA": "HYDROCODONE",
    "METADONA": "METHADONE",
    "BUPRENORFINA": "BUPRENORPHINE",
    "NALOXONA": "NALOXONE",
    "NALTREXONA": "NALTREXONE",

    # 肌肉鬆弛劑
    "CICLOBENZAPRINA": "CYCLOBENZAPRINE",
    "CARISOPRODOL": "CARISOPRODOL",
    "ORFENADRINA": "ORPHENADRINE",
    "BACLOFENO": "BACLOFEN",
    "TIZANIDINA": "TIZANIDINE",
    "DANTROLENO": "DANTROLENE",

    # 泌尿系統
    "TANSULOSINA": "TAMSULOSIN",
    "DOXAZOSINA": "DOXAZOSIN",
    "ALFUZOSINA": "ALFUZOSIN",
    "FINASTERIDA": "FINASTERIDE",
    "DUTASTERIDA": "DUTASTERIDE",
    "SILDENAFILA": "SILDENAFIL",
    "TADALAFILA": "TADALAFIL",
    "VARDENAFILA": "VARDENAFIL",
    "OXIBUTININA": "OXYBUTYNIN",
    "TOLTERODINA": "TOLTERODINE",
    "SOLIFENACINA": "SOLIFENACIN",
    "DARIFENACINA": "DARIFENACIN",

    # 眼科
    "TIMOLOL": "TIMOLOL",
    "LATANOPROSTA": "LATANOPROST",
    "BIMATOPROSTA": "BIMATOPROST",
    "TRAVOPROSTA": "TRAVOPROST",
    "BRIMONIDINA": "BRIMONIDINE",
    "DORZOLAMIDA": "DORZOLAMIDE",
    "BRINZOLAMIDA": "BRINZOLAMIDE",
    "PILOCARPINA": "PILOCARPINE",

    # 腫瘤藥物
    "METOTREXATO": "METHOTREXATE",
    "CICLOFOSFAMIDA": "CYCLOPHOSPHAMIDE",
    "CISPLATINA": "CISPLATIN",
    "CARBOPLATINA": "CARBOPLATIN",
    "OXALIPLATINA": "OXALIPLATIN",
    "DOXORRUBICINA": "DOXORUBICIN",
    "EPIRRUBICINA": "EPIRUBICIN",
    "PACLITAXEL": "PACLITAXEL",
    "DOCETAXEL": "DOCETAXEL",
    "VINCRISTINA": "VINCRISTINE",
    "VIMBLASTINA": "VINBLASTINE",
    "FLUOROURACILA": "FLUOROURACIL",
    "CAPECITABINA": "CAPECITABINE",
    "GENCITABINA": "GEMCITABINE",
    "IRINOTECANO": "IRINOTECAN",
    "TOPOTECANO": "TOPOTECAN",
    "IMATINIBE": "IMATINIB",
    "ERLOTINIBE": "ERLOTINIB",
    "GEFITINIBE": "GEFITINIB",
    "SORAFENIBE": "SORAFENIB",
    "SUNITINIBE": "SUNITINIB",
    "RITUXIMABE": "RITUXIMAB",
    "TRASTUZUMABE": "TRASTUZUMAB",
    "BEVACIZUMABE": "BEVACIZUMAB",
    "TAMOXIFENO": "TAMOXIFEN",
    "ANASTROZOL": "ANASTROZOLE",
    "LETROZOL": "LETROZOLE",
    "EXEMESTANO": "EXEMESTANE",

    # 免疫抑制劑
    "CICLOSPORINA": "CYCLOSPORINE",
    "TACROLIMO": "TACROLIMUS",
    "AZATIOPRINA": "AZATHIOPRINE",
    "MICOFENOLATO": "MYCOPHENOLATE",
    "SIROLIMO": "SIROLIMUS",
    "EVEROLIMO": "EVEROLIMUS",

    # 其他常用藥物
    "ATROPINA": "ATROPINE",
    "ESCOPOLAMINA": "SCOPOLAMINE",
    "ADRENALINA": "EPINEPHRINE",
    "NORADRENALINA": "NOREPINEPHRINE",
    "DOPAMINA": "DOPAMINE",
    "DOBUTAMINA": "DOBUTAMINE",
    "FENILEFRINA": "PHENYLEPHRINE",
    "EFEDRINA": "EPHEDRINE",
    "PSEUDOEFEDRINA": "PSEUDOEPHEDRINE",
    "NAFAZOLINA": "NAPHAZOLINE",
    "OXIMETAZOLINA": "OXYMETAZOLINE",
    "ALOPURINOL": "ALLOPURINOL",
    "FEBUXOSTATE": "FEBUXOSTAT",
    "COLCHICINA": "COLCHICINE",
    "ISOTRETINOÍNA": "ISOTRETINOIN",
    "TRETINÓINA": "TRETINOIN",
    "ADAPALENO": "ADAPALENE",
    "MINOXIDIL": "MINOXIDIL",
    "FINASTERIDA": "FINASTERIDE",
    "MELATONINA": "MELATONIN",
    "ZINCO": "ZINC",
    "GLICINA": "GLYCINE",
    "ALANINA": "ALANINE",
    "VALINA": "VALINE",
    "LEVOVALINA": "VALINE",
    "LEUCINA": "LEUCINE",
    "ISOLEUCINA": "ISOLEUCINE",
    "PROLINA": "PROLINE",
    "SERINA": "SERINE",
    "TREONINA": "THREONINE",
    "CISTEÍNA": "CYSTEINE",
    "METIONINA": "METHIONINE",
    "FENILALANINA": "PHENYLALANINE",
    "TIROSINA": "TYROSINE",
    "TRIPTOFANO": "TRYPTOPHAN",
    "HISTIDINA": "HISTIDINE",
    "LISINA": "LYSINE",
    "ARGININA": "ARGININE",
    "ASPARAGINA": "ASPARAGINE",
    "ÁCIDO ASPÁRTICO": "ASPARTIC ACID",
    "GLUTAMINA": "GLUTAMINE",
    "ÁCIDO GLUTÂMICO": "GLUTAMIC ACID",
    "GLICOSE": "GLUCOSE",
    "DEXTROSE": "GLUCOSE",
    "MANITOL": "MANNITOL",
    "SORBITOL": "SORBITOL",
    "CAFEÍNA": "CAFFEINE",
    "CÂNFORA": "CAMPHOR",
    "MENTOL": "MENTHOL",
    "EUCALIPTOL": "EUCALYPTOL",
    "ETINILESTRADIOL": "ETHINYL ESTRADIOL",
    "ESTRADIOL": "ESTRADIOL",
    "ESTRIOL": "ESTRIOL",
    "PROGESTERONA": "PROGESTERONE",
    "MEDROXIPROGESTERONA": "MEDROXYPROGESTERONE",
    "NORETISTERONA": "NORETHISTERONE",
    "LEVONORGESTREL": "LEVONORGESTREL",
    "DESOGESTREL": "DESOGESTREL",
    "GESTODENO": "GESTODENE",
    "DROSPIRENONA": "DROSPIRENONE",
    "DIENOGESTE": "DIENOGEST",
    "TESTOSTERONA": "TESTOSTERONE",
    "OXANDROLONA": "OXANDROLONE",
    "NANDROLONA": "NANDROLONE",

    # 更多常見藥物翻譯
    "GUAIFENESINA": "GUAIFENESIN",
    "CLAVULANATO": "CLAVULANIC ACID",
    "ÁCIDO CLAVULÂNICO": "CLAVULANIC ACID",
    "BROMOPRIDA": "BROMOPRIDE",
    "DIOSMINA": "DIOSMIN",
    "HESPERIDINA": "HESPERIDIN",
    "TINIDAZOL": "TINIDAZOLE",
    "ALBENDAZOL": "ALBENDAZOLE",
    "MEBENDAZOL": "MEBENDAZOLE",
    "IVERMECTINA": "IVERMECTIN",
    "NITAZOXANIDA": "NITAZOXANIDE",
    "SECNIDAZOL": "SECNIDAZOLE",
    "ORNIDAZOL": "ORNIDAZOLE",
    "TOLNAFTATO": "TOLNAFTATE",
    "CLIQUINOL": "CLIOQUINOL",
    "CLIOQUINOL": "CLIOQUINOL",
    "QUINOSOL": "QUINOSOL",
    "ACEBROFILINA": "ACEBROFILINA",
    "BETAISTINA": "BETAHISTINE",
    "CIPROTERONA": "CYPROTERONE",
    "MEDROXIPROGESTERONA": "MEDROXYPROGESTERONE",
    "BACITRACINA": "BACITRACIN",
    "POLIMIXINA B": "POLYMYXIN B",
    "GRAMICIDINA": "GRAMICIDIN",
    "TIROTRICINA": "TYROTHRICIN",
    "CLOSTEBOL": "CLOSTEBOL",
    "BUTILESCOPOLAMINA": "SCOPOLAMINE BUTYLBROMIDE",
    "BUTILBROMETO": "BUTYLBROMIDE",
    "HIOSCIAMINA": "HYOSCYAMINE",
    "HIOSCINA": "SCOPOLAMINE",
    "ESCOPOLAMINA": "SCOPOLAMINE",
    "FENILBUTAZONA": "PHENYLBUTAZONE",
    "PIROXICAM": "PIROXICAM",
    "TENOXICAM": "TENOXICAM",
    "LORNOXICAM": "LORNOXICAM",
    "CETOPROFENO": "KETOPROFEN",
    "FLURBIPROFENO": "FLURBIPROFEN",
    "CETOROLACO": "KETOROLAC",
    "TROMETAMOL": "TROMETHAMINE",
    "TROMETAMINA": "TROMETHAMINE",
    "LISDEXANFETAMINA": "LISDEXAMFETAMINE",
    "DIMESILATO": "DIMESYLATE",
    "DESVENLAFAXINA": "DESVENLAFAXINE",
    "HEMIFUMARATO": "HEMIFUMARATE",
    "MEDOXOMILA": "MEDOXOMIL",
    "MEDOXOMIL": "MEDOXOMIL",
}


def translate_portuguese_drug_name(name: str) -> str:
    """將葡萄牙語藥名翻譯為英文格式

    例如：
    - "CLORIDRATO DE FLUOXETINA" → "FLUOXETINE HYDROCHLORIDE"
    - "IBUPROFENO SÓDICO" → "IBUPROFEN SODIUM"
    - "ZOLPIDEM HEMITARTARATO" → "ZOLPIDEM HEMITARTRATE"

    Args:
        name: 葡萄牙語藥名

    Returns:
        英文格式藥名
    """
    if not name:
        return ""

    name = name.upper().strip()

    # 處理前綴形式 "CLORIDRATO DE X" → "X HYDROCHLORIDE"
    for pt_prefix, en_suffix in PT_TO_EN_SALT_PREFIX.items():
        pattern = rf"^{re.escape(pt_prefix)}\s+(.+)$"
        match = re.match(pattern, name)
        if match:
            base_name = match.group(1).strip()
            # 遞迴處理剩餘部分（可能還有後綴）
            base_name = translate_portuguese_drug_name(base_name)
            return f"{base_name} {en_suffix}"

    # 處理後綴形式（離子形式）
    for pt_suffix, en_suffix in PT_TO_EN_SALT_SUFFIX.items():
        if name.endswith(" " + pt_suffix) or name.endswith(pt_suffix):
            # 移除葡萄牙語後綴
            if name.endswith(" " + pt_suffix):
                base = name[:-len(pt_suffix)-1].strip()
            else:
                # 可能是組合詞如 "NAPROXENO SÓDICO"
                base = re.sub(rf"\s*{re.escape(pt_suffix)}$", "", name).strip()
            if base:
                # 遞迴翻譯基本名稱
                base = translate_portuguese_drug_name(base)
                return f"{base} {en_suffix}"

    # 處理水合物形式
    for pt_hydrate, en_hydrate in PT_TO_EN_HYDRATE.items():
        if pt_hydrate in name:
            name = name.replace(pt_hydrate, en_hydrate)

    # 翻譯藥物名稱本身
    # 先嘗試完全匹配
    if name in PT_TO_EN_DRUG_NAMES:
        return PT_TO_EN_DRUG_NAMES[name]

    # 嘗試匹配包含鹽類的情況，如 "FLUOXETINA HYDROCHLORIDE"
    # 先處理可能已經部分翻譯的名稱
    words = name.split()
    translated_words = []
    for word in words:
        if word in PT_TO_EN_DRUG_NAMES:
            translated_words.append(PT_TO_EN_DRUG_NAMES[word])
        else:
            translated_words.append(word)
    translated_name = " ".join(translated_words)

    return translated_name


def normalize_ingredient(name: str) -> str:
    """標準化單一成分名稱

    處理邏輯：
    1. 移除括號內的同義詞（EQ TO ...）
    2. 移除其他括號內容（如 VIT B2）
    3. 翻譯葡萄牙語藥名
    4. 統一大小寫
    5. 移除多餘空白

    Args:
        name: 原始成分名稱

    Returns:
        標準化後的名稱
    """
    if not name:
        return ""

    # 統一全形括號為半形
    name = name.replace("（", "(").replace("）", ")")

    # 移除括號內容（包含 EQ TO 的同義詞、VIT 等）
    # 但保留括號前的主名稱
    name = re.sub(r"\s*\([^)]*\)", "", name)

    # 移除鹽類後綴的多餘資訊（保留鹽類如 HCL, SODIUM 等）
    name = name.strip()

    # 統一大寫
    name = name.upper()

    # 翻譯葡萄牙語
    name = translate_portuguese_drug_name(name)

    # 移除多餘空白
    name = re.sub(r"\s+", " ", name)

    return name.strip()


def extract_ingredients(ingredient_str: str) -> List[str]:
    """從主成分欄位提取所有成分

    支援多種分隔符號：
    - 巴西 ANVISA: 逗號 (,)
    - 台灣 FDA: 分號 (;) 或 (;;)

    Args:
        ingredient_str: 主成分欄位原始值

    Returns:
        標準化後的成分列表
    """
    if not ingredient_str:
        return []

    # 統一分隔符號
    # 台灣: ;; 或 ;
    # 巴西: , (但需避免切割 "SODIUM, POTASSIUM" 等)
    ingredient_str = ingredient_str.replace(";;", ";").replace("；", ";")

    # 先嘗試分號分隔
    if ";" in ingredient_str:
        parts = ingredient_str.split(";")
    else:
        # 使用逗號分隔（巴西格式）
        parts = ingredient_str.split(",")

    # 標準化每個成分
    ingredients = []
    for part in parts:
        normalized = normalize_ingredient(part)
        if normalized and normalized not in ingredients:
            ingredients.append(normalized)

    return ingredients


def extract_primary_ingredient(ingredient_str: str) -> str:
    """提取主要成分（第一個成分）

    Args:
        ingredient_str: 主成分略述欄位原始值

    Returns:
        主要成分名稱（標準化後）
    """
    ingredients = extract_ingredients(ingredient_str)
    return ingredients[0] if ingredients else ""


def extract_base_name(name: str) -> Optional[str]:
    """從藥名中提取基本名稱（移除鹽類形式）

    例如：
    - "FLUOXETINE HYDROCHLORIDE" → "FLUOXETINE"
    - "IBUPROFEN SODIUM" → "IBUPROFEN"

    Args:
        name: 標準化後的藥名

    Returns:
        基本名稱，若無法提取則返回 None
    """
    if not name:
        return None

    name = name.upper().strip()

    # 英文鹽類後綴列表（按長度排序，先匹配較長的）
    en_salt_suffixes = [
        # 長後綴優先
        " LAURYL SULFATE",
        " DIHYDROCHLORIDE",
        " TRIHYDROCHLORIDE",
        " HYDROCHLORIDE",
        " HEMITARTRATE",
        " BITARTRATE",
        " DIPROPIONATE",
        " SESQUIHYDRATE",
        " HEXAHYDRATE",
        " TRIHYDRATE",
        " DIHYDRATE",
        " HEMIHYDRATE",
        " MONOHYDRATE",
        " ANHYDROUS",
        " UNDECANOATE",
        " ENANTHATE",
        " CYPIONATE",
        " DECANOATE",
        " HEXANOATE",
        " XINAFOATE",
        " GLUCONATE",
        " CARBONATE",
        " BICARBONATE",
        " SUCCINATE",
        " GLUTAMATE",
        " ASPARTATE",
        " PALMITATE",
        " STEARATE",
        " EMBONATE",
        " PAMOATE",
        " BUTYRATE",
        " OROTATE",
        " VALERATE",
        " PIVALATE",
        " ACETATE",
        " FUROATE",
        " OLEATE",
        " SULFATE",
        " BISULFATE",
        " CITRATE",
        " LACTATE",
        " NITRATE",
        " OXALATE",
        " MALEATE",
        " TARTRATE",
        " FUMARATE",
        " MESYLATE",
        " BESYLATE",
        " TOSYLATE",
        " BENZOATE",
        " BROMIDE",
        " CHLORIDE",
        " IODIDE",
        " PHOSPHATE",
        " HYDROXIDE",
        " ACETONIDE",
        " PROPIONATE",
        " TRISODIUM",
        " DISODIUM",
        " SODIUM",
        " POTASSIUM",
        " CALCIUM",
        " MAGNESIUM",
        " ALUMINUM",
        " AMMONIUM",
        " MEGLUMINE",
        " FERRIC",
        " FERROUS",
        " ZINC",
        " OXIDE",
        " HCL",
        " HBR",
    ]

    base = name
    for suffix in en_salt_suffixes:
        if base.endswith(suffix):
            base = base[:-len(suffix)].strip()
            break

    # 如果成功移除了後綴，返回基本名稱
    if base != name and base:
        return base

    return None


def generate_synonyms(name: str) -> List[str]:
    """為藥名生成可能的同義詞

    包括：
    1. 移除鹽類後綴的基本名稱
    2. 原始葡萄牙語名稱
    3. 常見別名

    Args:
        name: 標準化後的藥名

    Returns:
        同義詞列表
    """
    synonyms = []

    # 提取基本名稱
    base = extract_base_name(name)
    if base and base != name:
        synonyms.append(base)

    # L-/D-/DL- 前綴處理
    for prefix in ["L-", "D-", "DL-", "LEVO", "DEXTRO"]:
        if name.startswith(prefix):
            without_prefix = name[len(prefix):].strip()
            if without_prefix and without_prefix not in synonyms:
                synonyms.append(without_prefix)

    return synonyms


def get_all_synonyms(ingredient_str: str) -> List[Tuple[str, List[str]]]:
    """提取成分及其所有同義詞

    從括號中的 EQ TO 提取同義詞，並自動生成常見變體

    Args:
        ingredient_str: 主成分欄位原始值

    Returns:
        [(主名稱, [同義詞列表]), ...]
    """
    if not ingredient_str:
        return []

    # 統一分隔符號
    ingredient_str = ingredient_str.replace(";;", ";").replace("；", ";")

    # 選擇分隔符
    if ";" in ingredient_str:
        parts = ingredient_str.split(";")
    else:
        parts = ingredient_str.split(",")

    results = []
    for part in parts:
        part = part.strip()
        if not part:
            continue

        # 統一括號
        part = part.replace("（", "(").replace("）", ")")

        # 提取主名稱（括號前的部分）
        main_match = re.match(r"^([^(]+)", part)
        if not main_match:
            continue

        raw_name = main_match.group(1).strip().upper()
        raw_name = re.sub(r"\s+", " ", raw_name)

        # 翻譯葡萄牙語
        main_name = translate_portuguese_drug_name(raw_name)

        synonyms = []

        # 如果翻譯後不同，原名也是同義詞
        if raw_name != main_name:
            synonyms.append(raw_name)

        # 提取所有 EQ TO 同義詞（台灣格式）
        eq_matches = re.findall(r"EQ TO\s+([^)]+)", part, re.IGNORECASE)
        for match in eq_matches:
            syn = match.strip().upper()
            syn = re.sub(r"\s+", " ", syn)
            syn = re.sub(r"\s*\(.*$", "", syn)
            if syn and syn != main_name and syn not in synonyms:
                synonyms.append(syn)

        # 生成額外同義詞（移除鹽類等）
        extra_synonyms = generate_synonyms(main_name)
        for syn in extra_synonyms:
            if syn not in synonyms and syn != main_name:
                synonyms.append(syn)

        results.append((main_name, synonyms))

    return results
