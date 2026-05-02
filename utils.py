from langchain_nvidia_ai_endpoints import ChatNVIDIA
from langchain.chains import ConversationChain

def get_chat_response(prompt, memory, api_key):
    model = ChatNVIDIA(
        model="meta/llama-3.3-70b-instruct",
        api_key=api_key,
        base_url="https://integrate.api.nvidia.com/v1"
    )
    chain = ConversationChain(llm=model, memory=memory)
    
    response = chain.invoke({"input": prompt})
    return response["response"]