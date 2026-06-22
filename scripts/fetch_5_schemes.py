import requests
import pandas as pd
import os

scheme_codes = [
    119551,
    120503,
    118632,
    119092,
    120841
]

os.makedirs("data/raw", exist_ok=True)

for code in scheme_codes:

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    scheme_name = data["meta"]["scheme_name"]

    filename = (
        scheme_name
        .replace("/", "_")
        .replace(" ", "_")
        + ".csv"
    )

    df = pd.DataFrame(data["data"])

    df.to_csv(
        f"data/raw/{filename}",
        index=False
    )

    print(f"Saved {filename}")