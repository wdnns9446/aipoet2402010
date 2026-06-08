import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="AI Poet",
    page_icon="📝",
    layout="centered"
)

st.title("📝 AI Poet")
st.write("주제를 입력하면 AI가 짧은 시를 만들어줍니다.")

# Streamlit secrets에서 API Key 가져오기
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

topic = st.text_input("시의 주제를 입력하세요", placeholder="예: 고양이, 바다, 시험기간, 첫사랑")

style = st.selectbox(
    "시의 분위기를 선택하세요",
    ["감성적", "슬픈", "희망적인", "재미있는", "웅장한", "몽환적인"]
)

length = st.radio(
    "시의 길이",
    ["짧게", "보통", "길게"],
    horizontal=True
)

if st.button("시 만들기"):
    if topic.strip() == "":
        st.warning("주제를 먼저 입력해주세요!")
    else:
        with st.spinner("AI가 시를 쓰는 중입니다..."):
            prompt = f"""
            너는 한국어 시인이다.
            주제: {topic}
            분위기: {style}
            길이: {length}

            조건:
            - 한국어로 작성
            - 제목 포함
            - 너무 어렵지 않게 작성
            - 감성적인 표현 사용
            - 시 형태로 줄바꿈해서 출력
            """

            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "너는 감성적인 한국어 시를 쓰는 AI 시인이다."},
                    {"role": "user", "content": prompt}
                ]
            )

            poem = response.choices[0].message.content

            st.subheader("✨ 완성된 시")
            st.write(poem)

st.divider()
st.caption("AI Poet Streamlit App")