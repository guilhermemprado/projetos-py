from bs4 import BeautifulSoup
import requests

# Objeto site recebendo o conteudo da quisição http do site...
site = requests.get("https://www.Climatempo.com.br/").content

# Objeto soup baiando do site html
soup = BeautifulSoup(site, 'html.parser')

# Transforma html em string e o print vai exibir o html
#print(soup.prettify())

temperatura = soup.find("span", class_="_block _margin-b-5 -gray")

print(temperatura)

print(soup.p)