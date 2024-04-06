#import required modules
from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium import webdriver
import requests

#Make a page request using the request module.
url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(url)

#Get all the tables of the page using find_all() method
tables = soup.find_all("table")

#Create an empty list
stars = []

#Get all the <tr> tags from the table
tr_tags = table_body.find_all('tr')

# For loop to take out all the <td> tags
for tr in tr_tags:
        td_tags = tr.find_all('td')
        
        # Keep all the <td> rows in the empty list made earlier
        if len(td_tags) > 0:
            stars.append([td.text.strip() for td in td_tags])
    
# Convert list into Pandas DataFrame
 df = pd.DataFrame(stars)
    
# Save into CSV
df.to_csv("stars_data.csv", index=False)