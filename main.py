import streamlit as st
from langchain.memory import ConversationBufferMemory
# This remains the same, but we will update the internal logic in utils.py
from utils import get_chat_response

st.title("💬 NVIDIA Meta AI 助手")

with st.sidebar:
    # 1. Update label and link for NVIDIA
    nvidia_api_key = st.text_input("请输入 NVIDIA API Key：", type="password")
    st.markdown("[获取 NVIDIA API key](https://nvidia.com)")

if "memory" not in st.session_state:
    st.session_state["memory"] = ConversationBufferMemory(return_messages=True)
    st.session_state["messages"] = [{"role": "ai",
                                     "content": "你好，我是由 NVIDIA 驱动的 Meta AI 助手，有什么可以帮你的吗？"}]

for message in st.session_state["messages"]:
    st.chat_message(message["role"]).write(message["content"])

prompt = st.chat_input()
if prompt:
    # 2. Check for NVIDIA key instead of OpenAI
    if not nvidia_api_key:
        st.info("请输入你的 NVIDIA API Key")
        st.stop()
        
    st.session_state["messages"].append({"role": "human", "content": prompt})
    st.chat_message("human").write(prompt)

    with st.spinner("NVIDIA AI 正在思考中..."):
        # 3. Pass the NVIDIA key to the response function
        response = get_chat_response(prompt, st.session_state["memory"],
                                     nvidia_api_key)
    
    msg = {"role": "ai", "content": response}
    st.session_state["messages"].append(msg)
    st.chat_message("ai").write(response)