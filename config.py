import requests

#токен телеграмм бота
token = '6029918707:AAEJvhZoUkXXbhSquqyNcC27pggBZH4ckMU'
data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()