from dotenv import load_dotenv
import os
import requests
import csv
import json

load_dotenv()

API_KEY = os.getenv('TOKEN')

def companies_list(API_KEY):
    
    URL = f'https://api.hubapi.com/crm/v4/objects/companies'

    response = requests.get(URL, headers={
        'Authorization': f'Bearer {API_KEY}'
    })
    
    companies = response.json()
    print(json.dumps(companies, indent=2))
    
    companies_csv = 'empresas.csv'
    
    with open(companies_csv, mode='w', newline='') as file:
        fieldnames = ["id", "createdate", "name"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
    
        for item in companies['results']:
            row = {
                "id": item["id"],
                "createdate": item["properties"]["createdate"],
                "name": item["properties"]["name"]
            }
            
            writer.writerow(row)

    print(f'Arquivo {companies_csv} criado com sucesso!')
    
companies_list(API_KEY)