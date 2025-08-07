from config import EMAIL_CONFIG
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib


def send_email(subject: str, body_text: str, body_html: str = None) -> None:
    """
    Invia un'email con oggetto `subject`, testo semplice `body_text` e opzionale `body_html`.
    """
    msg = MIMEMultipart('alternative')
    msg['From'] = EMAIL_CONFIG['sender']
    msg['To'] = EMAIL_CONFIG['recipient']
    msg['Subject'] = subject

    # Parte testo (obbligatoria)
    part1 = MIMEText(body_text, 'plain')
    msg.attach(part1)

    # Parte HTML (opzionale)
    if body_html:
        part2 = MIMEText(body_html, 'html')
        msg.attach(part2)

    # Invio via SMTP
    with smtplib.SMTP(EMAIL_CONFIG['smtp_server'], EMAIL_CONFIG['port']) as server:
        server.starttls()
        server.login(EMAIL_CONFIG['sender'], EMAIL_CONFIG['password'])
        server.send_message(msg)

    print("✅ Email inviata con successo.")
