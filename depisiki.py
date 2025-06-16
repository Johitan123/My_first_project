
import os 
os.system('cls' if os.name == 'nt' else 'clear')

import requests
import json
# API Key de DeepSeek
# Asegúrate de reemplazar esto con tu propia clave de API de DeepSeek
deepseeki_api = "sk-261fce15ea1d46c59e66beda93e6a523"



def call_deepseek(deepseeki_api, prompt):
    url = "https://api.deepseek.com/chat/completions"
    headers = {
        "Authorization": f"Bearer {deepseeki_api}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ],
        "stream": False
    }

    response = requests.post(url, headers=headers, json=data)
    try:
        response_data = response.json()
    except json.JSONDecodeError:
        print("❌ Error: La respuesta no es JSON válida.")
        return None

    # Manejo de errores en la respuesta
    if "error" in response_data:
        print("❌ Error en la respuesta de la API:")
        print(response_data["error"]["message"])
        return None

    return response_data

# Llamada a la función
api_response = call_deepseek(deepseeki_api, "Haz un poema sobre la programación")

# Mostrar el contenido si no hubo error
if api_response and "choices" in api_response:
    print(api_response["choices"][0]["message"]["content"])
else:
    print("⚠️ No se pudo obtener una respuesta válida de la API.")