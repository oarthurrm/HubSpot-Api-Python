from dotenv import load_dotenv
import os
import requests
import csv
import json

load_dotenv()
    
API_KEY = os.getenv('TOKEN')

def payments_list(API_KEY):
    
    URL = f'https://api.hubapi.com/crm/v4/objects/commerce_payments'

    response = requests.get(URL, headers={
        'Authorization': f'Bearer {API_KEY}'
    })
    
    payments = response.json()
    print(json.dumps(payments, indent=2))
    
    payments_csv = 'pagamentos.csv'
    
    with open(payments_csv, mode='w', newline='') as file:
        fieldnames = ["id", "email", "firstname", "lastname", "createdate", "lastmodifieddate"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
    
        for item in payments['results']:
            row = {
                "id": item["id"],
                "email": item["properties"]["email"],
            }
            
            writer.writerow(row)

    print(f'Arquivo {payments_csv} criado com sucesso!')
        
payments_list(API_KEY)