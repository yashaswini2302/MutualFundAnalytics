import pandas as pd
import numpy as np

# Read updated fund master (40 schemes)
funds = pd.read_csv("data/processed/fund_master.csv")

# Create business-day date range
dates = pd.date_range(
    start="2022-01-01",
    end="2026-06-20",
    freq="B"
)

rows = []

np.random.seed(42)

for _, fund in funds.iterrows():

    nav = np.random.uniform(10, 100)

    for date in dates:

        change = np.random.normal(0.0005, 0.015)
        nav *= (1 + change)

        nav = max(nav, 5)

        rows.append({
            "date": date.strftime("%d-%m-%Y"),
            "nav": round(nav, 4),
            "fund_name": fund["scheme_name"]
        })

nav_df = pd.DataFrame(rows)

nav_df.to_csv(
    "data/raw/nav_history.csv",
    index=False
)

print("NAV history generated.")
print("Total records:", len(nav_df))