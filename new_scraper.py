
from bs4 import BeautifulSoup
import requests
import time
import pandas as pd

# NASA Exoplanet URL
START_URL = "https://https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"

# Webdriver
browser = webdriver.Chrome("D:/Setup/chromedriver_win32/chromedriver.exe")
browser.get(START_URL)

time.sleep(10)

new_stars_data = []

def scrape():
    soup = BeautifulSoup(browser.page_source,"html.parser")
    bright_star_table = soup.find("table",attrs = {"class":"wikitable"})

    table_body = bright_star_table.find("tbody")
    table_rows = table_body.find_all("tr")
    for row in table_rows:
        table_cols = row.find_all("td")
        temp_list = []
        for col in table_cols:
            data = col.text.strip()
            temp_list.append(data)
        new_stars_data.append(temp_list)
scrape()

stars_data = []
for i in range(0,len(new_stars_data)):
    star_name = new_stars_data[i][1]
    distance = new_stars_data[i][3]
    mass = new_stars_data[i][5]
    radius = new_stars_data[i][6]
    lum = new_stars_data[i][7]

    new_data = [star_name,distance,mass,radius,lum]
    stars_data.append(new_data)

headers = ["star_name","distance","mass","radius","lum"]

star_df_1 = pd.DataFrame(stars_data,columns = headers)

star_df_1. to_csv("scrape_data.csv",index = True,index_label="id")

