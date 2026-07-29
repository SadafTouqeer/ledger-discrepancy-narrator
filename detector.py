import pandas as pd

def load_data():
    erp = pd.read_csv("data/erp.csv")
    bank = pd.read_csv("data/bank.csv")
    crm = pd.read_csv("data/crm.csv")
    return erp, bank, crm

def find_duplicates(df, system_name):
    duplicates = df[df.duplicated(subset=["transaction_id"], keep=False)]
    results = []
    if not duplicates.empty:
        for txn_id in duplicates["transaction_id"].unique():
            results.append({
                "type": "DUPLICATE",
                "system": system_name,
                "transaction_id": txn_id,
                "detail": f"Transaction {txn_id} appears more than once in {system_name}"
            })
    return results

def find_amount_mismatches(erp, bank, crm):
    results = []
    merged_eb = pd.merge(erp, bank, on="transaction_id", suffixes=("_erp", "_bank"))
    for _, row in merged_eb.iterrows():
        if round(row["amount_erp"], 2) != round(row["amount_bank"], 2):
            results.append({
                "type": "AMOUNT_MISMATCH",
                "system": "ERP vs Bank",
                "transaction_id": row["transaction_id"],
                "detail": f"Transaction {row['transaction_id']}: ERP shows ${row['amount_erp']} but Bank shows ${row['amount_bank']}"
            })
    merged_ec = pd.merge(erp, crm, on="transaction_id", suffixes=("_erp", "_crm"))
    for _, row in merged_ec.iterrows():
        if round(row["amount_erp"], 2) != round(row["amount_crm"], 2):
            results.append({
                "type": "AMOUNT_MISMATCH",
                "system": "ERP vs CRM",
                "transaction_id": row["transaction_id"],
                "detail": f"Transaction {row['transaction_id']}: ERP shows ${row['amount_erp']} but CRM shows ${row['amount_crm']}"
            })
    return results

def find_missing_transactions(erp, bank, crm):
    results = []
    erp_ids = set(erp["transaction_id"].unique())
    bank_ids = set(bank["transaction_id"].unique())
    crm_ids = set(crm["transaction_id"].unique())

    in_bank_not_erp = bank_ids - erp_ids
    for txn_id in in_bank_not_erp:
        results.append({
            "type": "MISSING",
            "system": "Bank only",
            "transaction_id": txn_id,
            "detail": f"Transaction {txn_id} exists in Bank but not in ERP"
        })

    in_erp_not_crm = erp_ids - crm_ids
    for txn_id in in_erp_not_crm:
        results.append({
            "type": "MISSING",
            "system": "ERP not in CRM",
            "transaction_id": txn_id,
            "detail": f"Transaction {txn_id} exists in ERP but not in CRM"
        })

    in_crm_not_erp = crm_ids - erp_ids
    for txn_id in in_crm_not_erp:
        results.append({
            "type": "MISSING",
            "system": "CRM only",
            "transaction_id": txn_id,
            "detail": f"Transaction {txn_id} exists in CRM but not in ERP"
        })
    return results

def find_date_mismatches(erp, bank, crm):
    results = []
    merged_eb = pd.merge(erp, bank, on="transaction_id", suffixes=("_erp", "_bank"))
    for _, row in merged_eb.iterrows():
        if row["date_erp"] != row["date_bank"]:
            results.append({
                "type": "DATE_MISMATCH",
                "system": "ERP vs Bank",
                "transaction_id": row["transaction_id"],
                "detail": f"Transaction {row['transaction_id']}: ERP date {row['date_erp']} but Bank date {row['date_bank']}"
            })
    return results

def run_detection():
    erp, bank, crm = load_data()
    all_issues = []
    all_issues += find_duplicates(bank, "Bank")
    all_issues += find_amount_mismatches(erp, bank, crm)
    all_issues += find_missing_transactions(erp, bank, crm)
    all_issues += find_date_mismatches(erp, bank, crm)
    return all_issues