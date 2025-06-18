import os
import traceback

from services import EvolutionAPI

#instânciar
evo_client = EvolutionAPI()

try:
    sale = {'id': 1, 'valor': 10000}
    print(sale.id)
except Exception as error:
    message = f'Falha ao processar venda: {error}\n\nTraceback: {traceback.format_exc()}'
    evo_client.send_message(
        number=os.getenv('EVO_PHONE_LOGGER'),
        text=message,
    )
