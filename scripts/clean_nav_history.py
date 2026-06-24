import pandas as pd

# Load data
df = pd.read_csv("data/raw/nav_history.csv")

# Convert date column
df["date"] = pd.to_datetime(
    df["date"],
    format="%d-%m-%Y",
    errors="coerce"
)

# Remove invalid dates
df = df.dropna(subset=["date"])

# Convert NAV to numeric
df["nav"] = pd.to_numeric(
    df["nav"],
    errors="coerce"
)

# Remove invalid NAV values
df = df[df["nav"] > 0]

# Remove duplicates
df = df.drop_duplicates()

# Sort by fund and date
df = df.sort_values(
    by=["fund_name", "date"]
)

# Save cleaned file
df.to_csv(
    "data/processed/nav_history_clean.csv",
    index=False
)

print(df.head())
print("Cleaned NAV history saved successfully!")