from pydantic_settings import BaseSettings
from pydantic import Field

class Settings(BaseSettings):
    tebi_endpoint: str = Field(..., env="TEBI_ENDPOINT")
    tebi_access_key: str = Field(..., env="TEBI_ACCESS_KEY")
    tebi_secret_key: str = Field(..., env="TEBI_SECRET_KEY")
    
    class Config:
        env_file = ".env"
        

settings = Settings()
