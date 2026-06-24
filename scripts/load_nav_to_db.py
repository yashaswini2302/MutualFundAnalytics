import sqlite3
import pandas as pd

conn = sqlite3.connect("bluestock_mf.db")

nav = pd.read_csv("data/processed/nav_history_clean.csv")

# Get fund IDs
funds = pd.read_sql(
    "SELECT fund_id, fund_name FROM dim_fund",
    conn
)

nav = nav.merge(
    funds,
    on="fund_name",
    how="left"
)

nav["date_id"] = None

nav = nav[
    [
        "fund_id",
        "date_id",
        "nav"
    ]
]

nav.to_sql(
    "fact_nav",
    conn,
    if_exists="append",
    index=False
)

print("NAV history loaded")

conn.close()