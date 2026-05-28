import streamlit as st
import pandas as pd
import time
from datetime import datetime

st.set_page_config(page_title="Labor-Link", layout="wide", initial_sidebar_state="collapsed")

YOUTUBE_URL = "https://youtu.be/FY3NkpmMN3U?si=5ruAbhqOmVnANB7n"

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;500;600;700;800;900&display=swap');

* { font-family:'Noto Sans KR', sans-serif; }
.stApp { background:#ffffff; }

.block-container {
    padding-top:0 !important;
    padding-left:0 !important;
    padding-right:0 !important;
    max-width:100% !important;
}

#MainMenu, footer, header { visibility:hidden !important; }
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
[data-testid="stHeader"],
[data-testid="stDeployButton"] {
    display:none !important;
}

.top-nav {
    height:74px;
    background:white;
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:0 34px;
    border-bottom:1px solid #e5e7eb;
    box-shadow:0 2px 12px rgba(15,23,42,.08);
    position:sticky;
    top:0;
    z-index:999;
}

.logo {
    display:flex;
    align-items:center;
    gap:12px;
    font-size:29px;
    font-weight:900;
    color:#0f172a;
}

.logo-icon {
    width:42px;
    height:42px;
    border-radius:12px;
    background:linear-gradient(135deg,#2563eb,#60a5fa);
    display:flex;
    align-items:center;
    justify-content:center;
    color:white;
    font-size:24px;
}

.nav-menu {
    display:flex;
    align-items:center;
    gap:62px;
    font-size:17px;
    font-weight:800;
    color:#0f172a;
}

.nav-item {
    position:relative;
    padding:27px 0;
    cursor:pointer;
}

.nav-item:hover,
.nav-item.active {
    color:#2563eb;
}

.nav-item.active {
    border-bottom:3px solid #2563eb;
}

.dropdown {
    display:none;
    position:absolute;
    top:74px;
    left:50%;
    transform:translateX(-50%);
    width:820px;
    background:white;
    padding:28px 34px;
    border-radius:0 0 16px 16px;
    box-shadow:0 18px 45px rgba(15,23,42,.18);
    border:1px solid #e5e7eb;
    z-index:9999;
}

.nav-item:hover .dropdown {
    display:flex;
    gap:34px;
}

.drop-col {
    min-width:170px;
    padding-right:24px;
    border-right:1px solid #e5e7eb;
}

.drop-col:last-child { border-right:none; }

.drop-title {
    color:#1d4ed8;
    font-size:17px;
    font-weight:900;
    margin-bottom:16px;
}

.drop-link {
    color:#334155;
    font-size:15px;
    font-weight:500;
    margin:11px 0;
}

.stTabs { padding:0 42px 45px 42px; }

.stTabs [data-baseweb="tab-list"] {
    gap:8px;
    background:#f8fafc;
    padding:12px;
    border-radius:14px;
    margin-top:22px;
    margin-bottom:22px;
    flex-wrap:wrap;
}

.stTabs [data-baseweb="tab"] {
    height:44px;
    border-radius:10px;
    padding:0 18px;
    font-size:15px;
    font-weight:700;
    color:#475569;
    background:transparent;
}

.stTabs [aria-selected="true"] {
    color:#2563eb !important;
    background:white !important;
    box-shadow:0 3px 10px rgba(15,23,42,.08);
}

.hero-wrap {
    display:grid;
    grid-template-columns:42% 58%;
    background:linear-gradient(90deg,#fffaf3 0%,#f3f8ff 55%,#ffffff 100%);
    border-bottom:1px solid #e5e7eb;
    min-height:430px;
    margin:-22px -42px 0 -42px;
}

.hero-left { padding:76px 40px 50px 72px; }

.hero-left h1 {
    font-size:46px;
    line-height:1.22;
    color:#0f2a55;
    font-weight:900;
    margin-bottom:22px;
}

.hero-left p {
    font-size:18px;
    line-height:1.8;
    color:#334155;
    margin-bottom:28px;
}

.main-btn {
    display:inline-block;
    background:#2563eb;
    color:white;
    padding:14px 26px;
    border-radius:8px;
    font-weight:800;
    box-shadow:0 7px 18px rgba(37,99,235,.25);
}

.hero-video { padding:50px 50px 42px 0; }

.video-frame {
    background:white;
    padding:12px;
    border-radius:16px;
    box-shadow:0 12px 32px rgba(15,23,42,.18);
    border:1px solid #e5e7eb;
}

.content-wrap { padding:34px 12px 20px 12px; }

.section-title {
    font-size:25px;
    font-weight:900;
    color:#0f172a;
    margin-bottom:22px;
}

.video-grid {
    display:grid;
    grid-template-columns:repeat(5,1fr);
    gap:22px;
}

.thumb {
    height:135px;
    border-radius:12px;
    padding:20px;
    font-size:22px;
    line-height:1.35;
    font-weight:900;
    color:#0f172a;
    position:relative;
}

.time {
    position:absolute;
    right:10px;
    bottom:10px;
    background:rgba(0,0,0,.82);
    color:white;
    font-size:13px;
    padding:3px 7px;
    border-radius:5px;
}

.card-title {
    font-weight:800;
    color:#0f172a;
    margin-top:12px;
    font-size:15px;
}

.card-meta {
    font-size:13px;
    color:#64748b;
    margin-top:6px;
}

.info-card {
    background:#fff;
    padding:24px;
    border-radius:16px;
    box-shadow:0 4px 12px rgba(0,0,0,.05);
    border:1px solid #F1F5F9;
    margin-bottom:20px;
}

.step-container {
    display:flex;
    justify-content:space-between;
    margin-bottom:20px;
    padding:10px;
    background:#f1f5f9;
    border-radius:10px;
}

.step {
    text-align:center;
    font-size:14px;
    font-weight:600;
    color:#94a3b8;
    width:25%;
}

.step.active {
    color:#2563eb;
    font-weight:800;
}
</style>
""", unsafe_allow_html=True)

# 상단바
st.markdown("""
<div class="top-nav">
    <div class="logo">
        <div class="logo-icon">🔗</div>
        <div>Labor Link</div>
    </div>
</div>
""", unsafe_allow_html=True)

tabs = st.tabs([
    "플랫폼 소개",
    "정서 케어 (AI)",
    "맞춤 법률 진단",
    "계약서 AI 판독",
    "녹취록 AI 변환",
    "증거 및 진정서",
    "📍 쉼터 지도"
])

with tabs[0]:
    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-left">
            <h1>노동자의 권리를<br>연결하는 곳,<br>Labor Link</h1>
            <p>
                일용직 노동자를 포함한 모든 노동자의 권익 보호와<br>
                건강한 노동 환경을 위해 정보를 연결합니다.
            </p>
            <div class="main-btn">자세히 알아보기 →</div>
        </div>
        <div class="hero-video">
            <div class="video-frame">
    """, unsafe_allow_html=True)

    st.video(YOUTUBE_URL)

    st.markdown("""
            </div>
        </div>
    </div>

    <div class="content-wrap">
        <div class="section-title">추천 노동 관련 영상</div>
        <div class="video-grid">
            <div>
                <div class="thumb" style="background:#bfdbfe;">일용직 노동자가<br>꼭 알아야 할<br>권리 5가지 <span class="time">5:12</span></div>
                <div class="card-title">일용직 노동자가 꼭 알아야 할 권리 5가지</div>
                <div class="card-meta">노동법 TV · 조회수 1.2만회 · 2개월 전</div>
            </div>
            <div>
                <div class="thumb" style="background:#5b9a8b; color:white;">임금체불 시<br>대처 방법 <span class="time">4:38</span></div>
                <div class="card-title">임금체불 시 대처 방법 총정리</div>
                <div class="card-meta">노동법 TV · 조회수 2.3만회 · 1개월 전</div>
            </div>
            <div>
                <div class="thumb" style="background:#fde7b4;">근로계약서<br>작성 시<br>주의사항 <span class="time">6:01</span></div>
                <div class="card-title">근로계약서 작성 시 주의사항</div>
                <div class="card-meta">노동법 TV · 조회수 1.8만회 · 3개월 전</div>
            </div>
            <div>
                <div class="thumb" style="background:#ddd6fe;">산업재해 발생 시<br>보상 절차<br>알아보기 <span class="time">6:54</span></div>
                <div class="card-title">산업재해 발생 시 보상 절차 알아보기</div>
                <div class="card-meta">노동법 TV · 조회수 1.5만회 · 2개월 전</div>
            </div>
            <div>
                <div class="thumb" style="background:#bae6fd;">퇴직금 계산 방법<br>쉽게 이해하기 <span class="time">3:59</span></div>
                <div class="card-title">퇴직금 계산 방법 쉽게 이해하기</div>
                <div class="card-meta">노동법 TV · 조회수 9천회 · 1개월 전</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tabs[1]:
    st.markdown("### 내러티브 테라피 기반 AI 감정 치유 공간")
    st.caption("현재는 시연용 AI 상담 모드입니다.")

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {
                "role": "assistant",
                "content": "안녕하세요. 오늘 현장에서 마음 아픈 일이 있으셨나요? 혼자 앓지 말고 편하게 털어놓아 주세요."
            }
        ]

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    if prompt := st.chat_input("이곳에 상황이나 심경을 입력하세요..."):
        st.session_state.messages.append({"role": "user", "content": prompt})

        with st.chat_message("user"):
            st.write(prompt)

        demo_response = (
            "말씀해 주셔서 고마워요. 그런 상황을 겪으면 위축되고 불안해지는 것이 당연합니다. "
            "하지만 부당한 대우를 받은 것이 당신의 잘못은 아닙니다. "
            "필요하다면 근로계약서, 임금 내역, 문자나 녹취 같은 자료를 차분히 모아두는 것이 도움이 됩니다."
        )

        with st.chat_message("assistant"):
            st.write(demo_response)

        st.session_state.messages.append({"role": "assistant", "content": demo_response})

with tabs[2]:
    st.markdown("### 취약계층 맞춤 진단 및 계산기")
    st.markdown("<div class='info-card'>#### 기초 근무 환경 정보</div>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    c1.number_input("상시 근로자 수", min_value=1, value=5)
    c2.radio("계약 형태", ["일반 근로계약서", "3.3% 프리랜서 위임 계약"])
    c3.number_input("1주 소정 근로시간", min_value=1, value=16)

    situation = st.selectbox(
        "권익 피해 유형을 선택해 주세요.",
        [
            "선택하세요",
            "외국인 노동자 권리 보장 및 체류 협박 대응",
            "임금채권 소멸시효 및 체불 모델",
            "위장 프리랜서 검증",
            "직장 내 괴롭힘"
        ]
    )

    if situation == "외국인 노동자 권리 보장 및 체류 협박 대응":
        st.error("💡 미등록 외국인 노동자라 하더라도 제공한 노동에 대한 임금 및 산재 보상 권리는 보호받을 수 있습니다.")
    elif situation == "임금채권 소멸시효 및 체불 모델":
        st.info("체불된 임금은 단순한 돈이 아니라 노동 시간이 제대로 보상받지 못한 문제입니다.")
    elif situation == "위장 프리랜서 검증":
        st.write("프리랜서 계약을 맺었더라도 실질적으로 지휘·감독을 받았다면 근로자성이 인정될 수 있습니다.")
        if st.checkbox("고용주가 출퇴근 시간과 장소를 지정하나요?") and st.checkbox("구체적인 업무 지시를 받나요?"):
            st.error("진단 결과: 근로자일 가능성이 높습니다. 주휴수당 미지급은 위법 소지가 있습니다.")
    elif situation == "직장 내 괴롭힘":
        if st.checkbox("지위나 우위 구조를 이용했는가?") and st.checkbox("적정 범위를 초과한 폭언/차별인가?"):
            st.error("요건 충족 가능성이 있습니다. 증거 보관함에 보존하세요.")

with tabs[3]:
    st.markdown("### 📸 스마트폰 근로계약서 AI 분석 (OCR)")
    uploaded_img = st.file_uploader("계약서 이미지 업로드 (jpg, png)", type=["jpg", "png", "jpeg"])

    if uploaded_img:
        with st.spinner("AI가 스캔하고 있습니다..."):
            time.sleep(2)

        st.error(
            "⚠️ **[주의] 위장 프리랜서 조항 발견!**\n\n"
            "해당 계약서에 **'3.3% 사업소득세 공제'** 및 **'위임 계약'**이 감지되었습니다. "
            "불법 계약일 확률이 높습니다."
        )

with tabs[4]:
    if "evidence_db" not in st.session_state:
        st.session_state.evidence_db = []

    st.markdown("### 🎙️ 폭언/협박 녹취록 AI 텍스트 변환 (STT)")
    uploaded_audio = st.file_uploader("녹음 파일 업로드 (mp3, wav)", type=["mp3", "wav"])

    if uploaded_audio:
        with st.spinner("AI가 텍스트 변환 및 키워드 추출 중입니다..."):
            time.sleep(2)

        st.success("✅ **변환 완료:** \"내일부터 당장 나오지 마. 노동청에 신고한다고? 해볼 테면 해봐.\"")

        if st.button("이 녹취록을 [증거 보관함]에 즉시 저장"):
            st.session_state.evidence_db.append({
                "일자": datetime.now().strftime("%Y-%m-%d"),
                "유형": "음성 녹취 (STT)",
                "정황": "녹취 변환: 기습 해고 및 협박성 발언 포함"
            })
            st.rerun()

with tabs[5]:
    if "evidence_db" not in st.session_state:
        st.session_state.evidence_db = []

    st.markdown("### 증거 아카이빙 및 노동청 진정서 생성")

    step = min(len(st.session_state.evidence_db) + 1, 4)

    st.markdown(f"""
    <div class="step-container">
        <div class="step {'active' if step >= 1 else ''}">1. 권리 인지</div>
        <div class="step {'active' if step >= 2 else ''}">2. 증거 수집 ({len(st.session_state.evidence_db)}건)</div>
        <div class="step {'active' if step >= 3 else ''}">3. 진정서 완성</div>
        <div class="step {'active' if step >= 4 else ''}">4. 노동청 신고</div>
    </div>
    """, unsafe_allow_html=True)

    st.progress(step * 25)

    with st.expander("➕ 수동으로 증거 기록 추가하기"):
        d = st.date_input("피해 발생 일자")
        t = st.text_area("객관적 정황 기술")

        if st.button("데이터 백업", type="primary") and t:
            st.session_state.evidence_db.append({
                "일자": d.strftime("%Y-%m-%d"),
                "유형": "수동 기록",
                "정황": t
            })
            st.rerun()

    if len(st.session_state.evidence_db) > 0:
        st.dataframe(pd.DataFrame(st.session_state.evidence_db), use_container_width=True)

        petition = f"입증 자료 총 {len(st.session_state.evidence_db)}건\n"
        petition += "\n".join([
            f"[{i+1}] {ev['일자']} | {ev['정황']}"
            for i, ev in enumerate(st.session_state.evidence_db)
        ])

        st.download_button(
            "📝 진정서 다운로드 (.txt)",
            f"[임금체불 및 근로기준법 위반 진정서]\n\n{petition}\n\n고용노동부 관할 지방고용노동청장 귀하",
            "petition.txt"
        )

with tabs[6]:
    st.markdown("### 📍 내 주변 기관 및 쉼터")
    st.map(pd.DataFrame({
        "lat": [37.5665, 37.4979, 37.5683],
        "lon": [126.9780, 127.0276, 126.9878],
        "name": ["서울노동권익센터", "이동노동자 쉼터", "지방고용노동청"]
    }))