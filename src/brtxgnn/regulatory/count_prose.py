"""正文許可證張數的程式改寫（2026-11-24 建，用戶決定；做法照 KrTxGNN／MyTxGNN 同名檔，規則是本站葡萄牙文句型）。

正文裡「N registros válidos／N de M registros válidos／Dos N registros, V estão válidos／V válidos e C cancelados」這類 ANVISA 登記張數敘述，
由程式依許可證快照（snapshots/br_licenses.json.gz 的 facts）改寫，每週資料更新後跟著改，不逐筆寫查核紀錄（同 Tw／Kr／My：程式改寫的張數
敘述是程式產生的正文）。

只改「句型明確、數字確定是本藥登記張數」的地方，其餘一律不動：
  - 句子要有登記名詞（registro(s)、licença(s)、autorização／autorizações），而且沒有試驗、文獻、交互作用等字樣。
  - 跳過：查核框（<!-- review -->）、程式許可證區塊（<!-- licenses -->）、表格列、標題、front matter；
    查核紀錄 replacement／anchor 所在的句子（改了紀錄會對不上）。
  - 整句不動（列在 skipped）：有保留（pelo menos、parcial、incompleta、pode…）、講證據包或查詢結果（Evidence Pack、consulta、
    retornou、encontrad、localizad…；「segundo os dados compilados」＝事實層同一份資料，不算）、相對數（outros、demais、restantes、além…、adicionais）、劑型或廠商子集（comprimido、
    injetável、solução…、empresa、laboratório…）、單方／複方子集（isolado、associação…）；事實層 partial 的頁整頁不動。
  - 數字不動：顯示筆數（tabela、acima、abaixo、listad、exibid、principais、exemplos…）、文字數詞（um、dois… 跟冠詞分不開，不改）、
    劑量與年份。
角色看數字前後：cancelad／caducad／inativ／vencid／revogad→註銷；válid／vigente／ativ→有效；「X de Y」的 Y、「Dos N」「total de N」
「Todos os N」→總數；後面直接接登記名詞→總數（同一句另有明確的有效／註銷數字時確定是總數，否則總數或有效數兩種讀法都算對）。
數字已等於該角色的任一合理讀法就不動；不等於時兩種讀法相同才改，不同就列為 ambiguous。
原數字是 0（建立在 0 張前提上）不改、列為 zero-premise；改寫會跨過 1（葡萄牙文單複數 registro／registros、válido／válidos 要跟著變）
不改、列為 plural；要改請寫查核紀錄。
前提檢查：句子說「todos／ambos … válidos」「nenhum cancelado」而事實不符時整句不動、列為 premise。
同一行只要有一句含登記數字而被略過，整行都不動（免得前後句數字對不上）。
"""
from __future__ import annotations

import re

from .site_config import C

MARKET = re.compile(C["MARKET_RE"])
SENT_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-ZÁÉÍÓÚÂÊÔÃÕÇ*\[(>-])")
# 數字：不在字中、不是小數或千分位的一部分；句尾的「12.」算（句點後不是數字）
NUM = re.compile(r"(?<![\w.,/-])(\d+)(?![\w,/%-]|[.,]\d)")
NOUN = r"(?:registros?|licen[çc]as?|autoriza[çc](?:ão|ões))"
LICENSE = re.compile(r"\b(?:registros?|licen[çc]as?|autoriza[çc](?:ão|ões))\b", re.I)
NOT_LICENSE = re.compile(r"intera[çc]|ensaio|estudo|artigo|PMID|NCT|ReBEC|ClinicalTrials|paciente|casos?\b|evento|efeito|\bmg\b|\bml\b|%|"
                         r"\banos?\b|\bmeses\b|\bsemanas?\b|\bdias?\b|candidat|previs|pontua|score|literatura|publica", re.I)
HEDGED = re.compile(r"pelo menos|no m[íi]nimo|ao menos|parcia|incomplet|\bpode\b|\bpodem\b|Evidence Pack|pacote|consulta|"
                    r"retorn|encontrad|localizad|identificad|recuperad|\boutr[oa]s?\b|\bdemais\b|restantes|\balém\b|adiciona|"
                    r"incluindo|entre eles|dentre|veterin|export|fabricante|empresa|laborat|Ltda|S\.A\.|detentor|"
                    r"comprimid|c[áa]psul|injet[áa]ve|solu[çc]|pomada|creme|\bgel\b|col[íi]rio|xarope|suspens|spray|adesivo|ampola|"
                    r"frasco|forma farmac|apresenta[çc]|isolad|associa[çc]|combina[çc]|princ[íi]pio ativo [úu]nico|monof[áa]rmac|"
                    r"nome comercial|marca|gen[ée]ric|similar", re.I)
