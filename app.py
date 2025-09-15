import streamlit as st
from dotenv import load_dotenv
import os
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

# .envからAPIキーを読み込む
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# LLMの設定
llm = ChatOpenAI(openai_api_key=api_key, model="gpt-3.5-turbo")

# 関数：入力テキストと専門家の種類を受け取り回答を返す
def get_llm_response(user_input: str, expert_type: str) -> str:
    if expert_type == "旅行プランナー":
        system_prompt = "あなたは経験豊富な旅行プランナーです。旅行プランを提案してください。"
    elif expert_type == "栄養士":
        system_prompt = "あなたは管理栄養士です。健康に配慮した食事アドバイスをしてください。"
    else:
        system_prompt = "あなたは専門家です。質問に答えてください。"

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input)
    ]
    response = llm(messages)
    return response.content

# Streamlit UI
st.title("💡 LLM搭載 Web アプリ")
st.write("入力した質問を選択した専門家に相談できます。")

expert_type = st.radio("相談する専門家を選んでください：", ("旅行プランナー", "栄養士"))
user_input = st.text_input("質問を入力してください")

if st.button("送信"):
    if user_input.strip():
        answer = get_llm_response(user_input, expert_type)
        st.subheader("回答")
        st.write(answer)
    else:
        st.warning("質問を入力してください。")