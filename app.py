import openai
import streamlit as st

# OpenAI API 키 설정
openai.api_key = "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"
st.title("영어 단어 뜻 검색기")

# 사용자 입력 받기
word = st.text_input("단어를 입력하세요:")

# 단어 의미 가져오기
if word:
    # OpenAI API를 통해 단어의 뜻을 설명 받기
    prompt = f"의미랑 발음이랑 영어의 한글 발음 알려줘 '{word}' 이 단어가 들어간 간단한 영어로 된 문장 하나 만들어줘."
    
    try:
        # OpenAI ChatGPT API 호출
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # GPT 모델
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        
        # API 응답에서 뜻 가져오기
        meaning = response['choices'][0]['message']['content']
        
        # Streamlit에 결과 출력
        st.write(f"'{word}'의 뜻: {meaning}")
    except Exception as e:
        st.write(f"오류가 발생했습니다: {e}")

