from pydantic_settings import BaseSettings, SettingsConfigDict

class GeminiSettings(BaseSettings):
    GOOGLE_API_KEY: str
    GOOGLE_MODEL_NAME: str
    TEMPERATURE: float = 0.0

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )

gemini_settings = GeminiSettings()
# print(settings.model_dump())