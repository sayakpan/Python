import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
from tqdm import tqdm

dataSource = "Dehradun.xlsx"
df = pd.read_excel(dataSource)

urls = df["website"].to_list()

phone_numbers = []

for id, row in df.iterrows():
    base_url = row["website"]
    if "https" or "http" in base_url:
        base_url.replace("https", "http")
    else:
        base_url = "http://" + base_url
    print(base_url)

# for url in tqdm(urls, bar_format="{l_bar}{bar}{r_bar}", colour="cyan"):
#     try:
#         if "https" or "http" in url:
#             url.replace("https", "http")
#         else:
#             url = "http://" + url

#         print(url)
# response = requests.get(url)
# soup = BeautifulSoup(response.content, "html.parser")
# phone_regex = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"
# phone_numbers_on_page = re.findall(phone_regex, soup.get_text())
# # print(f"{url}: {phone_numbers_on_page}")
# if len(phone_numbers_on_page) > 0:
#     phone_numbers.append(phone_numbers_on_page)
# else:
#     #     phone_numbers.append("Null")
# except:
#     print("\n\n\tWebsite not Opening : " + url + "\n")
#     phone_numbers.append("Null")
#     pass

# df["phone_number"] = phone_numbers
# df.to_excel(f"{dataSource}_with_phone_numbers.xlsx", index=False)

# print("\nExtraction Successful !!\n")
