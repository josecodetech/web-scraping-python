from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
# ruta a driver
CHROME_DRIVER = "chromedriver.exe"
# configuracion apertura pestañas
chrome_options = Options()
chrome_options.add_argument("--new-window")
chrome_options.add_experimental_option("detach", True)
# inicia driver
driver = webdriver.Chrome(service=Service(CHROME_DRIVER), options=chrome_options)
# driver.get("https://josecodetech.es")
# leemos urls
with open('urls.txt', 'r') as file:
    urls = file.readlines()
# abrir cada url en nueva pestaña
for url in urls:
    url = url.strip()
    if url:
        driver.execute_script(f"window.open('{url}', '_blank');")
        time.sleep(1) # retraso para no sobrecargar el navegador
# mantenemos unos segundos abierta
# time.sleep(20)
# cerramos
# driver.quit()