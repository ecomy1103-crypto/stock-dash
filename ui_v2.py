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
  --bg:#F5F8FD;
  --surface:#FFFFFF;
  --surface-soft:#F8FBFF;
  --line:#E6ECF5;
  --text:#0F172A;
  --muted:#64748B;
  --blue:#2F6BFF;
  --blue-soft:#EAF2FF;
  --green:#0EA56A;
  --red:#F04452;
  --orange:#F59E0B;
  --purple:#7C5CFC;
}
html, body, [class*="css"] {
  font-family: Pretendard, "Noto Sans KR", "Apple SD Gothic Neo", sans-serif;
}
.stApp {
  background:
    radial-gradient(circle at 80% 0%, rgba(77,131,255,.08), transparent 30%),
    var(--bg);
  color:var(--text);
}
.block-container {
  max-width:1540px;
  padding-top:1.25rem;
  padding-bottom:4rem;
}
header[data-testid="stHeader"] {
  background:rgba(245,248,253,.88);
  backdrop-filter:blur(14px);
}
section[data-testid="stSidebar"] {
  background:#FFFFFF;
  border-right:1px solid var(--line);
}
section[data-testid="stSidebar"] > div {
  padding-top:.9rem;
}
[data-testid="stSidebar"] .stRadio > label { display:none; }
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] { gap:.28rem; }
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label {
  border-radius:12px;
  padding:.58rem .7rem;
  transition:all .16s ease;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:hover {
  background:#F5F8FD;
}
[data-testid="stSidebar"] .stRadio div[role="radiogroup"] label:has(input:checked) {
  background:var(--blue-soft);
  color:#1D4ED8;
  font-weight:800;
}
h1,h2,h3,h4 {
  color:var(--text);
  letter-spacing:-.035em;
}
h1 { font-weight:850; }
h2,h3 { font-weight:780; }
p,li { line-height:1.62; }
[data-testid="stCaptionContainer"] { color:var(--muted); }
[data-testid="stMetric"] {
  background:var(--surface);
  border:1px solid var(--line);
  border-radius:18px;
  padding:16px 18px;
  box-shadow:0 10px 30px rgba(15,23,42,.04);
}
[data-testid="stMetricLabel"] { color:var(--muted); font-weight:650; }
[data-testid="stMetricValue"] { color:var(--text); font-weight:820; }
[data-testid="stVerticalBlockBorderWrapper"] {
  border-color:var(--line)!important;
  border-radius:18px!important;
  background:var(--surface);
  box-shadow:0 10px 30px rgba(15,23,42,.035);
}
.stButton > button,.stFormSubmitButton > button {
  border-radius:11px;
  min-height:2.7rem;
  font-weight:750;
}
.stButton > button[kind="primary"],.stFormSubmitButton > button[kind="primary"] {
  background:linear-gradient(135deg,#2563EB,#4F7FFF);
  border-color:#2563EB;
}
.stTextInput input,.stTextArea textarea,.stSelectbox div[data-baseweb="select"] > div {
  border-radius:12px!important;
  background:#FFFFFF;
}
.stTabs [data-baseweb="tab-list"] { gap:8px; }
.stTabs [data-baseweb="tab"] { border-radius:10px; padding:8px 12px; }
.stDataFrame {
  border:1px solid var(--line);
  border-radius:14px;
  overflow:hidden;
}
.planx-brand {
  display:flex; align-items:center; gap:11px; margin:4px 0 20px 0;
}
.planx-brand-mark {
  width:38px; height:38px; border-radius:12px;
  display:flex; align-items:center; justify-content:center;
  background:linear-gradient(145deg,#2563EB,#60A5FA);
  color:white; font-size:20px; font-weight:900;
  box-shadow:0 8px 20px rgba(37,99,235,.20);
}
.planx-brand-title {
  font-size:19px; line-height:1.1; font-weight:850; letter-spacing:-.03em;
}
.planx-brand-sub {
  font-size:10px; color:#94A3B8; margin-top:3px; letter-spacing:.03em;
}
.planx-hero {
  background:linear-gradient(135deg,#FFFFFF 0%,#F9FBFF 55%,#EEF4FF 100%);
  border:1px solid #E2E8F0;
  border-radius:22px;
  padding:25px 28px;
  margin-bottom:17px;
  box-shadow:0 14px 38px rgba(15,23,42,.045);
}
.planx-eyebrow {
  color:#2563EB; font-size:11px; font-weight:850; letter-spacing:.09em;
  text-transform:uppercase; margin-bottom:7px;
}
.planx-hero h1 { margin:0; font-size:32px; line-height:1.18; }
.planx-hero p { margin:8px 0 0; color:#64748B; font-size:14px; }
.planx-card {
  background:#FFFFFF;
  border:1px solid var(--line);
  border-radius:18px;
  padding:17px 18px;
  min-height:118px;
  box-shadow:0 10px 30px rgba(15,23,42,.035);
}
.planx-card-title {
  font-size:12px; color:#64748B; margin-bottom:8px; font-weight:750;
}
.planx-card-value {
  font-size:23px; color:#0F172A; font-weight:850; letter-spacing:-.035em;
  font-variant-numeric:tabular-nums;
}
.planx-card-note { margin-top:7px; font-size:11px; color:#94A3B8; }
.planx-empty {
  background:#FBFDFF;
  border:1px dashed #CBD5E1;
  border-radius:16px;
  padding:22px;
  color:#64748B;
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
  gap:18px; margin:2px 0 18px;
}
.dashboard-title h1 { margin:0; font-size:34px; }
.dashboard-title p { margin:6px 0 0; color:#64748B; font-size:14px; }
.dashboard-clock {
  color:#64748B; font-size:12px; white-space:nowrap;
  background:#FFFFFF; border:1px solid var(--line); border-radius:999px;
  padding:8px 12px;
}
.dashboard-section {
  display:flex; justify-content:space-between; align-items:center;
  margin:6px 0 10px;
}
.dashboard-section-title {
  font-size:17px; font-weight:850; letter-spacing:-.03em; color:#0F172A;
}
.dashboard-kicker { font-size:11px; color:#94A3B8; }
.dashboard-panel {
  background:#FFFFFF; border:1px solid var(--line); border-radius:18px;
  padding:17px 18px; box-shadow:0 10px 30px rgba(15,23,42,.035);
}
.dashboard-chip {
  display:inline-flex; padding:5px 9px; border-radius:999px;
  background:#EFF6FF; color:#2563EB; font-size:10px; font-weight:800;
}
hr { border-color:var(--line)!important; }
@media (max-width:900px) {
  .block-container { padding-left:1rem; padding-right:1rem; }
  .planx-hero { padding:21px 19px; }
  .planx-hero h1,.dashboard-title h1 { font-size:28px; }
  .dashboard-title { align-items:flex-start; flex-direction:column; }
}
</style>
""",
        unsafe_allow_html=True,
    )


def brand():
    st.markdown(
        """
<div class="planx-brand">
  <div class="planx-brand-mark">▥</div>
  <div>
    <div class="planx-brand-title">StockDash</div>
    <div class="planx-brand-sub">INVESTMENT OS · DATA TO INSIGHT</div>
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
