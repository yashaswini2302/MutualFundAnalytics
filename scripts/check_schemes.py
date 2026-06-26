import pandas as pd
import glob
import os

csv_files = glob.glob("data/raw/*.csv")

funds = []

for file in csv_files:
    if os.path.basename(file) not in [
        "nav_history.csv",
        "investor_transactions.csv",
        "scheme_performance.csv"
    ]:
        funds.append(os.path.basename(file))

print("Total scheme files:", len(funds))

print("\nScheme names:\n")
for i, fund in enumerate(sorted(funds), 1):
    print(f"{i}. {fund}")