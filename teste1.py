
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import time
import random
import re

tempo = [1.2,1.3,1.4,1.5,1.6,1.7,1.8,1.9]
temp = random.choice(tempo)

class Google:
	def __init__(self, driver):
		self.driver = driver
		self.url = 'https://www.google.com.br'
		self.search_bar = 'q'
		self.btn_search = 'btnK'
		self.btn_lucky =  'btnI'
		self.index = "r"
		self.RESULTS_LOCATOR = "//div/h3/a"

	def navigate(self):
		self.driver.get(self.url)

	def search(self, word=None):
		time.sleep(0.11)
		self.driver.find_element_by_name(self.search_bar).send_keys(word)
		time.sleep(11)
		self.driver.find_element_by_name(self.btn_search).click()
		time.sleep(2)

	def click_site(self):
		self.driver.find_element_by_class_name(self.index).click()

	def pesquisar_url(self):
		
		self.html = self.driver.page_source
		#self.html = self.driver.find_element_by_tag_name('h3') 
		#time.sleep(1)
		#self.html.get_attribute('href')
		#self.driver.find_element_by_tag_name('h1')
		#print(self.html.text)
		#http = 'https://'
		#tratamento_url = []
		html = self.driver.page_source
		google_page = bs(html, 'html.parser')
		#nav = google_page.nav
		matched_elements = google_page.find_elements_by_xpath('//a[starts-with(@href, "https://catracalivre.com.br")]')
    	if matched_elements:
    		matched_elements[0].click()






		#for link in google_page.find_all('a', attrs={'href': re.compile("^https://")}):
		#	print(link.get_attribute('href'))
		

ff = webdriver.Firefox()
g = Google(ff)
g.navigate()
g.search('google filha da puta')
time.sleep(3.8)
#g.click_site()
g.pesquisar_url()
