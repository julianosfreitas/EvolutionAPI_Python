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
    'mediatype': 'image',
    'mimetype': 'image/png',
    'caption': 'Imagem legal',
    'media': 'https://images.icon-icons.com/2699/PNG/512/python_logo_icon_168886.png',
    'fileName': 'image.png',
    # 'delay': 10000, # simular "digitando"
}
response = requests.post(
    url=f'{BASE_URL}/message/sendMedia/{INSTANCE_NAME}',
    json=payload,
    headers=headers,
)
print(response.json())
