from pydantic_settings import BaseSettings, SettingsConfigDict

class GeminiSettings(BaseSettings):
    GOOGLE_API_KEY: str
    GOOGLE_MODEL_NAME: str
    GEMINI_TEMPERATURE: float = 0.0

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

class AzureOpenAISettings(BaseSettings):
    AZURE_OPENAI_API_KEY:str 
    AZURE_OPENAI_ENDPOINT:str
    AZURE_OPENAI_MODEL:str
    AZURE_OPENAI_API_VERSION_OLD:str
    AZURE_OPENAI_API_VERSION:str
    AZURE_DEPLOYMENT_NAME:str
    AZURE_OPENAI_TEMPERATURE:float = 0.0

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

gemini_settings = GeminiSettings()
azure_openai_settings = AzureOpenAISettings()
# print(settings.model_dump())