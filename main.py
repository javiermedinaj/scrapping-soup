import requests
from bs4 import BeautifulSoup

url = "https://javier-medina-portfolio.vercel.app/"

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

# A partir de aquí, puedes manipular y analizar el contenido HTML utilizando BeautifulSoup
# por ejemplo, puedes encontrar elementos, extraer datos, etc.

# Ejemplo: imprimir el título de la página
title = soup.title

print(title.text)
"""print(soup.prettify())"""
tags = soup.find_all("div")

for divs in tags:
    print(divs.text)
