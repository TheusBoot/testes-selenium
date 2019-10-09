#from bs4 import BeautifulSoup
#import requests
#import re

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup as bsoup

ffox = webdriver.Firefox()
time.sleep(0.9)
ffox.get('https://www.google.com.br')
pchave = 'dinheiro'

time.sleep(1)
ffox.find_element_by_css_selector('input[title="Pesquisar"]').send_keys(pchave)
time.sleep(9)
ffox.find_element_by_css_selector('input[title="Pesquisar"]').send_keys(Keys.ENTER)
time.sleep(2.7)

html_atual = ffox.page_source
sopa = bsoup(html_atual, 'html.parser')
resultados = sopa.find_all(attrs={"class": "r"})

for i in resultados:
    print(i.find('h3').text)
    print(i.find('a').get('href'))







