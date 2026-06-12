import streamlit as st
import html

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ResearchMind AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Syne:wght@700;800&family=JetBrains+Mono:wght@300;400;500&display=swap');

html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif !important;
    color: #E2E8F0;
}
.stApp { background: #050609 !important; }
#MainMenu, footer, header { visibility: hidden; }

/* keep Streamlit's own block-container but override padding/width */
.block-container {
    padding-top: 0 !important;
    padding-bottom: 4rem !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
    max-width: 960px !important;
}

/* ── scrollbar ── */
::-webkit-scrollbar { width: 4px; }
::-webkit-scrollbar-track { background: #0A0C12; }
::-webkit-scrollbar-thumb { background: #1E293B; border-radius: 99px; }

/* ══════════════════════════════════════════════════
   HERO
══════════════════════════════════════════════════ */
.hero-wrap {
    position: relative;
    padding: 5rem 1rem 3.5rem;
    text-align: center;
    overflow: hidden;
    margin-left: -1rem;
    margin-right: -1rem;
}
.hero-bg {
    position: absolute; inset: 0;
    background:
        radial-gradient(ellipse 80% 55% at 20% 0%,  rgba(74,222,128,0.13) 0%, transparent 60%),
        radial-gradient(ellipse 60% 45% at 80% 5%,  rgba(139,92,246,0.10) 0%, transparent 55%),
        radial-gradient(ellipse 50% 40% at 50% 100%,rgba(6,182,212,0.08)  0%, transparent 50%),
        #050609;
    animation: meshShift 9s ease-in-out infinite alternate;
}
@keyframes meshShift {
    0%   { filter: hue-rotate(0deg)  brightness(1);    }
    50%  { filter: hue-rotate(12deg) brightness(1.06); }
    100% { filter: hue-rotate(-8deg) brightness(1);    }
}
.hero-grid {
    position: absolute; inset: 0;
    background-image:
        linear-gradient(rgba(74,222,128,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(74,222,128,0.04) 1px, transparent 1px);
    background-size: 48px 48px;
    mask-image: radial-gradient(ellipse 70% 70% at 50% 50%, black 40%, transparent 100%);
}
.orb {
    position: absolute; border-radius: 50%;
    filter: blur(70px); opacity: 0.16;
    animation: floatOrb linear infinite;
    pointer-events: none;
}
.orb-1 { width:300px; height:300px; background:#4ADE80; top:-80px;  left:-60px;  animation-duration:14s; }
.orb-2 { width:240px; height:240px; background:#818CF8; top:40px;   right:-70px; animation-duration:19s; animation-delay:-7s; }
.orb-3 { width:180px; height:180px; background:#22D3EE; bottom:-20px; left:35%;  animation-duration:23s; animation-delay:-11s; }
@keyframes floatOrb {
    0%   { transform: translate(0,0)        rotate(0deg);   }
    25%  { transform: translate(30px,-20px) rotate(90deg);  }
    50%  { transform: translate(-20px,25px) rotate(180deg); }
    75%  { transform: translate(18px,8px)   rotate(270deg); }
    100% { transform: translate(0,0)        rotate(360deg); }
}

.hero-content { position: relative; z-index: 2; }

.hero-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #4ADE80;
    margin-bottom: 1.3rem;
    display: inline-flex; align-items: center; gap: 0.7rem;
    animation: fadeUp 0.8s ease both;
}
.hero-eyebrow::before { content:''; width:36px; height:1px; background: linear-gradient(90deg,transparent,#4ADE80); }
.hero-eyebrow::after  { content:''; width:36px; height:1px; background: linear-gradient(90deg,#4ADE80,transparent); }

.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(2.8rem, 6.5vw, 5rem);
    font-weight: 800;
    line-height: 1.02;
    letter-spacing: -0.03em;
    color: #F8FAFC;
    margin-bottom: 0.6rem;
    animation: fadeUp 0.8s 0.12s ease both;
}
.hero-title .gw {
    background: linear-gradient(135deg,#4ADE80 0%,#22D3EE 50%,#818CF8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: drop-shadow(0 0 28px rgba(74,222,128,0.35));
}
.hero-sub {
    font-size: 1.05rem; font-weight: 400;
    color: #475569; max-width: 500px; line-height: 1.7;
    margin: 0 auto 2.8rem;
    animation: fadeUp 0.8s 0.24s ease both;
}
.badges-row {
    display: flex; gap: 0.55rem; justify-content: center;
    flex-wrap: wrap; animation: fadeUp 0.8s 0.36s ease both;
}
.badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.66rem; letter-spacing: 0.07em;
    padding: 0.32rem 0.8rem; border-radius: 99px; border: 1px solid;
    display: inline-flex; align-items: center; gap: 0.35rem;
    animation: badgeBob 3s ease-in-out infinite;
}
.b1 { color:#4ADE80; border-color:rgba(74,222,128,0.3);  background:rgba(74,222,128,0.07);  animation-delay:0s;   }
.b2 { color:#22D3EE; border-color:rgba(34,211,238,0.3);  background:rgba(34,211,238,0.07);  animation-delay:.4s;  }
.b3 { color:#A78BFA; border-color:rgba(167,139,250,0.3); background:rgba(167,139,250,0.07); animation-delay:.8s;  }
.b4 { color:#FB923C; border-color:rgba(251,146,60,0.3);  background:rgba(251,146,60,0.07);  animation-delay:1.2s; }
@keyframes badgeBob {
    0%,100%{ opacity:.75; transform:translateY(0);    }
    50%    { opacity:1;   transform:translateY(-3px); }
}
@keyframes fadeUp {
    from { opacity:0; transform:translateY(22px); }
    to   { opacity:1; transform:translateY(0);    }
}

/* ══════════════════════════════════════════════════
   INPUT CARD
══════════════════════════════════════════════════ */
.input-card {
    background: rgba(15,18,28,0.85);
    border: 1px solid rgba(74,222,128,0.14);
    border-radius: 18px;
    padding: 2rem 2.2rem 1.8rem;
    margin-bottom: 2rem;
    backdrop-filter: blur(20px);
    box-shadow: 0 0 0 1px rgba(74,222,128,0.04), 0 20px 48px rgba(0,0,0,0.55);
    position: relative; overflow: hidden;
}
.input-card::before {
    content:''; position:absolute; top:0; left:10%; right:10%; height:1px;
    background: linear-gradient(90deg, transparent, rgba(74,222,128,0.45), transparent);
}

/* Streamlit input overrides */
.stTextInput > label {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.68rem !important; font-weight: 400 !important;
    letter-spacing: 0.16em !important; text-transform: uppercase !important;
    color: #4ADE80 !important; margin-bottom: 0.5rem !important;
}
.stTextInput > div > div > input {
    background: rgba(5,6,9,0.85) !important;
    border: 1px solid rgba(255,255,255,0.07) !important;
    border-radius: 12px !important;
    color: #F1F5F9 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 1rem !important; font-weight: 400 !important;
    padding: 0.9rem 1.2rem !important;
    transition: border-color 0.3s, box-shadow 0.3s !important;
}
.stTextInput > div > div > input::placeholder { color: #1E293B !important; }
.stTextInput > div > div > input:focus {
    border-color: rgba(74,222,128,0.5) !important;
    box-shadow: 0 0 0 3px rgba(74,222,128,0.08), 0 0 18px rgba(74,222,128,0.1) !important;
}

/* Button */
.stButton > button {
    background: linear-gradient(135deg,#16a34a,#15803d) !important;
    color: #F0FDF4 !important; border: none !important;
    border-radius: 12px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important; font-size: 0.95rem !important;
    letter-spacing: 0.04em !important;
    padding: 0.9rem 1.6rem !important; width: 100% !important;
    transition: all 0.28s cubic-bezier(0.4,0,0.2,1) !important;
    box-shadow: 0 4px 22px rgba(74,222,128,0.22), 0 0 0 1px rgba(74,222,128,0.18) !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 32px rgba(74,222,128,0.35), 0 0 0 1px rgba(74,222,128,0.32) !important;
    background: linear-gradient(135deg,#22c55e,#16a34a) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* ══════════════════════════════════════════════════
   PIPELINE TRACKER
══════════════════════════════════════════════════ */
.pipeline-wrap { margin-bottom: 1.8rem; }
.pipeline-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.62rem; letter-spacing: 0.18em;
    text-transform: uppercase; color: #1E293B;
    text-align: center; margin-bottom: 1.4rem;
}
.pipeline-track {
    display: flex; align-items: center;
    justify-content: center; gap: 0;
}
.step-node { display:flex; flex-direction:column; align-items:center; gap:0.55rem; flex-shrink:0; }
.node-circle {
    width: 68px; height: 68px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.45rem;
    border: 2px solid #1E293B; background: #0A0C12;
    transition: all 0.45s cubic-bezier(0.34,1.56,0.64,1);
    position: relative;
}
.step-idle   .node-circle { filter: grayscale(1) opacity(.35); }
.step-active .node-circle {
    border-color: #4ADE80; background: rgba(74,222,128,0.08);
    box-shadow: 0 0 0 7px rgba(74,222,128,0.10), 0 0 0 14px rgba(74,222,128,0.05), 0 0 32px rgba(74,222,128,0.32);
    animation: nodeBreath 1.5s ease-in-out infinite;
}
.step-done .node-circle {
    border-color: #22c55e; background: rgba(34,197,94,0.10);
    box-shadow: 0 0 18px rgba(34,197,94,0.22);
}
@keyframes nodeBreath {
    0%,100%{ box-shadow:0 0 0 7px rgba(74,222,128,0.10),0 0 0 14px rgba(74,222,128,0.05),0 0 32px rgba(74,222,128,0.32); }
    50%    { box-shadow:0 0 0 10px rgba(74,222,128,0.16),0 0 0 22px rgba(74,222,128,0.07),0 0 52px rgba(74,222,128,0.42); }
}
/* done checkmark */
.step-done .node-circle::after {
    content:'✓'; position:absolute; inset:0;
    display:flex; align-items:center; justify-content:center;
    font-size:1.55rem; color:#4ADE80;
    background:rgba(5,6,9,0.72); border-radius:50%;
    animation: checkPop 0.32s cubic-bezier(0.34,1.56,0.64,1) both;
}
@keyframes checkPop {
    from { transform:scale(0) rotate(-40deg); opacity:0; }
    to   { transform:scale(1) rotate(0deg);   opacity:1; }
}
.node-lbl {
    font-size: 0.78rem; font-weight: 600; letter-spacing: 0.04em; text-align: center;
}
.step-idle   .node-lbl { color:#1E293B; }
.step-active .node-lbl { color:#4ADE80; }
.step-done   .node-lbl { color:#334155; }
.node-sub {
    font-family:'JetBrains Mono',monospace; font-size:0.58rem;
    letter-spacing:0.06em; text-transform:uppercase; text-align:center;
}
.step-idle   .node-sub { color:#0F172A; }
.step-active .node-sub { color:#166534; }
.step-done   .node-sub { color:#1E293B; }

/* connector line between nodes */
.conn-line {
    height: 2px; flex: 1; min-width: 28px; max-width: 60px;
    background: #0F172A; position: relative; overflow: hidden;
    border-radius: 2px;
}
.conn-line.conn-done {
    background: linear-gradient(90deg,#4ADE80,#22D3EE);
    box-shadow: 0 0 6px rgba(74,222,128,0.4);
}
.conn-line.conn-active::after {
    content:''; position:absolute; top:0; left:-100%; right:0; bottom:0;
    background: linear-gradient(90deg,transparent,#4ADE80,transparent);
    animation: lineFlow 1.5s ease-in-out infinite;
}
@keyframes lineFlow { from{left:-100%} to{left:100%} }

/* ══════════════════════════════════════════════════
   STATUS BANNER
══════════════════════════════════════════════════ */
.status-banner {
    display:flex; align-items:center; gap:0.9rem;
    padding: 0.9rem 1.4rem; border-radius: 14px;
    border: 1px solid rgba(74,222,128,0.14);
    background: rgba(74,222,128,0.04);
    margin-bottom: 1.8rem;
    font-size: 0.9rem; font-weight: 500; color: #94A3B8;
    position: relative; overflow: hidden;
}
.status-banner::before {
    content:''; position:absolute; top:0; left:-100%; width:100%; height:100%;
    background: linear-gradient(90deg,transparent,rgba(74,222,128,0.03),transparent);
    animation: shimmer 2.5s ease-in-out infinite;
}
@keyframes shimmer { from{left:-100%} to{left:200%} }
.status-banner.done-banner { border-color:rgba(74,222,128,0.3); color:#4ADE80; }
.pulse-ring {
    width:12px; height:12px; border-radius:50%;
    background:#4ADE80; flex-shrink:0; position:relative;
}
.pulse-ring::before,.pulse-ring::after {
    content:''; position:absolute; inset:-4px; border-radius:50%;
    border:2px solid #4ADE80; animation:ringOut 1.6s ease-out infinite;
}
.pulse-ring::after { animation-delay:.8s; }
@keyframes ringOut { 0%{transform:scale(.5);opacity:.8} 100%{transform:scale(2.6);opacity:0} }
.step-tag {
    font-family:'JetBrains Mono',monospace; font-size:0.63rem;
    letter-spacing:0.1em; padding:0.18rem 0.6rem; border-radius:99px;
    background:rgba(74,222,128,0.1); color:#4ADE80;
    border:1px solid rgba(74,222,128,0.2); margin-left:auto; flex-shrink:0;
}

/* ══════════════════════════════════════════════════
   RESULT DISPLAY
══════════════════════════════════════════════════ */
/* Tabs */
.stTabs [data-baseweb="tab-list"] {
    background: transparent !important; gap:.25rem !important;
    border-bottom: 1px solid rgba(255,255,255,0.06) !important;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important; color:#475569 !important;
    font-family:'Space Grotesk',sans-serif !important;
    font-size:0.88rem !important; font-weight:500 !important;
    padding:0.6rem 1.2rem !important; border-radius:8px 8px 0 0 !important;
    transition: color 0.2s !important;
}
.stTabs [data-baseweb="tab"]:hover { color:#94A3B8 !important; }
.stTabs [aria-selected="true"] {
    color:#4ADE80 !important; background:rgba(74,222,128,0.04) !important;
    border-bottom:2px solid #4ADE80 !important;
}

/* Topic chip */
.topic-chip {
    display:inline-flex; align-items:center; gap:0.6rem;
    padding:0.45rem 1rem;
    background:rgba(74,222,128,0.07); border:1px solid rgba(74,222,128,0.2);
    border-radius:99px; margin-bottom:1.5rem;
}
.tc-label { font-family:'JetBrains Mono',monospace; font-size:0.62rem; color:#4ADE80; letter-spacing:.12em; text-transform:uppercase; }
.tc-value { font-size:0.88rem; font-weight:500; color:#E2E8F0; }

/* Source card */
.src-card {
    background:rgba(10,12,18,0.9); border:1px solid rgba(255,255,255,0.06);
    border-radius:14px; overflow:hidden; margin-bottom:1rem;
}
.src-head {
    display:flex; align-items:center; gap:0.75rem;
    padding:0.9rem 1.2rem; border-bottom:1px solid rgba(255,255,255,0.05);
    background:rgba(255,255,255,0.02);
}
.src-icon { width:32px; height:32px; border-radius:9px; display:flex; align-items:center; justify-content:center; font-size:0.95rem; flex-shrink:0; }
.src-title { font-size:0.78rem; font-weight:600; letter-spacing:.05em; text-transform:uppercase; color:#64748B; }
.src-body {
    padding:1.1rem 1.2rem;
    font-size:0.875rem; line-height:1.78; color:#64748B;
    white-space:pre-wrap; word-break:break-word;
    max-height:360px; overflow-y:auto;
}
.src-body::-webkit-scrollbar{width:3px}
.src-body::-webkit-scrollbar-thumb{background:#1E293B;border-radius:2px}

/* Report card */
.report-card {
    background:rgba(10,12,18,0.9); border:1px solid rgba(255,255,255,0.06);
    border-top:2px solid #4ADE80; border-radius:14px;
    padding:1.8rem 2rem; margin-bottom:1.2rem;
    box-shadow:0 0 40px rgba(74,222,128,0.05);
}
.report-eyebrow {
    font-family:'JetBrains Mono',monospace; font-size:0.63rem;
    letter-spacing:.18em; text-transform:uppercase; color:#4ADE80;
    margin-bottom:1rem; display:flex; align-items:center; gap:.5rem;
}
.report-body { font-size:0.95rem; line-height:1.85; color:#CBD5E1; }

/* Feedback card */
.feedback-card {
    background:rgba(10,12,18,0.9); border:1px solid rgba(255,255,255,0.06);
    border-top:2px solid #F87171; border-radius:14px;
    padding:1.8rem 2rem; margin-bottom:1.2rem;
    box-shadow:0 0 40px rgba(248,113,113,0.04);
}

/* Download button */
.stDownloadButton > button {
    background:transparent !important; border:1px solid rgba(255,255,255,0.09) !important;
    color:#475569 !important; font-family:'Space Grotesk',sans-serif !important;
    font-size:0.8rem !important; font-weight:500 !important;
    padding:0.5rem 1.2rem !important; border-radius:8px !important;
    transition:all .2s !important;
}
.stDownloadButton > button:hover {
    border-color:rgba(74,222,128,0.4) !important; color:#4ADE80 !important;
    background:rgba(74,222,128,0.05) !important;
}

/* Idle empty state */
.empty-state { text-align:center; padding:3rem 0 1.5rem; }
.empty-icon  { font-size:3rem; display:block; opacity:.18; animation:emptyFloat 3s ease-in-out infinite; margin-bottom:.8rem; }
@keyframes emptyFloat { 0%,100%{transform:translateY(0)} 50%{transform:translateY(-8px)} }
.empty-txt   { font-size:.88rem; color:#1E293B; font-weight:500; }

/* Alert */
div[data-testid="stAlert"] { border-radius:12px !important; }
</style>
""", unsafe_allow_html=True)


# ══ HELPERS ═══════════════════════════════════════════════════════════════════

STEPS = [
    ("◎", "Search",  "Web Discovery"),
    ("⬡", "Scrape",  "Deep Extraction"),
    ("✦", "Write",   "Synthesis"),
    ("⌖", "Review",  "Critic Analysis"),
]

def render_pipeline(active_step: int):
    """active_step: 0-3 = that step running; 4 = all done; -1 = idle"""
    track = ""
    for i, (icon, label, sub) in enumerate(STEPS):
        if i < active_step:
            cls = "step-done"
        elif i == active_step:
            cls = "step-active"
        else:
            cls = "step-idle"

        track += f"""
        <div class="{cls} step-node">
            <div class="node-circle">{icon}</div>
            <div class="node-lbl">{label}</div>
            <div class="node-sub">{sub}</div>
        </div>"""

        if i < len(STEPS) - 1:
            if i < active_step - 1 or (i < active_step):
                line_cls = "conn-done"
            elif i == active_step:
                line_cls = "conn-active"
            else:
                line_cls = ""
            track += f'<div class="conn-line {line_cls}"></div>'

    st.markdown(
        f'<div class="pipeline-wrap">'
        f'<div class="pipeline-label">— pipeline status —</div>'
        f'<div class="pipeline-track">{track}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )


def render_status(text: str, tag: str = "", complete: bool = False):
    banner_cls = "done-banner" if complete else ""
    dot = '<span style="font-size:1.1rem;line-height:1">✓</span>' if complete else '<div class="pulse-ring"></div>'
    tag_html = f'<span class="step-tag">{tag}</span>' if tag else ""
    st.markdown(
        f'<div class="status-banner {banner_cls}">{dot}'
        f'<span>{text}</span>{tag_html}</div>',
        unsafe_allow_html=True,
    )


def source_card(icon, icon_bg, title, raw_content):
    safe = html.escape(str(raw_content))
    st.markdown(
        f'<div class="src-card">'
        f'  <div class="src-head">'
        f'    <div class="src-icon" style="background:{icon_bg}">{icon}</div>'
        f'    <div class="src-title">{title}</div>'
        f'  </div>'
        f'  <div class="src-body">{safe}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )


# ══ SESSION STATE ══════════════════════════════════════════════════════════════
if "result"    not in st.session_state: st.session_state.result    = None
if "ran_topic" not in st.session_state: st.session_state.ran_topic = ""


# ══ HERO ══════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero-wrap">
    <div class="hero-bg"></div>
    <div class="hero-grid"></div>
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>
    <div class="hero-content">
        <div class="hero-eyebrow">⚡ Multi-Agent AI System</div>
        <div class="hero-title">Research,&nbsp;<span class="gw">Automated.</span></div>
        <p class="hero-sub">
            Four specialized AI agents — searching, scraping, writing,
            and critiquing — working in sequence to deliver
            publication-ready research.
        </p>
        <div class="badges-row">
            <span class="badge b1">◎&nbsp;Search Agent</span>
            <span class="badge b2">⬡&nbsp;Scrape Agent</span>
            <span class="badge b3">✦&nbsp;Writer Agent</span>
            <span class="badge b4">⌖&nbsp;Critic Agent</span>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


# ══ INPUT CARD ════════════════════════════════════════════════════════════════
st.markdown('<div class="input-card">', unsafe_allow_html=True)
col_in, col_btn = st.columns([5, 1.2], gap="medium")
with col_in:
    topic = st.text_input(
        "Research Topic",
        placeholder="e.g. Quantum computing applications in drug discovery",
    )
with col_btn:
    st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)
    run = st.button("⚡  Run", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)


# ══ IDLE ══════════════════════════════════════════════════════════════════════
if not run and st.session_state.result is None:
    render_pipeline(-1)
    st.markdown("""
        <div class="empty-state">
            <span class="empty-icon">⚡</span>
            <div class="empty-txt">Enter a topic above and run the pipeline to generate your report.</div>
        </div>
    """, unsafe_allow_html=True)


# ══ RUN ═══════════════════════════════════════════════════════════════════════
if run:
    if not topic.strip():
        st.warning("Please enter a research topic first.")
        st.stop()

    try:
        import agents
    except ImportError as e:
        st.error(f"Could not import agents module: {e}")
        st.stop()

    st.session_state.result    = None
    st.session_state.ran_topic = topic

    prog_ph   = st.empty()
    status_ph = st.empty()
    state     = {}

    # Step 1 — Search
    with prog_ph.container():  render_pipeline(0)
    with status_ph.container(): render_status("Search agent is scouring the web for sources…", "01 / 04")

    try:
        sa = agents.build_search_agent()
        sr = sa.invoke({"messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]})
        state["search_results"] = sr["messages"][-1].content
    except Exception as e:
        st.error(f"Search agent error: {e}"); st.stop()

    # Step 2 — Scrape
    with prog_ph.container():  render_pipeline(1)
    with status_ph.container(): render_status("Reader agent is extracting full page content…", "02 / 04")

    try:
        ra = agents.build_reader_agent()
        sc = ra.invoke({"messages": [("user",
            f"Based on the following search results about '{topic}', "
            f"pick the most relevant URL and scrape it for deeper content.\n\n"
            f"Search Results:\n{state['search_results'][:800]}")]})
        state["scraped_content"] = sc["messages"][-1].content
    except Exception as e:
        st.error(f"Reader agent error: {e}"); st.stop()

    # Step 3 — Write
    with prog_ph.container():  render_pipeline(2)
    with status_ph.container(): render_status("Writer agent is composing the structured report…", "03 / 04")

    try:
        combined = (f"SEARCH RESULTS:\n{state['search_results']}\n\n"
                    f"DETAILED SCRAPED CONTENT:\n{state['scraped_content']}")
        state["report"] = agents.writer_chain.invoke({"topic": topic, "research": combined})
    except Exception as e:
        st.error(f"Writer chain error: {e}"); st.stop()

    # Step 4 — Critic
    with prog_ph.container():  render_pipeline(3)
    with status_ph.container(): render_status("Critic agent is reviewing and scoring the report…", "04 / 04")

    try:
        state["feedback"] = agents.critic_chain.invoke({"report": state["report"]})
    except Exception as e:
        st.error(f"Critic chain error: {e}"); st.stop()

    # Done
    with prog_ph.container():  render_pipeline(4)
    with status_ph.container(): render_status("Pipeline complete — your report is ready.", complete=True)

    st.session_state.result = state


# ══ RESULTS ═══════════════════════════════════════════════════════════════════
if st.session_state.result:
    state       = st.session_state.result
    topic_label = st.session_state.ran_topic

    st.markdown(
        f'<div class="topic-chip">'
        f'<span class="tc-label">Topic</span>'
        f'<span class="tc-value">{html.escape(topic_label)}</span>'
        f'</div>',
        unsafe_allow_html=True,
    )

    tab_report, tab_sources, tab_feedback = st.tabs([
        "⚡  Final Report",
        "🔎  Source Data",
        "⌖  Critic Feedback",
    ])

    # ── Report tab ──
    with tab_report:
        report_text = state.get("report", "")
        safe_report = html.escape(str(report_text))
        st.markdown(
            f'<div class="report-card">'
            f'  <div class="report-eyebrow">⬡ Research Output</div>'
            f'  <div class="report-body">{safe_report}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )
        if isinstance(report_text, str):
            st.download_button(
                "⬇  Download report (.txt)", data=report_text,
                file_name=f"report_{topic_label[:40].replace(' ','_')}.txt",
                mime="text/plain",
            )

    # ── Sources tab ──
    with tab_sources:
        c1, c2 = st.columns(2, gap="large")
        with c1:
            source_card("🔍", "rgba(74,222,128,0.10)", "Web Search Results",    state.get("search_results",  ""))
        with c2:
            source_card("🌐", "rgba(34,211,238,0.10)", "Scraped Page Content",  state.get("scraped_content", ""))

    # ── Feedback tab ──
    with tab_feedback:
        feedback_text = state.get("feedback", "")
        safe_feedback = html.escape(str(feedback_text))
        st.markdown(
            f'<div class="feedback-card">'
            f'  <div class="report-eyebrow" style="color:#F87171">⌖ Critic Analysis</div>'
            f'  <div class="report-body">{safe_feedback}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )
        if isinstance(feedback_text, str):
            st.download_button(
                "⬇  Download feedback (.txt)", data=feedback_text,
                file_name=f"feedback_{topic_label[:40].replace(' ','_')}.txt",
                mime="text/plain",
            )