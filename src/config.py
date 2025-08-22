# config.py

import os
from dotenv import load_dotenv

load_dotenv()
DATA_SOURCE = os.getenv("DATA_SOURCE", "html").strip().lower()  # 'csv' | 'html'

REGIONE = os.getenv("REGIONE")

TABELLA_REGIONE = int(os.getenv("TABELLA_REGIONE"))

LOG_FILE = os.getenv("LOG_FILE")

EMAIL_CONFIG = {
    "sender": os.getenv("EMAIL_SENDER"),
    "recipient": os.getenv("EMAIL_RECIPIENT"),
    "smtp_server": os.getenv("EMAIL_SMTP_SERVER", "smtp.gmail.com"),
    "port": int(os.getenv("EMAIL_SMTP_PORT", 587)),
    "password": os.getenv("EMAIL_PASSWORD"),
    
}