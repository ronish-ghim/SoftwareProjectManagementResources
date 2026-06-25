"""
extract_structured_notes.py — Extract structured markdown notes from SPM class PDFs.
"""

import fitz, os, re, sys, unicodedata

BASE = r"C:\Users\Rons\OneDrive\Desktop\CSIT\7th Sem\SPM"
CLASS_DIR = os.path.join(BASE, "Class_notes")
NOTES_DIR = os.path.join(BASE, "notes")
ASSETS_DIR = os.path.join(NOTES_DIR, "assets")
DECORATIVE_THRESHOLD = 10
BULLET_RE = re.compile("[\uf097\uf0d8\uf020\u2022]")

SKIP_TITLES = {
    "Syllabus", "Evaluation Process", "DISCLAIMER", "Disclaimer",
    "Course Instructor", "Course Overview and",
    "Text Books", "Reference Books", "References", "Assignment-I",
}

CHAPTER_INFO = {
    1: {"title": "Introduction to Software Project Management", "hours": "5 Hrs.", "pdf": "Chapter_1_Introduction to Software Project Management.pdf"},
    2: {"title": "Project Analysis", "hours": "8 Hrs.", "pdf": "Chapter_2_Project Analysis.pdf"},
    3: {"title": "Activity Planning and Scheduling", "hours": "7 Hrs.", "pdf": "Chapter_3_Activity Planning and Scheduling.pdf"},
    4: {"title": "Risk Management", "hours": "4 Hrs.", "pdf": "Chapter_4_Risk Management.pdf"},
    5: {"title": "Resource Allocation", "hours": "4 Hrs.", "pdf": "Chapter_5_Resource Allocation.pdf"},
    6: {"title": "Monitoring and Control", "hours": "4 Hrs.", "pdf": "Chapter_6_Monitoring and Control.pdf"},
    7: {"title": "Managing Contracts and People", "hours": "5 Hrs.", "pdf": "Chapter_7_Managing Contract and People.pdf"},
    8: {"title": "Software Quality Assurance and Testing", "hours": "5 Hrs.", "pdf": "Chapter_8_ Software Quality Assurance and Testing.pdf"},
    9: {"title": "Software Configuration Management", "hours": "3 Hrs.", "pdf": "Chapter_9_Software Configuration Management.pdf"},
}

