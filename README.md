# Ledger Discrepancy Narrator

AI-powered financial reconciliation tool that automatically detects discrepancies across ERP, Bank, and CRM systems and explains them in plain English using Generative AI.

---

## What It Does

Finance teams waste hours every month manually comparing transaction logs across multiple systems. This tool automates the entire process:

1. Ingests transaction data from ERP, Bank, and CRM CSV files
2. Detects discrepancies automatically (duplicates, amount mismatches, missing transactions, date gaps)
3. Explains each discrepancy in plain English using Generative AI
4. Generates a professional audit-ready Word document report

---

## Demo Output

```
============================================================
   LEDGER DISCREPANCY NARRATOR
   Financial Reconciliation Tool | 2026
============================================================

[1/3] Running discrepancy detection...

Found 5 discrepancies:
  -> [DUPLICATE] TXN003: Transaction TXN003 appears more than once in Bank
  -> [AMOUNT_MISMATCH] TXN008: ERP shows $1750.0 but Bank shows $1755.0
  -> [MISSING] TXN003: Transaction TXN003 exists in ERP but not in CRM
  -> [MISSING] TXN009: Transaction TXN009 exists in CRM but not in ERP
  -> [DATE_MISMATCH] TXN005: ERP date 2026-06-05 but Bank date 2026-06-07

[2/3] Generating AI narratives...
[3/3] Generating report...

Done! Report generated successfully!
============================================================
```

---

## Project Structure

```
ledger_discrepancy_narrator/
├── data/
│   ├── erp.csv          <- ERP system transactions
│   ├── bank.csv         <- Bank feed transactions
│   └── crm.csv          <- CRM/billing transactions
├── reports/             <- Generated Word reports saved here
├── main.py              <- Pipeline orchestrator
├── detector.py          <- Discrepancy detection engine
├── narrator.py          <- AI narrative generator
├── reporter.py          <- Word document report generator
└── requirements.txt     <- Python dependencies
```

---

## Discrepancy Types Detected

| Type | Description |
|------|-------------|
| DUPLICATE | Same transaction appears more than once in a system |
| AMOUNT_MISMATCH | Same transaction has different amounts across systems |
| MISSING | Transaction exists in one system but not another |
| DATE_MISMATCH | Same transaction has different dates across systems |

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.10 | Core language |
| Pandas | Data ingestion and matching |
| OpenRouter API | Free AI narrative generation |
| python-docx | Word document generation |
| colorama | Terminal color output |

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/SadafTouqeer/ledger-discrepancy-narrator.git
cd ledger-discrepancy-narrator
```

2. Install dependencies:

```bash
pip install pandas python-docx openai colorama
```

3. Add your OpenRouter API key in narrator.py:

```python
api_key="YOUR_OPENROUTER_API_KEY_HERE"
```

Get a free key at: https://openrouter.ai

---

## Usage

```bash
python main.py
```

The tool will automatically read CSV files from the data/ folder, detect all discrepancies, generate AI explanations, and save a Word report in the reports/ folder.

---

## Sample Data Format

Your CSV files should follow this schema:

```
transaction_id,date,amount,type,counterparty,status
TXN001,2026-06-01,5000.00,invoice,ABC Corp,posted
TXN002,2026-06-02,1200.00,invoice,XYZ Ltd,posted
```

---

## Report Output

The generated Word document includes:

- Executive Summary with discrepancy type counts
- Detailed findings for each discrepancy
- AI-generated plain-English root-cause explanation
- Linked source transaction evidence
- Professional formatting suitable for audit workpapers

---

## Author

Sadaf Touqeer
Generative AI Internship Project | 2026

---

## License

MIT License - free to use and modify.
