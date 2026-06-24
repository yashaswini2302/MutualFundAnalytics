import pandas as pd
import os

raw_folder = "data/raw"

all_data = []

for file in os.listdir(raw_folder):

    if file.endswith(".csv") and file != "nav_history.csv":

        file_path = os.path.join(raw_folder, file)

        df = pd.read_csv(file_path)

        df["fund_name"] = file.replace(".csv", "")

        all_data.append(df)

nav_history = pd.concat(all_data, ignore_index=True)

nav_history.to_csv(
    "data/raw/nav_history.csv",
    index=False
)

print(nav_history.head())
print("nav_history.csv created successfully!")