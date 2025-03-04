from lunr import lunr
import pandas as pd
import json

df = pd.read_csv("./data/modified.csv")
docs = df.to_dict("records")

idx = lunr(ref="id", fields=df.columns, documents=docs)

serialized_idx = idx.serialize()
with open("idx.json", "w") as fd:
    json.dump(serialized_idx, fd)


print("Done ✅")
