import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("bluestock_mf.db")

# Load fund master
funds = pd.read_csv("data/processed/fund_master.csv")

# Rename column to match schema
funds = funds.rename(columns={
    "scheme_code": "amfi_code",
    "scheme_name": "fund_name"
})

# Keep only required columns
funds = funds[
    [
        "amfi_code",
        "fund_name",
        "fund_house",
        "scheme_category",
        "scheme_type"
    ]
]

# Insert into dim_fund table
funds.to_sql(
    "dim_fund",
    conn,
    if_exists="append",
    index=False
)

print("dim_fund loaded successfully")

conn.close()