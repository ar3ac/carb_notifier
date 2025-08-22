import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent / "src"))
from src.downloader import scarica_pagina_mimit
from src.extractor import estrai_prezzi_lombardia, prezzi_to_html
from src.notifier import send_email
from src.csv_extractor import estrai_prezzi_da_csv
from src.config import REGIONE, LOG_FILE, DATA_SOURCE

import logging


def setup_logging():
    handlers = [logging.StreamHandler()]  # sempre console
    if LOG_FILE:
        handlers.append(logging.FileHandler(LOG_FILE, encoding="utf-8"))
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=handlers
    )


def main():
    setup_logging()
    logging.info("Fonte dati: %s", DATA_SOURCE)
    logging.info("Avvio carb_notifier per la regione: %s", REGIONE)

    try:
        html = scarica_pagina_mimit()
        logging.info("Pagina MIMIT scaricata con successo")

        if DATA_SOURCE == "csv":
            dati = estrai_prezzi_da_csv(REGIONE)      # lista di dict compatibile
        elif DATA_SOURCE == "html":
            html = scarica_pagina_mimit()
            dati = estrai_prezzi_lombardia(html)
        else:
            raise ValueError("DATA_SOURCE deve essere 'csv' o 'html'")

        logging.info("Prezzi estratti: %s", dati[1]) # Log della seconda voce per esempio

        html_email = prezzi_to_html(dati)
        logging.info("Tabella HTML generata")

        plain_text = "Prezzi medi carburanti. Usa un client email HTML per la versione completa."

        send_email(
            subject=f"⛽ Prezzi medi carburanti in {REGIONE}",
            body_text=plain_text,
            body_html=html_email,
        )
        logging.info("Email inviata con successo")

    except Exception as e:
        logging.exception("Errore durante l'esecuzione: %s", e)


if __name__ == "__main__":
    main()
