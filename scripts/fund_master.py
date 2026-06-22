import requests
import pandas as pd
import os

scheme_codes = [
    125497,
    119551,
    120503,
    118632,
    119092,
    120841
]

fund_master = []

for code in scheme_codes:
    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)
    data = response.json()

    meta = data["meta"]

    fund_master.append({
        "scheme_code": meta.get("scheme_code"),
        "scheme_name": meta.get("scheme_name"),
        "fund_house": meta.get("fund_house"),
        "scheme_type": meta.get("scheme_type"),
        "scheme_category": meta.get("scheme_category")
    })

df = pd.DataFrame(fund_master)

os.makedirs("data/processed", exist_ok=True)

df.to_csv(
    "data/processed/fund_master.csv",
    index=False
)

print("\nUNIQUE FUND HOUSES")
print(df["fund_house"].unique())

print("\nUNIQUE CATEGORIES")
print(df["scheme_category"].unique())

print("\nFUND MASTER CREATED")