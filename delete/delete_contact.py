import hubspot
from pprint import pprint
from hubspot.crm.products import ApiException
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('TOKEN')

client = hubspot.Client.create(access_token=API_KEY)

contact_id = '83631537517'

try:
    api_response = client.crm.contacts.basic_api.archive(contact_id=contact_id)
    pprint(api_response)
except ApiException as e:
    print(e)