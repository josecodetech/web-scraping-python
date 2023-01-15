from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import time
url = 'https://josecodetech.es/'
opciones = webdriver.ChromeOptions()
opciones.add_argument('--incognito')
driver = webdriver.Chrome(executable_path='chromedriver', options=opciones)
driver.get(url)
driver.implicitly_wait(0.4)
try:
    acepta_cookies = driver.find_element(
        by=By.XPATH, value='/html/body/footer/div/div[2]/p/button')
    acepta_cookies.click()
    print('Cookie aceptada')
    # print(type(acepta_cookies))
    # print(acepta_cookies)
except Exception as e:
    print(f'Ha ocurrido el error -> {e}')
finally:
    driver.implicitly_wait(1)
    driver.quit()
