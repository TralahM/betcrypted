from selenium import webdriver
import auth

browser = webdriver.Firefox('/usr/local/bin/geckodriver')

browser.get(auth.url)

# Find login form
fbutton = browser.find_element_by_xpath('//*[@id="open_log_reg_panel"]')
fbutton.click()
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

# go to predictions
# get data table
# extract table data
# save table data csv

# upload table csv to server
