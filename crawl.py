from selenium import webdriver
import auth
from time import sleep
from datetime import datetime
import csv

browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')

browser.get('https://betegy.com/predictions')

# Find login form
menu = browser.find_element_by_xpath('/html/body/header/a[3]/i')
menu.click()
sleep(.5)
fbutton = browser.find_element_by_xpath('//*[@id="login_tab"]')
lgntab = browser.find_element_by_xpath('//*[@id="login_tab"]')
lgntab.click()

username = browser.find_element_by_xpath(
    '/html/body/aside[2]/div/div[2]/div[2]/div/form/div[1]/input[1]')
password = browser.find_element_by_xpath(
    '/html/body/aside[2]/div/div[2]/div[2]/div/form/div[1]/input[2]')
loginbtn = browser.find_element_by_xpath(
    '/html/body/aside[2]/div/div[2]/div[2]/div/form/div[5]/button')
# send username
username.send_keys(auth.username)
# send password
password.send_keys(auth.password)
# click submit
loginbtn.click()
clsbtn = browser.find_element_by_xpath('/html/body/aside[2]/div/a')
clsbtn.click()
sleep(18)
raw_text = browser.find_element_by_css_selector('.stacks').text
raw_text_list = raw_text.split('\n')
row0 = raw_text_list[0:28][1:]
row1 = raw_text_list[28:57][1:-1]
row2 = raw_text_list[57:86][1:-1]
row3 = raw_text_list[86:115][1:-1]
row4 = raw_text_list[115:144][1:-1]
row5 = raw_text_list[144:173][1:-1]
row6 = raw_text_list[173:202][1:-1]
row7 = raw_text_list[202:][1:-1]
rgames = row0+row1+row2+row3+row4+row5+row6+row7

ixs = [i*9 for i in range(1, 25)]
games = []
for k in ixs:
    try:
        col = rgames[k-9:k]
        col.pop(2)
        col.pop(3)
        col.pop(4)
        col[-2] = col[-2].replace(',', '_')
        games.append(col)
    except:
        pass
with open(str(datetime.now().date())+"games.csv", "w") as fp:
    headers = ['teams', 'home', 'draw', 'away', 'date', 'league']
    writer = csv.writer(fp)
    writer.writerow(headers)
    print(','.join(headers))
    for gm in games:
        writer.writerow(gm)
        print(','.join(gm))

# get data table
# extract table data
# save table data csv

# upload table csv to server
