import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent / "src"))

from src.downloader import scarica_pagina_mimit
from src.extractor import estrai_prezzi_lombardia, prezzi_to_html
from src.notifier import send_email

if __name__ == "__main__":
    html = scarica_pagina_mimit()
    dati = estrai_prezzi_lombardia(html)
    html_email = prezzi_to_html(dati)

    plain_text = "Prezzi medi carburanti. Usa un client email HTML per la versione completa."

    send_email(
        subject="⛽ Prezzi medi carburanti in Lombardia",
        body_text=plain_text,
        body_html=html_email
    )
