import pandas as pd
import requests
import re
from bs4 import BeautifulSoup
from tqdm import tqdm

dataSource = "schools"
df = pd.read_csv(f"{dataSource}.csv")
phone_numbers = []


urls = df["website"].tolist()

url_combinations = [
    "contact",
    "contact-us",
    "contactus",
    "about",
    "about-us",
    "aboutus",
    "aboutus.html",
    "contact.html",
    "contact-us.html",
    "contactus.html",
    "about.html",
    "about-us.html",
    "aboutus.html",
    "contact.php",
    "contact-us.php",
    "contactus.php",
    "about.php",
    "about-us.php",
    "aboutus.php",
]

all_possible_urls = []



for url in tqdm(urls, bar_format="{l_bar}{bar}{r_bar}", colour="cyan"):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, "html.parser")
        phone_regex = r"\b\d{3}[-.]?\d{3}[-.]?\d{4}\b"
        phone_numbers_on_page = re.findall(phone_regex, soup.get_text())
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
