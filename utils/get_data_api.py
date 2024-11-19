import requests

url = "https://elprofemiguel.com/APIS_JSON/becas_laborales_api.json"

def obtenerBecasAPI():
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        becas = data["listado_becas"]
        return becas
    except requests.exceptions.RequestException as e:
        raise Exception(e)
