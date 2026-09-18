from __future__ import annotations

import html
import streamlit as st


NAV_ITEMS = [
    ("홈", "⌂"),
    ("시장 현황", "▥"),
    ("종목 분석", "◫"),
    ("공시 분석", "▤"),
    ("테마 & 섹터", "◇"),
    ("포트폴리오", "▣"),
    ("관심 종목", "☆"),
    ("AI 인사이트", "✦"),
    ("데이터 연결 관리", "⚙"),
]


def apply_theme():
    st.markdown(
        """
<style>
:root {
  --bg:#F3F8FF;
  --surface:rgba(255,255,255,.88);
  --surface-strong:#FFFFFF;
  --line:rgba(116,145,190,.18);
  --text:#0B1739;
  --muted:#6D7B98;
  --blue:#2F6BFF;
  --cyan:#15C6FF;
  --green:#18C77A;
  --red:#FF4D6D;
  --orange:#FF9F2F;
  --purple:#7C5CFC;
  --navy:#071A3C;
}
@keyframes bgShift {
  0% { background-position:0% 0%,100% 0%,50% 100%; }
  50% { background-position:12% 8%,88% 5%,45% 92%; }
  100% { background-position:0% 0%,100% 0%,50% 100%; }
}
@keyframes gradientFlow {
  0% { background-position:0% 50%; }
  50% { background-position:100% 50%; }
  100% { background-position:0% 50%; }
}
@keyframes pulseDot {
  0%,100% { box-shadow:0 0 0 0 rgba(24,199,122,.38),0 0 18px rgba(24,199,122,.35); transform:scale(1); }
  50% { box-shadow:0 0 0 7px rgba(24,199,122,0),0 0 26px rgba(24,199,122,.55); transform:scale(1.12); }
}
@keyframes floatUp {
  0%,100% { transform:translateY(0); }
  50% { transform:translateY(-4px); }
}
@keyframes shimmer {
  0% { transform:translateX(-140%) skewX(-18deg); }
  55%,100% { transform:translateX(220%) skewX(-18deg); }
}
@keyframes pointGlow {
  0%,100% { opacity:.72; filter:drop-shadow(0 0 3px currentColor); }
  50% { opacity:1; filter:drop-shadow(0 0 10px currentColor); }
}
@keyframes tickerMove {
  from { transform:translateX(0); }
  to { transform:translateX(-50%); }
}
html, body, [class*="css"] {
  font-family:Pretendard,"Noto Sans KR","Apple SD Gothic Neo",sans-serif;
}
.stApp {
  color:var(--text);
  background:
    radial-gradient(circle at 12% 12%, rgba(49,122,255,.14), transparent 24%),
    radial-gradient(circle at 88% 8%, rgba(124,92,252,.12), transparent 25%),
    radial-gradient(circle at 45% 88%, rgba(21,198,255,.10), transparent 30%),
    linear-gradient(180deg,#F7FBFF 0%,#EEF5FF 100%);
  background-size:120% 120%,120% 120%,130% 130%,100% 100%;
  animation:bgShift 18s ease-in-out infinite;
}
.block-container {
  max-width:1600px;
  padding-top:1rem;
  padding-bottom:5rem;
}
header[data-testid="stHeader"] {
  background:rgba(247,251,255,.72);
  backdrop-filter:blur(16px);
}
section[data-testid="stSidebar"] {
  background:linear-gradient(180deg,rgba(255,255,255,.96),rgba(241,247,255,.94));
  border-right:1px solid rgba(93,132,190,.16);
  box-shadow:10px 0 35px rgba(32,75,145,.04);
}
section[data-testid="stSidebar"] > div { padding-top:.8rem; }
[data-testid="stSidebar"] .stRadio > label { display:none; }
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] { gap:.34rem; }
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
  position:relative;
  border-radius:14px;
  padding:.68rem .72rem;
  transition:transform .18s ease,background .18s ease,box-shadow .18s ease;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
  background:rgba(232,242,255,.9);
  transform:translateX(3px);
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked) {
  color:#FFFFFF;
  font-weight:800;
  background:linear-gradient(120deg,#1E63F3,#44B7FF,#6F73FF);
  background-size:200% 200%;
  animation:gradientFlow 5s ease infinite;
  box-shadow:0 12px 26px rgba(47,107,255,.24),inset 0 1px rgba(255,255,255,.38);
}
h1,h2,h3,h4 { color:var(--text); letter-spacing:-.04em; }
h1 { font-weight:860; }
h2,h3 { font-weight:790; }
p,li { line-height:1.62; }
[data-testid="stCaptionContainer"] { color:var(--muted); }
[data-testid="stMetric"] {
  background:rgba(255,255,255,.9);
  border:1px solid var(--line);
  border-radius:20px;
  padding:16px 18px;
  box-shadow:0 12px 34px rgba(26,73,145,.07);
  transition:transform .2s ease,box-shadow .2s ease;
}
[data-testid="stMetric"]:hover {
  transform:translateY(-3px);
  box-shadow:0 18px 42px rgba(26,73,145,.12);
}
[data-testid="stMetricLabel"] { color:var(--muted); font-weight:680; }
[data-testid="stMetricValue"] { color:var(--text); font-weight:840; }
[data-testid="stVerticalBlockBorderWrapper"] {
  border-color:var(--line)!important;
  border-radius:20px!important;
  background:rgba(255,255,255,.88);
  box-shadow:0 12px 34px rgba(26,73,145,.065);
  backdrop-filter:blur(14px);
  transition:transform .2s ease,box-shadow .2s ease;
}
[data-testid="stVerticalBlockBorderWrapper"]:hover {
  transform:translateY(-2px);
  box-shadow:0 18px 46px rgba(26,73,145,.10);
}
.stButton > button,.stFormSubmitButton > button {
  border-radius:12px;
  min-height:2.72rem;
  font-weight:780;
  transition:transform .18s ease,box-shadow .18s ease;
}
.stButton > button:hover,.stFormSubmitButton > button:hover { transform:translateY(-1px); }
.stButton > button[kind="primary"],.stFormSubmitButton > button[kind="primary"] {
  color:#FFF;
  border:0;
  background:linear-gradient(115deg,#215EF5,#35B8FF,#745CFF);
  background-size:220% 220%;
  animation:gradientFlow 5s ease infinite;
  box-shadow:0 10px 24px rgba(47,107,255,.22);
}
.stTextInput input,.stTextArea textarea,.stSelectbox div[data-baseweb="select"] > div {
  border-radius:13px!important;
  background:rgba(255,255,255,.92);
  border-color:rgba(116,145,190,.22)!important;
}
.stTabs [data-baseweb="tab-list"] { gap:8px; }
.stTabs [data-baseweb="tab"] { border-radius:11px; padding:9px 13px; }
.stDataFrame {
  border:1px solid var(--line);
  border-radius:15px;
  overflow:hidden;
}
.planx-brand { display:flex; align-items:center; gap:11px; margin:4px 0 22px; }
.planx-brand-mark {
  width:40px; height:40px; border-radius:13px;
  display:flex; align-items:center; justify-content:center;
  background:linear-gradient(145deg,#1F62F4,#32C1FF 55%,#755DFF);
  background-size:180% 180%;
  animation:gradientFlow 5s ease infinite,floatUp 4s ease-in-out infinite;
  color:white; font-size:20px; font-weight:900;
  box-shadow:0 10px 28px rgba(47,107,255,.28),0 0 22px rgba(21,198,255,.16);
}
.planx-brand-title { font-size:20px; line-height:1.05; font-weight:860; letter-spacing:-.035em; }
.planx-brand-sub { font-size:9px; color:#8A99B8; margin-top:4px; letter-spacing:.08em; }
.planx-hero {
  position:relative; overflow:hidden;
  background:linear-gradient(135deg,rgba(255,255,255,.96),rgba(242,248,255,.92),rgba(239,242,255,.9));
  border:1px solid rgba(126,155,201,.16);
  border-radius:24px; padding:26px 29px; margin-bottom:18px;
  box-shadow:0 18px 46px rgba(26,73,145,.07);
}
.planx-hero:after {
  content:""; position:absolute; inset:-40% auto -40% -30%;
  width:36%; background:linear-gradient(90deg,transparent,rgba(255,255,255,.85),transparent);
  animation:shimmer 6s ease-in-out infinite;
}
.planx-eyebrow { color:#2F6BFF; font-size:11px; font-weight:850; letter-spacing:.1em; margin-bottom:7px; }
.planx-hero h1 { margin:0; font-size:33px; line-height:1.18; }
.planx-hero p { margin:8px 0 0; color:#6D7B98; font-size:14px; }
.planx-card {
  position:relative; overflow:hidden;
  background:rgba(255,255,255,.92);
  border:1px solid var(--line);
  border-radius:20px; padding:18px 19px; min-height:120px;
  box-shadow:0 12px 34px rgba(26,73,145,.06);
  transition:transform .2s ease,box-shadow .2s ease;
}
.planx-card:hover { transform:translateY(-3px); box-shadow:0 18px 44px rgba(26,73,145,.11); }
.planx-card-title { font-size:12px; color:#6D7B98; margin-bottom:8px; font-weight:760; }
.planx-card-value { font-size:23px; color:#0B1739; font-weight:860; letter-spacing:-.035em; font-variant-numeric:tabular-nums; }
.planx-card-note { margin-top:7px; font-size:11px; color:#93A0B8; }
.planx-empty {
  background:rgba(250,253,255,.72); border:1px dashed #C7D6ED; border-radius:17px;
  padding:22px; color:#6D7B98;
}
.planx-source {
  display:inline-flex; align-items:center; gap:5px;
  color:#64748B; background:#F8FAFC; border:1px solid #E2E8F0;
  padding:4px 8px; border-radius:999px; font-size:10px;
}
.planx-status-ok { color:#047857; background:#ECFDF5; border-color:#A7F3D0; }
.planx-status-wait { color:#92400E; background:#FFFBEB; border-color:#FDE68A; }
.planx-status-bad { color:#B91C1C; background:#FEF2F2; border-color:#FECACA; }

.dashboard-title {
  display:flex; justify-content:space-between; align-items:flex-end;
  gap:18px; margin:0 0 12px;
}
.dashboard-title h1 { margin:0; font-size:36px; }
.dashboard-title p { margin:7px 0 0; color:#64748B; font-size:14px; }
.dashboard-clock {
  color:#64748B; font-size:12px; white-space:nowrap;
  background:rgba(255,255,255,.8); border:1px solid var(--line); border-radius:999px;
  padding:8px 12px; box-shadow:0 8px 24px rgba(26,73,145,.05);
}
.dashboard-chip {
  display:inline-flex; align-items:center; gap:6px; padding:5px 10px; border-radius:999px;
  background:linear-gradient(110deg,#EAF3FF,#EEF0FF); color:#245DE8; font-size:10px; font-weight:850;
  box-shadow:inset 0 0 0 1px rgba(47,107,255,.08);
}
.trend-chips { display:flex; flex-wrap:wrap; gap:7px; margin:4px 0 15px; }
.trend-chip {
  padding:6px 10px; border-radius:999px; font-size:10px; color:#5E6D89;
  background:rgba(255,255,255,.76); border:1px solid rgba(116,145,190,.14);
  box-shadow:0 6px 18px rgba(26,73,145,.04); transition:all .18s ease;
}
.trend-chip:hover { color:#2F6BFF; transform:translateY(-2px); box-shadow:0 10px 24px rgba(47,107,255,.10); }

.home-kpi {
  position:relative; overflow:hidden; min-height:132px; padding:18px 19px;
  border-radius:22px; border:1px solid rgba(255,255,255,.7);
  box-shadow:0 14px 38px rgba(33,76,145,.08);
  transition:transform .2s ease,box-shadow .2s ease;
}
.home-kpi:hover { transform:translateY(-4px) scale(1.01); box-shadow:0 22px 52px rgba(33,76,145,.14); }
.home-kpi:after {
  content:""; position:absolute; inset:-50% auto -50% -34%; width:30%;
  background:linear-gradient(90deg,transparent,rgba(255,255,255,.62),transparent);
  animation:shimmer 5.8s ease-in-out infinite;
}
.home-kpi.blue { background:linear-gradient(135deg,#FFFFFF 0%,#EEF4FF 58%,#E8F0FF 100%); }
.home-kpi.green { background:linear-gradient(135deg,#FFFFFF 0%,#ECFFF8 58%,#E5FFF5 100%); }
.home-kpi.purple { background:linear-gradient(135deg,#FFFFFF 0%,#F3EFFF 58%,#ECE9FF 100%); }
.home-kpi.orange { background:linear-gradient(135deg,#FFFFFF 0%,#FFF4E6 58%,#FFF0D7 100%); }
.kpi-top { display:flex; justify-content:space-between; align-items:center; gap:10px; }
.kpi-icon {
  width:34px; height:34px; border-radius:12px; display:flex; align-items:center; justify-content:center;
  font-size:17px; background:rgba(255,255,255,.76); box-shadow:0 7px 18px rgba(33,76,145,.08);
}
.kpi-badge { font-size:9px; font-weight:850; padding:5px 8px; border-radius:999px; background:rgba(255,255,255,.72); }
.kpi-title { margin-top:10px; font-size:11px; font-weight:750; color:#697995; }
.kpi-value { margin-top:4px; font-size:25px; font-weight:880; letter-spacing:-.045em; color:#0B1739; font-variant-numeric:tabular-nums; }
.kpi-note { margin-top:6px; font-size:10px; color:#7A8AA6; }
.kpi-glow {
  position:absolute; width:90px; height:90px; border-radius:50%; right:-20px; bottom:-28px;
  filter:blur(12px); opacity:.35;
}
.blue .kpi-glow { background:#4C7DFF; } .green .kpi-glow { background:#22D695; }
.purple .kpi-glow { background:#8B6CFF; } .orange .kpi-glow { background:#FFA43B; }

.dashboard-section { display:flex; justify-content:space-between; align-items:center; margin:3px 0 10px; }
.dashboard-section-title { font-size:18px; font-weight:860; letter-spacing:-.035em; color:#0B1739; }
.dashboard-kicker { font-size:10px; color:#92A0B8; }

.dark-chart-card {
  position:relative; overflow:hidden;
  background:
    radial-gradient(circle at 75% 10%,rgba(35,149,255,.24),transparent 27%),
    linear-gradient(155deg,#071A3C 0%,#0A2852 58%,#073968 100%);
  border:1px solid rgba(76,179,255,.36); border-radius:22px; padding:17px 18px 15px;
  box-shadow:0 18px 52px rgba(4,35,84,.24),inset 0 1px rgba(255,255,255,.08);
  color:#EAF5FF;
}
.dark-chart-card:before {
  content:""; position:absolute; left:0; right:0; top:0; height:2px;
  background:linear-gradient(90deg,transparent,#26C8FF,#7C5CFC,transparent);
  background-size:200% 100%; animation:gradientFlow 4s linear infinite;
}
.dark-chart-head { display:flex; justify-content:space-between; gap:12px; align-items:flex-start; margin-bottom:6px; }
.dark-chart-symbol { font-size:22px; font-weight:860; color:#FFF; }
.dark-chart-meta { font-size:10px; color:#91B6DA; margin-top:3px; }
.live-pill {
  display:inline-flex; align-items:center; gap:6px; font-size:9px; color:#9CEFD0;
  padding:5px 8px; border-radius:999px; border:1px solid rgba(63,231,165,.22);
  background:rgba(11,54,70,.52);
}
.live-dot { width:7px; height:7px; border-radius:50%; background:#23DB8F; animation:pulseDot 1.8s ease-in-out infinite; }
.chart-svg { width:100%; height:auto; display:block; margin-top:4px; }
.chart-grid { stroke:rgba(155,195,235,.13); stroke-width:1; }
.chart-line-a { fill:none; stroke:#25C8FF; stroke-width:3.1; filter:drop-shadow(0 0 6px rgba(37,200,255,.5)); }
.chart-line-b { fill:none; stroke:#8F6BFF; stroke-width:2.5; filter:drop-shadow(0 0 5px rgba(143,107,255,.45)); }
.chart-area { fill:url(#areaFill); opacity:.44; }
.chart-point-a { fill:#25C8FF; color:#25C8FF; animation:pointGlow 2s ease-in-out infinite; }
.chart-point-b { fill:#9B7EFF; color:#9B7EFF; animation:pointGlow 2.5s ease-in-out infinite; }
.chart-axis { fill:#7FA3C8; font-size:10px; }

.portfolio-card,.watch-card,.market-card,.activity-card {
  background:rgba(255,255,255,.9); border:1px solid var(--line); border-radius:22px;
  padding:17px 18px; box-shadow:0 14px 38px rgba(33,76,145,.07); backdrop-filter:blur(14px);
}
.portfolio-ring {
  width:150px; height:150px; border-radius:50%; margin:8px auto 14px; position:relative;
  box-shadow:0 12px 35px rgba(47,107,255,.14),0 0 28px rgba(21,198,255,.10);
  animation:floatUp 5s ease-in-out infinite;
}
.portfolio-ring:after {
  content:""; position:absolute; inset:26px; border-radius:50%;
  background:rgba(255,255,255,.96); box-shadow:inset 0 0 0 1px rgba(116,145,190,.10);
}
.ring-center {
  position:absolute; inset:0; display:flex; align-items:center; justify-content:center; text-align:center;
  z-index:2; flex-direction:column; pointer-events:none;
}
.ring-center small { font-size:9px; color:#8391AA; }
.ring-center strong { font-size:14px; color:#0B1739; margin-top:3px; }
.watch-row,.activity-row {
  display:grid; align-items:center; gap:8px; padding:9px 0; border-bottom:1px solid rgba(116,145,190,.10);
  font-size:11px;
}
.watch-row { grid-template-columns:1.35fr .75fr .65fr; }
.activity-row { grid-template-columns:1fr .9fr .75fr; }
.watch-row:last-child,.activity-row:last-child { border-bottom:0; }
.watch-name { font-weight:800; color:#132248; }
.watch-sub { color:#92A0B8; font-size:9px; margin-top:2px; }
.watch-price { text-align:right; font-weight:780; color:#17264A; font-variant-numeric:tabular-nums; }
.watch-tag { text-align:right; color:#2F6BFF; font-size:9px; font-weight:800; }
.market-mini {
  min-height:104px; border-radius:17px; padding:13px 14px; position:relative; overflow:hidden;
  background:linear-gradient(145deg,#FFFFFF,#F6F9FF); border:1px solid rgba(116,145,190,.12);
}
.market-mini:after {
  content:""; position:absolute; width:72px; height:72px; border-radius:50%; right:-26px; bottom:-32px;
  background:radial-gradient(circle,#7D9FFF,transparent 66%); opacity:.20;
}
.market-mini-title { font-size:10px; font-weight:820; color:#273659; }
.market-mini-value { margin-top:8px; font-size:16px; font-weight:860; color:#0B1739; }
.market-mini-cap { margin-top:8px; font-size:8px; color:#91A0B9; }

.ticker-shell {
  margin-top:13px; border-radius:15px; overflow:hidden;
  background:linear-gradient(90deg,#061735,#0A2A55,#071A3C);
  border:1px solid rgba(65,153,255,.25); box-shadow:0 12px 32px rgba(4,35,84,.18);
}
.ticker-track {
  display:flex; width:max-content; min-width:200%; gap:38px; padding:10px 0;
  color:#C7DFFF; font-size:10px; font-weight:740; white-space:nowrap;
  animation:tickerMove 28s linear infinite;
}
.ticker-track span { display:inline-flex; align-items:center; gap:7px; }
.ticker-track b { color:#60E5B1; }
.ticker-live { width:7px; height:7px; border-radius:50%; background:#22D695; animation:pulseDot 1.8s ease-in-out infinite; }
.market-grid { display:grid; grid-template-columns:repeat(4,minmax(0,1fr)); gap:9px; }
.sidebar-promo {
  position:relative; overflow:hidden; margin:18px 0 8px; padding:16px 15px;
  border-radius:19px; color:#EAF5FF;
  background:radial-gradient(circle at 85% 15%,rgba(65,198,255,.32),transparent 28%),linear-gradient(145deg,#0B2A61,#1154A8 58%,#176FD4);
  border:1px solid rgba(80,180,255,.28); box-shadow:0 16px 38px rgba(8,51,120,.20);
}
.sidebar-promo:after {
  content:""; position:absolute; width:100px; height:100px; border-radius:50%; right:-38px; bottom:-48px;
  background:radial-gradient(circle,rgba(74,220,255,.7),transparent 68%); opacity:.45;
  animation:floatUp 5s ease-in-out infinite;
}
.sidebar-promo-badge { font-size:9px; color:#A9DFFF; letter-spacing:.08em; font-weight:850; }
.sidebar-promo-title { margin-top:7px; font-size:16px; line-height:1.35; font-weight:850; letter-spacing:-.03em; }
.sidebar-promo-note { margin-top:6px; font-size:9px; color:#B9D1F0; line-height:1.55; }
.sidebar-promo-cta {
  display:inline-flex; margin-top:11px; padding:7px 10px; border-radius:10px;
  background:rgba(255,255,255,.12); border:1px solid rgba(255,255,255,.16); color:#FFFFFF;
  font-size:9px; font-weight:800;
}

hr { border-color:rgba(116,145,190,.13)!important; }
@media (max-width:900px) {
  .block-container { padding-left:1rem; padding-right:1rem; }
  .planx-hero { padding:21px 19px; }
  .planx-hero h1,.dashboard-title h1 { font-size:28px; }
  .dashboard-title { align-items:flex-start; flex-direction:column; }
  .portfolio-ring { width:128px; height:128px; }
  .portfolio-ring:after { inset:23px; }
  .market-grid { grid-template-columns:repeat(2,minmax(0,1fr)); }
}
@media (max-width:560px) {
  .market-grid { grid-template-columns:1fr; }
}

/* MARKET PULSE — dark dashboard visual system */
:root {
  --bg:#06111f; --surface:#0b1b2d; --surface-2:#10243a; --line:#1d3855;
  --text:#eef7ff; --muted:#89a2be; --accent:#22d3ee; --green:#22c55e; --red:#f43f5e;
}
html,body,[data-testid="stAppViewContainer"] {
  background:radial-gradient(circle at 72% -12%,rgba(26,89,150,.24),transparent 34%),#06111f!important;
  color:var(--text)!important;
}
[data-testid="stHeader"] { background:rgba(6,17,31,.76)!important; }
[data-testid="stSidebar"] {
  background:linear-gradient(180deg,#092039 0%,#071525 100%)!important;
  border-right:1px solid var(--line)!important;
}
[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
[data-testid="stSidebar"] label { color:#a9bed4!important; }
[data-testid="stSidebar"] [role="radiogroup"] label {
  padding:.7rem .8rem!important; border-radius:9px!important; transition:.18s ease!important;
}
[data-testid="stSidebar"] [role="radiogroup"] label:has(input:checked) {
  color:#fff!important; background:linear-gradient(90deg,#1151a2,#176bd2)!important;
  box-shadow:0 9px 24px rgba(19,97,204,.28)!important;
}
.block-container { max-width:1680px!important; padding-top:1.45rem!important; }
h1,h2,h3,h4,.dashboard-title h1,.dashboard-section-title { color:var(--text)!important; }
p,[data-testid="stCaptionContainer"],.dashboard-title p,.dashboard-clock,.dashboard-kicker { color:var(--muted)!important; }
.planx-brand-title { color:#eaf8ff!important; }
.planx-brand-sub { color:#6e91b4!important; }
.planx-brand-mark {
  background:linear-gradient(145deg,#17d3e6,#1e71ff)!important;
  box-shadow:0 0 28px rgba(34,211,238,.28)!important;
}
.dashboard-chip,.trend-chip {
  color:#9edfff!important; background:rgba(18,54,84,.72)!important;
  border:1px solid rgba(55,125,179,.28)!important; box-shadow:none!important;
}
.dashboard-clock { background:#0b1b2d!important; border-color:var(--line)!important; box-shadow:none!important; }
.stTextInput input,.stTextArea textarea,.stSelectbox div[data-baseweb="select"]>div {
  background:#0b1b2d!important; color:#eaf5ff!important; border-color:#28496a!important;
}
.stTextInput input::placeholder { color:#718ba8!important; }
.home-kpi {
  background:linear-gradient(145deg,#0d2034,#0a192a)!important;
  border:1px solid var(--line)!important; box-shadow:0 14px 36px rgba(0,0,0,.24)!important;
}
.home-kpi:after { opacity:.08!important; }
.kpi-icon,.kpi-badge { background:#112942!important; color:#a9dfff!important; box-shadow:none!important; }
.kpi-title,.kpi-note { color:var(--muted)!important; }
.kpi-value { color:#f2f8ff!important; }
.green .kpi-value { color:var(--green)!important; }
.home-kpi:hover { box-shadow:0 18px 44px rgba(0,0,0,.34),0 0 22px rgba(34,211,238,.08)!important; }
.dark-chart-card {
  background:radial-gradient(circle at 75% 10%,rgba(26,121,201,.18),transparent 30%),linear-gradient(155deg,#07182a,#0b2138)!important;
  border-color:#1d4262!important; box-shadow:0 18px 46px rgba(0,0,0,.28)!important;
}
.portfolio-card,.watch-card,.market-card,.activity-card,[data-testid="stVerticalBlockBorderWrapper"] {
  background:linear-gradient(145deg,rgba(14,31,50,.98),rgba(10,24,40,.98))!important;
  border-color:var(--line)!important; box-shadow:0 14px 36px rgba(0,0,0,.22)!important;
}
.watch-row,.activity-row { border-bottom-color:rgba(78,120,157,.18)!important; }
.watch-name,.watch-price,.ring-center strong { color:#eaf4ff!important; }
.watch-sub,.ring-center small { color:var(--muted)!important; }
.watch-tag { color:var(--accent)!important; }
.portfolio-ring:after { background:#0d2034!important; box-shadow:inset 0 0 0 1px var(--line)!important; }
.market-mini {
  background:linear-gradient(145deg,#10243a,#0b1c2e)!important; border-color:var(--line)!important;
}
.market-mini-title,.market-mini-value { color:#eaf4ff!important; }
.market-mini-cap { color:var(--muted)!important; }
[data-testid="stMetric"] {
  background:#0c1c2e!important; border-color:var(--line)!important; box-shadow:0 12px 30px rgba(0,0,0,.2)!important;
}
[data-testid="stMetricLabel"] { color:var(--muted)!important; }
[data-testid="stMetricValue"] { color:var(--text)!important; }
.stDataFrame { border-color:var(--line)!important; }
[data-testid="stDataFrame"] { filter:saturate(.92) brightness(.86); }
.planx-hero,.planx-card {
  background:linear-gradient(145deg,#0e2034,#0a192a)!important; border-color:var(--line)!important;
  box-shadow:0 16px 38px rgba(0,0,0,.22)!important;
}
.planx-hero h1,.planx-card-value { color:var(--text)!important; }
.planx-hero p,.planx-card-title,.planx-card-note { color:var(--muted)!important; }
.planx-eyebrow { color:var(--accent)!important; }
.planx-empty { background:#0c1c2e!important; border-color:#294866!important; color:var(--muted)!important; }
.planx-empty strong { color:#dbeafe!important; }
.sidebar-promo {
  background:radial-gradient(circle at 85% 15%,rgba(34,211,238,.25),transparent 30%),linear-gradient(145deg,#092646,#0c4381)!important;
}
.stButton>button,.stFormSubmitButton>button { border-color:#285175!important; color:#dff4ff!important; background:#102943!important; }
.stButton>button[kind="primary"],.stFormSubmitButton>button[kind="primary"] {
  background:linear-gradient(115deg,#1168c9,#12a9c4)!important; color:#fff!important;
}
hr { border-color:rgba(78,120,157,.2)!important; }

</style>
""",
        unsafe_allow_html=True,
    )


