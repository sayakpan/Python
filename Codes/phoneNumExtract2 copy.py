import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
from tqdm import tqdm

dataSource = "schools"
df = pd.read_csv(f"{dataSource}.csv")
phone_numbers = []


# def add_https(url):
#     if not url.startswith("http"):
#         return "http://" + url
#     else:
#         return url


# urls = df["website"].apply(add_https).tolist()
urls = df["website"].tolist()

for url in tqdm(urls, bar_format="{l_bar}{bar}{r_bar}", colour="cyan"):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        phone_regex = r"\b(\d{3}[-.]?\d{3}[-.]?\d{4}|\d{5}[- ]?\d{6}|(\+91|0)?[ -]?(\d{2}|[1-9]{1})[ -]?[1-9]{1}\d{9})\b|(?:(?:(?:\+|0{0,2})91(\s*[-]\s*)?)?(\d{2,5})\2{0,2}(\s*[-]\s*)?(\d{6,8}))"

        phone_numbers_on_page = re.findall(phone_regex, soup.get_text())
        # print(f"{url}: {phone_numbers_on_page}")
        if len(phone_numbers_on_page) > 0:
            phone_numbers.append(phone_numbers_on_page)
        else:
            phone_numbers.append("Null")
    except:
        print("\n\n\tWebsite not Opening : " + url + "\n")
        phone_numbers.append("Null")
        pass

df["phone_number"] = phone_numbers
df.to_excel(f"{dataSource}_with_phone_numbers.xlsx", index=False)

print("\nExtraction Successful !!\n")
