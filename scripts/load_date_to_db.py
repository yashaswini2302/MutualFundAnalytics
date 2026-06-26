import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("bluestock_mf.db")

# Read NAV history
nav = pd.read_csv("data/processed/nav_history_clean.csv")

# Get unique dates
dates = pd.DataFrame({
    "full_date": sorted(nav["date"].unique())
})

# Convert to datetime
dates["full_date"] = pd.to_datetime(dates["full_date"])

# Create date columns
dates["year"] = dates["full_date"].dt.year
dates["month"] = dates["full_date"].dt.month
dates["day"] = dates["full_date"].dt.day

# Rename for database
dates = dates.rename(columns={"full_date": "full_date"})

# Save to database
dates.to_sql(
    "dim_date",
    conn,
    if_exists="replace",
    index_label="date_id"
)

print("Date dimension loaded successfully.")
print("Rows:", len(dates))

conn.close()