import requests
from bs4 import BeautifulSoup
import pandas as pd

skill = input("Ingresa el nombre del trabajo: ").strip()
place = input("Ingresa la ciudad: ").strip()
no_of_pages = int(input("ingresa la cantidad de paginas: "))

data = []

for page in range(1):
    url = f"https://ar.indeed.com/jobs?q={skill}&l={place}&start={page * 10}"

# realizar solicitud get

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

offers = soup.find_all("div", class_="job_seen_beacon")

for offer in offers:
    job_title = offer.find(
        "h2", class_="jobTitle css-1h4a4n5 eu4oa1w0").text.strip()
    if job_title is not None:
        jobs = job_title.text.strip()
        data.append({"titulo de trabajo": jobs})

# creacion de dataframe
df = pd.DataFrame(data)
df.to_csv("indeed.csv", index=False)
