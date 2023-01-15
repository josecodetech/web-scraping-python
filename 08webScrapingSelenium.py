from selenium import
from selenium.webdriver.chrome.options import Options
import time
url = 'https://josecodetech.es/'
opciones = webdriver.ChromeOptions()
opciones.add_argument('--incognito')
driver = webdriver.Chrome(executable_path='chromedriver', options=opciones)
time.sleep(2)
driver.get(url)
time.sleep(2)
driver.close()
