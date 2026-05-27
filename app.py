import streamlit as st

st.set_page_config(
    page_title="송정우 | 한전KDN",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="expanded",
)

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300;400;500;600;700;800;900&display=swap');

:root {
    --bg-dark:   #060D1F;
    --bg-card:   rgba(15, 27, 51, 0.7);
    --navy-900:  #0A1428;
    --navy-800:  #0F1B33;
    --navy-700:  #1B2A4A;
    --navy-600:  #2A3A5C;
    --navy-500:  #4A5A7C;
    --navy-400:  #7A89AB;
    --navy-300:  #B8C0D6;
    --navy-200:  #DDE2EE;
    --navy-100:  #F0F2F8;
    --navy-50:   #F8F9FC;
    --accent:    #4F8EFF;
    --accent2:   #00D2FF;
    --accent3:   #7C3AED;
    --gold:      #F59E0B;
    --success:   #10B981;
    --danger:    #EF4444;
    --grad-main: linear-gradient(135deg, #4F8EFF 0%, #00D2FF 100%);
    --grad-card: linear-gradient(135deg, rgba(79,142,255,0.15) 0%, rgba(0,210,255,0.08) 100%);
    --shadow-sm: 0 1px 3px rgba(0,0,0,0.3);
    --shadow-md: 0 4px 16px rgba(0,0,0,0.25);
    --shadow-lg: 0 12px 40px rgba(0,0,0,0.35);
}

html, body, [class*="css"] {
    font-family: 'Noto Sans KR', -apple-system, sans-serif !important;
    word-break: keep-all;
}

/* ─── 전체 배경 ─── */
.stApp {
    background: var(--bg-dark) !important;
}
.main .block-container {
    background: transparent !important;
    padding: 2rem 1.5rem !important;
    max-width: 900px !important;
}

/* ─── 사이드바 ─── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #0A1428 0%, #06101E 100%) !important;
    border-right: 1px solid rgba(79,142,255,0.15) !important;
}
[data-testid="stSidebar"] > div:first-child {
    padding-top: 0 !important;
}

.sb-brand {
    background: linear-gradient(135deg, rgba(79,142,255,0.2) 0%, rgba(0,210,255,0.1) 100%);
    border-bottom: 1px solid rgba(79,142,255,0.2);
    padding: 28px 20px 24px;
    text-align: center;
    margin-bottom: 8px;
}
.sb-avatar-wrap {
    position: relative;
    width: 88px; height: 88px;
    margin: 0 auto 14px;
}
.sb-avatar {
    width: 88px; height: 88px;
    border-radius: 50%;
    background: linear-gradient(135deg, #1B2A4A, #0A1428);
    display: flex; align-items: center; justify-content: center;
    font-size: 2.4rem;
    border: 2.5px solid transparent;
    background-clip: padding-box;
    box-shadow: 0 0 0 2.5px #4F8EFF, 0 0 20px rgba(79,142,255,0.4);
}
.sb-status-dot {
    position: absolute;
    bottom: 4px; right: 4px;
    width: 14px; height: 14px;
    background: var(--success);
    border-radius: 50%;
    border: 2px solid #0A1428;
    box-shadow: 0 0 8px rgba(16,185,129,0.6);
}
.sb-name {
    font-size: 1.15rem; font-weight: 800;
    color: #fff !important;
    letter-spacing: -0.02em;
    margin-bottom: 4px;
}
.sb-role {
    font-size: 0.72rem;
    color: rgba(79,142,255,0.9) !important;
    font-weight: 600;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    margin-bottom: 12px;
}
.sb-badges {
    display: flex; gap: 6px; justify-content: center; flex-wrap: wrap;
}
.sb-badge {
    font-size: 0.65rem; font-weight: 700;
    padding: 2px 9px;
    border-radius: 999px;
    background: rgba(79,142,255,0.15);
    border: 1px solid rgba(79,142,255,0.4);
    color: #8BBFFF !important;
    letter-spacing: 0.05em;
}
.sb-badge.green {
    background: rgba(16,185,129,0.15);
    border-color: rgba(16,185,129,0.4);
    color: #6EE7B7 !important;
}

/* Streamlit radio 스타일 오버라이드 */
[data-testid="stSidebar"] [data-testid="stRadio"] label {
    color: #B8C0D6 !important;
    font-size: 0.9rem !important;
    font-weight: 500 !important;
}
[data-testid="stSidebar"] [data-testid="stRadio"] label:hover {
    color: #fff !important;
}

/* ─── 페이지 헤더 ─── */
.page-header {
    display: flex; align-items: center; gap: 12px;
    margin-bottom: 28px;
    padding-bottom: 20px;
    border-bottom: 1px solid rgba(79,142,255,0.2);
}
.page-header-icon {
    width: 44px; height: 44px;
    background: var(--grad-main);
    border-radius: 12px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.3rem;
    box-shadow: 0 4px 12px rgba(79,142,255,0.4);
    flex-shrink: 0;
}
.page-header-title {
    font-size: 1.6rem; font-weight: 800;
    color: #fff;
    letter-spacing: -0.03em;
}
.page-header-sub {
    font-size: 0.78rem;
    color: var(--navy-400);
    margin-top: 2px;
}

/* ─── 히어로 카드 ─── */
.hero-card {
    background: linear-gradient(135deg, #0F1B33 0%, #0A1020 60%, #060D1F 100%);
    border: 1px solid rgba(79,142,255,0.2);
    border-radius: 24px;
    padding: 48px 36px 40px;
    text-align: center;
    position: relative;
    overflow: hidden;
    margin-bottom: 24px;
    box-shadow: var(--shadow-lg);
}
.hero-card::before {
    content: '';
    position: absolute;
    top: -60px; left: 50%;
    transform: translateX(-50%);
    width: 300px; height: 300px;
    background: radial-gradient(circle, rgba(79,142,255,0.12) 0%, transparent 70%);
    pointer-events: none;
}
.hero-card::after {
    content: '';
    position: absolute;
    bottom: -40px; right: -40px;
    width: 200px; height: 200px;
    background: radial-gradient(circle, rgba(0,210,255,0.08) 0%, transparent 70%);
    pointer-events: none;
}
.hero-avatar {
    width: 100px; height: 100px;
    border-radius: 50%;
    background: linear-gradient(135deg, #1B2A4A, #0A1428);
    display: flex; align-items: center; justify-content: center;
    font-size: 3rem;
    margin: 0 auto 20px;
    box-shadow: 0 0 0 3px rgba(79,142,255,0.5), 0 0 30px rgba(79,142,255,0.3);
    position: relative; z-index: 1;
}
.hero-name {
    font-size: 2.4rem; font-weight: 900;
    color: #fff;
    letter-spacing: -0.04em;
    margin-bottom: 8px;
    position: relative; z-index: 1;
}
.hero-name span {
    background: var(--grad-main);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}
.hero-title-row {
    display: flex; align-items: center; justify-content: center; gap: 10px;
    margin-bottom: 24px;
    position: relative; z-index: 1;
}
.hero-badge {
    display: inline-flex; align-items: center; gap: 5px;
    padding: 5px 14px;
    border-radius: 999px;
    font-size: 0.78rem; font-weight: 700;
    letter-spacing: 0.06em;
}
.hero-badge.blue {
    background: rgba(79,142,255,0.2);
    border: 1px solid rgba(79,142,255,0.5);
    color: #8BBFFF;
}
.hero-badge.cyan {
    background: rgba(0,210,255,0.15);
    border: 1px solid rgba(0,210,255,0.4);
    color: #67E8F9;
}
.hero-divider {
    border: none;
    border-top: 1px solid rgba(255,255,255,0.08);
    margin: 24px 0;
    position: relative; z-index: 1;
}
.hero-tagline {
    font-size: 0.92rem;
    color: rgba(255,255,255,0.55);
    line-height: 1.8;
    position: relative; z-index: 1;
}

/* ─── 스탯 카드 ─── */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    margin-bottom: 20px;
}
.stat-card {
    background: var(--bg-card);
    border: 1px solid rgba(79,142,255,0.15);
    border-radius: 16px;
    padding: 20px 16px;
    text-align: center;
    backdrop-filter: blur(10px);
    transition: border-color 0.2s, box-shadow 0.2s;
}
.stat-card:hover {
    border-color: rgba(79,142,255,0.4);
    box-shadow: 0 4px 20px rgba(79,142,255,0.15);
}
.stat-number {
    font-size: 2rem; font-weight: 900;
    background: var(--grad-main);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    line-height: 1;
    margin-bottom: 4px;
}
.stat-label {
    font-size: 0.72rem; color: var(--navy-400);
    font-weight: 600;
    letter-spacing: 0.05em;
}

/* ─── 정보 카드 그리드 ─── */
.info-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 24px;
}
.info-item {
    background: var(--bg-card);
    border: 1px solid rgba(79,142,255,0.12);
    border-radius: 14px;
    padding: 16px 18px;
    display: flex; align-items: center; gap: 14px;
    backdrop-filter: blur(10px);
    transition: border-color 0.2s;
}
.info-item:hover { border-color: rgba(79,142,255,0.3); }
.info-icon-wrap {
    width: 40px; height: 40px;
    background: var(--grad-card);
    border-radius: 10px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.2rem;
    flex-shrink: 0;
    border: 1px solid rgba(79,142,255,0.2);
}
.info-label { font-size: 0.63rem; color: var(--navy-400); font-weight: 700; letter-spacing: 0.08em; text-transform: uppercase; }
.info-value { font-size: 0.88rem; font-weight: 600; color: #E0E6F0; margin-top: 2px; }

/* ─── 기술 스택 태그 ─── */
.tag-section-title {
    font-size: 0.68rem; font-weight: 700; color: var(--navy-400);
    letter-spacing: 0.1em; text-transform: uppercase;
    display: flex; align-items: center; gap: 8px;
    margin-bottom: 12px; margin-top: 20px;
}
.tag-section-title::after {
    content: ''; flex: 1;
    height: 1px; background: rgba(79,142,255,0.15);
}
.tags-wrap { display: flex; flex-wrap: wrap; gap: 8px; }
.tag {
    display: inline-flex; align-items: center; gap: 5px;
    padding: 5px 13px;
    border-radius: 999px;
    font-size: 0.78rem; font-weight: 600;
    border: 1px solid transparent;
    transition: transform 0.15s, box-shadow 0.15s;
}
.tag:hover { transform: translateY(-1px); }
.tag-lang  { background: rgba(79,70,229,0.15); color: #A5B4FC; border-color: rgba(79,70,229,0.3); }
.tag-db    { background: rgba(16,185,129,0.12); color: #6EE7B7; border-color: rgba(16,185,129,0.25); }
.tag-gis   { background: rgba(245,158,11,0.12); color: #FCD34D; border-color: rgba(245,158,11,0.25); }
.tag-infra { background: rgba(6,182,212,0.12); color: #67E8F9; border-color: rgba(6,182,212,0.25); }
.tag-new   { background: rgba(168,85,247,0.12); color: #D8B4FE; border-color: rgba(168,85,247,0.25); }

/* ─── 자기소개 카드 ─── */
.intro-card {
    background: var(--bg-card);
    border: 1px solid rgba(79,142,255,0.12);
    border-radius: 16px;
    padding: 22px 24px;
    margin-top: 8px;
    backdrop-filter: blur(10px);
    color: rgba(255,255,255,0.75);
    font-size: 0.9rem;
    line-height: 1.9;
}
.intro-card strong { color: #fff; }

/* ─── 경력 타임라인 ─── */
.timeline {
    position: relative;
    padding-left: 32px;
    margin-bottom: 24px;
}
.timeline::before {
    content: '';
    position: absolute;
    left: 10px; top: 8px; bottom: 8px;
    width: 2px;
    background: linear-gradient(180deg, #4F8EFF 0%, rgba(79,142,255,0.1) 100%);
}
.tl-item {
    position: relative;
    margin-bottom: 28px;
}
.tl-dot {
    position: absolute;
    left: -26px; top: 6px;
    width: 14px; height: 14px;
    border-radius: 50%;
    background: var(--accent);
    border: 2px solid var(--bg-dark);
    box-shadow: 0 0 10px rgba(79,142,255,0.5);
}
.tl-dot.current {
    background: var(--accent2);
    box-shadow: 0 0 14px rgba(0,210,255,0.6);
    animation: pulse-dot 2s infinite;
}
@keyframes pulse-dot {
    0%, 100% { box-shadow: 0 0 10px rgba(0,210,255,0.5); }
    50% { box-shadow: 0 0 20px rgba(0,210,255,0.8); }
}
.tl-card {
    background: var(--bg-card);
    border: 1px solid rgba(79,142,255,0.12);
    border-radius: 14px;
    padding: 18px 20px;
    backdrop-filter: blur(10px);
    transition: border-color 0.2s, box-shadow 0.2s;
}
.tl-card:hover {
    border-color: rgba(79,142,255,0.3);
    box-shadow: 0 4px 16px rgba(79,142,255,0.1);
}
.tl-top {
    display: flex; align-items: flex-start;
    justify-content: space-between; gap: 12px;
    margin-bottom: 6px;
}
.tl-title { font-size: 0.97rem; font-weight: 700; color: #E0E6F0; }
.tl-period {
    font-size: 0.7rem; font-weight: 700;
    padding: 3px 10px; border-radius: 999px;
    background: rgba(79,142,255,0.15);
    border: 1px solid rgba(79,142,255,0.3);
    color: #8BBFFF;
    white-space: nowrap; flex-shrink: 0;
}
.tl-period.current {
    background: rgba(0,210,255,0.15);
    border-color: rgba(0,210,255,0.3);
    color: #67E8F9;
}
.tl-org { font-size: 0.78rem; color: var(--navy-400); margin-bottom: 8px; }
.tl-desc { font-size: 0.83rem; color: rgba(255,255,255,0.55); line-height: 1.7; }
.tl-tags { display: flex; flex-wrap: wrap; gap: 6px; margin-top: 10px; }

/* ─── 스킬 카드 ─── */
.skill-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
    gap: 16px;
    margin-bottom: 24px;
}
.skill-cat-card {
    background: var(--bg-card);
    border: 1px solid rgba(79,142,255,0.12);
    border-radius: 16px;
    padding: 18px 18px;
    backdrop-filter: blur(10px);
    transition: border-color 0.2s, box-shadow 0.2s;
}
.skill-cat-card:hover {
    border-color: rgba(79,142,255,0.3);
    box-shadow: 0 4px 16px rgba(79,142,255,0.1);
}
.skill-cat-label {
    font-size: 0.65rem; font-weight: 700;
    color: var(--accent);
    letter-spacing: 0.1em; text-transform: uppercase;
    margin-bottom: 14px; padding-bottom: 10px;
    border-bottom: 1px solid rgba(79,142,255,0.15);
}
.skill-item {
    display: flex; flex-direction: column;
    gap: 6px; padding: 10px 0;
    border-bottom: 1px solid rgba(255,255,255,0.04);
}
.skill-item:last-child { border-bottom: none; padding-bottom: 0; }
.skill-item-top {
    display: flex; align-items: center; gap: 8px;
}
.skill-icon { font-size: 1rem; flex-shrink: 0; }
.skill-name { font-size: 0.84rem; font-weight: 600; color: #D0D8EE; flex: 1; }
.skill-level {
    font-size: 0.65rem; font-weight: 700; padding: 1px 7px;
    border-radius: 999px;
}
.lv-expert   { background: rgba(79,142,255,0.2); color: #8BBFFF; border: 1px solid rgba(79,142,255,0.3); }
.lv-advanced { background: rgba(16,185,129,0.15); color: #6EE7B7; border: 1px solid rgba(16,185,129,0.25); }
.lv-mid      { background: rgba(245,158,11,0.15); color: #FCD34D; border: 1px solid rgba(245,158,11,0.25); }
.lv-learning { background: rgba(168,85,247,0.15); color: #D8B4FE; border: 1px solid rgba(168,85,247,0.25); }
.skill-bar-bg {
    height: 4px; background: rgba(255,255,255,0.08);
    border-radius: 999px; overflow: hidden;
}
.skill-bar {
    height: 100%; border-radius: 999px;
    background: var(--grad-main);
    transition: width 0.5s ease;
}
.skill-hint { font-size: 0.68rem; color: var(--navy-500); }

/* ─── 레퍼런스 카드 ─── */
.ref-card {
    background: var(--bg-card);
    border: 1px solid rgba(79,142,255,0.12);
    border-radius: 16px;
    padding: 22px 24px;
    margin-bottom: 16px;
    backdrop-filter: blur(10px);
    transition: border-color 0.2s, box-shadow 0.2s;
}
.ref-card:hover {
    border-color: rgba(79,142,255,0.3);
    box-shadow: 0 6px 24px rgba(79,142,255,0.1);
}
.ref-card-top {
    display: flex; align-items: flex-start;
    justify-content: space-between; gap: 12px;
    margin-bottom: 4px;
}
.ref-number {
    width: 28px; height: 28px;
    background: var(--grad-main);
    border-radius: 8px;
    display: flex; align-items: center; justify-content: center;
    font-size: 0.72rem; font-weight: 800;
    color: #fff;
    flex-shrink: 0; margin-top: 2px;
}
.ref-title { font-size: 1rem; font-weight: 700; color: #E0E6F0; flex: 1; }
.ref-period {
    font-size: 0.7rem; font-weight: 700;
    padding: 3px 10px; border-radius: 999px;
    background: rgba(79,142,255,0.15);
    border: 1px solid rgba(79,142,255,0.3);
    color: #8BBFFF;
    white-space: nowrap; flex-shrink: 0;
}
.ref-role { font-size: 0.78rem; color: var(--accent2); margin: 6px 0 10px; font-weight: 500; }
.ref-desc { font-size: 0.84rem; color: rgba(255,255,255,0.55); line-height: 1.8; margin-bottom: 14px; }
.ref-tags { display: flex; flex-wrap: wrap; gap: 6px; }

/* ─── 일정 카드 ─── */
.event-card {
    background: var(--bg-card);
    border: 1px solid rgba(79,142,255,0.12);
    border-radius: 14px;
    padding: 16px 20px;
    margin-bottom: 10px;
    display: flex; align-items: center; gap: 16px;
    backdrop-filter: blur(10px);
    transition: border-color 0.2s, box-shadow 0.2s;
}
.event-card:hover {
    border-color: rgba(79,142,255,0.3);
    box-shadow: 0 4px 16px rgba(79,142,255,0.1);
}
.event-card.today {
    border-color: rgba(0,210,255,0.4);
    background: linear-gradient(135deg, rgba(0,210,255,0.08) 0%, rgba(79,142,255,0.05) 100%);
}
.event-date-box {
    min-width: 52px; text-align: center;
    background: rgba(79,142,255,0.12);
    border: 1px solid rgba(79,142,255,0.2);
    border-radius: 12px; padding: 8px;
    flex-shrink: 0;
}
.event-date-box.today-box {
    background: var(--grad-main);
    border-color: transparent;
    box-shadow: 0 4px 12px rgba(79,142,255,0.3);
}
.event-day   { font-size: 1.4rem; font-weight: 900; color: #fff; line-height: 1; }
.event-dow   { font-size: 0.62rem; color: rgba(255,255,255,0.6); font-weight: 600; }
.event-title { font-size: 0.92rem; font-weight: 700; color: #D0D8EE; }
.event-desc  { font-size: 0.76rem; color: var(--navy-400); margin-top: 3px; }
.event-badge {
    margin-left: auto;
    font-size: 0.65rem; font-weight: 700;
    padding: 2px 9px; border-radius: 999px;
    background: rgba(0,210,255,0.15);
    border: 1px solid rgba(0,210,255,0.3);
    color: #67E8F9;
    flex-shrink: 0;
}

/* ─── 게시판 ─── */
.board-header {
    display: flex; align-items: center; justify-content: space-between;
    margin-bottom: 14px;
}
.board-count {
    font-size: 0.82rem; color: var(--navy-400);
    font-weight: 600;
}
.board-table {
    width: 100%; border-collapse: collapse;
    font-size: 0.88rem;
    background: var(--bg-card);
    border: 1px solid rgba(79,142,255,0.12);
    border-radius: 16px;
    overflow: hidden;
    backdrop-filter: blur(10px);
}
.board-table th {
    background: rgba(79,142,255,0.08);
    color: var(--navy-400);
    font-weight: 700; font-size: 0.72rem;
    padding: 12px 16px;
    text-align: left;
    border-bottom: 1px solid rgba(79,142,255,0.15);
    letter-spacing: 0.05em; text-transform: uppercase;
}
.board-table td {
    padding: 13px 16px;
    border-bottom: 1px solid rgba(255,255,255,0.04);
    color: #B8C0D6;
}
.board-table tr:last-child td { border-bottom: none; }
.board-table tr:hover td { background: rgba(79,142,255,0.05); color: #E0E6F0; }
.post-title-cell { color: #D0D8EE !important; font-weight: 500 !important; }

/* ─── 연락하기 ─── */
.contact-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 14px;
    margin-bottom: 28px;
}
.contact-card {
    background: var(--bg-card);
    border: 1px solid rgba(79,142,255,0.12);
    border-radius: 16px;
    padding: 20px;
    text-align: center;
    backdrop-filter: blur(10px);
    transition: border-color 0.2s, box-shadow 0.2s, transform 0.15s;
    cursor: pointer;
}
.contact-card:hover {
    border-color: rgba(79,142,255,0.4);
    box-shadow: 0 6px 24px rgba(79,142,255,0.15);
    transform: translateY(-2px);
}
.contact-card-icon {
    width: 52px; height: 52px;
    border-radius: 14px;
    display: flex; align-items: center; justify-content: center;
    font-size: 1.5rem;
    margin: 0 auto 12px;
}
.contact-card-icon.blue  { background: rgba(79,142,255,0.2); border: 1px solid rgba(79,142,255,0.3); }
.contact-card-icon.cyan  { background: rgba(0,210,255,0.15); border: 1px solid rgba(0,210,255,0.3); }
.contact-card-icon.green { background: rgba(16,185,129,0.15); border: 1px solid rgba(16,185,129,0.25); }
.contact-card-icon.purple{ background: rgba(168,85,247,0.15); border: 1px solid rgba(168,85,247,0.25); }
.contact-card-label { font-size: 0.72rem; color: var(--navy-400); font-weight: 700; letter-spacing: 0.06em; text-transform: uppercase; margin-bottom: 4px; }
.contact-card-value { font-size: 0.88rem; font-weight: 600; color: #D0D8EE; }

.contact-form-card {
    background: var(--bg-card);
    border: 1px solid rgba(79,142,255,0.15);
    border-radius: 20px;
    padding: 28px 28px;
    backdrop-filter: blur(10px);
}
.contact-form-title {
    font-size: 1.05rem; font-weight: 700; color: #E0E6F0;
    margin-bottom: 4px;
}
.contact-form-sub {
    font-size: 0.8rem; color: var(--navy-400);
    margin-bottom: 20px;
}
.response-time-badge {
    display: inline-flex; align-items: center; gap: 6px;
    padding: 6px 14px; border-radius: 999px;
    background: rgba(16,185,129,0.12);
    border: 1px solid rgba(16,185,129,0.25);
    color: #6EE7B7;
    font-size: 0.72rem; font-weight: 700;
    margin-bottom: 20px;
}

/* ─── 공통 Streamlit 위젯 다크 오버라이드 ─── */
.stTextInput input, .stTextArea textarea, .stSelectbox select {
    background: rgba(255,255,255,0.05) !important;
    border: 1px solid rgba(79,142,255,0.25) !important;
    border-radius: 10px !important;
    color: #E0E6F0 !important;
    font-family: 'Noto Sans KR', sans-serif !important;
}
.stTextInput input:focus, .stTextArea textarea:focus {
    border-color: rgba(79,142,255,0.6) !important;
    box-shadow: 0 0 0 3px rgba(79,142,255,0.1) !important;
}
.stTextInput label, .stTextArea label {
    color: var(--navy-300) !important;
    font-size: 0.82rem !important;
    font-weight: 600 !important;
}
.stButton button {
    background: var(--grad-main) !important;
    border: none !important;
    border-radius: 10px !important;
    color: #fff !important;
    font-weight: 700 !important;
    font-family: 'Noto Sans KR', sans-serif !important;
    padding: 10px 24px !important;
    box-shadow: 0 4px 14px rgba(79,142,255,0.35) !important;
    transition: box-shadow 0.2s, transform 0.15s !important;
}
.stButton button:hover {
    box-shadow: 0 6px 20px rgba(79,142,255,0.5) !important;
    transform: translateY(-1px);
}
.stExpander {
    background: var(--bg-card) !important;
    border: 1px solid rgba(79,142,255,0.15) !important;
    border-radius: 14px !important;
}
.stExpander summary { color: #B8C0D6 !important; }
.stSuccess, .stWarning, .stInfo {
    background: rgba(16,185,129,0.08) !important;
    border: 1px solid rgba(16,185,129,0.2) !important;
    border-radius: 10px !important;
    color: #6EE7B7 !important;
}
.stWarning {
    background: rgba(245,158,11,0.08) !important;
    border-color: rgba(245,158,11,0.2) !important;
    color: #FCD34D !important;
}
.stRadio label { color: #B8C0D6 !important; }

/* ─── 푸터 ─── */
.footer-bar {
    text-align: center;
    font-size: 0.72rem;
    color: rgba(255,255,255,0.25);
    margin-top: 40px;
    padding-top: 20px;
    border-top: 1px solid rgba(79,142,255,0.1);
}
.footer-bar span { color: rgba(79,142,255,0.6); }

/* ─── Streamlit 기본 UI 숨기기 ─── */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
[data-testid="stStatusWidget"] { display: none !important; }
[data-testid="stDecoration"] { display: none !important; }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ── 사이드바 ──────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sb-brand">
        <div class="sb-avatar-wrap">
            <div class="sb-avatar">👨‍💼</div>
            <div class="sb-status-dot"></div>
        </div>
        <div class="sb-name">송정우</div>
        <div class="sb-role">한전KDN · 과장</div>
        <div class="sb-badges">
            <span class="sb-badge">⚡ 전력 IT</span>
            <span class="sb-badge green">● 재직 중</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "메뉴",
        [
            "🏠 소개",
            "📊 경력",
            "💡 보유스킬",
            "📁 레퍼런스",
            "📅 일정",
            "📋 게시판",
            "📬 연락하기",
        ],
        label_visibility="collapsed",
    )

    st.markdown("""
    <div style="margin-top:24px;padding:14px 16px;background:rgba(79,142,255,0.06);border:1px solid rgba(79,142,255,0.15);border-radius:12px;">
        <div style="font-size:0.65rem;font-weight:700;color:#4A5A7C;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:8px;">빠른 연락</div>
        <div style="font-size:0.78rem;color:#8BBFFF;margin-bottom:4px;">📧 songjw_77@kdn.com</div>
        <div style="font-size:0.78rem;color:#67E8F9;">🏢 한전KDN 본사</div>
    </div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# 소개 페이지
# ══════════════════════════════════════════════════════════════
if page == "🏠 소개":

    st.markdown("""
    <div class="hero-card">
        <div class="hero-avatar">👨‍💼</div>
        <div class="hero-name"><span>송 정 우</span></div>
        <div class="hero-title-row">
            <span class="hero-badge blue">⚡ 한전KDN</span>
            <span class="hero-badge cyan">과 장</span>
        </div>
        <hr class="hero-divider" />
        <div class="hero-tagline">
            전력 IT 시스템 개발 · GIS 공간정보 · 풀스택 바이브코딩
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="stats-grid">
        <div class="stat-card">
            <div class="stat-number">8+</div>
            <div class="stat-label">경력 (년)</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">4</div>
            <div class="stat-label">주요 프로젝트</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">11</div>
            <div class="stat-label">보유 기술</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="info-grid">
        <div class="info-item">
            <div class="info-icon-wrap">🏢</div>
            <div>
                <div class="info-label">소속</div>
                <div class="info-value">한전KDN</div>
            </div>
        </div>
        <div class="info-item">
            <div class="info-icon-wrap">💼</div>
            <div>
                <div class="info-label">직급</div>
                <div class="info-value">과장</div>
            </div>
        </div>
        <div class="info-item">
            <div class="info-icon-wrap">📧</div>
            <div>
                <div class="info-label">이메일</div>
                <div class="info-value">songjw_77@kdn.com</div>
            </div>
        </div>
        <div class="info-item">
            <div class="info-icon-wrap">🗺️</div>
            <div>
                <div class="info-label">전문분야</div>
                <div class="info-value">전력 IT · GIS</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="tag-section-title">🛠 기술 스택</div>
    <div class="tags-wrap">
        <span class="tag tag-lang">Java</span>
        <span class="tag tag-lang">JSP</span>
        <span class="tag tag-lang">CSS</span>
        <span class="tag tag-gis">ArcGIS</span>
        <span class="tag tag-db">Oracle</span>
        <span class="tag tag-db">MySQL</span>
        <span class="tag tag-db">MariaDB</span>
        <span class="tag tag-infra">Unix</span>
        <span class="tag tag-infra">JEUS</span>
        <span class="tag tag-new">Python</span>
        <span class="tag tag-new">Streamlit</span>
    </div>
    <div class="tag-section-title" style="margin-top:20px;">📝 자기소개</div>
    <div class="intro-card">
        안녕하세요! 한전KDN에서 <strong>전력 IT 시스템</strong> 개발 및 운영을 담당하고 있는 <strong>송정우 과장</strong>입니다.<br/><br/>
        전력설비 GIS 시스템, 고객 서비스 포털, 배전 운영 자동화 등 다양한 공공 IT 프로젝트에서
        <strong>Java 백엔드 개발</strong>과 <strong>ArcGIS 기반 공간 데이터 시각화</strong>를 중심으로 경력을 쌓아왔습니다.<br/><br/>
        현재는 Python / Streamlit을 활용한 풀스택 바이브코딩을 실습하며 AI 기반 업무 자동화에 관심을 갖고 있습니다.
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="footer-bar">⚡ <span>한전KDN</span> · 송정우 개인 포트폴리오</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# 경력 타임라인
# ══════════════════════════════════════════════════════════════
elif page == "📊 경력":

    st.markdown("""
    <div class="page-header">
        <div class="page-header-icon">📊</div>
        <div>
            <div class="page-header-title">경력 타임라인</div>
            <div class="page-header-sub">Career History · 8+ Years</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    career = [
        {
            "title":   "전력 IT 시스템 개발 · 운영",
            "org":     "한전KDN 디지털솔루션부 · 과장",
            "period":  "2022 – 현재",
            "current": True,
            "desc":    "전력설비 GIS 통합관리 시스템 신규 구축 및 운영. ArcGIS Server 기반 실시간 공간 데이터 시각화, Python 자동화 스크립트 도입으로 업무 효율 30% 개선.",
            "tags":    [("tag-gis","ArcGIS"), ("tag-lang","Java"), ("tag-new","Python"), ("tag-infra","JEUS")],
        },
        {
            "title":   "고객 서비스 포털 고도화",
            "org":     "한전KDN 서비스개발팀 · 대리",
            "period":  "2019 – 2022",
            "current": False,
            "desc":    "전기요금 조회·고장 신고·민원 접수 통합 웹 포털 개발. JSP/Java 풀스택 개발, REST API 설계, MySQL 쿼리 최적화로 응답속도 40% 향상.",
            "tags":    [("tag-lang","Java"), ("tag-lang","JSP"), ("tag-db","MySQL"), ("tag-lang","CSS")],
        },
        {
            "title":   "배전 운영 자동화 시스템 구축",
            "org":     "한전KDN 배전IT팀 · 주임",
            "period":  "2017 – 2019",
            "current": False,
            "desc":    "배전 설비 점검 이력 자동 수집 및 이상 감지 알림 시스템 개발. Unix 서버 환경에서 Java 배치 프로세스 구현, Oracle DB 연동.",
            "tags":    [("tag-lang","Java"), ("tag-db","Oracle"), ("tag-infra","Unix"), ("tag-infra","JEUS")],
        },
        {
            "title":   "사내 DB 통합 마이그레이션",
            "org":     "한전KDN IT인프라팀 · 주임",
            "period":  "2016 – 2017",
            "current": False,
            "desc":    "Oracle에서 MariaDB로의 대규모 DB 마이그레이션. 데이터 정합성 검증, 인덱스 전략 수립, 슬로우쿼리 개선으로 응답속도 40% 단축.",
            "tags":    [("tag-db","Oracle"), ("tag-db","MariaDB"), ("tag-infra","Unix")],
        },
        {
            "title":   "IT 개발 입문 · 공공시스템 적응",
            "org":     "한전KDN 신입 개발자",
            "period":  "2016",
            "current": False,
            "desc":    "Java 기반 공공 IT 시스템 개발 환경(JEUS, Oracle, Unix) 적응. 사내 표준 프레임워크 및 개발 방법론 습득.",
            "tags":    [("tag-lang","Java"), ("tag-db","Oracle"), ("tag-infra","JEUS")],
        },
    ]

    timeline_items = ""
    for c in career:
        tags_html = " ".join(f'<span class="tag {cls}" style="font-size:0.68rem;padding:3px 9px;">{name}</span>' for cls, name in c["tags"])
        dot_class = "tl-dot current" if c["current"] else "tl-dot"
        period_class = "tl-period current" if c["current"] else "tl-period"
        timeline_items += f"""
        <div class="tl-item">
            <div class="{dot_class}"></div>
            <div class="tl-card">
                <div class="tl-top">
                    <div class="tl-title">{c['title']}</div>
                    <span class="{period_class}">{c['period']}</span>
                </div>
                <div class="tl-org">{c['org']}</div>
                <div class="tl-desc">{c['desc']}</div>
                <div class="tl-tags">{tags_html}</div>
            </div>
        </div>
        """

    st.markdown(f'<div class="timeline">{timeline_items}</div>', unsafe_allow_html=True)
    st.markdown('<div class="footer-bar">⚡ <span>한전KDN</span> · 송정우 개인 포트폴리오</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# 보유스킬 페이지
# ══════════════════════════════════════════════════════════════
elif page == "💡 보유스킬":

    st.markdown("""
    <div class="page-header">
        <div class="page-header-icon">💡</div>
        <div>
            <div class="page-header-title">보유 스킬</div>
            <div class="page-header-sub">Tech Stack · 11 Skills</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    SKILLS = {
        "🖥️ 프로그래밍 언어": [
            ("☕", "Java",    "백엔드 · 엔터프라이즈",  90, "Expert",   "lv-expert"),
            ("🌐", "JSP",     "서버사이드 웹 개발",      80, "Advanced", "lv-advanced"),
            ("🎨", "CSS",     "UI 스타일링 · 반응형",    75, "Advanced", "lv-advanced"),
            ("🐍", "Python",  "데이터 분석 · 자동화",    60, "Mid",      "lv-mid"),
        ],
        "🗄️ 데이터베이스": [
            ("🗃️", "Oracle",  "엔터프라이즈 RDBMS",     85, "Expert",   "lv-expert"),
            ("🐬", "MySQL",   "오픈소스 RDBMS",          80, "Advanced", "lv-advanced"),
            ("🔷", "MariaDB", "MySQL 포크 · 오픈소스",   75, "Advanced", "lv-advanced"),
        ],
        "🗺️ GIS · 공간정보": [
            ("🗺️", "ArcGIS", "공간 데이터 · 지도 시각화", 85, "Expert", "lv-expert"),
        ],
        "⚙️ 인프라 · 미들웨어": [
            ("🖥️", "Unix",   "서버 운영 · 셸 스크립트",   80, "Advanced", "lv-advanced"),
            ("⚙️", "JEUS",   "국산 WAS · 공공 인프라",     75, "Advanced", "lv-advanced"),
        ],
        "✨ 학습 중": [
            ("🚀", "Streamlit", "Python 웹앱 · 데이터 대시보드", 55, "Learning", "lv-learning"),
            ("🤖", "AI/LLM",   "Claude API · 생성형 AI 활용",    45, "Learning", "lv-learning"),
        ],
    }

    cols = st.columns(2)
    col_idx = 0
    for cat, skills in SKILLS.items():
        items_html = ""
        for icon, name, hint, pct, lv, lv_cls in skills:
            items_html += f"""
            <div class="skill-item">
                <div class="skill-item-top">
                    <span class="skill-icon">{icon}</span>
                    <span class="skill-name">{name}</span>
                    <span class="skill-level {lv_cls}">{lv}</span>
                </div>
                <div class="skill-bar-bg">
                    <div class="skill-bar" style="width:{pct}%"></div>
                </div>
                <div class="skill-hint">{hint}</div>
            </div>
            """
        with cols[col_idx % 2]:
            st.markdown(
                f'<div class="skill-cat-card"><div class="skill-cat-label">{cat}</div>{items_html}</div>',
                unsafe_allow_html=True,
            )
        col_idx += 1

    st.markdown('<div class="footer-bar">⚡ <span>한전KDN</span> · 송정우 개인 포트폴리오</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# 레퍼런스 페이지
# ══════════════════════════════════════════════════════════════
elif page == "📁 레퍼런스":

    st.markdown("""
    <div class="page-header">
        <div class="page-header-icon">📁</div>
        <div>
            <div class="page-header-title">프로젝트 레퍼런스</div>
            <div class="page-header-sub">Project Portfolio · 4 Projects</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    projects = [
        {
            "title":  "전력설비 GIS 통합관리 시스템 구축",
            "period": "2022.03 – 2023.06",
            "role":   "백엔드 개발 · DB 설계 · GIS 연동",
            "desc":   "전국 배전·송전 설비의 위치 및 속성 정보를 통합 관리하는 GIS 기반 시스템. ArcGIS Server와 Oracle DB를 연동해 실시간 설비 현황 조회 및 공간 분석 기능을 구현했습니다.",
            "tags":   [("tag-lang","Java"), ("tag-gis","ArcGIS"), ("tag-db","Oracle"), ("tag-infra","JEUS")],
        },
        {
            "title":  "고객 서비스 포털 시스템 고도화",
            "period": "2021.01 – 2022.02",
            "role":   "풀스택 개발 · API 설계",
            "desc":   "전기요금 조회, 고장 신고, 민원 접수 등 고객 서비스를 통합 제공하는 웹 포털. JSP/CSS 기반 프론트엔드와 Java 백엔드를 연계하고 MySQL로 데이터를 관리했습니다.",
            "tags":   [("tag-lang","Java"), ("tag-lang","JSP"), ("tag-lang","CSS"), ("tag-db","MySQL")],
        },
        {
            "title":  "배전 운영 자동화 시스템",
            "period": "2019.06 – 2020.12",
            "role":   "백엔드 개발 · 배치 처리 설계",
            "desc":   "배전 설비 점검 이력 자동 수집 및 이상 감지 알림 시스템. Unix 서버 환경에서 Java 배치 프로세스를 운영하고 Oracle DB와 연동해 운영 효율을 향상시켰습니다.",
            "tags":   [("tag-lang","Java"), ("tag-db","Oracle"), ("tag-infra","Unix"), ("tag-infra","JEUS")],
        },
        {
            "title":  "사내 업무시스템 DB 통합 마이그레이션",
            "period": "2018.03 – 2019.05",
            "role":   "DB 설계 · 마이그레이션 · 쿼리 최적화",
            "desc":   "Oracle에서 MariaDB로의 대규모 DB 마이그레이션 프로젝트. 데이터 정합성 검증 스크립트 작성, 인덱스 전략 수립, 슬로우쿼리 개선을 통해 응답속도를 40% 단축했습니다.",
            "tags":   [("tag-db","Oracle"), ("tag-db","MariaDB"), ("tag-infra","Unix"), ("tag-lang","Java")],
        },
    ]

    for i, p in enumerate(projects):
        tag_html = " ".join(f'<span class="tag {cls}">{name}</span>' for cls, name in p["tags"])
        st.markdown(f"""
        <div class="ref-card">
            <div class="ref-card-top">
                <div class="ref-number">{i+1:02d}</div>
                <div class="ref-title">{p['title']}</div>
                <span class="ref-period">{p['period']}</span>
            </div>
            <div class="ref-role">▸ {p['role']}</div>
            <div class="ref-desc">{p['desc']}</div>
            <div class="ref-tags">{tag_html}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="footer-bar">⚡ <span>한전KDN</span> · 송정우 개인 포트폴리오</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# 일정 페이지
# ══════════════════════════════════════════════════════════════
elif page == "📅 일정":

    st.markdown("""
    <div class="page-header">
        <div class="page-header-icon">📅</div>
        <div>
            <div class="page-header-title">일정</div>
            <div class="page-header-sub">2026년 5월 주요 일정</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    events = [
        {"day": "5",  "dow": "월", "title": "어린이날",          "desc": "공휴일",                      "today": False, "badge": "공휴일"},
        {"day": "12", "dow": "월", "title": "팀 주간회의",        "desc": "오전 10:00 · 대회의실",        "today": False, "badge": None},
        {"day": "19", "dow": "화", "title": "프로젝트 중간 보고", "desc": "GIS 시스템 진행현황",           "today": False, "badge": "보고"},
        {"day": "27", "dow": "수", "title": "오늘",               "desc": "2026년 5월 27일",               "today": True,  "badge": "TODAY"},
        {"day": "28", "dow": "목", "title": "시스템 배포",         "desc": "운영 서버 반영 예정",           "today": False, "badge": "배포"},
        {"day": "30", "dow": "토", "title": "월말 결산 보고",      "desc": "5월 업무 실적 정리",            "today": False, "badge": None},
    ]

    for e in events:
        card_cls = "event-card today" if e["today"] else "event-card"
        box_cls  = "event-date-box today-box" if e["today"] else "event-date-box"
        badge_html = f'<span class="event-badge">{e["badge"]}</span>' if e["badge"] else ""
        st.markdown(f"""
        <div class="{card_cls}">
            <div class="{box_cls}">
                <div class="event-day">{e['day']}</div>
                <div class="event-dow">{e['dow']}</div>
            </div>
            <div class="event-info">
                <div class="event-title">{e['title']}</div>
                <div class="event-desc">{e['desc']}</div>
            </div>
            {badge_html}
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="footer-bar">⚡ <span>한전KDN</span> · 송정우 개인 포트폴리오</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# 게시판 페이지
# ══════════════════════════════════════════════════════════════
elif page == "📋 게시판":

    st.markdown("""
    <div class="page-header">
        <div class="page-header-icon">📋</div>
        <div>
            <div class="page-header-title">게시판</div>
            <div class="page-header-sub">Notice Board</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if "posts" not in st.session_state:
        st.session_state.posts = [
            {"no": 3, "title": "Streamlit 학습 후기",       "date": "2026-05-26", "views": 12},
            {"no": 2, "title": "GIS 시스템 개발 노트 공유",  "date": "2026-05-20", "views": 34},
            {"no": 1, "title": "첫 게시글입니다",            "date": "2026-05-15", "views": 51},
        ]

    with st.expander("✏️ 새 글 작성", expanded=False):
        with st.form("write_form", clear_on_submit=True):
            new_title = st.text_input("제목", placeholder="제목을 입력하세요")
            new_body  = st.text_area("내용", placeholder="내용을 입력하세요", height=120)
            submitted = st.form_submit_button("등록")
            if submitted:
                if new_title.strip():
                    new_no = (st.session_state.posts[0]["no"] + 1) if st.session_state.posts else 1
                    st.session_state.posts.insert(0, {
                        "no": new_no,
                        "title": new_title.strip(),
                        "date": "2026-05-27",
                        "views": 0,
                    })
                    st.success("게시글이 등록되었습니다.")
                    st.rerun()
                else:
                    st.warning("제목을 입력해주세요.")

    rows_html = "".join(
        f'<tr>'
        f'<td style="width:50px">{p["no"]}</td>'
        f'<td class="post-title-cell">{p["title"]}</td>'
        f'<td style="width:110px">{p["date"]}</td>'
        f'<td style="width:70px">{p["views"]}</td>'
        f'</tr>'
        for p in st.session_state.posts
    )
    st.markdown(f"""
    <div style="margin-bottom:10px;font-size:0.8rem;color:#4A5A7C;font-weight:600;">
        총 {len(st.session_state.posts)}건
    </div>
    <table class="board-table">
        <thead><tr>
            <th>번호</th>
            <th>제목</th>
            <th>작성일</th>
            <th>조회</th>
        </tr></thead>
        <tbody>{rows_html}</tbody>
    </table>
    """, unsafe_allow_html=True)

    st.markdown('<div class="footer-bar">⚡ <span>한전KDN</span> · 송정우 개인 포트폴리오</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# 연락하기 페이지
# ══════════════════════════════════════════════════════════════
elif page == "📬 연락하기":

    st.markdown("""
    <div class="page-header">
        <div class="page-header-icon">📬</div>
        <div>
            <div class="page-header-title">연락하기</div>
            <div class="page-header-sub">Contact · Get in Touch</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="contact-grid">
        <div class="contact-card">
            <div class="contact-card-icon blue">📧</div>
            <div class="contact-card-label">이메일</div>
            <div class="contact-card-value">songjw_77@kdn.com</div>
        </div>
        <div class="contact-card">
            <div class="contact-card-icon cyan">🏢</div>
            <div class="contact-card-label">소속</div>
            <div class="contact-card-value">한전KDN 본사</div>
        </div>
        <div class="contact-card">
            <div class="contact-card-icon green">💼</div>
            <div class="contact-card-label">직급</div>
            <div class="contact-card-value">과장 (Manager)</div>
        </div>
        <div class="contact-card">
            <div class="contact-card-icon purple">⚡</div>
            <div class="contact-card-label">전문분야</div>
            <div class="contact-card-value">전력 IT · GIS</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="contact-form-card">
        <div class="contact-form-title">메시지 보내기</div>
        <div class="contact-form-sub">업무 협력, 기술 문의, 프로젝트 제안 등 자유롭게 연락 주세요.</div>
        <div class="response-time-badge">
            <span>●</span> 평균 응답시간 1 영업일 이내
        </div>
    </div>
    """, unsafe_allow_html=True)

    if "msg_sent" not in st.session_state:
        st.session_state.msg_sent = False

    if st.session_state.msg_sent:
        st.success("✅ 메시지가 성공적으로 전송되었습니다! 빠른 시일 내에 답변 드리겠습니다.")
        if st.button("새 메시지 작성"):
            st.session_state.msg_sent = False
            st.rerun()
    else:
        with st.form("contact_form", clear_on_submit=False):
            col1, col2 = st.columns(2)
            with col1:
                sender_name = st.text_input("이름 *", placeholder="홍길동")
            with col2:
                sender_email = st.text_input("이메일 *", placeholder="example@email.com")

            subject_options = [
                "업무 협력 제안",
                "기술 문의",
                "프로젝트 제안",
                "GIS / 공간정보 관련",
                "기타",
            ]
            subject = st.selectbox("문의 유형", subject_options)
            message = st.text_area("메시지 *", placeholder="메시지 내용을 입력해주세요...", height=150)

            submitted = st.form_submit_button("📨 메시지 전송")
            if submitted:
                if sender_name.strip() and sender_email.strip() and message.strip():
                    st.session_state.msg_sent = True
                    st.rerun()
                else:
                    st.warning("이름, 이메일, 메시지는 필수 입력 항목입니다.")

    st.markdown("""
    <div style="margin-top:24px;background:rgba(79,142,255,0.06);border:1px solid rgba(79,142,255,0.15);border-radius:14px;padding:18px 20px;">
        <div style="font-size:0.72rem;font-weight:700;color:#4A5A7C;letter-spacing:0.08em;text-transform:uppercase;margin-bottom:10px;">근무 시간</div>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px;">
            <div style="font-size:0.82rem;color:#8BBFFF;">평일 (월~금)</div>
            <div style="font-size:0.82rem;color:#D0D8EE;font-weight:600;">09:00 – 18:00</div>
            <div style="font-size:0.82rem;color:#4A5A7C;">주말 · 공휴일</div>
            <div style="font-size:0.82rem;color:#4A5A7C;">휴무</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="footer-bar">⚡ <span>한전KDN</span> · 송정우 개인 포트폴리오</div>', unsafe_allow_html=True)
