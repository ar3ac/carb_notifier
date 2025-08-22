# src/csv_extractor.py
import csv
import io
import requests

MIMIT_CSV_URL = "https://www.mimit.gov.it/images/stories/carburanti/MediaRegionaleStradale.csv"

def _slice_from_header(text: str) -> str:
    """Ritorna la porzione di testo a partire dalla riga che contiene l'header CSV."""
    lines = text.splitlines()
    for i, line in enumerate(lines):
        # header atteso (case-insensitive) con i 4 campi
        if all(k in line.upper() for k in ("REGIONE", "TIPOLOGIA", "EROGAZIONE", "PREZZO MEDIO")):
            return "\n".join(lines[i:])
    # se non trovato, restituisci tutto (meglio che fallire subito)
    return text

def estrai_prezzi_da_csv(regione: str) -> list[dict]:
    """
    Ritorna una lista di dict compatibile con extractor.py:
    [{"carburante": <str>, "tipo": <str>, "prezzo": <str>}, ...]
    """
    resp = requests.get(MIMIT_CSV_URL, timeout=20)
    resp.raise_for_status()

    # decoding tollerante
    for enc in ("utf-8", "latin-1", "cp1252"):
        try:
            text = resp.content.decode(enc)
            break
        except UnicodeDecodeError:
            continue

    text = _slice_from_header(text)
    reader = csv.DictReader(io.StringIO(text), delimiter=";")

    regione_norm = regione.strip().lower()
    risultati: list[dict] = []

    for row in reader:
        # normalizza chiavi in modo difensivo (alcuni CSV hanno spazi extra)
        regione_val = (row.get("REGIONE") or row.get("Regione") or "").strip().lower()
        if regione_val != regione_norm:
            continue

        carburante = (row.get("TIPOLOGIA") or row.get("Tipologia") or "").strip()
        tipo = (row.get("EROGAZIONE") or row.get("Erogazione") or "").strip()   # "SELF"/"SERVITO" o vuoto
        prezzo = (row.get("PREZZO MEDIO") or row.get("Prezzo medio") or "").strip()  # lascio stringa (virgola/punto come da sorgente)

        if not carburante or not prezzo:
            continue

        risultati.append({
            "carburante": carburante,  # es. "Benzina", "Gasolio", "GPL", "Metano"
            "tipo": tipo,              # "SELF" | "SERVITO" | ""
            "prezzo": prezzo,          # stringa, compatibile con prezzi_to_html()
        })

    return risultati

if __name__ == "__main__":
    print(estrai_prezzi_da_csv("Lombardia"))
