import hubspot
from hubspot.crm.deals import SimplePublicObjectInputForCreate, ApiException
from dotenv import load_dotenv
import os
from pprint import pprint

# Carregar as variáveis de ambiente
load_dotenv()

# Obtenha a chave da API do HubSpot do arquivo .env
API_KEY = os.getenv('TOKEN')

# Configurar o cliente HubSpot com o token de API
client = hubspot.Client.create(access_token=API_KEY)

# Defina as propriedades do contato a ser criado
properties = {
    "dealname": "Venda de Teclado para Microsoft",
    "amount": "100",
    "dealstage": "contractsent",
    "hs_object_id": "28700921399",
}

# Cria a instância do contato com as propriedades
deal_input = SimplePublicObjectInputForCreate(properties=properties)

try:
    # Cria o contato no HubSpot CRM
    api_response = client.crm.deals.basic_api.create(simple_public_object_input_for_create=deal_input)
    pprint(api_response)  # Mostra a resposta da API

except ApiException as e:
    print(f"Exception when calling HubSpot API: {e}")
