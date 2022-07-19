import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import csv
import os

# Setup Selenium for BS4 scraping
driver = webdriver.Chrome(R'C:\Users\rcman\Downloads\Compressed\chromedriver_win32\chromedriver')

driver.get(R"https://www.lastepochtools.com/db/category/swords/items")


heights = []
counter = 0
for i in range(1,300):
    bg = driver.find_element_by_css_selector('body')
    time.sleep(0.1)
    bg.send_keys(Keys.END)
    heights.append(driver.execute_script("return document.body.scrollHeight"))
    try :
        bottom = heights[i-16]
    except:
        pass
    if i%16 ==0:
        new_bottom = heights[i-1]
        if bottom == new_bottom:
            break

# BS4 scraping:
soup = BeautifulSoup(driver.page_source, 'html.parser')

weapon_list = []

for x in soup.find_all('div', attrs = {'class':'item-description'}):
    weapon = {}
    w_name = x.contents[0].find_all('a', attrs = {'class':'item-name rarity0'})
    if w_name == []:
        pass
    else:
        weapon['type'] = x.contents[1].text
        weapon['name'] = w_name[0].text
        weapon_list.append(weapon)

print(weapon_list)

# CSV File
filename = 'last_epoch_data.csv'

if os.path.exists(filename):
    os.remove(filename)
    print("Deleted: {}".format(filename))
else:
    pass

with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['type', 'name'])
    w.writeheader()
    for weapon in weapon_list:
        w.writerow(weapon)

driver.close()