import streamlit as st
import openai
import os

# OpenAI API 키 설정
openai.api_key = st.secrets["OPENAI_API_KEY"]  # GitHub secrets에서 관리할 수 있음

st.title("AI 기반 수면 패턴 도우미")

# 사용자 입력 받기
sleep_data = st.text_area("오늘의 수면 데이터를 입력하세요 (예: 수면 시간, 질 등)")

# 수면 패턴 분석
if st.button("수면 패턴 분석하기"):
    if sleep_data:
        # OpenAI API 호출
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"이 수면 데이터를 바탕으로 개선할 수 있는 수면 패턴을 제시해주세요: {sleep_data}",
            max_tokens=150
        )
        st.write(response.choices[0].text.strip())
    else:
        st.error("수면 데이터를 입력하세요.")
