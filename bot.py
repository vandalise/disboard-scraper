import requests
from bs4 import BeautifulSoup
import time
from dhooks import Webhook

#hook = Webhook("input webhook here")

urls = []
while True:
    keywords = ["put", "your", "keywords", "like", "this"] 
    for keyword in keywords:
        r = requests.get(f'https://disboard.org/servers/tag/{keyword}/1', ).text
        if "Too Many Requests" in r:
            print("Ratelimited")
        else:
            print("Working")
        servers = BeautifulSoup(r, 'html.parser').findAll('div', class_="column is-one-third-desktop is-half-tablet")
        for server in servers:
            eyedee = server.find('a', class_="button button-join is-discord").get('data-id')
            if eyedee in urls:
                pass
            else:
                urls.append(eyedee)
                url = f"https://disboard.org/site/get-invite/{eyedee}"
                x = requests.get(url)
                tempinvite = x.text
                invite = tempinvite.replace('"', '')
                print(invite)
                #hook.send(f"{invite}  | ``https://disboard.org/server/{eyedee}``")
    time.sleep(5)