# Chapter structure: list of (heading_level, heading_title, [slide_title_patterns])
# Each entry maps a syllabus topic to a heading with its slide groups.
CHAPTER_STRUCT = {
    1: [
        ("##", "Software Engineering and Software Product", [
            "Introduction", "About Software Project", "About Software Project Management",
        ]),
        ("##", "Objectives of SPM", [
            "Objectives of SPM",
        ]),
        ("##", "Software Project: Definition and Characteristics", [
            "Some Project Initiatives", "Project Parameters", "Project Objectives",
            "Project Objective", "Classification of Projects",
            "According to Source of Capital", "According to Project Content",
            "According to its Involvement", "According to its Objectives",
            "Software Project", "Software Project vs Other Projects",
        ]),
        ("##", "Categories of Software Projects", [
            "Categories of Software Project",
        ]),
        ("##", "Project Manager", [
            "Project Manager", "Skills of Project Manager", "Roles & Responsibilities",
        ]),
        ("##", "Project Management", [
            "Project Management", "Project Management Objectives",
            "Why Project Management", "Advantages of Project Management",
        ]),
        ("##", "Activities Covered by SPM", [
            "Activities Covered by Software", "Activities Covered by SPM",
        ]),
        ("##", "Project Management Cycle", [
            "Project Management Life Cycle", "Project Life Cycle",
        ]),
        ("###", "Initiation Phase", [
            "Initiation", "Steps in Initiation Phase",
        ]),
        ("###", "Planning Phase", [
            "Planning", "Steps for the Planning Phase",
        ]),
        ("###", "Execution Phase", [
            "Execution", "Steps in Execution Phase",
        ]),
        ("###", "Closure Phase", [
            "Closure Phase", "Steps in Closure Phase",
        ]),
        ("##", "SPM Framework", [
            "SPM Framework",
        ]),
        ("##", "Types of Project Plan", [
            "Project Plan", "Types of Project Plan",
        ]),
    ],
    2: [
        ("##", "Introduction to Project Analysis", [
            "Introduction",
        ]),
        ("##", "Strategic Assessment", [
            "Strategic Assessment", "SA Programme Management", "SA Portfolio Management",
        ]),
        ("##", "Technical Assessment", [
            "Technical Assessment",
        ]),
        ("##", "Economic Analysis", [
            "Economical Assessment",
        ]),
        ("###", "Present Worth Method", [
            "Present Worth Method", "Present Worth Method Example",
        ]),
        ("###", "Future Worth Method", [
            "Future Worth Method", "Future Worth Method Example",
        ]),
        ("###", "Annual Worth Method", [
            "Annual Worth Method", "Annual Worth Method Example",
        ]),
        ("###", "Internal Rate of Return (IRR)", [
            "Internal Rate of Return",
        ]),
        ("###", "Benefit-Cost Ratio (BCR)", [
            "Benefit-Cost Ratio",
        ]),
        ("###", "Uniform Gradient Cash Flow", [
            "Uniform Gradient",
        ]),
        ("###", "Comparison of Mutually Exclusive Alternatives", [
            "Mutually Exclusive",
        ]),
        ("####", "Numerical Examples", [
            "Numerical",
        ]),
    ],
    3: [
        ("##", "Objectives of Activity Planning", [
            "Process and Activity", "Introduction to Activity", "Activity Attributes",
            "Activity Sequencing", "Activity Planning", "Objectives of Activity Planning",
            "When to Start Activity Planning", "Different Levels of Plans",
        ]),
        ("##", "Identifying Activities", [
            "Identifying Activity", "Activity Based Approach",
        ]),
        ("##", "Work Breakdown Structure (WBS)", [
            "Work Breakdown Structure", "Product Based Approach", "Hybrid Approach",
        ]),
        ("##", "Bar Chart (Gantt Chart)", [
            "Bar Chart", "Gantt Chart",
        ]),
        ("##", "Network Planning Models", [
            "Network Planning", "Network Diagram",
        ]),
        ("###", "Critical Path Method (CPM)", [
            "Critical Path Method", "CPM",
        ]),
        ("###", "Program Evaluation and Review Technique (PERT)", [
            "Program Evaluation", "PERT",
        ]),
        ("###", "Precedence Diagramming Method (PDM)", [
            "Precedence Diagramming", "PDM",
        ]),
        ("##", "Shortening Project Duration", [
            "Shortening Project Duration", "Crashing",
        ]),
        ("##", "Identifying Critical Activities", [
            "Identifying Critical Activities",
        ]),
    ],
    4: [
        ("##", "Introduction to Risk Management", [
            "Risk",
        ]),
        ("##", "Types of Risk", [
            "Types of Risk",
        ]),
        ("##", "Risk Identification", [
            "Identify Risks", "Identify Risk",
        ]),
        ("##", "Risk Analysis", [
            "Risk Analysis", "Qualitative Risk Analysis",
            "Quantitative Risk Analysis",
        ]),
        ("##", "Risk Evaluation Using Z-Values", [
            "Evaluation of Risk",
        ]),
        ("##", "Risk Response and Control", [
            "Risk Avoidance", "Risk Mitigation", "Risk Monitoring",
            "Project Risk Management", "Plan Risk Management",
            "Risk Management Plan",
        ]),
    ],
    5: [
        ("##", "Identifying Resource Requirements", [
            "Resource", "Types of Resource", "Identifying Resource Requirement",
            "Resource Planning", "Resource Organization",
        ]),
        ("##", "Resource Allocation", [
            "Resource Allocation", "Issues in Resource Allocation",
        ]),
        ("##", "Resource Scheduling", [
            "Resource Scheduling",
        ]),
        ("##", "Resource Smoothing", [
            "Resource Smoothing",
        ]),
        ("##", "Resource Balancing", [
            "Resource Balancing", "Resource Leveling",
            "Smoothing vs Leveling",
        ]),
    ],
    6: [
        ("##", "Introduction to Monitoring and Control", [
            "Introduction", "Project Monitoring",
        ]),
        ("##", "Collecting Data", [
            "Setting Check Points", "Collecting Data",
            "Partial Completion Report", "Risk Report",
            "Visualizing Progress",
        ]),
        ("##", "Visualizing Progress", [
            "Gantt Chart", "Slip Chart", "Ball Chart",
        ]),
        ("##", "Cost Monitoring", [
            "Cost Monitoring", "Cost Schedule",
        ]),
        ("##", "Earned Value Analysis", [
            "Earned Value", "EVA",
        ]),
        ("##", "Project Control", [
            "Project Control",
        ]),
    ],
    7: [
        ("##", "Introduction to Contracts", [
            "Introduction", "Contract",
        ]),
        ("##", "Types of Contract", [
            "Types of Contract",
        ]),
        ("###", "Fixed-Price Contract", [
            "Fixed-Price", "Fixed Price",
        ]),
        ("###", "Cost Reimbursable Contract", [
            "Cost Reimbursable",
        ]),
        ("###", "Time and Material Contract", [
            "Time and Material", "Time & Material",
        ]),
        ("###", "Software Development Subscription", [
            "Subscription", "SDS",
        ]),
        ("##", "Stages in Contract", [
            "Stages in Contract",
        ]),
        ("###", "Contract Creation", [
            "Creation",
        ]),
        ("###", "Negotiation and Collaboration", [
            "Negotiation",
        ]),
        ("###", "Review and Approval", [
            "Review and Approval",
        ]),
        ("###", "Administration and Execution", [
            "Administration", "Execution",
        ]),
        ("###", "Ongoing Management and Renewal", [
            "Ongoing Management", "Renewal",
        ]),
        ("###", "Reporting and Tracking", [
            "Reporting",
        ]),
        ("##", "Contract Placement", [
            "Placement",
        ]),
        ("##", "Typical Terms of a Contract", [
            "Typical Terms",
        ]),
        ("##", "Contract Management", [
            "Contract Management",
        ]),
        ("##", "Acceptance", [
            "Acceptance",
        ]),
        ("##", "Managing People", [
            "Managing People", "Managing People and Organizing",
        ]),
        ("###", "Understanding Behavior", [
            "Understanding Behavior",
        ]),
        ("###", "Selecting the Right Person", [
            "Selecting the Right Person",
        ]),
        ("###", "Motivation", [
            "Motivation",
        ]),
        ("###", "Working in Groups and Teams", [
            "Working in Groups", "Becoming a Team",
        ]),
        ("###", "Decision Making", [
            "Decision Making",
        ]),
        ("###", "Leadership", [
            "Leadership",
        ]),
        ("###", "Organizational Structures", [
            "Organizational Structures", "Organizational Structure",
        ]),
    ],
    8: [
        ("##", "Testing Principles and Objectives", [
            "Testing", "Principles of Testing",
            "Software Testing Principles", "Objective of Testing",
        ]),
        ("##", "Test Plan and Test Case", [
            "Test Case", "Test Plan",
        ]),
        ("##", "Types of Testing", [
            "Types of Testing",
        ]),
        ("##", "Levels of Testing", [
            "Level of Testing",
        ]),
        ("###", "Unit Testing", [
            "Unit Testing",
        ]),
        ("###", "Integration Testing", [
            "Integration Testing",
        ]),
        ("###", "System Testing", [
            "System Testing",
        ]),
        ("###", "Acceptance Testing", [
            "Acceptance Testing",
        ]),
        ("##", "Test Strategies", [
            "Testing Strategies", "Test Strategies",
        ]),
        ("##", "Verification and Validation", [
            "Verification", "Validation",
        ]),
        ("##", "Software Quality", [
            "Software Quality",
        ]),
        ("##", "SEI-CMM", [
            "SEI-CMM", "CMM",
        ]),
        ("##", "SQA Activities and Plan", [
            "SQA Activities", "QA Organization",
            "SQA Plan",
        ]),
    ],
    9: [
        ("##", "Introduction to SCM", [
            "Introduction", "Software Configuration Management",
        ]),
        ("##", "Need for SCM", [
            "Need of SCM",
        ]),
        ("##", "Basic Configuration Management", [
            "SCM Basic Configuration", "Basic Configuration",
        ]),
        ("##", "SCM Roles and Responsibilities", [
            "SCM Role", "SCM Responsibilities",
        ]),
        ("##", "Management Responsibilities", [
            "Management Function",
        ]),
        ("##", "Baseline", [
            "Baseline",
        ]),
    ],
}

