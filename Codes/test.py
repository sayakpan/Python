import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import json

data = pd.read_csv("D:\\Coding\\Code\\Python\\url-all.csv")
all_status_code = []
all_url = []

for id, row in data.iterrows():
    base_url = row["url"]
    all_url.append(base_url)

for url in all_url:
    response = requests.head(url)
    status_code = response.status_code
    all_status_code.append(status_code)
    print(url)
    print(status_code)

data = {"url": all_url, "status_code": all_status_code}
df = pd.DataFrame(data)
df.to_csv("status_code.csv", index=False, header=True)

print("\n-----Process Complete-----\n")
