# ⛽ carb_notifier

Uno script Python che estrae **i prezzi medi giornalieri dei carburanti in Lombardia** da fonti ufficiali (Ministero delle Imprese e del Made in Italy) e li invia via **email in formato HTML**.

## 🚀 Funzionalità

- Scarica automaticamente il PDF giornaliero dei prezzi
- Estrae i prezzi dei 4 carburanti principali:
  - Gasolio
  - Benzina
  - GPL
  - Metano
- Invia una **email HTML** ben formattata (con fallback in testo semplice)
- Progetto modulare, pronto per essere schedulato via `crontab` o esteso

## 📸 Anteprima output email

| Carburante | Tipo     | Prezzo (€) |
|------------|----------|------------|
| Gasolio    | SELF     | 1.641      |
| Benzina    | SELF     | 1.696      |
| GPL        | SERVITO  | 0.692      |
| Metano     | SERVITO  | 1.404      |

## 🔧 Setup

1. **Clona il repo**

```bash
git clone https://github.com/ar3ac/carb_notifier.git
cd carb_notifier
```

2. **Crea ed attiva un virtualenv**

```bash
python -m venv venv
source venv/bin/activate
```

3. **Installa le dipendenze**

```bash
pip install -r requirements.txt
```

4. **Crea il file `.env`** copiando da `.env.example`

```bash
cp .env.example .env
```

Compila i campi con i tuoi dati (usa una [App Password Gmail](https://myaccount.google.com/apppasswords)).

### `.env` (esempio)

```env
EMAIL_SENDER=tu@gmail.com
EMAIL_RECIPIENT=tu@email.it
EMAIL_PASSWORD=app-password-generata
```

5. **Esegui lo script**

```bash
python main.py
```

---

## 🛠 Tecnologie usate

- `requests`, `beautifulsoup4`, `smtplib`
- `python-dotenv` per la gestione delle credenziali
- `pdfplumber` per l'estrazione dei dati dal PDF ufficiale

## 📅 Idee future

- Scheduling automatico via `crontab`
- Integrazione Telegram bot
- Estensione ad altre regioni
- Esportazione CSV o Google Sheets

---

## 👨‍💻 Autore

Luca Marrazzo – [GitHub](https://github.com/ar3ac)

---

## 🧠 Perché questo progetto?

Questo progetto fa parte del mio percorso personale per diventare **Python Developer** con focus su **automazione e backend**.  
Obiettivo: realizzare strumenti utili, concreti e professionali da mostrare nel mio portfolio.