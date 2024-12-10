import hubspot
from pprint import pprint
from hubspot.crm.products import ApiException
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('TOKEN')

client = hubspot.Client.create(access_token=API_KEY)

deal_id = '29885665204'

try:
    api_response = client.crm.deals.basic_api.archive(deal_id=deal_id)
    pprint(api_response)
except ApiException as e:
    print(e)