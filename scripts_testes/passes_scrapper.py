from selenium import webdriver
from pandas import *
import pandas
import numpy as np
import matplotlib.pyplot as plt
from sqlalchemy import *
from time import sleep

browser = webdriver.Chrome('/usr/local/bin/chromedriver')

# player_id = '1628366' # define o jogador
# season = '2018-19' # define temporada (ano completo + ano final)
# season_type = 'Regular%20Season' # período da temporada ( Regular%20Season, Playoffs)

# url = 'https://stats.nba.com/player/'+player_id+'/passes-dash/?Season='+season+'&SeasonType='+season_type
# browser.get(url)

# player_ids = []
# player_names = []
# table = browser.find_element_by_class_name('nba-stat-table__overflow')

# for line_id, lines in enumerate(table.text.split('\n')):
#     if line_id == 0:
#         column_names = lines.split(' ')[1:]
#     else:
#         if line_id % 3 == 1:
#             player_ids.append(lines)
#         if line_id % 3 == 2:
#             player_names.append(lines)

# #print(player_ids)

# print(player_names)
# browser.get(url)

total_games = 'https://stats.nba.com/search/team-game/#?sort=GAME_DATE&dir=1&Season=2018-19&SeasonType=Regular%20Season'
browser.get(total_games)


browser.find_element_by_xpath('//*[@id="custom-filters"]/div/table/tbody/tr/td[4]/button').click()
browser.find_element_by_xpath('//*[@id="streak-finder"]/div[2]/section/div/div[2]/div/div[2]/stats-run-it/button').click()
sleep(2)
for i in range(1,50):
    sleep(0.5)
    browser.find_element_by_xpath('//*[@id="stat-table"]/nba-stat-table/div[2]/div/a').click()

games_id = []
for game in range(1,2461):
    games_id.append(browser.find_element_by_xpath('//*[@id="stat-table"]/nba-stat-table/div[1]/div[1]/table/tbody/tr['+str(game)+']/td[3]/a').get_attribute('href'))
print(games_id)
