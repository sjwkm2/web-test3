import streamlit as st

# ── 페이지 설정 ──────────────────────────────────────────────
st.set_page_config(
    page_title="송정우 | 한전KDN",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ── KDN 네이비 디자인 시스템 CSS ────────────────────────────
CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;600;700;800&display=swap');

:root {
    --navy-900: #0A1428;
    --navy-800: #0F1B33;
    --navy-700: #1B2A4A;
    --navy-600: #2A3A5C;
    --navy-500: #4A5A7C;
    --navy-400: #7A89AB;
    --navy-300: #B8C0D6;
    --navy-200: #DDE2EE;
    --navy-100: #F0F2F8;
    --navy-50:  #F8F9FC;
    --accent:   #3D6FE0;
    --gold:     #3D6FE0;
}

html, body, [class*="css"] {
    font-family: 'Noto Sans KR', -apple-system, sans-serif !important;
    word-break: keep-all;
}

/* 사이드바 */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, var(--navy-800) 0%, var(--navy-900) 100%) !important;
}
[data-testid="stSidebar"] * { color: #E6E8EB !important; }
[data-testid="stSidebar"] .sidebar-brand {
    text-align: center;
    padding: 24px 16px 16px;
    border-bottom: 1px solid rgba(255,255,255,0.1);
    margin-bottom: 12px;
}
[data-testid="stSidebar"] .sidebar-avatar {
    width: 80px; height: 80px;
    border-radius: 50%;
    background: var(--navy-700);
    display: flex; align-items: center; justify-content: center;
    font-size: 2rem;
    margin: 0 auto 12px;
    border: 3px solid var(--accent);
}
[data-testid="stSidebar"] .sidebar-name {
    font-size: 1.1rem; font-weight: 700; color: #fff !important;
    margin-bottom: 4px;
}
[data-testid="stSidebar"] .sidebar-sub {
    font-size: 0.72rem; color: var(--navy-400) !important;
    letter-spacing: 0.05em; text-transform: uppercase;
}

/* 메인 컨테이너 */
.main .block-container { padding: 2rem 1.5rem; max-width: 860px; }

/* 히어로 카드 */
.hero-card {
    background: linear-gradient(135deg, var(--navy-700) 0%, var(--navy-900) 100%);
    border-radius: 20px;
    padding: 40px 32px;
    text-align: center;
    color: #fff;
    margin-bottom: 24px;
    box-shadow: 0 20px 40px rgba(15,27,51,0.3);
}
.hero-avatar {
    width: 96px; height: 96px;
    background: rgba(255,255,255,0.12);
    border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-size: 2.8rem;
    margin: 0 auto 16px;
    border: 3px solid rgba(61,111,224,0.6);
}
.hero-name {
    font-size: 2rem; font-weight: 800;
    letter-spacing: -0.03em;
    margin-bottom: 6px;
}
.hero-badge {
    display: inline-block;
    background: rgba(61,111,224,0.3);
    border: 1px solid rgba(61,111,224,0.6);
    color: #a8c4ff;
    font-size: 0.75rem; font-weight: 700;
    padding: 3px 12px;
    border-radius: 999px;
    letter-spacing: 0.12em;
    margin-bottom: 20px;
}
.hero-divider {
    border: none; border-top: 1px solid rgba(255,255,255,0.12);
    margin: 20px 0;
}

/* 정보 카드 그리드 */
.info-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
    margin-bottom: 24px;
}
.info-item {
    background: #fff;
    border: 1px solid var(--navy-200);
    border-radius: 12px;
    padding: 14px 16px;
    display: flex; align-items: center; gap: 12px;
    box-shadow: 0 1px 3px rgba(15,27,51,0.06);
}
.info-icon { font-size: 1.4rem; flex-shrink: 0; }
.info-label { font-size: 0.65rem; color: var(--navy-500); font-weight: 600; letter-spacing: 0.05em; text-transform: uppercase; }
.info-value { font-size: 0.9rem; font-weight: 600; color: var(--navy-800); margin-top: 2px; }

