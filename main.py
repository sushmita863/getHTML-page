######################Get HTML page #######################
import requests
from bs4 import BeautifulSoup

#write an url from where you have to fatch the html pagr
URL="https://facebook.com/"
page=requests.get(URL)

soup=BeautifulSoup(page.content,'html.parser')
print(soup.prettify)