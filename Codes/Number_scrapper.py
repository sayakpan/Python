import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
from tqdm import tqdm

dataSource = "schools"
data = pd.read_csv(f"{dataSource}.csv")
all_records = []
phone_numbers = []

for id, row in data.iterrows():
    try:
        base_url, output = row["website"], []

        url_combinations = [
            "contact",
            "contact-us",
            "contactus",
            "about",
            "about-us",
            "aboutus",
        ]

        all_url = []

        if base_url[-1] == "/":
            all_url.append(base_url[:-1])
            for comb in url_combinations:
                value = f"{base_url}{comb}"
                all_url.append(value)
        else:
            all_url.append(base_url)
            for comb in url_combinations:
                value = f"{base_url}/{comb}"
                all_url.append(value)

        for url in tqdm(all_url, bar_format="{l_bar}{bar}{r_bar}", colour="cyan"):
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

            print(phone_numbers)

        all_records.append(phone_numbers)
        print(all_records)
    except:
        print("\n!!!!!!!!!!!  ERROR   !!!!!!!!!!!\n")
        pass

    # finally:
    #     data["phone_number"] = all_records
    #     data.to_excel(f"{dataSource}_with_phone_numbers.xlsx", index=False)
    #     print("\nExtraction Successful !!\n")
