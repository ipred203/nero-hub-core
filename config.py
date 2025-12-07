from dotenv import load_dotenv
import os

load_dotenv()

class Config:
    app_name = os.getenv("APP_NAME", "nero hub")