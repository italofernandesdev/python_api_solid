from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    MYSQL_USER: str = "root"
    MYSQL_PASSWORD: str = "root6Beer"
    MYSQL_HOST: str = "localhost"
    MYSQL_PORT: int = 3306
    MYSQL_DB: str = "test_userdb"
    SECRET_KEY: str = "<c{q:k3b405TN[?"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        env_file = ".env"

settings = Settings()
