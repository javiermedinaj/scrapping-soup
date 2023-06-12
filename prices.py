import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://listado.mercadolibre.com.ar/libro-js#D[A:libro%20js"

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

"""prices = soup.find_all("span", {"class": "price-tag-fraction"})

for price in prices:
    print(price.text)"""

items = soup.find_all("li", class_="ui-search-layout__item")

# array para cargar los datos
data = []

for item in items:
    name = item.find(
        "h2", class_="ui-search-item__title shops__item-title").text.strip()
    price = item.find("span", class_="price-tag-fraction").text.strip(
    ).replace("Bs.", "").replace(",", ".")

    data.append({"Nombre": name, "Precio": price})

df = pd.DataFrame(data)
df.to_csv("prices.csv", index=False)
