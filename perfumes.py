import requests
from bs4 import BeautifulSoup
import pandas as pd

no_of_pages = int(input("Ingresa la cantidad de páginas: "))

data = []

for page in range(1, no_of_pages + 1):
    url = f"https://www.farmacity.com/perfumes-y-fragancias/hombres?page={page}"
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    products = soup.find_all("div", class_="product-card-container")

    for product in products:
        product_name = product.find(
            "div", class_="product-card-name").text.strip()
        product_brand = product.find(
            "div", class_="product-card-brand").text.strip()

        product_price_container = product.find(
            "div", class_="product-card-price")
        product_best_price = product_price_container.find(
            "span", class_="best-price")

        if product_best_price is not None:
            product_best_price = product_best_price.text.strip()
        else:
            product_best_price = "No disponible"

        data.append({
            "Nombre del producto": product_name,
            "Marca del producto": product_brand,
            "Mejor precio del producto": product_best_price
        })

df = pd.DataFrame(data)
df.to_csv("productos.csv", index=False)
