import requests
from bs4 import BeautifulSoup
import re
import pandas as pd
import json
data = pd.read_csv('D:\\Coding\\Code\\Python\\url.csv')
all_records = []
i = 1
for id, row in data.iterrows():
    try:
        print('\n>>>  Executed %d \n' % i)

        i = i+1
        base_url, output = row['url'], []

        print('\n%s\n' % base_url)
        title = "NULL"
        if 'https' or 'http' in base_url:
            base_url.replace('https', 'http')
        else:
            base_url = 'http://'+base_url
        url_combinations = ['contact', 'contact-us', 'contactus', 'about', 'about-us', 'aboutus', 'aboutus.html', 'contact.html', 'contact-us.html', 'contactus.html',
                            'about.html', 'about-us.html', 'aboutus.html', 'contact.php', 'contact-us.php', 'contactus.php', 'about.php', 'about-us.php', 'aboutus.php']
        all_url = []
        if base_url[-1] == '/':
            all_url.append(base_url[:-1])
            for comb in url_combinations:
                value = f"{base_url}{comb}"
                all_url.append(value)
        else:
            all_url.append(base_url)
            for comb in url_combinations:
                value = f"{base_url}/{comb}"
                all_url.append(value)
        result = {}
        for url in all_url:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")

                if soup.find('title') is not None:
                    if soup.find('title').text is not None:
                        print(soup.find('title').text)
                        title = soup.find('title').text

                links = []
                for tag in soup.find_all():
                    links.append(str(tag))

                for link in links:
                    lst = re.findall('[\w.+-]+@[\w-]+\.[\w.-]+', link)
                    output = output + lst
        result['url'] = str(base_url)
        result['title'] = str(soup.find('title').text)
        result['emails'] = str(", ".join(list(set(output))))
        all_records.append(result)
    except:
        print('\n!!!!!!!!!!!  ERROR   !!!!!!!!!!!\n')
        title = "NULL"
        pass
with open('all_email.txt', 'w') as outfile:
    json.dump(all_records, outfile)
print('\n-----Process Complete-----\n')
