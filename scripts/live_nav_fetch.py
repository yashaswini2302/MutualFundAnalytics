import requests
import pandas as pd
import os

url = "https://api.mfapi.in/mf/125497"

response = requests.get(url)

data = response.json()

# Create folder if not exists
os.makedirs("data/raw", exist_ok=True)

# NAV history
nav_df = pd.DataFrame(data["data"])

# Save CSV
nav_df.to_csv(
    "data/raw/sbi_small_cap_nav.csv",
    index=False
)

print(nav_df.head())
print("CSV Saved Successfully!")