import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm

dataSource = "edustroke_Custom"
df = pd.read_excel(f"{dataSource}.xlsx")

urls = df["website"].tolist()

phone_regex = r"\b(\d{3}[-.]?\d{3}[-.]?\d{4}|\d{5}[- ]?\d{6}|(\+91|0)?[ -]?(\d{2}|[1-9]{1})[ -]?[1-9]{1}\d{9})\b|(?:(?:(?:\+|0{0,2})91(\s*[-]\s*)?)?(\d{2,5})\2{0,2}(\s*[-]\s*)?(\d{6,8}))"


def extract_phone_numbers(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "lxml")
        phone_numbers_on_page = re.findall(phone_regex, soup.get_text())
        if not phone_numbers_on_page:
            phone_numbers_on_page = ["Null"]
        cleaned_numbers = []
        for number in phone_numbers_on_page:
            if isinstance(number, tuple):
                cleaned_number = "".join([str(x) for x in number if x])
                cleaned_numbers.append(cleaned_number)
            elif isinstance(number, str):
                cleaned_numbers.append(number)
        return cleaned_numbers
    except:
        # print("\n\n\tWebsite not Opening : " + url + "\n")
        return ["Null"]


with ThreadPoolExecutor() as executor:
    phone_numbers = list(
        tqdm(
            executor.map(extract_phone_numbers, urls),
            total=len(urls),
            bar_format="{l_bar}{bar}{r_bar}",
            colour="red",
        )
    )

df["phone_number"] = phone_numbers
df.to_excel(f"{dataSource}_with_phone_numbers.xlsx", index=False)
print("\nExtraction Successful !!\n")
