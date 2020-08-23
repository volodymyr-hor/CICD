import requests 

URL = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"

def get_data(URL):
    responce = requests.get(URL)
    data = responce.json()
    show_currencies(data)

def show_currencies(currency):
    for item in currency:
        print(item["ccy"] + " : "+ item["base_ccy"] + " " + item["buy"] + " | " + item["sale"])

get_data(URL)     


