from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time
url = 'https://josecodetech.es/'
opciones = webdriver.ChromeOptions()
opciones.add_argument('--incognito')
driver = webdriver.Chrome(executable_path='chromedriver', options=opciones)
driver.get(url)
# obtenemos titulo
titulo = driver.title
print(titulo)
print('*'*50)
# obtenemos tarjetas web
tarjetas = driver.find_elements(by=By.CLASS_NAME, value='card')
for tarjeta in tarjetas:
    print(tarjeta.text)
print('*'*50)
driver.implicitly_wait(0.2)
# obtenemos enlace de una tarjeta
tarjeta = driver.find_element(by=By.CLASS_NAME, value='card')
# print(tarjeta.text)
enlace = driver.find_element(
    by=By.XPATH, value='/html/body/main/div/div/div/div[1]/div/figure/a')
# print(enlace)
print("Cambiamos de pagina ...")
driver.implicitly_wait(0.2)
enlace.click()
driver.implicitly_wait(0.2)
print("Vuelvo a la pagina inicial")
driver.back()  # driver.refresh() driver.forward()
time.sleep(2)
driver.close()  # driver.quit()
