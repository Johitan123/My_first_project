import os 
os.system('cls' if os.name == 'nt' else 'clear')

import re
import requests

url = "https://www.apple.com/es/shop/buy-mac/macbook-air/"

response = requests.get(url)

if response.status_code == 200:
 print("La solicitud fue exitosa.")

 html = response.text

 price_pattern = r"<span class=\"rc-prices-fullprice\">(.*?)</span>"
 match = re.findall(price_pattern, html)
if match:
    print(f"Precio encontrado: {match[0]}")


#get the tittle if the pattern is found
title_pattern = r"<title>(.*?)</title>"
match = re.findall(title_pattern, html)
if match:
    print(f"Título encontrado: {match[0]}")