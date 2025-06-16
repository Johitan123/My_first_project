
import os 
os.system('cls' if os.name == 'nt' else 'clear')

from bs4 import BeautifulSoup
import re
import requests

url = "https://www.apple.com/es/shop/buy-mac/macbook-air/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
response = requests.get(url, headers=headers)

if response.status_code == 200:
 print("\nLa solicitud fue exitosa.")

 soup = BeautifulSoup(response.text, 'html.parser')

 #print(soup.prettify()[0:100])
 title_tag = soup.title
 if title_tag:
     print(f"\nTítulo encontrado: {title_tag.text}")


     #price_span = soup.find("span", class_="rc-prices-fullprice")
     #if price_span:
       #  print(f"Precio encontrado: {price_span.text}")
     #else:
       #  print("No se encontró el precio.")
"""
     price_span = soup.find_all("span", class_="rc-prices-fullprice")
     if price_span:
         for price in price_span:
             print(f"Precio encontrado: {price.text}")
         else:
             print("No se encontró el precio.")
    """
    # find each product and get the name and the price
products = soup.find_all(class_="rc-productselection-item")
for product in products:
    name = product.find(class_="list-title").text
    price = product.find("span", class_="rc-prices-fullprice").text
    print(f"Producto con las características:\n{name}\nPrecio: {price}\n\n\n")
else:
    print("No se encontraron productos.")
  