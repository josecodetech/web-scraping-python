from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pandas as pd


def guardar_datos(datos):
    df = pd.DataFrame(datos)
    df.to_csv('noticias.csv')
    print("Datos guardados")


url = 'https://elcorreoweb.es/'
opciones = webdriver.ChromeOptions()
opciones.add_argument('--icognito')
driver = webdriver.Chrome(executable_path='chromedriver', options=opciones)
driver.get(url)
driver.implicitly_wait(0.4)

try:
    acepta_cookies = driver.find_element(
        by=By.XPATH, value='/html/body/div[1]/div/div/div/div[2]/div/button[2]')
    acepta_cookies.click()
    seccion_noticias = driver.find_element(
        by=By.XPATH, value='/html/body/div[2]/div/div[2]/div[1]/div/div[11]/div/section/div/div/div/div/ul')
    noticias = seccion_noticias.find_elements(by=By.TAG_NAME, value='li')
    datos = []
    for noticia in noticias:
        encabezado_titulo = noticia.find_element(
            by=By.CLASS_NAME, value='headline')
        enlace_web = encabezado_titulo.find_element(by=By.TAG_NAME, value='a')
        enlace = enlace_web.get_attribute('href')
        titulo = enlace_web.text
        print(titulo)
        print(enlace)
        print('*'*40)
        driver.implicitly_wait(0.5)
        dict_datos = {'titulo': titulo, 'enlace': enlace}
        datos.append(dict_datos)
    guardar_datos(datos)
    for dato in datos:
        print(f"Titulo: {dato['titulo']}\nEnlace: {dato['enlace']}\n")
except Exception as e:
    print(f'Ha ocurrido el error -> {e}')
finally:
    driver.implicitly_wait(0.5)
    driver.quit()
