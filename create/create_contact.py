import hubspot
from hubspot.crm.contacts import SimplePublicObjectInputForCreate, ApiException
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
    "firstname": "Camila",
    "lastname": "Fonseca",
    "email": "camila.fonseca@gmail.com",
    "phone": "123-456-7890",
    "company": "Data Trend"
}

# Cria a instância do contato com as propriedades
contact_input = SimplePublicObjectInputForCreate(properties=properties)

try:
    # Cria o contato no HubSpot CRM
    api_response = client.crm.contacts.basic_api.create(simple_public_object_input_for_create=contact_input)
    pprint(api_response)  # Mostra a resposta da API

except ApiException as e:
    print(f"Exception when calling HubSpot API: {e}")
