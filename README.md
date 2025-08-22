
# ⛽️ Carb Notifier

Uno strumento automatizzato per estrarre i **prezzi medi giornalieri dei carburanti** in Italia dal sito ufficiale del [MIMIT](https://dgsaie.mise.gov.it/prezzi-medi-giornalieri-carburanti) e inviarli via **email in formato HTML**.

---

## 📌 Funzionalità

- Consulta i prezzi medi aggiornati del carburante
- Estrae i dati della regione configurata (es. Lombardia)
- Genera una **tabella HTML** pulita e leggibile con i prezzi di: Gasolio, Benzina, GPL, Metano
- Invia l'email automaticamente al destinatario configurato

---

## 📦 Requisiti

- Python 3.10+
- Account email SMTP (es. Gmail)
- File `.env` per salvare le credenziali in modo sicuro

---

## 🚀 Esecuzione

1. Clona il repository
2. Crea e attiva un ambiente virtuale:

```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

3. Installa le dipendenze:
```bash
pip install -r requirements.txt
```

4. Crea un file `.env` partendo da `.env.example` e compila i campi richiesti

5. Avvia lo script:
```bash
python main.py
```

Riceverai un'email con la tabella HTML dei prezzi medi dei carburanti.

---

## 🔧 Configurazione

Nel file `src/config.py` puoi impostare:

```python
REGIONE = "Lombardia"       # Regione da estrarre
TABELLA_REGIONE = 8         # Indice della tabella corrispondente alla regione nella pagina HTML ufficiale MIMIT
```

Assicurati che il valore `TABELLA_REGIONE` corrisponda alla tabella giusta del PDF ufficiale del MIMIT.

Puoi anche modificare l’oggetto e i destinatari email nel dizionario `EMAIL_CONFIG` all’interno dello stesso file.

---

## 📂 Struttura progetto

```
carb_notifier/
├── main.py
├── requirements.txt
├── .env.example
├── README.md
├── src/
│   ├── config.py
│   ├── downloader.py
│   ├── extractor.py
│   ├── notifier.py
│   └── __init__.py
└── tests/
    └── __init__.py
```

---

## 🔒 Sicurezza

- Le credenziali sono gestite tramite `.env`
- Il file `.env.example` ti aiuta a preparare un `.env` valido


---
## ⏱️ Automazione

Puoi programmare l’esecuzione automatica dello script ogni giorno usando cron (Linux/macOS) o Operazioni pianificate (Windows).

### Esempio con cron (Linux/Raspberry Pi)
Apri il crontab:
```bash

crontab -e

```

Aggiungi una riga come questa per far girare lo script ogni giorno alle 7:30:
```bash

30 7 * * * /usr/bin/python3 /percorso/assoluto/carb_notifier/main.py >> /var/log/carb_notifier.log 2>&1

```
30 7 * * * → orario (7:30 del mattino)

/usr/bin/python3 → percorso al tuo interprete Python

/percorso/assoluto/carb_notifier/main.py → percorso al tuo script

>> /var/log/carb_notifier.log 2>&1 → salva i log (utile per debug)

### Windows (Operazioni pianificate)

Apri Task Scheduler

Crea una nuova attività pianificata

Imposta l’orario desiderato

Comando da eseguire:
```bash

python C:\percorso\carb_notifier\main.py

```
---

## 📬 Esempio email ricevuta

L’email ricevuta conterrà una tabella simile a questa, in formato HTML:

| Carburante | Tipo     | Prezzo |
|------------|----------|--------|
| Gasolio    | SELF     | 1.641  |
| Benzina    | SELF     | 1.696  |
| GPL        | SERVITO  | 0.692  |
| Metano     | SERVITO  | 1.404  |

---

## 🛠 Possibili estensioni future

- Supporto a più regioni
- Invio su Telegram
- Salvataggio storico in CSV o database
- Scheduler automatico (es. `cron`)

---

## 📄 Licenza

Progetto personale di [Luca Marrazzo](https://github.com/ar3ac) — libero uso per studio e portfolio.
