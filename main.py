import requests
from bs4 import BeautifulSoup
import json

url = 'https://scrapingclub.com/exercise/list_basic/?page=1'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
tag = soup.find_all('h4')
price = soup.find_all('h5')

for i in range(len(price)):
    print(tag[i].text)
    print(price[i].text)
    print('_______________________')

