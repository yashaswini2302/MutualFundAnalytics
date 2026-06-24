import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

# Load transactions
transactions = pd.read_csv(
    "data/processed/investor_transactions_clean.csv"
)

# Get fund mapping
funds = pd.read_sql(
    "SELECT fund_id, amfi_code FROM dim_fund",
    conn
)

# Convert amfi_code -> fund_id
transactions = transactions.merge(
    funds,
    on="amfi_code",
    how="left"
)

# Keep only columns required by fact_transactions
transactions = transactions[
    [
        "transaction_id",
        "fund_id",
        "investor_id",
        "transaction_type",
        "amount",
        "transaction_date",
        "kyc_status"
    ]
]

transactions.to_sql(
    "fact_transactions",
    conn,
    if_exists="append",
    index=False
)

print("Transactions loaded successfully")

conn.close()