import random
import time
import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="오늘 뭐 먹지? 점심 메뉴 추천기", page_icon="🍱", layout="centered"
)

# 2. 메뉴 데이터 (카테고리별 분류)
MENU_DICT = {
    "한식": [
        "김치찌개",
        "된장찌개",
        "제육볶음",
        "비빔밥",
        "국밥",
        "불고기",
        "칼국수",
        "냉면",
    ],
    "중식": ["짜장면", "짬뽕", "탕수육", "마라탕", "볶음밥", "마파두부"],
    "일식": ["초밥", "돈까스", "라멘", "우동", "규동(소고기덮밥)", "카레"],
    "양식": ["파스타", "피자", "햄버거", "스테이크", "리조또", "샌드위치"],
    "분식/기타": ["떡볶이", "김밥", "쌀국수", "타코", "샐러드", "포케"],
}

# 3. 앱 제목 및 설명
st.title("🍱 오늘의 점심 메뉴 추천기")
st.write("매일 점심시간마다 고민되는 메뉴, 버튼 한 번으로 해결해 드립니다!")
st.divider()

# 4. 사이드바: 옵션 설정 및 메뉴 추가
with st.sidebar:
    st.header("⚙️ 추천 옵션")

    # 카테고리 선택 (기본값: 전체 선택)
    selected_categories = st.multiselect(
        "원하는 음식 종류를 선택하세요:",
        options=list(MENU_DICT.keys()),
        default=list(MENU_DICT.keys()),
    )

    st.divider()

    # 나만의 메뉴 추가 기능
    custom_menu = st.text_input(
        "후보에 추가하고 싶은 메뉴가 있나요?", placeholder="예: 마라샹궈"
    )

# 5. 선택된 카테고리의 메뉴들을 하나의 리스트로 합치기
candidate_menus = []
for category in selected_categories:
    candidate_menus.extend(MENU_DICT[category])

# 사용자가 입력한 메뉴가 있다면 리스트에 추가
if custom_menu.strip():
    candidate_menus.append(custom_menu.strip())

# 6. 메인 화면: 메뉴 추천 버튼 및 결과 출력
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    recommend_btn = st.button(
        "🎲 오늘의 점심 추천받기!", use_container_width=True, type="primary"
    )

if recommend_btn:
    if not candidate_menus:
        st.warning("⚠️ 사이드바에서 최소 1개 이상의 카테고리를 선택해 주세요!")
    else:
        # 두근거리는 효과를 위한 로딩 스피너
        with st.spinner("맛있는 메뉴를 고르는 중... 룰렛 돌아가는 중... 🎰"):
            time.sleep(1.0)  # 1초 대기

        # random.choice를 이용해 무작위로 1개 선택
        chosen_menu = random.choice(candidate_menus)

        # 풍선 애니메이션 효과
        st.balloons()

        # 결과 강조 출력
        st.success("🎉 오늘의 추천 메뉴가 결정되었습니다!")
        st.markdown(
            f"""
            <div style="text-align: center; padding: 30px; background-color: #f0f2f6; border-radius: 15px; margin-top: 10px;">
                <h3 style="color: #555; margin-bottom: 10px;">오늘 점심은 바로...</h3>
                <h1 style="color: #ff4b4b; font-size: 3em; margin: 0;">🍽️ {chosen_menu}</h1>
            </div>
            """,
            unsafe_allow_html=True,
        )

# 7. 하단: 현재 후보 메뉴 목록 보여주기 (접이식)
st.write("")
with st.expander("📋 현재 추천 후보 메뉴 전체보기"):
    if candidate_menus:
        st.write(", ".join(candidate_menus))
    else:
        st.write("선택된 메뉴가 없습니다.")
