

import os 
os.system('cls' if os.name == 'nt' else 'clear')

# Trabajando con la API de OpenAI
OPENAI_KEY = "-proj-2UXNCp5rtj-MQifKt3QGglN6mGFfquj1d3DEfVd5qAQMpiN7bIG6t0I8FbwA8JvENsbnd5IRyfT3BlbkFJj9p0FEk8Z4BHdwS4dLrEMyGiYe7ytcHmdmSohE6-pBAXucRaGmvvKVsykYlvuPdHipDk7MjAgA"
import requests
def call_openai_api(OPENAI_KEY, prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",
        "messages": [
            {
                "role": "user",
                "content": prompt,
                "temperature": 0.7,
                "max_tokens": 1000000
        }
    ]
}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

api_response = call_openai_api(OPENAI_KEY, "Explicame el sentido de la vida en 100 palabras, por favor.")

import json
#print(json.dumps(api_response, indent=2, ensure_ascii=False))
print(api_response["choices"][0]["message"]["content"])