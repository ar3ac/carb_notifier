# config.py

import os
from dotenv import load_dotenv

load_dotenv()

REGIONE = "Lombardia"
TABELLA_REGIONE = 8


EMAIL_CONFIG = {
    "sender": os.getenv("EMAIL_SENDER"),
    "recipient": os.getenv("EMAIL_RECIPIENT"),
    "smtp_server": os.getenv("EMAIL_SMTP_SERVER", "smtp.gmail.com"),
    "port": int(os.getenv("EMAIL_SMTP_PORT", 587)),
    "password": os.getenv("EMAIL_PASSWORD"),
}