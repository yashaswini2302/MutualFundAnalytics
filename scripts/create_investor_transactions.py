import pandas as pd
import random

funds = pd.read_csv("data/processed/fund_master.csv")

transaction_types = ["SIP", "Lumpsum", "Redemption"]

rows = []

for i in range(1000):
    fund = funds.sample(1).iloc[0]

    rows.append({
        "transaction_id": i + 1,
        "investor_id": random.randint(10000, 99999),
        "amfi_code": fund["scheme_code"],
        "fund_name": fund["scheme_name"],
        "transaction_type": random.choice(transaction_types),
        "amount": random.randint(500, 100000),
        "transaction_date": pd.Timestamp("2025-01-01")
                            + pd.Timedelta(days=random.randint(0, 500)),
        "kyc_status": random.choice(["Verified", "Pending"])
    })

df = pd.DataFrame(rows)

df.to_csv(
    "data/raw/investor_transactions.csv",
    index=False
)

print("investor_transactions.csv created")