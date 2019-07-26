import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import auth
from time import sleep
from datetime import datetime
import csv

os.environ['MOZ_HEADLESS'] = '1'  # run on the background
browser = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')
print(browser.session_id)

browser.get('https://betegy.com/predictions')

# Find login form


def login():
    menu = browser.find_element_by_xpath('/html/body/header/a[3]/i')
    menu.click()
    sleep(.5)
    # fbutton = browser.find_element_by_xpath('//*[@id="login_tab"]')
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


login()
all_games = browser.find_elements_by_css_selector(
    ".swiper-slide.match-link-wrapper.ng-scope")
with open(str(datetime.now().date())+"-games.csv", "w") as fp:
    headers = ['day', 'date', 'time', 'hometeam', 'awayteam', 'home', 'draw', 'away',
               'gg', 'no_gg', 'ov15', 'un15', 'ov25', 'un25', 'ov35', 'un35', 'cs', 'league']
    writer = csv.writer(fp)
    writer.writerow(headers)
    print(','.join(headers))
    for i in range(len(all_games)):
        try:
            game_teams = all_games[i].find_element_by_tag_name(
                "h3").text
            game_ht, game_at = game_teams.split('vs')
            game_market = all_games[i].find_element_by_css_selector(
                ".prediction-box.ng-scope")
            game_home = game_market.find_element_by_css_selector(
                "a:nth-child(1) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)").text.split('\n')[0]
            game_draw = game_market.find_element_by_css_selector(
                "a:nth-child(1) > div:nth-child(2) > div:nth-child(1) > span:nth-child(1)").text.split('\n')[0]
            game_away = game_market.find_element_by_css_selector(
                "a:nth-child(1) > div:nth-child(3) > div:nth-child(1) > span:nth-child(1)").text.split('\n')[0]
            element = WebDriverWait(browser, 13).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '.swiper-0 > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(3)')))
            game_day_date_time = all_games[i].find_element_by_css_selector(".match-data-box").find_element_by_css_selector(
                ".game-date").text
            game_day, game_date, game_time = game_day_date_time.split(',')
            game_league = all_games[i].find_element_by_css_selector(".match-data-box").find_element_by_css_selector(
                ".league-name").text
            all_games[i].find_element_by_css_selector(
                ".clickable-area").click()
            sleep(3)
            game_correct_score = browser.find_element_by_css_selector(
                ".top-score").text
            game_total_goals = browser.find_element_by_css_selector(
                ".total-goals-predictions")
            game_btts = game_total_goals.find_element_by_css_selector(
                ".btg-card.card-container.btg-btts")
            game_gg = game_btts.find_element_by_css_selector(
                "div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)").text
            game_ng = game_btts.find_element_by_css_selector(
                "div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)").text
            game_ovun = browser.find_elements_by_css_selector(
                ".btg-card.card-container.btg-simple-over-under")
            game_ov15 = game_ovun[0].find_element_by_css_selector(
                "div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)").text
            game_un15 = game_ovun[0].find_element_by_css_selector(
                "div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)").text
            game_ov25 = game_ovun[1].find_element_by_css_selector(
                "div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)").text
            game_un25 = game_ovun[1].find_element_by_css_selector(
                "div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)").text
            game_ov35 = game_ovun[2].find_element_by_css_selector(
                "div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > span:nth-child(1)").text
            game_un35 = game_ovun[2].find_element_by_css_selector(
                "div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > span:nth-child(1)").text
            writer.writerow([game_day, game_date, game_time, game_ht, game_at, game_home, game_draw, game_away,
                             game_gg, game_ng, game_ov15, game_un15, game_ov25, game_un25, game_ov35, game_un35, game_correct_score, game_league])
            print(",".join([game_day, game_date, game_time, game_ht, game_at, game_home, game_draw, game_away,
                            game_gg, game_ng, game_ov15, game_un15, game_ov25, game_un25, game_ov35, game_un35, game_correct_score, game_league]))
            browser.get('https://betegy.com/predictions')
            WebDriverWait(browser, 13).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".swiper-slide.match-link-wrapper.ng-scope"))
            )
            all_games = browser.find_elements_by_css_selector(
                ".swiper-slide.match-link-wrapper.ng-scope")
        except:
            pass
            browser.get('https://betegy.com/predictions')
            WebDriverWait(browser, 13).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".swiper-slide.match-link-wrapper.ng-scope"))
            )
            all_games = browser.find_elements_by_css_selector(
                ".swiper-slide.match-link-wrapper.ng-scope")
