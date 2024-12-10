from dotenv import load_dotenv
import os
import requests
import csv
import json

load_dotenv()

API_KEY = os.getenv('TOKEN')

def products_list(API_KEY):
    
    URL = f'https://api.hubapi.com/crm/v4/objects/products'

    response = requests.get(URL, headers={
        'Authorization': f'Bearer {API_KEY}'
    })
    
    products = response.json()
    print(json.dumps(products, indent=2))
    
    products_csv = 'produtos.csv'
    
    with open(products_csv, mode='w', newline='') as file:
        fieldnames = ["id", "createdate", "name", "price", "description"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
    
        for item in products['results']:
            row = {
                "id": item["id"],
                "createdate": item["properties"]["createdate"],
                "name": item["properties"]["name"],
                "price": item["properties"]["price"],
                "description": item["properties"]["description"]
            }
            
            writer.writerow(row)

    print(f'Arquivo {products_csv} criado com sucesso!')
    
products_list(API_KEY)