import requests


BASE_URL = 'http://localhost:8080'
INSTANCE_NAME = 'julianoevo'
EVOLUTION_AUTHENTICATION_API_KEY = 'Jul14n0'

headers = {
    'apikey': EVOLUTION_AUTHENTICATION_API_KEY,
    'Content-Type': 'application/json'
}
payload = {
    'number': '5581985517186',
    'text': 'Sou uma mensagem enviada via API do Evolution!\n\n de teste, não se preocupe!\n\n, voce pode enviar mensagens de texto, imagens, vídeos, áudios, documentos e muito mais!\n\n',
    'delay': 10000, # simular "digitando"
}
response = requests.post(
    url=f'{BASE_URL}/message/sendText/{INSTANCE_NAME}',
    json=payload,
    headers=headers,
)
print(response.json())
