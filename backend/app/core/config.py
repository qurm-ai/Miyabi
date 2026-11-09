from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )

    # Project Information
    PROJECT_NAME: str = "QuizAI"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = "development"

    # Database (PostgreSQL)
    POSTGRES_SERVER: str = "localhost"
    POSTGRES_PORT: int = 5432
    POSTGRES_USER: str = "postgres"
    POSTGRES_PASSWORD: str = ""
    POSTGRES_DB: str = "quizai_db"

    # Keycloak OIDC
    KEYCLOAK_SERVER_URL: str = "http://localhost:8080"
    KEYCLOAK_REALM: str = "quizai"
    KEYCLOAK_CLIENT_ID: str = "quizai-backend"
    KEYCLOAK_CLIENT_SECRET: str = ""

    # LLM (Ollama)
    LLM_PROVIDER: str = "fake"
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "llama3"


settings = Settings()

