import requests
from bs4 import BeautifulSoup 

def Fif(url,path):
    f = requests.get(url)
    with open (path, "w") as file :
        file.write(f.text)

url = "https://www.google.com/"

Fif(url, "Data/data.html")
with open("Data/data.html" ,"r") as file:
    html_doc = file.read()

soup = BeautifulSoup(html_doc , "html.parser")
x=(soup.tostring())
with open("Data/sample.html", "w") as s :
    s.write(soup)