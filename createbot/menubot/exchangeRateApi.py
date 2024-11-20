import requests
from pprint import pprint as print

API_KEY = '12bc4ee1d6cbe5c1738bea9a'

currency = 'USD'
url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/{currency}/UZS"

response = requests.get(url)
print(response.status_code)
print(response.json())
jsondata = response.json()
kurs = response.json()['conversion_rate'] 
print(f"Bugungi kurs=1 AQSH dollar = {kurs} so'm") 