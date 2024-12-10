import hubspot
from pprint import pprint
from hubspot.crm.products import SimplePublicObjectInputForCreate, ApiException
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('TOKEN')

client = hubspot.Client.create(access_token=API_KEY)

properties = {
    "name": "Iphone 14",
    "price": "3200",
}
simple_public_object_input_for_create = SimplePublicObjectInputForCreate(properties=properties)
try:
    api_response = client.crm.products.basic_api.create(simple_public_object_input_for_create=simple_public_object_input_for_create)
    pprint(api_response)
except ApiException as e:
    print(e)