def slugify(text):
    s = re.sub(r"[^\w\s-]", "", text.lower().strip())
    return re.sub(r"[\s_]+", "_", s)[:60]

def dedup_phrases(text):
    words = text.split()
    if len(words) < 4: return text
    for n in range(min(5, len(words)//2), 0, -1):
        i = 0
        while i + 2*n <= len(words):
            if words[i:i+n] == words[i+n:i+2*n]:
                words = words[:i+n] + words[i+2*n:]
                continue
            i += 1
    return ' '.join(words)

def normalize_unicode(text):
    """Normalize problematic Unicode to ASCII equivalents."""
    text = re.sub(r"[\u00B2]", "^2", text)
    text = re.sub(r"[\u00B3]", "^3", text)
    text = re.sub(r"[\u00B9]", "^1", text)
    text = re.sub(r"[\u2070]", "^0", text)
    text = re.sub(r"[\u2074]", "^4", text)
    text = re.sub(r"[\u2075]", "^5", text)
    text = re.sub(r"[\u2076]", "^6", text)
    text = re.sub(r"[\u2077]", "^7", text)
    text = re.sub(r"[\u2078]", "^8", text)
    text = re.sub(r"[\u2079]", "^9", text)
    text = unicodedata.normalize("NFKD", text)
    reps = {
        "\u2010": "-", "\u2011": "-", "\u2012": "-", "\u2013": "-",
        "\u2014": "-", "\u2015": "-", "\u2016": "||",
        "\u2025": "..", "\u2027": ".",
        "\u2032": "'", "\u2033": "''",
        "\u2212": "-",           # MINUS SIGN
        "\u2018": "'", "\u2019": "'",  # Curly single quotes
        "\u201C": '"', "\u201D": '"',  # Curly double quotes
        "\u00B4": "",            # ACUTE ACCENT (PDF multiplication artifact)
        "\uff0d": "-", "\uff5e": "~",
    }
    for old, new in reps.items():
        text = text.replace(old, new)
    text = re.sub(r"[\ue000-\uf8ff]", "", text)
    text = re.sub(r"[\u2000-\u200f]", " ", text)
    text = re.sub(r"[\u0300-\u036f]", "", text)
    return text

def format_spans(spans):
    """Detect bold/italic fonts from PDF spans and wrap in markdown.
    Merges consecutive spans with the same formatting to avoid fragmentation."""
    if not spans:
        return ""
    groups = []
    cur_bold = None
    cur_italic = None
    buf = ""
    bullet = False
    for i, s in enumerate(spans):
        font = s["font"]
        bold = "Bold" in font or "bold" in font
        italic = "Italic" in font or "italic" in font or "Oblique" in font or s["flags"] & 2
        t = normalize_unicode(s["text"])
        # Detect bullet in first span
        if i == 0 and BULLET_RE.match(t):
            bullet = True
            t = BULLET_RE.sub("", t)
        if (bold, italic) == (cur_bold, cur_italic):
            buf += t
        else:
            if buf:
                groups.append((cur_bold, cur_italic, buf))
            cur_bold, cur_italic = bold, italic
            buf = t
    if buf:
        groups.append((cur_bold, cur_italic, buf))
    parts = []
    for bold, italic, t in groups:
        if not t:
            continue
        if bold and italic:
            parts.append("***" + t + "***")
        elif bold:
            parts.append("**" + t + "**")
        elif italic:
            parts.append("*" + t + "*")
        else:
            parts.append(t)
    text = ("\u2022" if bullet else "") + "".join(parts)
    return text

def norm_bullets(text):
    text = BULLET_RE.sub("\u2022", text)
    return normalize_unicode(text)

def is_bullet_line(s):
    return s and s[0] == "\u2022"

def is_fragment(s):
    s = s.strip()
    if not s or len(s) < 3: return True
    if s in (")", "(", ").", ".)", "-", "--", ",", ":", ";", "..."): return True
    if re.match(r"^\([a-zA-Z ]+\)$", s) and len(s) < 30: return True
    if s.startswith(")") and len(s) < 20: return True
    if s.endswith("(") and len(s) < 20: return True
    return False

def clean_heading(t):
    return re.sub(r"\s+", " ", t.replace("_", " ")).strip().rstrip(":")

def strip_md_fmt(text):
    """Remove markdown bold/italic markers from text (for formula content)."""
    return re.sub(r'\*{1,3}([^*]+)\*{1,3}', r'\1', text)

def looks_like_formula(s):
    """Detect if text is a mathematical formula vs prose."""
    plain = strip_md_fmt(s)
    wc = len(plain.split())
    if wc > 30: return False  # never wrap long prose
    # Count math tokens: operators, numbers, parentheses, factor notation
    math_tokens = len(re.findall(r'[+\*/=()]|(?<![A-Za-z])-(?=[\d(])|\b\d+[\d,]*\.?\d*\b', plain))
    # Count English prose words (articles, verbs, prepositions, etc.)
    prose_words = len(re.findall(r'\b(is|are|was|were|be|been|the|a|an|this|that|for|and|nor|but|or|yet|so|with|from|to|of|in|on|at|by|as|than|then|each|which|will|would|could|may|also|based)\b', plain, re.I))
    # High math density => formula
    if wc >= 3 and wc <= 25:
        if prose_words <= max(1, wc // 5) and math_tokens >= max(3, wc // 2):
            return True
    # Explicit signals (regardless of prose)
    if re.search(r'\((P|F|A|G)/([PFAFG])\s*,', plain): return True  # (P/A, etc.)
    if re.search(r'\b(PW|FW|AW|NPV|BCR|ROI|IRR)\s*\(', plain, re.I) and ('=' in plain or re.search(r'\d+\s*[\+\-\*/]', plain)):
        return True
    # Short equation lines: "= -12345 + 67890" — require math context, avoid "= 16 Days"
    if re.search(r'^\s*=', plain) and (wc >= 5 or re.search(r'[\+\-\*/]', plain[plain.index('=')+1:])): return True
    if re.search(r'P\(z\s*[≤≤]', plain): return True
    if re.search(r'Ts\s*-?\s*Te', plain): return True
    if re.search(r'σ²|σ\^2', plain): return True
    return False

def to_latex(s):
    # Escape % FIRST (other LaTeX specials handled after subscript conversion)
    s = s.replace('%', r'\%')
    s = s.replace('&', r'\&')
    s = s.replace('$', r'\$')
    # Factor notation: (P/A, 20%, 10) - note % already escaped to \%
    s = re.sub(r'\((\w)/(\w),\s*(\d+)\\\%\s*,?\s*(\d+)\)', r'(\\text{\1}/\\text{\2}, \3\\%, \4)', s)
    s = re.sub(r'\((\w)/(\w),\s*i\\%\s*,?\s*(\d+)\)', r'(\\text{\1}/\\text{\2}, i\\%, \3)', s)
    s = re.sub(r'\((\w)/(\w),\s*i\s*,?\s*(\d+)\)', r'(\\text{\1}/\\text{\2}, i, \3)', s)
    # [1/(1+i)VAR] → fraction
    s = re.sub(r'\[1/\(1\+i\)(\w+)\]', r'\\frac{1}{(1+i)^{\1}}', s)
    # Subscripts: X_1, R_j (do before _ escaping so raw _ matches)
    s = re.sub(r'\b([A-Za-z]+)\_(\w)', r'\1_{\2}', s)
    s = re.sub(r'\b([A-Za-z]+)_(\w)', r'\1_{\2}', s)
    # Now escape remaining _
    s = s.replace('_', r'\_')
    # Caret for exponent: ^n → ^{n}
    s = re.sub(r'\^(\d+)', r'^{\1}', s)
    # Dots: .... or ...
    s = re.sub(r'\.{4,}', r'\\dots', s)
    s = re.sub(r'(?<!\s)\.{3}(?!\s)', r'\\dots', s)
    # Convert common text abbreviations to LaTeX text commands
    s = re.sub(r'\bPW\b', r'\\text{PW}', s)
    s = re.sub(r'\bFW\b', r'\\text{FW}', s)
    s = re.sub(r'\bAW\b', r'\\text{AW}', s)
    for t in ["NPV", "IRR", "BCR", "SPI", "CPI", "EAC", "ETC", "VAC", "BAC",
              "MARR", "ROI", "WACC", "PV", "FV", "PMT", "NPER", "RATE"]:
        s = re.sub(rf"\b{t}\b", f"\\\\text{{{t}}}", s)
    s = re.sub(r"\b(SV|CV|EV|AC|BAC)\b", r"\\text{\1}", s)
    # Remove Indian-style thousands separators in numbers (12,00,000 → 1200000)
    s = re.sub(r'\b(\d+),(\d+),(\d{3})\b', r'\1\2\3', s)
    s = re.sub(r'\b(\d+),(\d{3})\b', r'\1\2', s)
    return s

def extract_page_blocks(page):
    """Extract (title, content_items) from page using coordinate positions.
    content_items: list of (level, is_bullet, text)."""
    blocks = page.get_text('dict')['blocks']
    raw = []
    for block in blocks:
        if 'lines' not in block: continue
        for line in block['lines']:
            x0 = int(line['bbox'][0])
            text = dedup_phrases(format_spans(line['spans']).strip())
            if not text or is_fragment(text): continue
            raw.append((x0, text, is_bullet_line(text)))
    if not raw: return None, []

    title = clean_heading(raw[0][1])
    content = raw[1:]

    bullet_xs = [x for x, t, ib in content if ib]
    if not bullet_xs:
        return title, [(0, ib, t.lstrip("\u2022").strip() if ib else t) for x, t, ib in content]

    uniq = sorted(set(int(round(x, -1)) for x in bullet_xs))
    level_map = {rx: i for i, rx in enumerate(uniq)}

    result = []
    for x, t, ib in content:
        if ib:
            rx = int(round(x, -1))
            result.append((level_map.get(rx, 0), True, t.lstrip("\u2022").strip()))
        else:
            result.append((0, False, t))
    return title, result

def merge_hierarchy(items):
    """Merge continuation lines preserving hierarchy.
    Items: list of (level, is_bullet, text)."""
    if not items: return []
    result = [items[0]]
    for item in items[1:]:
        pl, pib, pt = result[-1]
        l, ib, t = item
        # Also treat colon as sentence-ending (prevents formulas merging into prose)
        ended = pt.rstrip()[-1] in ".!?:" if pt else False
        # Don't merge if next line looks like a formula (contains math operators)
        is_math = re.search(r'[\+\-\*/=]', t) and not re.search(r'\b(is|are|was|were|the|a|an|this|that)\b', t[:20], re.I)
        if is_math:
            result.append(item); continue
        if not ib:
            if not ended:
                result[-1] = (pl, pib, pt + " " + t); continue
        elif ib == pib and l == pl and t[0].islower():
            result[-1] = (pl, pib, pt + " " + t); continue
        result.append(item)
    cleaned = []
    for l, ib, t in result:
        t = re.sub(r"\s+\($", "", t)
        t = re.sub(r"^\)\s+", "", t)
        if t and len(t) > 2: cleaned.append((l, ib, t))
    return cleaned

def is_long_sentence(t):
    wc = len(t.split())
    return wc >= 12 and t.rstrip().endswith(".")

def highlight_key_terms(text):
    """Apply bold/italic formatting for key terms and patterns."""
    # Bold labels like Note:, Remember:, Important:, Key:, Definition:, Example:
    text = re.sub(r'\b(Note|Remember|Important|Key|Definition|Example|Warning|Tip|Caution|Summary)\s*:\s*', r'**\1:** ', text)
    # Bold "Key X" / "Important X" where X is a noun phrase
    text = re.sub(r'\*\*(Key|Important|Essential|Critical)\*\*:', r'**\1:**', text)
    # Italic surrounding quoted terms
    text = re.sub(r'"([^"]+)"', r'"*\1*"', text)
    return text

def render_hierarchy(items):
    """Render hierarchical items as nested markdown with formulas."""
    parts = []
    last_formula = None
    for level, is_bullet, text in items:
        text = highlight_key_terms(text)
        pad = "  " * level
        if looks_like_formula(text):
            fmt = strip_md_fmt(text)
            latex = to_latex(fmt)
            if latex == last_formula:
                continue
            last_formula = latex
            if parts and not parts[-1] == "":
                parts.append("")
            parts.append(pad + "$$")
            parts.append(pad + latex)
            parts.append(pad + "$$")
            parts.append("")
        elif is_bullet and is_long_sentence(text):
            parts.append(pad + text)
        elif is_bullet:
            parts.append(pad + "- " + text)
        else:
            parts.append(pad + text)
    return "\n".join(parts)

def save_images(doc, page_num, prefix):
    refs = []
    page = doc[page_num]
    os.makedirs(ASSETS_DIR, exist_ok=True)
    for img in page.get_images():
        xref = img[0]
        pix = fitz.Pixmap(doc, xref)
        if pix.width <= DECORATIVE_THRESHOLD and pix.height <= DECORATIVE_THRESHOLD: continue
        ext = "png" if pix.n >= 4 else "jpeg"
        save = pix if pix.n < 4 else fitz.Pixmap(fitz.csRGB, pix)
        existing = os.listdir(ASSETS_DIR) if os.path.isdir(ASSETS_DIR) else []
        nums = [int(m.group(1)) for f in existing for m in [re.search(rf"{prefix}(\d+)\.(png|jpe?g)", f)] if m]
        n = max(nums) + 1 if nums else 1
        fn = f"{prefix}{n:03d}.{ext}"
        save.save(os.path.join(ASSETS_DIR, fn))
        refs.append(fn)
    return refs

def classify_items(pairs):
    """Classify content items into paragraphs, bullet lists, formulas."""
    formulas = []
    bullets = []
    paras = []
    for is_b, text in pairs:
        if looks_like_formula(text):
            formulas.append(text)
        elif is_b:
            # Classify: long complete sentences → paragraph, short items → bullet
            word_count = len(text.split())
            ends_with_period = text.rstrip().endswith(".")
            if word_count >= 12 and ends_with_period:
                paras.append(text)
            elif word_count >= 15:
                paras.append(text)
            else:
                bullets.append(text)
        else:
            paras.append(text)
    return formulas, bullets, paras

def match_title(title, patterns):
    """Check if a slide title matches any pattern in a list."""
    t = title.lower().strip()
    for p in patterns:
        p = p.lower().strip()
        if p in t or t in p:
            return True
    return False

def extract_chapter(ch):
    info = CHAPTER_INFO[ch]
    pdf = os.path.join(CLASS_DIR, info["pdf"])
    if not os.path.exists(pdf): print(f"  SKIP: {pdf}"); return
    struct = CHAPTER_STRUCT.get(ch, [])

    print(f"\n--- Chapter {ch}: {info['title']} ---")
    doc = fitz.open(pdf)
    print(f"  Pages: {doc.page_count}")

    prefix = f"ch{ch:02d}_img_"
    groups = []
    cur_title = None
    cur_pages = []

    for i in range(doc.page_count):
        title, content = extract_page_blocks(doc[i])
        if not title: continue
        if title in SKIP_TITLES: continue
        if re.match(r"^Chapter\s+\d+:", title): continue
        if "End of Chapter" in title or "Thank You" in title: continue

        has_bullet = any(ib for _, ib, _ in content)
        page_has_info_img = any(p.width > DECORATIVE_THRESHOLD or p.height > DECORATIVE_THRESHOLD for p in [fitz.Pixmap(doc, x[0]) for x in doc[i].get_images()])
        if not has_bullet and not content and not page_has_info_img: continue

        merged_title = clean_heading(title)
        if has_bullet and content:
            fl, fib, ft = content[0]
            if not fib and len(ft) < 50 and ft[0].isupper():
                merged_title = clean_heading(title + " " + ft)
                content = content[1:]

        merged_content = merge_hierarchy(content)
        imgs = save_images(doc, i, prefix)

        if merged_title != cur_title:
            if cur_title and cur_pages: groups.append((cur_title, cur_pages))
            cur_title = merged_title
            cur_pages = [(merged_content, imgs)]
        else:
            cur_pages.append((merged_content, imgs))

    if cur_title and cur_pages: groups.append((cur_title, cur_pages))
    print(f"  Topics: {len(groups)}")
    doc.close()

    # Build heading hierarchy from CHAPTER_STRUCT
    out = []
    unit = f"{ch:02d}"
    slug = slugify(info["title"])
    out.append(f"# Unit {unit}: {info['title']}")
    out.append("")
    out.append(f"> **Hours:** {info['hours']} | **Source:** `{info['pdf']}`")
    out.append("")
    out.append("---\n")

    # For each section in the structure, write its heading and matched groups
    assigned_groups = set()
    for level, heading_title, patterns in struct:
        out.append(f"{level} {heading_title}\n")

        # Find matching groups
        matched = []
        for idx, (title, pages_data) in enumerate(groups):
            if idx in assigned_groups: continue
            if match_title(title, patterns):
                matched.append(idx)
                assigned_groups.add(idx)

        if not matched:
            # Still write the heading but note it has no slides
            out.append("*Content derived from class notes.*\n")
            continue

        for idx in matched:
            _, pages_data = groups[idx]
            items, imgs_all = [], []
            for merged, imgs in pages_data:
                items.extend(merged)
                imgs_all.extend(imgs)
            seen = set()
            unique_imgs = [x for x in imgs_all if not (x in seen or seen.add(x))]
            out.append(render_hierarchy(items) + "\n")
            for img_fn in unique_imgs:
                out.append(f"![{heading_title}](assets/{img_fn})\n")

    # Any unassigned groups (those not in the structure) go at the end
    unassigned = [i for i in range(len(groups)) if i not in assigned_groups]
    if unassigned:
        out.append("## Additional Topics\n")
        for idx in unassigned:
            title, pages_data = groups[idx]
            out.append(f"### {title}\n")
            items, imgs_all = [], []
            for merged, imgs in pages_data:
                items.extend(merged)
                imgs_all.extend(imgs)
            seen = set()
            unique_imgs = [x for x in imgs_all if not (x in seen or seen.add(x))]
            out.append(render_hierarchy(items) + "\n")
            for img_fn in unique_imgs:
                out.append(f"![{title}](assets/{img_fn})\n")

    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    fn = f"unit_{unit}_{slug}.md"
    fp = os.path.join(NOTES_DIR, fn)
    os.makedirs(NOTES_DIR, exist_ok=True)
    with open(fp, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"  -> {fn} ({text.count(chr(10))} lines)")

def main():
    os.makedirs(ASSETS_DIR, exist_ok=True)
    for ch in range(1, 10):
        extract_chapter(ch)

if __name__ == "__main__":
    main()
