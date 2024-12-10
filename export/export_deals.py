from dotenv import load_dotenv
import os
import requests
import csv
import json

load_dotenv()

API_KEY = os.getenv('TOKEN')

def deals_list(API_KEY):
    
    URL = f'https://api.hubapi.com/crm/v4/objects/deals'

    response = requests.get(URL, headers={
        'Authorization': f'Bearer {API_KEY}'
    })
    
    deals = response.json()
    print(json.dumps(deals, indent=2))
    
    deals_csv = 'negocios.csv'
    
    with open(deals_csv, mode='w', newline='') as file:
        fieldnames = ["id", "createdate", "dealname", "amount", "dealstage", ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
    
        for item in deals['results']:
            row = {
                "id": item["id"],
                "createdate": item["properties"]["createdate"],
                "dealname": item["properties"]["dealname"],
                "amount": item["properties"]["amount"],
                "dealstage": item["properties"]["dealstage"]
            }
            
            writer.writerow(row)

    print(f'Arquivo {deals_csv} criado com sucesso!')
    
deals_list(API_KEY)