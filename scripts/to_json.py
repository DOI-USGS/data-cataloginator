"""Script to convert tabluar data to individual JSON files

Usage:
    python to_json.py

Changes:
    Update the variable CSV_DATA_FILE to point to the CSV file

"""

import pandas as pd
import uuid

CSV_DATA_FILE = "./example/statements-2020-2021.csv"

df = pd.read_csv(CSV_DATA_FILE)
df["id"] = [uuid.uuid4() for _ in range(len(df))]

docs = df.to_dict("records")

# Save ids
df.to_csv("./data/modified.csv", index=False)

# Single JSON file
df.to_json("./data/records.json", orient="records", default_handler=str)


# Multiple JSON files
def gen_individual_json(df):
    for i, row in df.iterrows():
        row.to_json(
            f"./data/individual_json/{row.id}.json",
            orient="columns",
            default_handler=str,
        )


gen_individual_json(df)

print("Done ✅")
