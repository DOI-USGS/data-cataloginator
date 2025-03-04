import pandas as pd
from slugify import slugify

df = pd.read_csv("./data/modified.csv")

colums = df.columns

with open("./alias_file.txt", "w") as fd:
    for i in colums:
        fd.write(f"{slugify(i)} \n")