def brand():
    st.markdown(
        """
<div class="planx-brand">
  <div class="planx-brand-mark">↗</div>
  <div>
    <div class="planx-brand-title">MARKET PULSE</div>
    <div class="planx-brand-sub">STOCKDASH · DATA TO INSIGHT</div>
  </div>
</div>
""",
        unsafe_allow_html=True,
    )


def hero(title: str, subtitle: str, eyebrow: str = "PLANX INVESTMENT OS"):
    st.markdown(
        f"""
<div class="planx-hero">
  <div class="planx-eyebrow">{html.escape(eyebrow)}</div>
  <h1>{html.escape(title)}</h1>
  <p>{html.escape(subtitle)}</p>
</div>
""",
        unsafe_allow_html=True,
    )


def card(title: str, value: str, note: str = "", status: str = ""):
    status_html = f'<div class="planx-card-note">{html.escape(status)}</div>' if status else ""
    st.markdown(
        f"""
<div class="planx-card">
  <div class="planx-card-title">{html.escape(title)}</div>
  <div class="planx-card-value">{html.escape(value)}</div>
  <div class="planx-card-note">{html.escape(note)}</div>
  {status_html}
</div>
""",
        unsafe_allow_html=True,
    )


def empty_state(title: str, message: str):
    st.markdown(
        f"""
<div class="planx-empty">
  <strong style="color:#334155">{html.escape(title)}</strong><br>
  <span>{html.escape(message)}</span>
</div>
""",
        unsafe_allow_html=True,
    )


def source_badge(label: str, state: str = "wait"):
    cls = {"ok": "planx-status-ok", "bad": "planx-status-bad"}.get(state, "planx-status-wait")
    st.markdown(
        f'<span class="planx-source {cls}">{html.escape(label)}</span>',
        unsafe_allow_html=True,
    )
