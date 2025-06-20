

import requests
import base64 # Importando a biblioteca base64 para codificação

#Imagem localmente ela vem em formato binario, então precisamos convertê-la para base64
with open('image.png', 'rb') as arquivo:                    # Abrindo o arquivo em modo binário
    arq_binary = arquivo.read()                             # Lendo o arquivo em modo binário
    arq_b64 = base64.b64encode(arq_binary).decode('utf-8')  # Convertendo para string base64
    

url =  'http://localhost:8080/message/sendMedia/julianoevo'

payload = {
    "number": '5581982145002',
        "mediatype": "image",
        'filenmame': 'image.png',
        'caption': 'teste',
        'media': arq_b64

}

headers = {
    'apikey': 'Jul14n0',
    'Content-Type': 'application/json'
}

response = requests.request("POST", url, json=payload, headers=headers)

print(response.text)