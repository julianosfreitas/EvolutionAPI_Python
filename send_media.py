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
    'caption': 'Quando se trata de *decoração de interiores*, *cortina* e *persianas* são ambos elementos amplamente utilizados para controlar a entrada de luz,\n\n garantir *privacidade* e adicionar *beleza* às janelas,\n\n A *Romarri* pode te ajudar na escolha da melhor opção para o seu espaço.',
    'media': 'https://uniflex.com.br/wp-content/themes/yootheme/cache/32/Tres-scaled-3246b85f.webp',
    'fileName': 'image.png',
    'delay': 10000, # simular "digitando"
}
response = requests.post(
    url=f'{BASE_URL}/message/sendMedia/{INSTANCE_NAME}',
    json=payload,
    headers=headers,
)
print(response.json())
