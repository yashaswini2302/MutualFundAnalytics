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

# Get date IDs from dim_date
dates = pd.read_sql(
    "SELECT date_id, full_date FROM dim_date",
    conn
)

# Make sure both columns have the same format
nav["date"] = pd.to_datetime(nav["date"]).dt.strftime("%Y-%m-%d")
dates["full_date"] = pd.to_datetime(dates["full_date"]).dt.strftime("%Y-%m-%d")

# Merge to get date_id
nav = nav.merge(
    dates,
    left_on="date",
    right_on="full_date",
    how="left",
    validate="many_to_one"
)

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