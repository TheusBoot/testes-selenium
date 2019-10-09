from selenium import webdriver

search_query = input("Enter the search query")
search_query = search_query.replace(' ', '+') #structuring our search query for search url.
#executable_path = "/path/to/chromedriver"
#browser = webdriver.Chrome(executable_path=executable_path)
browser = webdriver.Firefox()

for i in range(20):
    browser.get("https://www.google.com/search?q=" + search_query + "&start=" + str(10 * i))
    matched_elements = browser.find_elements_by_xpath('//a[starts-with(@href, "https://www.thetaranights.com")]')
    if matched_elements:
        matched_elements[0].click()
        break


from bs4 import BeautifulSoup
import urllib.request

url_base:str = 'https://pt.wikipedia.org/wiki/Special:Search?search=parado+na+esquina&go=Go&ns0=1'

sauce = urllib.request.urlopen(f'{url_base}').read()
soup = BeautifulSoup(sauce, 'html.parser')

#for paragraph in soup.find_all('a'):

#soup.sorce
for url in soup.find_all('a'):
	print(url.get('href'))

#body = soup.body
#for paragraph in body.find_all('p'):
#	print(paragraph.text)
