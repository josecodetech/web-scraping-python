import requests
from bs4 import BeautifulSoup

url = "https://es.wikipedia.org/wiki/Python"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
introduccion = soup.find("div", class_="mw-parser-output").p.text
print(introduccion)

url_tabla = "https://es.wikipedia.org/wiki/Python#Caracter%C3%ADsticas_y_paradigmas"
tabla = soup.find("table", class_="wikitable")
filas = tabla.find_all("tr")[1:]
tipos_datos = []
for fila in filas:
    datos = fila.find_all("td")
    
    print(datos[0].text, datos[1].text, datos[3].text)
    datos = datos[0].text.strip()
    tipos_datos.append(datos)
print("*"*25)
print(tipos_datos)