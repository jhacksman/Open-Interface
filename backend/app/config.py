from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """Application settings."""
    APP_NAME: str = "Molmo Browser Test"
    DEBUG: bool = True
    MODEL_PATH: str = "/path/to/molmo"  # This will be configured during deployment
    
    class Config:
        env_file = ".env"

settings = Settings()
