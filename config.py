# config.py
from dotenv import load_dotenv
import os

load_dotenv()  # читает .env в корне

class Config:
    APP_NAME = os.getenv("APP_NAME", "Nero Hub")
