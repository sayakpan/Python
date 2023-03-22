import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

# read the CSV file into a pandas data frame
df = pd.read_csv("schools.csv")

# extract the website URLs from the data frame and store them in a list
urls = df["website"].tolist()

# create an empty list to store the "about" data
about_data = []

# loop through the URLs and extract the "about" data
for url in tqdm(urls, desc="Extracting About Data"):
    # use requests library to get the HTML content of the website
    response = requests.get(url)
    # use BeautifulSoup to parse the HTML content
    soup = BeautifulSoup(response.content, "lxml")
    # use CSS selectors to extract the "about" data
    about = soup.select_one("div.about")
    # check if about is None, i.e., the selector did not match any element
    if about is not None:
        # append the "about" data to the list
        about_data.append(about.get_text().strip())
    else:
        # append None to the list to indicate that no about data was found
        about_data.append(None)

# create a new column in the data frame to store the "about" data
df["about"] = about_data

# write the updated data frame to a new CSV file
df.to_csv("schools_with_about.csv", index=False)
