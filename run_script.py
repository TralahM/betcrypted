from selenium import webdriver
import os

os.environ['MOZ_HEADLESS'] = '1'

wd = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
wd.get("https://intoli.com/blog/running-selenium-with-headless-firefox/")
head = wd.find_element_by_xpath('//*[@id="heading-breadcrumbs"]')
if head:
    print(head.get_property('textContent').strip())
