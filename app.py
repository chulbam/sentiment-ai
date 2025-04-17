import streamlit as st
st.set_page_config(page_title="루의 감정분석기", page_icon="🧠", layout="centered")

st.markdown(
    """
    <style>
    body {
        background-color: #f9f5ff;
        color: #333333;
        font-family: 'Apple SD Gothic Neo', sans-serif;
    }
    .stTextInput > div > div > input {
        background-color: #ffffff;
        color: #111111;
        font-size: 18px;
    }
    .stButton>button {
        background-color: #7e5bef;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        height: 3em;
        width: 100%;
    }
    .stTextArea textarea {
        background-color: #fff6f6;
        font-size: 14px;
        line-height: 1.6;
    }
    </style>
    """,
    unsafe_allow_html=True
)

from textblob import TextBlob
from datetime import datetime

st.title("🧠 감정 분석기")
st.write("문장을 입력하면 AI가 감정을 분석해줍니다.")

text = st.text_input("감정을 분석할 문장을 입력하세요:")

if st.button("분석하기"):
    # 로그 파일 읽기
# 로그 먼저 보여주기 (너 스타일 유지)
if st.checkbox("이전 기록 보기"):
    try:
        with open("sentiment_log.txt", "r", encoding="utf-8") as f:
            log = f.read()
            st.text_area("📜 감정 분석 기록", log, height=250)
    except FileNotFoundError:
        st.info("아직 기록이 없습니다.")

# 감정 분석 버튼
if st.button("분석하기"):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0.5:
        result = "🤩 **엄청 긍정적인 문장이에요!** 오늘 기분 최고~"
    elif sentiment > 0:
        result = "😊 **긍정적인 문장이에요.** 괜찮은 하루였어요!"
    elif sentiment < -0.5:
        result = "😡 **엄청 부정적인 문장이에요!** 스트레스 많이 받았군요..."
    elif sentiment < 0:
        result = "☹️ **부정적인 문장이에요.** 속상했죠?"
    else:
        result = "😐 **중립적인 문장이에요.** 무던한 하루였네요."

    st.success(result)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("sentiment_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now}] 입력: {text}\n결과: {result}\n\n")

