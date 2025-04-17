import streamlit as st
from textblob import TextBlob
from datetime import datetime

st.title("🧠 감정 분석기")
st.write("문장을 입력하면 AI가 감정을 분석해줍니다.")

text = st.text_input("감정을 분석할 문장을 입력하세요:")

if st.button("분석하기"):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity

    if sentiment > 0.5:
        result = "🤩 엄청 긍정적인 문장이에요!"
    elif sentiment > 0:
        result = "😊 긍정적인 문장이에요!"
    elif sentiment < -0.5:
        result = "💢 엄청 짜증난 상태에요!"
    elif sentiment < 0:
        result = "😠 부정적인 문장이에요!"
    else:
        result = "😐 중립적인 문장이에요!"

    st.success(result)

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("sentiment_log.txt", "a", encoding="utf-8") as f:
        f.write(f"[{now}] 입력: {text}\n결과: {result}\n\n")
