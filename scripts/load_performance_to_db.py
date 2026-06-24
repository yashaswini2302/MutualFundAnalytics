import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

performance = pd.read_csv(
    "data/processed/scheme_performance_clean.csv"
)

funds = pd.read_sql(
    "SELECT fund_id, amfi_code FROM dim_fund",
    conn
)

performance = performance.merge(
    funds,
    on="amfi_code",
    how="left"
)

performance = performance[
    [
        "fund_id",
        "return_1y",
        "return_3y",
        "return_5y",
        "expense_ratio",
        "risk_grade"
    ]
]

performance.to_sql(
    "fact_performance",
    conn,
    if_exists="append",
    index=False
)

print("Performance loaded successfully")

conn.close()