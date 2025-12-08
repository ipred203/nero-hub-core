from dotenv import load_dotenv
import os

load_dotenv()  

class Config:
    APP_NAME = os.getenv("APP_NAME", "Nero Hub")
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}@db:5432/{os.getenv('POSTGRES_DB')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
