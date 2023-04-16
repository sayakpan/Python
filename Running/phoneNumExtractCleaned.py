import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
from tqdm import tqdm

dataSource = "Dehradun"
# df = pd.read_csv(f"{dataSource}.csv")
df = pd.read_excel(f"{dataSource}.xlsx")
phone_numbers = []

urls = df["website"].tolist()

for url in tqdm(urls, bar_format="{l_bar}{bar}{r_bar}", colour="cyan"):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")

        # Regular Expression
        phone_regex = r"\b(\d{3}[-.]?\d{3}[-.]?\d{4}|\d{5}[- ]?\d{6}|(\+91|0)?[ -]?(\d{2}|[1-9]{1})[ -]?[1-9]{1}\d{9})\b|(?:(?:(?:\+|0{0,2})91(\s*[-]\s*)?)?(\d{2,5})\2{0,2}(\s*[-]\s*)?(\d{6,8}))"

        phone_numbers_on_page = re.findall(phone_regex, soup.get_text())

        # print(f"{url}: {phone_numbers_on_page}")
        if not phone_numbers_on_page:
            phone_numbers_on_page = "Null"
        phone_numbers.append(phone_numbers_on_page)

    except:
        print("\n\n\tWebsite not Opening : " + url + "\n")
        phone_numbers.append("Null")
        pass

cleaned_phone_numbers = []

for page_numbers in phone_numbers:
    cleaned_numbers = []
    for number in page_numbers:
        if isinstance(number, tuple):
            cleaned_number = "".join([str(x) for x in number if x])
            cleaned_numbers.append(cleaned_number)
        elif isinstance(number, str):
            cleaned_numbers.append(number)
    cleaned_phone_numbers.append(cleaned_numbers)

df["phone_number"] = cleaned_phone_numbers
df.to_excel(f"{dataSource}_with_phone_numbers.xlsx", index=False)
print("\nExtraction Successful !!\n")
