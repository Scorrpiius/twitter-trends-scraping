import requests
from bs4 import BeautifulSoup

r = requests.get('https://trends24.in/france/')

soup = BeautifulSoup(r.content, 'html.parser')

s = soup.find_all('a', class_='trend-link')
for link in s :
    print(link.getText())