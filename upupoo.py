# -*- encoding=UTF-8 -*-

import requests
from bs4 import BeautifulSoup
def upupoo():
    content = requests.get('http://anime.upupoo.com').content
    soup = BeautifulSoup(content, 'html.parser')

    for div in soup.find_all('div', {'class': 'topText'}):
        print div.text.strip()
if __name__ == '__main__':
    upupoo()


