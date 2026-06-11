import streamlit as st

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="ResearchMind AI",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Master CSS + Animations ───────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=Syne:wght@400;500;600;700;800&family=JetBrains+Mono:wght@300;400;500&display=swap');

/* ══ RESET ══════════════════════════════════════════════════════════════ */
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

html, body, [class*="css"] {
    font-family: 'Space Grotesk', sans-serif;
    background: #050609 !important;
    color: #E2E8F0;
    -webkit-font-smoothing: antialiased;
}

.stApp { background: #050609 !important; }
#MainMenu, footer, header { visibility: hidden; }
.block-container {
    padding: 0 !important;
    max-width: 100% !important;
}

/* ══ SCROLLBAR ══════════════════════════════════════════════════════════ */
::-webkit-scrollbar { width: 5px; }
::-webkit-scrollbar-track { background: #0A0C12; }
::-webkit-scrollbar-thumb { background: #1E293B; border-radius: 99px; }
::-webkit-scrollbar-thumb:hover { background: #4ADE80; }

/* ══ HERO SECTION ═══════════════════════════════════════════════════════ */
.hero-wrapper {
    position: relative;
    min-height: 520px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 5rem 2rem 4rem;
    overflow: hidden;
}

/* Animated mesh gradient background */
.hero-bg {
    position: absolute;
    inset: 0;
    background:
        radial-gradient(ellipse 80% 60% at 20% 0%, rgba(74,222,128,0.12) 0%, transparent 60%),
        radial-gradient(ellipse 60% 50% at 80% 10%, rgba(139,92,246,0.10) 0%, transparent 55%),
        radial-gradient(ellipse 50% 40% at 50% 100%, rgba(6,182,212,0.08) 0%, transparent 50%),
        #050609;
    animation: meshShift 8s ease-in-out infinite alternate;
}
@keyframes meshShift {
    0%   { filter: hue-rotate(0deg)   brightness(1);    }
    50%  { filter: hue-rotate(15deg)  brightness(1.05); }
    100% { filter: hue-rotate(-10deg) brightness(1);    }
}

/* Floating orbs */
.orb {
    position: absolute;
    border-radius: 50%;
    filter: blur(60px);
    opacity: 0.18;
    animation: float linear infinite;
}
.orb-1 { width:320px; height:320px; background:#4ADE80; top:-80px; left:-60px;  animation-duration:14s; }
.orb-2 { width:260px; height:260px; background:#818CF8; top:60px;  right:-80px; animation-duration:18s; animation-delay:-6s; }
.orb-3 { width:200px; height:200px; background:#22D3EE; bottom:0;  left:30%;    animation-duration:22s; animation-delay:-10s; }
@keyframes float {
    0%   { transform: translate(0,0)      rotate(0deg);   }
    25%  { transform: translate(30px,-20px) rotate(90deg);  }
    50%  { transform: translate(-20px,30px) rotate(180deg); }
    75%  { transform: translate(20px,10px)  rotate(270deg); }
    100% { transform: translate(0,0)      rotate(360deg); }
}

/* Grid overlay */
.hero-grid {
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(rgba(74,222,128,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(74,222,128,0.04) 1px, transparent 1px);
    background-size: 48px 48px;
    mask-image: radial-gradient(ellipse 70% 70% at 50% 50%, black 40%, transparent 100%);
}

/* Scanline shimmer */
.hero-scanline {
    position: absolute;
    inset: 0;
    background: linear-gradient(
        to bottom,
        transparent 0%,
        rgba(74,222,128,0.015) 50%,
        transparent 100%
    );
    background-size: 100% 8px;
    animation: scan 3s linear infinite;
}
@keyframes scan {
    from { background-position: 0 -100%; }
    to   { background-position: 0  100%; }
}

/* Hero text */
.hero-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.72rem;
    font-weight: 400;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    color: #4ADE80;
    margin-bottom: 1.4rem;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.7rem;
    position: relative;
    z-index: 2;
    animation: fadeSlideUp 0.8s ease both;
}
.hero-eyebrow::before,
.hero-eyebrow::after {
    content: '';
    width: 40px; height: 1px;
    background: linear-gradient(90deg, transparent, #4ADE80);
}
.hero-eyebrow::after { background: linear-gradient(90deg, #4ADE80, transparent); }

.hero-title {
    font-family: 'Syne', sans-serif;
    font-size: clamp(3rem, 7vw, 5.5rem);
    font-weight: 800;
    line-height: 1.0;
    letter-spacing: -0.03em;
    color: #F8FAFC;
    position: relative;
    z-index: 2;
    margin-bottom: 0.6rem;
    animation: fadeSlideUp 0.8s 0.15s ease both;
}
.hero-title .glow-word {
    background: linear-gradient(135deg, #4ADE80 0%, #22D3EE 50%, #818CF8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    filter: drop-shadow(0 0 30px rgba(74,222,128,0.35));
}

.hero-sub {
    font-size: 1.1rem;
    font-weight: 400;
    color: #64748B;
    max-width: 520px;
    line-height: 1.65;
    position: relative;
    z-index: 2;
    margin-bottom: 3rem;
    animation: fadeSlideUp 0.8s 0.3s ease both;
}

/* ══ AGENT BADGES ═══════════════════════════════════════════════════════ */
.badges-row {
    display: flex;
    gap: 0.6rem;
    justify-content: center;
    flex-wrap: wrap;
    position: relative;
    z-index: 2;
    margin-bottom: 0;
    animation: fadeSlideUp 0.8s 0.45s ease both;
}
.badge {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    font-weight: 400;
    letter-spacing: 0.06em;
    padding: 0.35rem 0.85rem;
    border-radius: 99px;
    border: 1px solid;
    display: flex; align-items: center; gap: 0.4rem;
    animation: badgePulse 3s ease-in-out infinite;
}
.badge-1 { color:#4ADE80; border-color:rgba(74,222,128,0.3);  background:rgba(74,222,128,0.07);  animation-delay:0s;    }
.badge-2 { color:#22D3EE; border-color:rgba(34,211,238,0.3);  background:rgba(34,211,238,0.07);  animation-delay:0.5s;  }
.badge-3 { color:#A78BFA; border-color:rgba(167,139,250,0.3); background:rgba(167,139,250,0.07); animation-delay:1s;    }
.badge-4 { color:#FB923C; border-color:rgba(251,146,60,0.3);  background:rgba(251,146,60,0.07);  animation-delay:1.5s;  }
@keyframes badgePulse {
    0%,100% { opacity:0.75; transform:translateY(0);   }
    50%      { opacity:1;    transform:translateY(-2px); }
}

@keyframes fadeSlideUp {
    from { opacity:0; transform:translateY(24px); }
    to   { opacity:1; transform:translateY(0);    }
}

/* ══ MAIN CONTENT WRAPPER ═══════════════════════════════════════════════ */
.content-wrapper {
    max-width: 900px;
    margin: 0 auto;
    padding: 0 2rem 5rem;
}

/* ══ INPUT CARD ══════════════════════════════════════════════════════════ */
.input-card {
    background: rgba(15,18,28,0.8);
    border: 1px solid rgba(74,222,128,0.15);
    border-radius: 20px;
    padding: 2.2rem 2.4rem;
    margin-bottom: 2.5rem;
    backdrop-filter: blur(20px);
    box-shadow:
        0 0 0 1px rgba(74,222,128,0.05),
        0 24px 48px rgba(0,0,0,0.5),
        inset 0 1px 0 rgba(255,255,255,0.04);
    position: relative;
    overflow: hidden;
}
.input-card::before {
    content: '';
    position: absolute;
    top: 0; left: 10%; right: 10%;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(74,222,128,0.4), transparent);
}

.stTextInput > div > div > input {
    background: rgba(5,6,9,0.8) !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    border-radius: 12px !important;
    color: #F1F5F9 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 1.05rem !important;
    font-weight: 400 !important;
    padding: 1rem 1.3rem !important;
    transition: all 0.3s cubic-bezier(0.4,0,0.2,1) !important;
    letter-spacing: 0.01em !important;
}
.stTextInput > div > div > input::placeholder {
    color: #334155 !important;
}
.stTextInput > div > div > input:focus {
    border-color: rgba(74,222,128,0.5) !important;
    box-shadow:
        0 0 0 3px rgba(74,222,128,0.08),
        0 0 20px rgba(74,222,128,0.1) !important;
    background: rgba(5,6,9,0.95) !important;
}
.stTextInput > label {
    font-family: 'JetBrains Mono', monospace !important;
    font-size: 0.7rem !important;
    font-weight: 400 !important;
    letter-spacing: 0.15em !important;
    text-transform: uppercase !important;
    color: #4ADE80 !important;
    margin-bottom: 0.6rem !important;
}

/* ══ BUTTON ══════════════════════════════════════════════════════════════ */
.stButton > button {
    background: linear-gradient(135deg, #16a34a 0%, #15803d 100%) !important;
    color: #F0FDF4 !important;
    border: none !important;
    border-radius: 12px !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.95rem !important;
    letter-spacing: 0.04em !important;
    padding: 0.9rem 1.8rem !important;
    width: 100% !important;
    cursor: pointer !important;
    position: relative !important;
    overflow: hidden !important;
    transition: all 0.3s cubic-bezier(0.4,0,0.2,1) !important;
    box-shadow: 0 4px 24px rgba(74,222,128,0.25), 0 0 0 1px rgba(74,222,128,0.2) !important;
}
.stButton > button::after {
    content: '' !important;
    position: absolute !important;
    inset: 0 !important;
    background: linear-gradient(135deg, rgba(255,255,255,0.15) 0%, transparent 100%) !important;
    opacity: 0 !important;
    transition: opacity 0.2s !important;
}
.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 32px rgba(74,222,128,0.35), 0 0 0 1px rgba(74,222,128,0.35) !important;
    background: linear-gradient(135deg, #22c55e 0%, #16a34a 100%) !important;
}
.stButton > button:hover::after { opacity: 1 !important; }
.stButton > button:active { transform: translateY(0) !important; }

/* ══ PIPELINE TRACKER ═══════════════════════════════════════════════════ */
.pipeline-outer {
    margin-bottom: 2rem;
}
.pipeline-header {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #334155;
    margin-bottom: 1.2rem;
    text-align: center;
}
.pipeline-track {
    display: grid;
    grid-template-columns: 1fr 32px 1fr 32px 1fr 32px 1fr;
    align-items: center;
    gap: 0;
    margin-bottom: 1.4rem;
}
.connector-line {
    height: 2px;
    background: #0F172A;
    position: relative;
    overflow: hidden;
}
.connector-line.done {
    background: linear-gradient(90deg, #4ADE80, #22D3EE);
    box-shadow: 0 0 6px rgba(74,222,128,0.4);
}
.connector-line.active {
    background: #0F172A;
    overflow: hidden;
}
.connector-line.active::after {
    content: '';
    position: absolute;
    top: 0; left: -100%; right: 0; bottom: 0;
    background: linear-gradient(90deg, transparent, #4ADE80, transparent);
    animation: lineFlow 1.5s ease-in-out infinite;
}
@keyframes lineFlow {
    from { left: -100%; }
    to   { left:  100%; }
}

/* Step node */
.step-node {
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 0.6rem;
    position: relative;
}
.node-circle {
    width: 64px; height: 64px;
    border-radius: 50%;
    border: 2px solid #1E293B;
    background: #0A0C12;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.4rem;
    position: relative;
    transition: all 0.4s cubic-bezier(0.34,1.56,0.64,1);
    z-index: 1;
}
.step-node.idle   .node-circle { border-color:#1E293B; filter:grayscale(1) opacity(0.4); }
.step-node.active .node-circle {
    border-color: #4ADE80;
    background: rgba(74,222,128,0.08);
    box-shadow:
        0 0 0 6px rgba(74,222,128,0.1),
        0 0 0 12px rgba(74,222,128,0.05),
        0 0 30px rgba(74,222,128,0.3);
    animation: nodeBreath 1.4s ease-in-out infinite;
}
.step-node.done .node-circle {
    border-color: #22c55e;
    background: rgba(34,197,94,0.12);
    box-shadow: 0 0 20px rgba(34,197,94,0.25);
}
@keyframes nodeBreath {
    0%,100% { box-shadow: 0 0 0 6px rgba(74,222,128,0.1),  0 0 0 12px rgba(74,222,128,0.05), 0 0 30px rgba(74,222,128,0.3);  }
    50%      { box-shadow: 0 0 0 10px rgba(74,222,128,0.15), 0 0 0 20px rgba(74,222,128,0.07), 0 0 50px rgba(74,222,128,0.4); }
}

/* Done checkmark overlay */
.step-node.done .node-circle::after {
    content: '✓';
    position: absolute;
    inset: 0;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.5rem;
    color: #4ADE80;
    background: rgba(5,6,9,0.7);
    border-radius: 50%;
    animation: checkIn 0.3s cubic-bezier(0.34,1.56,0.64,1) both;
}
@keyframes checkIn {
    from { transform: scale(0) rotate(-45deg); opacity:0; }
    to   { transform: scale(1) rotate(0deg);   opacity:1; }
}

.node-label {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.78rem;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-align: center;
    line-height: 1.3;
}
.step-node.idle   .node-label { color: #334155; }
.step-node.active .node-label { color: #4ADE80; }
.step-node.done   .node-label { color: #64748B; }

.node-sub {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.6rem;
    color: #1E293B;
    text-align: center;
    letter-spacing: 0.06em;
    text-transform: uppercase;
}
.step-node.active .node-sub { color: #166534; }
.step-node.done   .node-sub { color: #1E293B; }

/* ══ STATUS BANNER ═══════════════════════════════════════════════════════ */
.status-banner {
    display: flex;
    align-items: center;
    gap: 1rem;
    padding: 1rem 1.4rem;
    border-radius: 14px;
    border: 1px solid rgba(74,222,128,0.15);
    background: rgba(74,222,128,0.04);
    margin-bottom: 2rem;
    font-size: 0.9rem;
    color: #94A3B8;
    font-weight: 500;
    position: relative;
    overflow: hidden;
}
.status-banner::before {
    content: '';
    position: absolute;
    top: 0; left: -100%; width: 100%; height: 100%;
    background: linear-gradient(90deg, transparent, rgba(74,222,128,0.03), transparent);
    animation: bannerShimmer 2.5s ease-in-out infinite;
}
@keyframes bannerShimmer {
    from { left: -100%; }
    to   { left:  200%; }
}
.status-banner.complete {
    border-color: rgba(74,222,128,0.3);
    background: rgba(74,222,128,0.06);
    color: #4ADE80;
}
.pulse-ring {
    width: 12px; height: 12px;
    border-radius: 50%;
    background: #4ADE80;
    flex-shrink: 0;
    position: relative;
}
.pulse-ring::before, .pulse-ring::after {
    content: '';
    position: absolute;
    inset: -4px;
    border-radius: 50%;
    border: 2px solid #4ADE80;
    animation: ringPulse 1.6s ease-out infinite;
}
.pulse-ring::after { animation-delay: 0.8s; }
@keyframes ringPulse {
    0%   { transform:scale(0.5); opacity:0.8; }
    100% { transform:scale(2.5); opacity:0;   }
}
.status-step-tag {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.1em;
    padding: 0.2rem 0.6rem;
    border-radius: 99px;
    background: rgba(74,222,128,0.1);
    color: #4ADE80;
    border: 1px solid rgba(74,222,128,0.2);
    margin-left: auto;
    flex-shrink: 0;
}

/* ══ RESULT TABS ═════════════════════════════════════════════════════════ */
.stTabs [data-baseweb="tab-list"] {
    background: transparent !important;
    gap: 0.3rem !important;
    border-bottom: 1px solid rgba(255,255,255,0.06) !important;
    padding-bottom: 0 !important;
}
.stTabs [data-baseweb="tab"] {
    background: transparent !important;
    color: #475569 !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.88rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.02em !important;
    padding: 0.65rem 1.2rem !important;
    border-radius: 8px 8px 0 0 !important;
    transition: color 0.2s !important;
}
.stTabs [data-baseweb="tab"]:hover { color: #94A3B8 !important; }
.stTabs [aria-selected="true"] {
    color: #4ADE80 !important;
    border-bottom: 2px solid #4ADE80 !important;
    background: rgba(74,222,128,0.04) !important;
}
[data-baseweb="tab-panel"] {
    padding: 1.8rem 0 0 !important;
}

/* ══ RESULT CARDS ════════════════════════════════════════════════════════ */
.rcard {
    background: rgba(10,12,18,0.9);
    border: 1px solid rgba(255,255,255,0.06);
    border-radius: 16px;
    overflow: hidden;
    margin-bottom: 1.2rem;
}
.rcard-head {
    display: flex;
    align-items: center;
    gap: 0.9rem;
    padding: 1.1rem 1.4rem;
    border-bottom: 1px solid rgba(255,255,255,0.05);
    background: rgba(255,255,255,0.02);
}
.rcard-icon {
    width: 36px; height: 36px;
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1rem;
    flex-shrink: 0;
}
.rcard-title {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.82rem;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    color: #94A3B8;
}
.rcard-body {
    padding: 1.3rem 1.4rem;
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.9rem;
    line-height: 1.8;
    color: #94A3B8;
    white-space: pre-wrap;
    word-break: break-word;
    max-height: 380px;
    overflow-y: auto;
}
.rcard-body::-webkit-scrollbar { width: 3px; }
.rcard-body::-webkit-scrollbar-thumb { background: #1E293B; border-radius: 2px; }

/* Main report card */
.main-report {
    background: rgba(10,12,18,0.9);
    border: 1px solid rgba(255,255,255,0.06);
    border-top: 2px solid #4ADE80;
    border-radius: 16px;
    padding: 2rem 2.2rem;
    margin-bottom: 1.4rem;
    box-shadow: 0 0 40px rgba(74,222,128,0.05);
}
.main-report-eyebrow {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #4ADE80;
    margin-bottom: 1rem;
    display: flex; align-items: center; gap: 0.5rem;
}
.main-report-body {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.97rem;
    line-height: 1.85;
    color: #CBD5E1;
    white-space: pre-wrap;
    word-break: break-word;
}

/* Feedback card */
.feedback-card {
    background: rgba(10,12,18,0.9);
    border: 1px solid rgba(255,255,255,0.06);
    border-top: 2px solid #F87171;
    border-radius: 16px;
    padding: 2rem 2.2rem;
    margin-bottom: 1.4rem;
    box-shadow: 0 0 40px rgba(248,113,113,0.04);
}

/* Topic chip */
.topic-chip {
    display: inline-flex;
    align-items: center;
    gap: 0.6rem;
    padding: 0.5rem 1.1rem;
    background: rgba(74,222,128,0.07);
    border: 1px solid rgba(74,222,128,0.2);
    border-radius: 99px;
    margin-bottom: 1.6rem;
}
.topic-chip-label {
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.65rem;
    color: #4ADE80;
    letter-spacing: 0.12em;
    text-transform: uppercase;
}
.topic-chip-value {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.88rem;
    font-weight: 500;
    color: #E2E8F0;
}

/* ══ DOWNLOAD BUTTON ═════════════════════════════════════════════════════ */
.stDownloadButton > button {
    background: transparent !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    color: #64748B !important;
    font-family: 'Space Grotesk', sans-serif !important;
    font-size: 0.8rem !important;
    font-weight: 500 !important;
    padding: 0.55rem 1.3rem !important;
    border-radius: 8px !important;
    transition: all 0.2s !important;
    letter-spacing: 0.02em !important;
}
.stDownloadButton > button:hover {
    border-color: rgba(74,222,128,0.4) !important;
    color: #4ADE80 !important;
    background: rgba(74,222,128,0.05) !important;
}

/* ══ IDLE EMPTY STATE ════════════════════════════════════════════════════ */
.empty-state {
    text-align: center;
    padding: 3rem 0 1rem;
}
.empty-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
    display: block;
    opacity: 0.25;
    animation: emptyFloat 3s ease-in-out infinite;
}
@keyframes emptyFloat {
    0%,100% { transform:translateY(0);    }
    50%      { transform:translateY(-8px); }
}
.empty-text {
    font-family: 'Space Grotesk', sans-serif;
    font-size: 0.88rem;
    color: #1E293B;
    font-weight: 500;
}

/* ══ WARNING / ERROR ═════════════════════════════════════════════════════ */
.stAlert {
    border-radius: 12px !important;
    border: 1px solid rgba(251,146,60,0.2) !important;
    background: rgba(251,146,60,0.05) !important;
    font-family: 'Space Grotesk', sans-serif !important;
}
</style>
""", unsafe_allow_html=True)


# ══ HERO ══════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="hero-wrapper">
    <div class="hero-bg"></div>
    <div class="hero-grid"></div>
    <div class="hero-scanline"></div>
    <div class="orb orb-1"></div>
    <div class="orb orb-2"></div>
    <div class="orb orb-3"></div>

    <div class="hero-eyebrow">⚡ Multi-Agent AI System</div>

    <div class="hero-title">
        Research, <span class="glow-word">Automated.</span>
    </div>

    <p class="hero-sub">
        Four specialized AI agents — searching, scraping, writing, and critiquing —
        working in sequence to produce publication-ready research reports.
    </p>

    <div class="badges-row">
        <span class="badge badge-1">◎ Search Agent</span>
        <span class="badge badge-2">⬡ Scrape Agent</span>
        <span class="badge badge-3">✦ Writer Agent</span>
        <span class="badge badge-4">⌖ Critic Agent</span>
    </div>
</div>
""", unsafe_allow_html=True)


# ══ PIPELINE STEP RENDERER ════════════════════════════════════════════════════
STEPS = [
    ("◎", "Search",  "Web Discovery"),
    ("⬡", "Scrape",  "Deep Extraction"),
    ("✦", "Write",   "Report Synthesis"),
    ("⌖", "Review",  "Critic Analysis"),
]

STEP_COLORS = ["#4ADE80", "#22D3EE", "#A78BFA", "#FB923C"]


def render_pipeline(active_step: int):
    track_items = ""
    for i, (icon, label, sub) in enumerate(STEPS):
        if i < active_step:
            state_cls = "done"
        elif i == active_step:
            state_cls = "active"
        else:
            state_cls = "idle"

        track_items += f"""
        <div class="step-node {state_cls}">
            <div class="node-circle">{icon}</div>
            <div class="node-label">{label}</div>
            <div class="node-sub">{sub}</div>
        </div>"""

        if i < len(STEPS) - 1:
            if i < active_step - 1:
                line_cls = "done"
            elif i == active_step - 1:
                line_cls = "done"
            elif i == active_step:
                line_cls = "active"
            else:
                line_cls = ""
            track_items += f'<div class="connector-line {line_cls}"></div>'

    st.markdown(f"""
    <div class="pipeline-outer">
        <div class="pipeline-header">— Pipeline Status —</div>
        <div class="pipeline-track">{track_items}</div>
    </div>
    """, unsafe_allow_html=True)


def render_status(msg: str, tag: str = "", complete: bool = False):
    cls = "complete" if complete else ""
    dot = '<div class="pulse-ring"></div>' if not complete else '<span style="font-size:1.1rem">✓</span>'
    tag_html = f'<span class="status-step-tag">{tag}</span>' if tag else ""
    st.markdown(f"""
    <div class="status-banner {cls}">
        {dot}
        <span>{msg}</span>
        {tag_html}
    </div>""", unsafe_allow_html=True)


def result_card(icon, bg, title, content):
    st.markdown(f"""
    <div class="rcard">
        <div class="rcard-head">
            <div class="rcard-icon" style="background:{bg}">{icon}</div>
            <div class="rcard-title">{title}</div>
        </div>
        <div class="rcard-body">{content}</div>
    </div>
    """, unsafe_allow_html=True)


# ══ SESSION STATE ═════════════════════════════════════════════════════════════
if "result" not in st.session_state:
    st.session_state.result = None
if "ran_topic" not in st.session_state:
    st.session_state.ran_topic = ""


# ══ CONTENT AREA ═════════════════════════════════════════════════════════════
st.markdown('<div class="content-wrapper">', unsafe_allow_html=True)

# Input card
st.markdown('<div class="input-card">', unsafe_allow_html=True)
col_input, col_btn = st.columns([5, 1.2], gap="medium")
with col_input:
    topic = st.text_input(
        "Research Topic",
        placeholder="e.g. Quantum computing applications in drug discovery",
        label_visibility="visible",
    )
with col_btn:
    st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)
    run = st.button("⚡  Run", use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)


# ══ IDLE STATE ════════════════════════════════════════════════════════════════
if not run and st.session_state.result is None:
    render_pipeline(-1)
    st.markdown("""
    <div class="empty-state">
        <span class="empty-icon">⚡</span>
        <div class="empty-text">Enter a topic and run the pipeline to generate your research report.</div>
    </div>
    """, unsafe_allow_html=True)


# ══ RUN PIPELINE ══════════════════════════════════════════════════════════════
if run:
    if not topic.strip():
        st.warning("Please enter a research topic first.")
        st.stop()

    try:
        import agents
    except ImportError as e:
        st.error(f"Could not import agents module: {e}")
        st.stop()

    st.session_state.result = None
    st.session_state.ran_topic = topic

    prog_ph   = st.empty()
    status_ph = st.empty()
    state = {}

    # ── Step 1: Search ──
    with prog_ph.container():
        render_pipeline(0)
    with status_ph.container():
        render_status("Search agent is scouring the web for sources…", "01 / 04")

    try:
        search_agent = agents.build_search_agent()
        search_result = search_agent.invoke({
            "messages": [("user", f"Find recent, reliable and detailed information about: {topic}")]
        })
        state["search_results"] = search_result["messages"][-1].content
    except Exception as e:
        st.error(f"Search agent failed: {e}")
        st.stop()

    # ── Step 2: Scrape ──
    with prog_ph.container():
        render_pipeline(1)
    with status_ph.container():
        render_status("Reader agent is extracting full page content…", "02 / 04")

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

    # ── Step 3: Write ──
    with prog_ph.container():
        render_pipeline(2)
    with status_ph.container():
        render_status("Writer agent is composing the structured report…", "03 / 04")

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

    # ── Step 4: Critic ──
    with prog_ph.container():
        render_pipeline(3)
    with status_ph.container():
        render_status("Critic agent is reviewing and scoring the report…", "04 / 04")

    try:
        state["feedback"] = agents.critic_chain.invoke({
            "report": state["report"]
        })
    except Exception as e:
        st.error(f"Critic chain failed: {e}")
        st.stop()

    # ── Done ──
    with prog_ph.container():
        render_pipeline(4)
    with status_ph.container():
        render_status("Pipeline complete — your report is ready.", complete=True)

    st.session_state.result = state


# ══ RESULTS ═══════════════════════════════════════════════════════════════════
if st.session_state.result:
    state = st.session_state.result
    topic_label = st.session_state.ran_topic

    st.markdown(f"""
    <div class="topic-chip">
        <span class="topic-chip-label">Topic</span>
        <span class="topic-chip-value">{topic_label}</span>
    </div>
    """, unsafe_allow_html=True)

    tab_report, tab_sources, tab_feedback = st.tabs([
        "⚡  Final Report",
        "🔎  Source Data",
        "⌖  Critic Feedback",
    ])

    with tab_report:
        report_text = state.get("report", "")
        st.markdown(f"""
        <div class="main-report">
            <div class="main-report-eyebrow">⬡ — Research Output</div>
            <div class="main-report-body">{report_text}</div>
        </div>
        """, unsafe_allow_html=True)
        if isinstance(report_text, str):
            st.download_button(
                label="⬇  Download report (.txt)",
                data=report_text,
                file_name=f"report_{topic_label[:40].replace(' ','_')}.txt",
                mime="text/plain",
            )

    with tab_sources:
        col_a, col_b = st.columns(2, gap="large")
        with col_a:
            result_card("🔍", "rgba(74,222,128,0.1)", "Web Search Results", state.get("search_results", ""))
        with col_b:
            result_card("🌐", "rgba(34,211,238,0.1)", "Scraped Page Content", state.get("scraped_content", ""))

    with tab_feedback:
        feedback_text = state.get("feedback", "")
        st.markdown(f"""
        <div class="feedback-card">
            <div class="main-report-eyebrow" style="color:#F87171;">⌖ — Critic Analysis</div>
            <div class="main-report-body">{feedback_text}</div>
        </div>
        """, unsafe_allow_html=True)
        if isinstance(feedback_text, str):
            st.download_button(
                label="⬇  Download feedback (.txt)",
                data=feedback_text,
                file_name=f"feedback_{topic_label[:40].replace(' ','_')}.txt",
                mime="text/plain",
            )

st.markdown('</div>', unsafe_allow_html=True)