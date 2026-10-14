#
import requests
from bs4 import BeautifulSoup

url = "https://www.paruluniversity.ac.in/"

response=requests.get(url)

soup=BeautifulSoup(response.text,"html.parser")# access a html tags

print("Title: ",soup.title.string if soup.title else " NO title")

h1_tags=soup.find_all("h1")
print("H1 count: ",len(h1_tags))

for h1 in h1_tags:
    print("H1:",h1.get_text(strip=True))