DISPLAY = re.compile(r"tabela|acima|abaixo|listad|\blista\b|exibid|mostrad|\bmostra|exemplo|principais|seguintes|a seguir|detalhad", re.I)
VALIDW = r"(?:v[áa]lid[oa]s?|vigentes?|ativ[oa]s?)"
CANCW = r"(?:cancelad[oa]s?|caducad[oa]s?|inativ[oa]s?|vencid[oa]s?|revogad[oa]s?)"
BLOCK = re.compile(r"<!-- (review|licenses):begin.*?<!-- \1:end[^>]*-->", re.S)
VERB = r"(?:(?:est[áa]|est[ãa]o|[ée]|s[ãa]o|encontra-se|encontram-se|permanece|permanecem|consta|constam|figura|figuram|segue|seguem|t[êe]m|tem)\s+(?:licen[çc]as?\s+|registros?\s+)?)?"


def _role(s, a, b):
    left, right = s[max(0, a - 30):a], s[b:b + 60]
    lo, ro = left.lower(), right.lower()
    if DISPLAY.search(lo[-25:]):
        return "display"
    # 「X de Y」「válidos de Y」「totalizando Y」的 Y＝總數
    if re.search(r"\d+\)?\s+de\s+(um\s+total\s+de\s+)?$", lo) or re.search(VALIDW + r"\s+de\s+$", lo) \
            or re.search(r"(totalizando|totalizam|totaliza|total de|num total de|no total de)\s+$", lo):
        return "total"
    # 「X dos Y registros são válidos」的 Y＝總數（有動詞）；「X dos Y registros válidos」（沒有動詞）的 Y＝有效數，照下面的規則
    if re.search(r"\d+\s+d[oa]s\s+$", lo) and re.match(r"\s*" + NOUN + r"\s+(?:\w+\s+)?(?:s[ãa]o|est[ãa]o|encontram-se|constam|permanecem|t[êe]m)\b", ro):
        return "total"
    # 「X de Y registros válidos」「(X de Y) estão válidos」的 X＝有效數
    if re.match(r"\s*de\s+\d+\)?\s*(?:" + NOUN + r"\s+)?(?:\w+\s+)?" + VERB + r"(?:\*\*)?" + VALIDW + r"\b", ro):
        return "valid"
    if re.match(r"\s*de\s+\d", ro):
        return "display" if DISPLAY.search(ro[:60]) else None
    if re.match(r"\s*(?:" + NOUN + r"\s+)?(?:(?!(?:v[áa]lid|vigent|ativ))\w+\s+)?" + VERB + r"(?:\*\*)?" + CANCW + r"\b", ro):
        return "cancelled"
    if re.match(r"\s*(?:" + NOUN + r"\s+)?(?:\w+\s+)?" + VERB + r"(?:\*\*)?" + VALIDW + r"\b", ro):
        return "valid"
    if re.match(r"\s*\*{0,2}\s*" + NOUN + r"\b", ro) or re.search(r"(há|existem|constam|total de|dos|das|todos os|todas as)\s+\*{0,2}$", lo):
        return "total"
    return None


def _readings(role, f, explicit=False):
    t, v, c = f.get("total"), f.get("valid"), f.get("cancelled")
    if role == "cancelled":
        return {c}, c
    if role == "valid":
        return {v}, v
    if explicit:  # 同一句另有明確的有效／註銷數字：沒有限定詞的那個就是總數
        return {t}, t
    return {t, v}, t if t == v else None


