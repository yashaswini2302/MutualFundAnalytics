import pandas as pd
import random
from pathlib import Path

# Load existing fund master
fund_master = pd.read_csv("data/processed/fund_master.csv")

fund_houses = [
    "SBI Mutual Fund",
    "HDFC Mutual Fund",
    "ICICI Prudential",
    "Axis Mutual Fund",
    "Nippon India",
    "Kotak Mutual Fund",
    "UTI Mutual Fund",
    "Aditya Birla Sun Life",
    "DSP Mutual Fund",
    "Canara Robeco",
    "Mirae Asset",
    "Franklin Templeton",
    "Tata Mutual Fund",
    "Invesco India",
    "Edelweiss Mutual Fund"
]

categories = [
    "Large Cap",
    "Mid Cap",
    "Small Cap",
    "Flexi Cap",
    "ELSS",
    "Debt",
    "Hybrid",
    "Index",
    "Sectoral",
    "Multi Cap"
]

scheme_types = [
    "Open Ended Schemes",
    "Open Ended Schemes",
    "Open Ended Schemes"
]

existing_codes = set(fund_master["scheme_code"])

new_rows = []

while len(new_rows) < 34:

    code = random.randint(200000, 999999)

    if code in existing_codes:
        continue

    existing_codes.add(code)

    house = random.choice(fund_houses)
    category = random.choice(categories)

    scheme_name = f"{house} {category} Fund {len(new_rows)+1}"

    new_rows.append({
        "scheme_code": code,
        "scheme_name": scheme_name,
        "fund_house": house,
        "scheme_type": random.choice(scheme_types),
        "scheme_category": category
    })

new_df = pd.DataFrame(new_rows)

updated = pd.concat([fund_master, new_df], ignore_index=True)

updated.to_csv("data/processed/fund_master.csv", index=False)

print("Total schemes:", len(updated))
print("Additional schemes generated successfully.")