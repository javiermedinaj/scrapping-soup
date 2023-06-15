import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Obtener el número de páginas desde el usuario
num_paginas = int(input("Ingrese el número de páginas a scrapear: "))

base_url = "https://ar.trabajosdiarios.com/ofertas-trabajo/en-buenos-aires/en-capital-federal?t=320&page="

data = []

for page in range(1, num_paginas + 1):
    url = base_url + str(page)
    response = requests.get(url)
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    jobs = soup.find_all("div", class_="card border-0 mb-3")

    for job in jobs:
        nombre = job.find("div", class_="font_3 fw-bold").text.strip()

        salario_div = job.find("div", class_="font_4 text-secondary")
        if salario_div:
            salario_text = salario_div.text.strip()
            salario_numeros = re.findall(r"\d+", salario_text)
            salario = "".join(salario_numeros)
        else:
            salario = "No disponible"

        lugar_divs = job.find_all("div", class_="font_4 text-secondary")
        if len(lugar_divs) >= 2:
            lugar_text = lugar_divs[1].text.strip()
            lugar = lugar_text
        else:
            lugar = "No disponible"

        link = job.find("a", class_="ink-secondary")["href"]
        link_completo = "https://ar.trabajosdiarios.com" + link

        data.append({"Nombre": nombre, "Sueldo": salario,
                    "Lugar": lugar, "Link": link_completo})

# Guardar los datos en un DataFrame
df = pd.DataFrame(data)
df.to_csv("trabajos.csv", index=False, encoding='utf-8')

print("Scraping finalizado")
