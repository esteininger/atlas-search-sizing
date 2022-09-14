import pandas as pd
import re
import math

# /_cat/indices?bytes=b

headers = ["health", "status", "index", "uuid", "pri", "rep", "docs.count", "docs.deleted", "store.size", "pri.store.size.bytes"]

file_path = "_cat-indexes.txt"
df = pd.read_csv(file_path, header=None, delimiter=r"\s+")

indexes = []
sum = 0
for i, row in df.iterrows():
    # we don't care if there are no docs in the index
    if row[6] == 0:
        continue

    # accumulate
    sum += row[6]

    o = {
        headers[6]:row[6],
        headers[9]:row[9]
    }
    indexes.append(o)

print(sum / (10 * (10 ** 6)))
