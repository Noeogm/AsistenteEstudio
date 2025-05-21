import random
import requests

def dato_curioso_random():
    if random.choice([True, False]):
        return dato_desde_numbers_api()
    else:
        return dato_desde_wikipedia()

#IMPORTAMOS DATO RANDOM DESDE numbersapi, requiere conexion a internet
def dato_desde_numbers_api():
    from datetime import date
    hoy = date.today()
    url = f"http://numbersapi.com/{hoy.month}/{hoy.day}/date"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.text
        else:
            return "No se pudo obtener el dato de NumbersAPI."
    except:
        return "Error al conectarse a NumbersAPI."
#IMPORTAMOS DATO RANDOM DESDE WIKIPEDIA
def dato_desde_wikipedia():
    url = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
    try:
        r = requests.get(url)
        if r.status_code == 200:
            data = r.json()
            return f"{data['title']}: {data['extract']}"
        else:
            return "No se pudo obtener el dato de Wikipedia."
    except:
        return "Error al conectarse a Wikipedia."
