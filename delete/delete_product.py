import hubspot
from pprint import pprint
from hubspot.crm.products import ApiException
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('TOKEN')

client = hubspot.Client.create(access_token=API_KEY)

product_id = ''

try:
    api_response = client.crm.products.basic_api.archive(product_id=product_id)
    pprint(api_response)
except ApiException as e:
    print(e)