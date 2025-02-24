from langchain_google_genai import ChatGoogleGenerativeAI

from src.configs import gemini_settings

class LLMModelLoader:
    def __init__(self,llm_type:str):
        self.llm = self.load_llm_model(llm_type=llm_type)
    
    def load_llm_model(self,llm_type:str):
        if llm_type == "google-gemini":
            return self.get_google_gemini_model()
        else:
            raise ValueError("Invalid LLM type")

    def get_google_gemini_model(self):
        return ChatGoogleGenerativeAI(
            model=gemini_settings.GOOGLE_MODEL_NAME,
            temperature=gemini_settings.TEMPERATURE,
            api_key=gemini_settings.GOOGLE_API_KEY
        )




