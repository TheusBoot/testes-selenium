import time
import random
import re

lista_p = ['nha','comida','dinheiro','conhecimento','tecnologia']
aleatorio_p = random.choice(lista_p)
lista = range(0,14)
aleatorio = random.choice(lista)

from selenium import webdriver

class Google:
	def __init__(self, driver):
		self.url = 'https://www.google.com.br'
		self.driver = driver
		self.box_class = 'srg'
		self.search_bar = 'q'
		self.btn_search = 'btnK'
		self.resultado = '//*[@id="rso"]/div[1]/h'
		self.box_class_2 = 'bkWMgd'
		self.site = 'none'
		self.bct = 'TbwUpd'
		#self.url = '//*[@id="rso"]/div[1]'
		self.box = 'r'
		self.word = aleatorio_p


	def navegate(self):
		time.sleep(0.01)
		self.driver.get(self.url)
		time.sleep(0.2)


	def search(self):
		time.sleep(aleatorio)
		self.driver.find_element_by_name(self.search_bar).send_keys(self.word)
		time.sleep(aleatorio)
		self.driver.find_element_by_name(self.btn_search).click()

	def _url_pesquisa(self):
		resultado = []
		pass_ = self.driver.find_elements_by_class_name(self.bct)
		for link in pass_:
			resultado.append(link)

		self.re = resultado[1]
		self.re.click()


	def _url_pesquisa_1(self):
		passs = self.driver.find_elements_by_class_name('iUh30 bc')
		for link in passs:
			print(link.text)

	def _url_1_pesquisa_2(self):
		resultado = []
		time.sleep(0.1)
		p = self.driver.find_elements_by_class_name(self.bct)
		for link in p:
			resultado.append(link.text)
		#print(resultado)
		b = str(resultado)
		
		x = b.split()
		#z= x.replace('"',"'")
		print(x)		
		
		for i in x:
			if 'https://clubedovalor.com.br' == i:
				print(f'link encontrado{i}')

			elif 'https://www1.folha.uol.com.br' == i:
				print(f'link encontrado: {i}')

			else:
				print('nada feito!')


		#rio = str(resultado)
		#pp = rio.split('›')
		#print(pp)
		#result = re.search('https://', pp)
		#print(result.groud(0))

		#print(riop)

			
			#none = resultado.find_element_by_class_name('TbwUpd')



#for url in soup.find_all('a'):
#	print(url.get('href'))


ff = webdriver.Firefox()
g = Google(ff)
g.navegate()
g.search()
#g._url_pesquisa()	
#g._url_pesquisa_1()
g._url_1_pesquisa_2()