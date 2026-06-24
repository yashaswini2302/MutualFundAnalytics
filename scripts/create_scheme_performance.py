import pandas as pd
import random

funds = pd.read_csv("data/processed/fund_master.csv")

rows = []

for _, fund in funds.iterrows():
    rows.append({
        "amfi_code": fund["scheme_code"],
        "fund_name": fund["scheme_name"],
        "return_1y": round(random.uniform(-5, 35), 2),
        "return_3y": round(random.uniform(0, 25), 2),
        "return_5y": round(random.uniform(5, 20), 2),
        "expense_ratio": round(random.uniform(0.1, 2.5), 2),
        "risk_grade": random.choice([
            "Low",
            "Moderate",
            "High",
            "Very High"
        ])
    })

df = pd.DataFrame(rows)

df.to_csv(
    "data/raw/scheme_performance.csv",
    index=False
)

print("scheme_performance.csv created")