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

## 🚀 Esecuzione locale

1. Clona il repository:
   ```bash
   git clone https://github.com/ar3ac/carb_notifier.git
   cd carb_notifier
   ```

2. Crea e attiva un ambiente virtuale:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
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
TABELLA_REGIONE = 8         # Indice tabella corrispondente nella pagina HTML ufficiale (se usi l'estrazione via HTML)
```

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
│   ├── csv_extractor.py
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

### Con cron (Linux/Raspberry Pi)
Puoi programmare l’esecuzione automatica dello script ogni giorno:

```bash
crontab -e
```

E aggiungi:
```bash
30 7 * * * /usr/bin/python3 /percorso/assoluto/carb_notifier/main.py >> /var/log/carb_notifier.log 2>&1
```

### Con Windows (Operazioni pianificate)
Imposta una nuova attività e come comando usa:
```bash
python C:\percorso\carb_notifier\main.py
```

---

## 🚀 GitHub Actions (CI)

Il progetto include un workflow **GitHub Actions** che permette di simulare l’esecuzione senza inviare email.  
In questo modo chi clona il repo può testarlo direttamente su GitHub.

- File workflow: `.github/workflows/simulate_notifier.yml`
- Trigger:
  - manuale con **Run workflow** dalla tab *Actions*
  - automatico al push su `main`

### Come usarlo
1. Vai su **Actions** nel tuo repository
2. Seleziona il workflow *Simulate carb_notifier (no email)*
3. Premi **Run workflow**
4. Controlla i log per vedere i prezzi estratti e l’anteprima HTML generata

---

## 📬 Esempio email ricevuta

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

---

## 📄 Licenza

Progetto personale di [Luca Marrazzo](https://github.com/ar3ac) — libero uso per studio e portfolio.
