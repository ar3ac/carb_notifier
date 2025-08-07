import requests
from bs4 import BeautifulSoup


def scarica_pagina_mimit():
    url = "https://www.mimit.gov.it/it/prezzo-medio-carburanti/regioni"
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.text


if __name__ == "__main__":
    html = scarica_pagina_mimit()
    print(html[:1000])  # Stampa i primi 1000 caratteri per test

