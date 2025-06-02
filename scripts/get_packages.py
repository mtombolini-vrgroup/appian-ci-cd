import requests
import json
import os

# Cargar configuración local de aplicaciones
with open("config/apps_config.json", "r") as f:
    apps_config = json.load(f)

# API Key y dominio (usa la API Key directamente para pruebas)
API_KEY = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI5YTA2ZjUyMy04MjczLTAwMzItNjllMS0wY2Y1ZjczMTYwNTkifQ.HBlQusj44ja2dPApgIO4VXxqScrnkReniMyvgXw88wc"
BASE_URL = "https://vrgroupdemo.appiancloud.com"

headers = {
    "appian-api-key": API_KEY,
    "Content-Type": "application/json"
}

# Diccionario para guardar resultados
packages_by_app = {}

# Iterar por cada aplicación configurada
for app_name, app_uuid in apps_config.items():
    url = f"{BASE_URL}/suite/deployment-management/v2/applications/{app_uuid}/packages"
    print(f"URL final: {url}")
    print(f"Headers: {headers}")
    print(f"Consultando paquetes para '{app_name}' ({app_uuid})...")

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        packages = {
            pkg['name']: pkg['uuid']
            for pkg in data.get('packages', [])
        }
        packages_by_app[app_name] = packages
    else:
        print(f"❌ Error al consultar {app_name}: {response.status_code} - {response.text}")

# Guardar como archivo JSON resultante
with open("config/packages_result.json", "w") as f:
    json.dump(packages_by_app, f, indent=2)

print("✅ Consulta finalizada. Paquetes guardados en 'config/packages_result.json'.")