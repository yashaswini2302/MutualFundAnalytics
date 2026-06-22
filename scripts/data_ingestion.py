import pandas as pd
import os

folder = "data/raw"

print("Checking datasets...\n")

for file in os.listdir(folder):

    if file.endswith(".csv"):

        filepath = os.path.join(folder, file)

        print("=" * 60)
        print("FILE:", file)

        df = pd.read_csv(filepath)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())

        print("\n")