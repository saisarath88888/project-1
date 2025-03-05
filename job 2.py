import requests 
from bs4 import BeautifulSoup
 
url="https://www.webscraper.io/test-sites"
r=requests.get(url)
#print(r.text)
soup=BeautifulSoup(r.text,'lxml')
tag=soup.find("div", class_ ="row test-site").p
print(tag.text.strip())
#print(soup.prettify())