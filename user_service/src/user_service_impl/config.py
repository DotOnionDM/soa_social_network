import os
from dotenv import load_dotenv

DEBUG_MODE = False


def load_debug():
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    else:
        raise RuntimeError("Config debug build failed")

    dotenv_path = os.path.join(os.getenv("MAIN_ENV_PATH"), ".env")
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)
    else:
        raise RuntimeError("Config debug build failed")


if os.getenv("POSTGRES_DB_USER_SERVICE") is None:
    DEBUG_MODE = True

if DEBUG_MODE:
    load_debug()

POSTGRES_USER_USER_SERVICE = os.getenv("POSTGRES_USER_USER_SERVICE")
POSTGRES_PASSWORD_USER_SERVICE = os.getenv("POSTGRES_PASSWORD_USER_SERVICE")
POSTGRES_DB_USER_SERVICE = os.getenv("POSTGRES_DB_USER_SERVICE")
host = "localhost:5433" if DEBUG_MODE else "postgres_db_users:5432"
DATABASE_URL = f"postgresql://{POSTGRES_USER_USER_SERVICE}:{POSTGRES_PASSWORD_USER_SERVICE}@{host}/{POSTGRES_DB_USER_SERVICE}"
