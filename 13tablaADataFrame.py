import pandas as pd
import requests

url = 'https://www.expansion.com/mercados/cotizaciones/indices/ibex35_I.IB.html'
r = requests.get(url)
#print(r.text)
df = pd.read_html(r.text,attrs={'id':'listado_valores'})
print(type(df))
print(df[0])
df[0].to_csv('bolsa.csv')
print('Fichero csv guardado')