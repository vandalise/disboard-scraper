import requests
from bs4 import BeautifulSoup
import time
from dhooks import Webhook

for i in range(3):
    keywords = ["put", "your", "keywords", "like", "this"] 
    for keyword in keywords:
        r = requests.get(f'https://disboard.org/servers/tag/{keyword}/{i}', ).text
        servers = BeautifulSoup(r, 'html.parser').findAll('div', class_="column is-one-third-desktop is-half-tablet")
        for server in servers:
            eyedee = server.find('a', class_="button button-join is-discord").get('data-id')
            url = f"https://disboard.org/site/get-invite/{eyedee}"
            x = requests.get(url)
            tempinvite = x.text
            invite = tempinvite.replace('"', '')
            print(invite)
