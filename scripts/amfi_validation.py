import pandas as pd

df = pd.read_csv("data/processed/fund_master.csv")

print("AMFI SCHEME CODES")

for code in df["scheme_code"]:
    print(f"{code} -> NAV data available")