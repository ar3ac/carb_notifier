from bs4 import BeautifulSoup
from typing import List, Dict
from downloader import scarica_pagina_mimit


def estrai_prezzi_lombardia(html: str) -> List[Dict[str, str]]:
    soup = BeautifulSoup(html, "html.parser")
    tabelle = soup.find_all("table")

    if len(tabelle) < 9:
        raise Exception("⚠️ Tabella Lombardia non trovata.")

    tabella = tabelle[8]  # Lombardia
    righe = tabella.find_all("tr")

    risultati = []
    for riga in righe:
        celle_th = riga.find_all("th")
        celle_td = riga.find_all("td")

        # Cerca righe con 1 <th> + 2 <td>
        if len(celle_th) == 1 and len(celle_td) == 2:
            carburante = celle_th[0].text.strip()
            tipo = celle_td[0].text.strip()
            prezzo = celle_td[1].text.strip()

            risultati.append({
                "carburante": carburante,
                "tipo": tipo,
                "prezzo": prezzo
            })

    return risultati


def prezzi_to_html(dati: List[Dict[str, str]]) -> str:
    html = """
    <html>
    <head>
        <style>
            body { font-family: Arial, sans-serif; }
            table { border-collapse: collapse; width: 100%; max-width: 400px; margin-top: 20px; }
            th, td { border: 1px solid #ccc; padding: 8px; text-align: center; }
            th { background-color: #f0f8ff; }
        </style>
    </head>
    <body>
        <h2>⛽ Prezzi medi dei carburanti in Lombardia</h2>
        <table>
            <thead>
                <tr>
                    <th>Carburante</th>
                    <th>Tipo</th>
                    <th>Prezzo (€)</th>
                </tr>
            </thead>
            <tbody>
    """

    for voce in dati:
        html += f"""
        <tr>
            <td>{voce['carburante']}</td>
            <td>{voce['tipo']}</td>
            <td>{voce['prezzo']}</td>
        </tr>
        """

    html += """
            </tbody>
        </table>
    </body>
    </html>
    """
    return html




if __name__ == "__main__":
    html = scarica_pagina_mimit()
    dati = estrai_prezzi_lombardia(html)
    for voce in dati:
        print(voce)
