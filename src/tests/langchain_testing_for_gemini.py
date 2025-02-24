from langchain_google_genai import ChatGoogleGenerativeAI

from src.configs import gemini_settings

llm = ChatGoogleGenerativeAI(
    model=gemini_settings.GOOGLE_MODEL_NAME,
    temperature=gemini_settings.TEMPERATURE,
    api_key=gemini_settings.GOOGLE_API_KEY
)

messages = [
    (
        "system",
        "You are a helpful assistant.",
    ),
    ("human", "tell me about sri lanka in 5 sentences"),
]
ai_msg = llm.invoke(messages)
print(ai_msg)