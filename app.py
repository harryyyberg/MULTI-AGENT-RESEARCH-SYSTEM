import streamlit as st
import time
import sys
import os

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ResearchMind — AI Research Pipeline",
    page_icon="🔬",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600&family=DM+Serif+Display:ital@0;1&display=swap');

/* ── Reset & base ── */
html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
    color: #E8E6E1;
}

.stApp {
    background: #0D0F14;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 2.5rem 3rem 4rem; max-width: 1100px; }

/* ── Typography ── */
.brand-headline {
    font-family: 'DM Serif Display', serif;
    font-size: 2.6rem;
    font-weight: 400;
    letter-spacing: -0.02em;
    color: #F0EDE8;
    line-height: 1.15;
    margin-bottom: 0.25rem;
}
.brand-headline em {
    font-style: italic;
    color: #7DD3C8;
}
.brand-sub {
    font-size: 0.92rem;
    color: #6B7280;
    font-weight: 400;
    letter-spacing: 0.04em;
    text-transform: uppercase;
    margin-bottom: 2.5rem;
}

/* ── Input area ── */
.stTextInput > div > div > input {
    background: #161921 !important;
    border: 1px solid #252830 !important;
    border-radius: 8px !important;
    color: #E8E6E1 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 1rem !important;
    padding: 0.85rem 1.1rem !important;
    transition: border-color 0.2s;
}
.stTextInput > div > div > input:focus {
    border-color: #7DD3C8 !important;
    box-shadow: 0 0 0 3px rgba(125, 211, 200, 0.08) !important;
}
.stTextInput > label {
    color: #9CA3AF !important;
    font-size: 0.8rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.06em !important;
    text-transform: uppercase !important;
    margin-bottom: 0.4rem !important;
}

/* ── Primary button ── */
.stButton > button {
    background: #7DD3C8 !important;
    color: #0D0F14 !important;
    border: none !important;
    border-radius: 8px !important;
    font-family: 'Inter', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    letter-spacing: 0.04em !important;
    padding: 0.75rem 2rem !important;
    cursor: pointer !important;
    transition: background 0.2s, transform 0.1s !important;
}
.stButton > button:hover {
    background: #5BBDB1 !important;
    transform: translateY(-1px) !important;
}
.stButton > button:active { transform: translateY(0) !important; }

/* ── Pipeline steps ── */
.pipeline-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 1px;
    background: #1C1F27;
    border: 1px solid #1C1F27;
    border-radius: 10px;
    overflow: hidden;
    margin: 1.8rem 0;
}
.step-cell {
    background: #161921;
    padding: 1.2rem 1rem;
    display: flex;
    flex-direction: column;
    gap: 0.4rem;
    transition: background 0.3s;
}
.step-cell.active { background: #0F1A19; }
.step-cell.done   { background: #0E1816; }
.step-dot {
    width: 8px; height: 8px;
    border-radius: 50%;
    background: #2A2D36;
    transition: background 0.3s;
}
.step-dot.active { background: #7DD3C8; box-shadow: 0 0 8px rgba(125,211,200,0.5); }
.step-dot.done   { background: #3D7A74; }
.step-label {
    font-size: 0.7rem;
    font-weight: 600;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: #4B5563;
    transition: color 0.3s;
}
.step-label.active { color: #7DD3C8; }
.step-label.done   { color: #3D7A74; }
.step-desc {
    font-size: 0.78rem;
    color: #6B7280;
    line-height: 1.4;
}

/* ── Result cards ── */
.result-card {
    background: #161921;
    border: 1px solid #1C1F27;
    border-radius: 10px;
    padding: 1.5rem 1.6rem;
    margin-bottom: 1.2rem;
}
.result-card-header {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    margin-bottom: 1rem;
    padding-bottom: 0.75rem;
    border-bottom: 1px solid #1C1F27;
}
.result-card-icon {
    width: 28px; height: 28px;
    border-radius: 6px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 0.9rem;
    flex-shrink: 0;
}
.icon-search  { background: rgba(125,211,200,0.1); }
.icon-scrape  { background: rgba(167,139,250,0.1); }
.icon-report  { background: rgba(251,191,36,0.1); }
.icon-critic  { background: rgba(251,113,133,0.1); }

.result-card-title {
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.07em;
    text-transform: uppercase;
    color: #9CA3AF;
}
.result-card-body {
    font-size: 0.88rem;
    color: #C9C4BC;
    line-height: 1.75;
    white-space: pre-wrap;
    word-break: break-word;
    max-height: 320px;
    overflow-y: auto;
    padding-right: 0.25rem;
}
.result-card-body::-webkit-scrollbar { width: 4px; }
.result-card-body::-webkit-scrollbar-track { background: transparent; }
.result-card-body::-webkit-scrollbar-thumb { background: #2A2D36; border-radius: 2px; }

/* ── Report full-width ── */
.report-card {
    background: #161921;
    border: 1px solid #252830;
    border-left: 3px solid #7DD3C8;
    border-radius: 10px;
    padding: 1.8rem 2rem;
    margin-bottom: 1.2rem;
}
.feedback-card {
    background: #161921;
    border: 1px solid #252830;
    border-left: 3px solid #F87171;
    border-radius: 10px;
    padding: 1.8rem 2rem;
    margin-bottom: 1.2rem;
}

/* ── Status bar ── */
.status-bar {
    display: flex;
    align-items: center;
    gap: 0.6rem;
    padding: 0.7rem 1rem;
    background: #161921;
    border: 1px solid #1C1F27;
    border-radius: 8px;
    margin-bottom: 1.4rem;
    font-size: 0.82rem;
    color: #9CA3AF;
}
.status-dot-running {
    width: 7px; height: 7px;
    border-radius: 50%;
    background: #7DD3C8;
    animation: pulse 1.2s infinite;
    flex-shrink: 0;
}
@keyframes pulse {
    0%, 100% { opacity: 1; }
    50%       { opacity: 0.3; }
}

/* ── Divider ── */
.section-divider {
    border: none;
    border-top: 1px solid #1C1F27;
    margin: 2rem 0;
}

/* ── Tab override ── */
.stTabs [data-baseweb="tab-list"] {
    background: transparent;
    gap: 0.2rem;
    border-bottom: 1px solid #1C1F27;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: #6B7280 !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.04em !important;
    padding: 0.5rem 1rem !important;
    border-radius: 6px 6px 0 0 !important;
}
.stTabs [aria-selected="true"] {
    color: #7DD3C8 !important;
    border-bottom: 2px solid #7DD3C8 !important;
}

/* ── Download button ── */
.stDownloadButton > button {
    background: transparent !important;
    border: 1px solid #2A2D36 !important;
    color: #9CA3AF !important;
    font-size: 0.8rem !important;
    padding: 0.5rem 1.2rem !important;
    border-radius: 6px !important;
}
.stDownloadButton > button:hover {
    border-color: #7DD3C8 !important;
    color: #7DD3C8 !important;
    background: rgba(125,211,200,0.05) !important;
}
</style>
""", unsafe_allow_html=True)


# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="brand-sub">Multi-Agent Research System</div>
<div class="brand-headline">Turn any topic into a<br><em>research-grade report.</em></div>
""", unsafe_allow_html=True)

st.markdown("<div style='height:0.2rem'></div>", unsafe_allow_html=True)


# ── Pipeline step renderer ────────────────────────────────────────────────────
STEPS = [
    ("Search",  "Web discovery",    "Finds recent, reliable sources across the web"),
    ("Scrape",  "Deep extraction",  "Reads full content from the best URLs"),
    ("Write",   "Report synthesis", "Composes a structured research report"),
    ("Review",  "Critic analysis",  "Evaluates quality and highlights gaps"),
]

def render_pipeline(active_step: int):
    cells = ""
    for i, (label, eyebrow, desc) in enumerate(STEPS):
        if i < active_step:
            dot_cls = "done"; label_cls = "done"; cell_cls = "done"
            mark = "✓ "
        elif i == active_step:
            dot_cls = "active"; label_cls = "active"; cell_cls = "active"
            mark = ""
        else:
            dot_cls = ""; label_cls = ""; cell_cls = ""
            mark = ""
        cells += f"""
        <div class="step-cell {cell_cls}">
            <div class="step-dot {dot_cls}"></div>
            <div class="step-label {label_cls}">{mark}{label}</div>
            <div class="step-desc">{desc}</div>
        </div>"""
    st.markdown(f'<div class="pipeline-grid">{cells}</div>', unsafe_allow_html=True)


def result_card(icon, icon_cls, title, content):
    st.markdown(f"""
    <div class="result-card">
        <div class="result-card-header">
            <div class="result-card-icon {icon_cls}">{icon}</div>
            <div class="result-card-title">{title}</div>
        </div>
        <div class="result-card-body">{content}</div>
    </div>
    """, unsafe_allow_html=True)


# ── Input row ─────────────────────────────────────────────────────────────────
col_input, col_btn = st.columns([5, 1], gap="small")
with col_input:
    topic = st.text_input(
        "Research Topic",
        placeholder="e.g. Quantum computing applications in drug discovery",
        label_visibility="visible",
    )
with col_btn:
    st.markdown("<div style='height:1.85rem'></div>", unsafe_allow_html=True)
    run = st.button("Run Pipeline", use_container_width=True)

st.markdown("<hr class='section-divider'>", unsafe_allow_html=True)


# ── Session state ─────────────────────────────────────────────────────────────
if "result" not in st.session_state:
    st.session_state.result = None
if "ran_topic" not in st.session_state:
    st.session_state.ran_topic = ""


# ── Idle state ────────────────────────────────────────────────────────────────
if not run and st.session_state.result is None:
    render_pipeline(-1)
    st.markdown("""
    <div style='text-align:center; padding: 2.5rem 0 1.5rem; color:#4B5563; font-size:0.85rem;'>
        Enter a topic above and click <strong style='color:#6B7280'>Run Pipeline</strong> to begin.
    </div>
    """, unsafe_allow_html=True)


# ── Run pipeline ──────────────────────────────────────────────────────────────
if run:
    if not topic.strip():
        st.warning("Please enter a research topic first.")
        st.stop()

    # Import here so missing deps show a clean error
    try:
        from pipeline import run_research_pipeline
    except ImportError as e:
        st.error(f"Could not import pipeline: {e}")
        st.stop()

    st.session_state.result = None
    st.session_state.ran_topic = topic

    # Step-by-step progress using a placeholder
    prog_ph   = st.empty()
    status_ph = st.empty()

    steps_done = {}

    # We monkey-patch the pipeline to emit progress between steps
    # by running it in a stepwise manner using a custom wrapper.

    import agents

    # Step 1 – Search
    with prog_ph.container():
        render_pipeline(0)
    status_ph.markdown("""
    <div class="status-bar">
        <div class="status-dot-running"></div>
        Step 1 of 4 — Search agent is scouring the web…
    </div>""", unsafe_allow_html=True)

    state = {}
    try:
        search_agent = agents.build_search_agent()
        search_result = search_agent.invoke({
            "messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]
        })
        state["search_results"] = search_result["messages"][-1].content
    except Exception as e:
        st.error(f"Search agent failed: {e}")
        st.stop()

    # Step 2 – Scrape
    with prog_ph.container():
        render_pipeline(1)
    status_ph.markdown("""
    <div class="status-bar">
        <div class="status-dot-running"></div>
        Step 2 of 4 — Reader agent is scraping top sources…
    </div>""", unsafe_allow_html=True)

    try:
        reader_agent = agents.build_reader_agent()
        scraped = reader_agent.invoke({
            "messages": [("user",
                f"Based on the following search results about '{topic}', "
                f"pick the most relevant URL and scrape it for deeper content.\n\n"
                f"Search Results:\n{state['search_results'][:800]}"
            )]
        })
        state["scraped_content"] = scraped["messages"][-1].content
    except Exception as e:
        st.error(f"Reader agent failed: {e}")
        st.stop()

    # Step 3 – Write
    with prog_ph.container():
        render_pipeline(2)
    status_ph.markdown("""
    <div class="status-bar">
        <div class="status-dot-running"></div>
        Step 3 of 4 — Writer is composing the report…
    </div>""", unsafe_allow_html=True)

    try:
        research_combined = (
            f"SEARCH RESULTS:\n{state['search_results']}\n\n"
            f"DETAILED SCRAPED CONTENT:\n{state['scraped_content']}"
        )
        state["report"] = agents.writer_chain.invoke({
            "topic": topic,
            "research": research_combined
        })
    except Exception as e:
        st.error(f"Writer chain failed: {e}")
        st.stop()

    # Step 4 – Critic
    with prog_ph.container():
        render_pipeline(3)
    status_ph.markdown("""
    <div class="status-bar">
        <div class="status-dot-running"></div>
        Step 4 of 4 — Critic is reviewing the report…
    </div>""", unsafe_allow_html=True)

    try:
        state["feedback"] = agents.critic_chain.invoke({
            "report": state["report"]
        })
    except Exception as e:
        st.error(f"Critic chain failed: {e}")
        st.stop()

    # Done
    with prog_ph.container():
        render_pipeline(4)
    status_ph.markdown("""
    <div class="status-bar" style="border-color:#3D7A74; color:#7DD3C8;">
        <div style="width:7px;height:7px;border-radius:50%;background:#7DD3C8;flex-shrink:0;"></div>
        Pipeline complete — report ready.
    </div>""", unsafe_allow_html=True)

    st.session_state.result = state


# ── Results ───────────────────────────────────────────────────────────────────
if st.session_state.result:
    state = st.session_state.result
    topic_label = st.session_state.ran_topic

    st.markdown(f"""
    <div style='margin-bottom:1.5rem'>
        <span style='font-size:0.72rem;font-weight:600;letter-spacing:0.08em;
                     text-transform:uppercase;color:#4B5563;'>Research topic</span><br>
        <span style='font-size:1.15rem;font-weight:500;color:#E8E6E1;'>{topic_label}</span>
    </div>
    """, unsafe_allow_html=True)

    tab_report, tab_sources, tab_feedback = st.tabs(["📄  Report", "🔎  Sources", "🗂️  Critic Feedback"])

    with tab_report:
        st.markdown(f"""
        <div class="report-card">
            <div style='font-size:0.72rem;font-weight:600;letter-spacing:0.08em;
                        text-transform:uppercase;color:#7DD3C8;margin-bottom:0.9rem;'>
                Final Report
            </div>
            <div style='font-size:0.9rem;color:#C9C4BC;line-height:1.8;white-space:pre-wrap;
                        word-break:break-word;'>
{state['report']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        report_text = state["report"]
        if isinstance(report_text, str):
            st.download_button(
                label="⬇  Download report (.txt)",
                data=report_text,
                file_name=f"research_{topic_label[:40].replace(' ','_')}.txt",
                mime="text/plain",
            )

    with tab_sources:
        col_a, col_b = st.columns(2, gap="medium")
        with col_a:
            result_card("🔍", "icon-search", "Web Search Results", state["search_results"])
        with col_b:
            result_card("🌐", "icon-scrape", "Scraped Page Content", state["scraped_content"])

    with tab_feedback:
        st.markdown(f"""
        <div class="feedback-card">
            <div style='font-size:0.72rem;font-weight:600;letter-spacing:0.08em;
                        text-transform:uppercase;color:#F87171;margin-bottom:0.9rem;'>
                Critic Analysis
            </div>
            <div style='font-size:0.9rem;color:#C9C4BC;line-height:1.8;white-space:pre-wrap;
                        word-break:break-word;'>
{state['feedback']}
            </div>
        </div>
        """, unsafe_allow_html=True)

        feedback_text = state["feedback"]
        if isinstance(feedback_text, str):
            st.download_button(
                label="⬇  Download feedback (.txt)",
                data=feedback_text,
                file_name=f"feedback_{topic_label[:40].replace(' ','_')}.txt",
                mime="text/plain",
            )