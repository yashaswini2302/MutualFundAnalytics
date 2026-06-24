import pandas as pd

df = pd.read_csv("data/raw/scheme_performance.csv")

# Convert returns to numeric
for col in ["return_1y", "return_3y", "return_5y"]:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove invalid return values
df = df.dropna(subset=["return_1y", "return_3y", "return_5y"])

# Expense ratio validation (task requirement: 0.1% - 2.5%)
df["expense_ratio"] = pd.to_numeric(
    df["expense_ratio"],
    errors="coerce"
)

df = df[
    (df["expense_ratio"] >= 0.1) &
    (df["expense_ratio"] <= 2.5)
]

# Standardize risk grades
valid_risk = [
    "Low",
    "Moderate",
    "High",
    "Very High"
]

df = df[df["risk_grade"].isin(valid_risk)]

# Remove duplicates
df = df.drop_duplicates()

# Save cleaned dataset
df.to_csv(
    "data/processed/scheme_performance_clean.csv",
    index=False
)

print("Scheme performance cleaned successfully")