/* 스킬 태그 */
.skill-section { margin-bottom: 24px; }
.skill-section-title {
    font-size: 0.68rem; font-weight: 700; color: var(--navy-500);
    letter-spacing: 0.1em; text-transform: uppercase;
    display: flex; align-items: center; gap: 8px;
    margin-bottom: 10px;
}
.skill-section-title::after {
    content: ''; flex: 1;
    height: 1px; background: var(--navy-200);
}
.tags-wrap { display: flex; flex-wrap: wrap; gap: 7px; }

.tag {
    display: inline-block;
    padding: 4px 12px;
    border-radius: 999px;
    font-size: 0.78rem; font-weight: 600;
    border: 1px solid transparent;
}
.tag-lang   { background: #EEF2FF; color: #4338CA; border-color: #C7D2FE; }
.tag-db     { background: #F0FDF4; color: #166534; border-color: #BBF7D0; }
.tag-gis    { background: #FFF7ED; color: #C2410C; border-color: #FED7AA; }
.tag-infra  { background: #F0F9FF; color: #0369A1; border-color: #BAE6FD; }
.tag-new    { background: #FDF4FF; color: #7E22CE; border-color: #E9D5FF; }

/* 섹션 타이틀 */
.section-title {
    font-size: 1.3rem; font-weight: 800;
    color: var(--navy-800);
    letter-spacing: -0.02em;
    margin-bottom: 20px;
    padding-bottom: 12px;
    border-bottom: 2px solid var(--navy-200);
}

/* 스킬 카드 그리드 */
.skill-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 16px;
    margin-bottom: 24px;
}
.skill-cat-card {
    background: #fff;
    border: 1px solid var(--navy-200);
    border-radius: 14px;
    padding: 16px;
    box-shadow: 0 1px 3px rgba(15,27,51,0.06);
}
.skill-cat-label {
    font-size: 0.65rem; font-weight: 700; color: var(--navy-500);
    letter-spacing: 0.08em; text-transform: uppercase;
    margin-bottom: 12px;
    padding-bottom: 8px;
    border-bottom: 1px solid var(--navy-100);
}
.skill-row-item {
    display: flex; align-items: center; gap: 10px;
    padding: 8px; margin: 4px -8px;
    border-radius: 8px;
    border: 1px solid transparent;
    cursor: default;
}
.skill-row-item:hover {
    background: var(--navy-100);
    border-color: var(--navy-200);
}
.skill-row-icon  { font-size: 1rem; flex-shrink: 0; }
.skill-row-name  { font-size: 0.85rem; font-weight: 600; color: var(--navy-800); }
.skill-row-hint  { font-size: 0.68rem; color: var(--navy-500); line-height: 1.3; }

/* 레퍼런스 카드 */
.ref-card {
    background: #fff;
    border: 1px solid var(--navy-200);
    border-radius: 14px;
    padding: 20px 22px;
    margin-bottom: 16px;
    box-shadow: 0 1px 3px rgba(15,27,51,0.06);
}
.ref-card:hover { box-shadow: 0 4px 12px rgba(15,27,51,0.1); }
.ref-card-top {
    display: flex; align-items: flex-start;
    justify-content: space-between; gap: 12px;
    margin-bottom: 6px;
}
.ref-title { font-size: 1rem; font-weight: 700; color: var(--navy-800); }
.ref-period {
    font-size: 0.72rem; font-weight: 600; color: var(--accent);
    background: #EEF2FF; padding: 2px 8px;
    border-radius: 999px; white-space: nowrap;
    flex-shrink: 0;
}
.ref-role { font-size: 0.78rem; color: var(--navy-500); margin-bottom: 8px; }
.ref-desc { font-size: 0.85rem; color: var(--navy-600); line-height: 1.7; margin-bottom: 12px; }
.ref-tags { display: flex; flex-wrap: wrap; gap: 6px; }

/* 일정 카드 */
.event-card {
    background: #fff;
    border: 1px solid var(--navy-200);
    border-radius: 12px;
    padding: 16px 20px;
    margin-bottom: 10px;
    display: flex; align-items: center; gap: 16px;
    box-shadow: 0 1px 3px rgba(15,27,51,0.06);
}
.event-date-box {
    min-width: 44px; text-align: center;
    background: var(--navy-100);
    border-radius: 10px; padding: 6px 8px;
}
.event-day   { font-size: 1.3rem; font-weight: 800; color: var(--navy-800); line-height: 1; }
.event-dow   { font-size: 0.65rem; color: var(--navy-500); font-weight: 600; }
.event-info  {}
.event-title { font-size: 0.92rem; font-weight: 700; color: var(--navy-800); }
.event-desc  { font-size: 0.75rem; color: var(--navy-500); margin-top: 2px; }

/* 게시판 */
.board-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.88rem;
}
.board-table th {
    background: var(--navy-100);
    color: var(--navy-600);
    font-weight: 700;
    padding: 10px 14px;
    text-align: left;
    border-bottom: 2px solid var(--navy-200);
    font-size: 0.75rem;
    letter-spacing: 0.04em;
}
.board-table td {
    padding: 12px 14px;
    border-bottom: 1px solid var(--navy-100);
    color: var(--navy-700);
}
.board-table tr:hover td { background: var(--navy-50); }

/* 푸터 */
.footer-text {
    text-align: center;
    font-size: 0.75rem;
    color: var(--navy-400);
    margin-top: 32px;
    padding-top: 16px;
    border-top: 1px solid var(--navy-200);
}

/* Streamlit 기본 요소 숨기기 */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ── 사이드바 ─────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div class="sidebar-brand">
        <div class="sidebar-avatar">👨‍💼</div>
        <div class="sidebar-name">송정우</div>
        <div class="sidebar-sub">한전KDN · 과장</div>
    </div>
    """, unsafe_allow_html=True)

    page = st.radio(
        "페이지 선택",
        ["🏠 소개", "📅 일정", "💡 보유스킬", "📁 레퍼런스", "📋 게시판"],
        label_visibility="collapsed",
    )

# ══════════════════════════════════════════════════════════════
# 소개 페이지
# ══════════════════════════════════════════════════════════════
if page == "🏠 소개":

    # 히어로 카드
    st.markdown("""
    <div class="hero-card">
        <div class="hero-avatar">👨‍💼</div>
        <div class="hero-name">송 정 우</div>
        <div class="hero-badge">과 장</div>
        <hr class="hero-divider" />
        <div style="font-size:0.85rem; color:rgba(255,255,255,0.7); line-height:1.8;">
            풀스택 바이브코딩 실습 프로젝트
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 정보 카드
    st.markdown("""
    <div class="info-grid">
        <div class="info-item">
            <span class="info-icon">🏢</span>
            <div>
                <div class="info-label">소속</div>
                <div class="info-value">한전KDN</div>
            </div>
        </div>
        <div class="info-item">
            <span class="info-icon">💼</span>
            <div>
                <div class="info-label">직급</div>
                <div class="info-value">과장</div>
            </div>
        </div>
        <div class="info-item">
            <span class="info-icon">📧</span>
            <div>
                <div class="info-label">이메일</div>
                <div class="info-value">songjw_77@kdn.com</div>
            </div>
        </div>
        <div class="info-item">
            <span class="info-icon">📱</span>
            <div>
                <div class="info-label">연락처</div>
                <div class="info-value">010-****-****</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 기술 스택
    st.markdown("""
    <div class="skill-section">
        <div class="skill-section-title">🛠 기술 스택</div>
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
    </div>
    """, unsafe_allow_html=True)

    # 자기소개 텍스트
    st.markdown("""
    <div class="skill-section">
        <div class="skill-section-title">📝 자기소개</div>
    </div>
    """, unsafe_allow_html=True)

    st.info(
        "안녕하세요! 한전KDN에서 **전력 IT 시스템** 개발 및 운영을 담당하고 있는 **송정우 과장**입니다.\n\n"
        "전력설비 GIS 시스템, 고객 서비스 포털, 배전 운영 자동화 등 다양한 공공 IT 프로젝트에서\n"
        "**Java 백엔드 개발**과 **ArcGIS 기반 공간 데이터 시각화**를 중심으로 경력을 쌓아왔습니다.\n\n"
        "현재는 Python/Streamlit을 활용한 풀스택 바이브코딩을 실습 중입니다."
    )

    st.markdown('<div class="footer-text">⚡ 한전KDN · 풀스택 바이브코딩 실습 프로젝트</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# 일정 페이지
# ══════════════════════════════════════════════════════════════
elif page == "📅 일정":
    st.markdown('<div class="section-title">📅 일정</div>', unsafe_allow_html=True)

    events = [
        {"day": "5",  "dow": "월", "title": "어린이날",         "desc": "공휴일"},
        {"day": "12", "dow": "월", "title": "팀 주간회의",       "desc": "오전 10:00 · 대회의실"},
        {"day": "19", "dow": "화", "title": "프로젝트 중간 보고","desc": "GIS 시스템 진행현황"},
        {"day": "28", "dow": "목", "title": "시스템 배포",        "desc": "운영 서버 반영 예정"},
        {"day": "30", "dow": "토", "title": "월말 결산 보고",     "desc": "5월 업무 실적 정리"},
    ]

    st.markdown("**2026년 5월 주요 일정**")
    for e in events:
        st.markdown(f"""
        <div class="event-card">
            <div class="event-date-box">
                <div class="event-day">{e['day']}</div>
                <div class="event-dow">{e['dow']}</div>
            </div>
            <div class="event-info">
                <div class="event-title">{e['title']}</div>
                <div class="event-desc">{e['desc']}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="footer-text">⚡ 한전KDN · 풀스택 바이브코딩 실습 프로젝트</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# 보유스킬 페이지
# ══════════════════════════════════════════════════════════════
elif page == "💡 보유스킬":
    st.markdown('<div class="section-title">💡 보유스킬</div>', unsafe_allow_html=True)

    SKILLS = {
        "🖥️ 프로그래밍 언어": [
            ("☕", "Java",      "백엔드 · 엔터프라이즈"),
            ("🌐", "JSP",       "서버사이드 웹 개발"),
            ("🎨", "CSS",       "UI 스타일링 · 반응형"),
            ("🐍", "Python",    "데이터 분석 · 자동화"),
        ],
        "🗄️ 데이터베이스": [
            ("🗃️", "Oracle",   "엔터프라이즈 RDBMS"),
            ("🐬", "MySQL",    "오픈소스 RDBMS"),
            ("🔷", "MariaDB",  "MySQL 포크 · 오픈소스"),
        ],
        "🗺️ GIS": [
            ("🗺️", "ArcGIS",  "공간 데이터 · 지도 시각화"),
        ],
        "⚙️ 인프라 · 미들웨어": [
            ("🖥️", "Unix",    "서버 운영 · 셸 스크립트"),
            ("⚙️", "JEUS",    "국산 WAS · 공공 인프라"),
        ],
        "✨ 새로 배우는 중": [
            ("🚀", "Streamlit", "Python 웹앱 · 데이터 대시보드"),
            ("🤖", "AI/ML",    "클로드 API · 생성형 AI 활용"),
        ],
    }

    cols = st.columns(2)
    col_idx = 0
    for cat, skills in SKILLS.items():
        rows_html = "".join(
            f'<p style="display:flex;align-items:center;gap:10px;padding:8px 6px;margin:2px 0;border-radius:8px;">'
            f'<span style="font-size:1rem;flex-shrink:0;">{icon}</span>'
            f'<span style="flex:1;">'
            f'<strong style="font-size:0.85rem;color:#0F1B33;font-weight:600;display:block;">{name}</strong>'
            f'<em style="font-size:0.68rem;color:#4A5A7C;font-style:normal;line-height:1.3;">{hint}</em>'
            f'</span></p>'
            for icon, name, hint in skills
        )
        with cols[col_idx % 2]:
            st.markdown(
                f'<div class="skill-cat-card"><div class="skill-cat-label">{cat}</div>{rows_html}</div>',
                unsafe_allow_html=True,
            )
        col_idx += 1

    st.markdown('<div class="footer-text">⚡ 한전KDN · 풀스택 바이브코딩 실습 프로젝트</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# 레퍼런스 페이지
# ══════════════════════════════════════════════════════════════
elif page == "📁 레퍼런스":
    st.markdown('<div class="section-title">📁 레퍼런스</div>', unsafe_allow_html=True)

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

    for p in projects:
        tag_html = " ".join(f'<span class="tag {cls}">{name}</span>' for cls, name in p["tags"])
        st.markdown(f"""
        <div class="ref-card">
            <div class="ref-card-top">
                <div class="ref-title">{p['title']}</div>
                <span class="ref-period">{p['period']}</span>
            </div>
            <div class="ref-role">{p['role']}</div>
            <div class="ref-desc">{p['desc']}</div>
            <div class="ref-tags">{tag_html}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown('<div class="footer-text">⚡ 한전KDN · 풀스택 바이브코딩 실습 프로젝트</div>', unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════
# 게시판 페이지
# ══════════════════════════════════════════════════════════════
elif page == "📋 게시판":
    st.markdown('<div class="section-title">📋 게시판</div>', unsafe_allow_html=True)

    # session_state 초기화
    if "posts" not in st.session_state:
        st.session_state.posts = [
            {"no": 3, "title": "Streamlit 학습 후기",      "date": "2026-05-26", "views": 12},
            {"no": 2, "title": "GIS 시스템 개발 노트 공유", "date": "2026-05-20", "views": 34},
            {"no": 1, "title": "첫 게시글입니다",           "date": "2026-05-15", "views": 51},
        ]

    # 글쓰기 폼
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

    # 게시글 목록
    st.markdown(f"**총 {len(st.session_state.posts)}건**")

    rows_html = "".join(
        f'<tr>'
        f'<td style="width:50px;padding:12px 14px;border-bottom:1px solid #F0F2F8;color:#1B2A4A;font-size:0.85rem">{p["no"]}</td>'
        f'<td style="padding:12px 14px;border-bottom:1px solid #F0F2F8;color:#1B2A4A;font-size:0.88rem;font-weight:500">{p["title"]}</td>'
        f'<td style="width:110px;padding:12px 14px;border-bottom:1px solid #F0F2F8;color:#4A5A7C;font-size:0.8rem">{p["date"]}</td>'
        f'<td style="width:70px;padding:12px 14px;border-bottom:1px solid #F0F2F8;color:#4A5A7C;font-size:0.8rem">{p["views"]}</td>'
        f'</tr>'
        for p in st.session_state.posts
    )
    st.markdown(f"""
    <table class="board-table" style="width:100%;border-collapse:collapse;background:#fff;border:1px solid #DDE2EE;border-radius:12px;overflow:hidden">
        <thead><tr>
            <th style="width:50px">번호</th>
            <th>제목</th>
            <th style="width:110px">작성일</th>
            <th style="width:70px">조회</th>
        </tr></thead>
        <tbody>{rows_html}</tbody>
    </table>
    """, unsafe_allow_html=True)

    st.markdown('<div class="footer-text">⚡ 한전KDN · 풀스택 바이브코딩 실습 프로젝트</div>', unsafe_allow_html=True)
