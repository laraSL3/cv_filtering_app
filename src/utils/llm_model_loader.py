from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAI
from langchain_openai import AzureChatOpenAI

from src.configs import gemini_settings,azure_openai_settings

class LLMModelLoader:
    def __init__(self,llm_type:str):
        self.llm = self.load_llm_model(llm_type=llm_type)
    
    def load_llm_model(self,llm_type:str):
        if llm_type == "google-gemini":
            return self._get_google_gemini_model()
        elif llm_type == "azure-openai":
            return self._get_azure_openai_model()
        else:
            raise ValueError("Invalid LLM type")

    def _get_google_gemini_model(self):
        return ChatGoogleGenerativeAI(
            model=gemini_settings.GOOGLE_MODEL_NAME,
            temperature=gemini_settings.GEMINI_TEMPERATURE,
            api_key=gemini_settings.GOOGLE_API_KEY
        )
    
    def _get_azure_openai_model(self):
        return AzureChatOpenAI(
            api_key=azure_openai_settings.AZURE_OPENAI_API_KEY,  # or your api key
            azure_deployment=azure_openai_settings.AZURE_OPENAI_MODEL,  # or your deployment
            api_version=azure_openai_settings.AZURE_OPENAI_API_VERSION,  # or your api version
            azure_endpoint=azure_openai_settings.AZURE_OPENAI_ENDPOINT,  # or your endpoint
            temperature=azure_openai_settings.AZURE_OPENAI_TEMPERATURE
        )




