# scripts/generate_latest.py
import os
import json
import datetime as dt
import csv
import statistics as stats
import pathlib


def read_rows_from_csv(path):
    rows = []
    if not os.path.exists(path):
        return rows
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def main():
    # Se il tuo scraper salva un CSV, indica il percorso qui (o via env CARB_CSV)
    csv_path = os.environ.get("CARB_CSV", "data/latest.csv")
    rows = read_rows_from_csv(csv_path)

    out = {
        "generated_at": dt.datetime.utcnow().isoformat() + "Z",
        "source": "MIMIT (scrape via carb_notifier)",
        "count": len(rows),
    }

    # Se c'è il CSV, prova a calcolare medie per carburante
    if rows:
        by_fuel = {}
        for r in rows:
            fuel = r.get("fuel") or r.get(
                "carburante") or r.get("product") or "unknown"
            price = r.get("price") or r.get("prezzo") or r.get("Prezzo")
            try:
                p = float(str(price).replace(",", "."))
            except Exception:
                continue
            by_fuel.setdefault(fuel, []).append(p)
        out["avg_price_by_fuel"] = {
            k: round(sum(v) / len(v), 3) for k, v in by_fuel.items() if v
        }
    else:
        out["note"] = "CSV non trovato: heartbeat per test (aggiungi lo step che genera il CSV)."

    docs = pathlib.Path("docs")
    docs.mkdir(parents=True, exist_ok=True)
    with open(docs / "latest.json", "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print("Scritto docs/latest.json")


if __name__ == "__main__":
    main()
