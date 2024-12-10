import hubspot
from pprint import pprint
from hubspot.crm.products import ApiException
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('TOKEN')

client = hubspot.Client.create(access_token=API_KEY)

company_id = '26624247601'

try:
    api_response = client.crm.companies.basic_api.archive(company_id=company_id)
    pprint(api_response)
except ApiException as e:
    print(e)