def _premise_ok(sent, f):
    lo = sent.lower()
    if re.search(r"\b(todos|todas|ambos|ambas)\b[^.]{0,40}" + VALIDW + r"|nenhum\w*\s+(\w+\s+){0,2}(est[áa]\s+|foi\s+)?" + CANCW +
                 r"|sem\s+(registros?\s+)?cancelad|\b0\s+cancelad", lo) and (f.get("valid") != f.get("total") or f.get("cancelled")):
        return False
    if re.search(r"\b(os|as|seus|suas)\s+\d+\s+" + NOUN + r"\b[^.;]{0,40}?\b(est[ãa]o|s[ãa]o|encontram-se|constam|permanecem)\s+(como\s+)?(\*\*)?" + VALIDW, lo) \
            and (f.get("valid") != f.get("total") or f.get("cancelled")):
        return False  # 「Os N registros (…) estão válidos」＝全部有效
    if re.search(r"\b(todos|todas|ambos|ambas)\b[^.]{0,40}" + CANCW, lo) and f.get("valid"):
        return False
    return True


def rewrite_sentence(sent, f):
    """回傳 (新句子, 跳過理由或 None)。"""
    if not NUM.search(sent) or not LICENSE.search(sent):
        return sent, None
    if NOT_LICENSE.search(sent):
        return sent, None
    # 4 位數以上（登記號、年份）不是張數
    found = [(m, _role(sent, m.start(), m.end())) for m in NUM.finditer(sent) if len(m.group(1)) <= 3]
    if not any(r not in (None, "display") for _, r in found):
        return sent, None
    if HEDGED.search(sent):
        return sent, "hedged/subset"
    explicit = any(r in ("valid", "cancelled") for _, r in found)
    subs = []
    for m, role in found:
        if role in (None, "display"):
            continue
        old = int(m.group(1))
        ok, v = _readings(role, f, explicit)
        if old in ok:
            continue
        if v is None:
            return sent, "ambiguous"
        if old == 0:
            return sent, "zero-premise"
        if (old == 1) != (v == 1) and not re.match(r"\s*(?:[).,;:]|$)", sent[m.end():]):
            return sent, "plural"  # 後面接名詞／形容詞／動詞：單複數要跟著變
        subs.append((m, v))
    if not subs:
        return sent, None
    if not _premise_ok(sent, f):
        return sent, "premise"
    out, pos = [], 0
    for m, v in subs:
        out.append(sent[pos:m.start(1)])
        out.append(str(v))
        pos = m.end(1)
    out.append(sent[pos:])
    return "".join(out), None


def _line(ln, f, protect, skipped):
    if ln.startswith(("|", "#", "{:")) or not ln.strip():
        return ln
    parts = SENT_SPLIT.split(ln)
    seps = SENT_SPLIT.findall(ln)
    new, held = [], False
    for s in parts:
        if any(p and (p in s or s in p) for p in protect):
            new.append(s)
            continue
        ns, why = rewrite_sentence(s, f)
        if why:
            skipped.append((why, s.strip()))
            held = True
        new.append(ns)
    if held:  # 同一行有句子判斷不了：整行不動，免得改了一句、旁邊的句子對不上
        return ln
    out = new[0]
    for sep, s in zip(seps, new[1:]):
        out += sep + s
    return out


def rewrite(text, facts, protect=()):
    """text：整頁 markdown。facts：快照的 facts。回傳 (新內容, skipped)。front matter、查核框、程式區塊、表格、查核紀錄表不動。"""
    skipped = []
    if not facts or facts.get("partial") or facts.get("total") is None:
        return text, skipped
    protect = [p.strip() for p in protect if p and len(p.strip()) >= 6]
    fm_end = 0
    if text.startswith("---"):
        j = text.find("\n---", 3)
        fm_end = j + 4 if j > 0 else 0
    body = text[fm_end:]
    keep = []

    def hold(m):
        keep.append(m.group(0))
        return f"\x00{len(keep) - 1}\x00"
    body = BLOCK.sub(hold, body)
    lines, frozen = [], False
    for ln in body.split("\n"):
        if ln.startswith("## "):  # 查核紀錄表與免責聲明（程式產生）之後不改
            frozen = frozen or ln.startswith(C["T"]["log_head"]) or bool(re.match(r"## (?:" + C["T"]["disclaimer_re"] + ")", ln))
        lines.append(ln if ("\x00" in ln or frozen) else _line(ln, facts, protect, skipped))
    body = re.sub(r"\x00(\d+)\x00", lambda m: keep[int(m.group(1))], "\n".join(lines))
    return text[:fm_end] + body, skipped
