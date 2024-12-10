from dotenv import load_dotenv
import os
import requests
import csv
import json

load_dotenv()

API_KEY = os.getenv('TOKEN')

def tickets_list(API_KEY):
    
    URL = f'https://api.hubapi.com/crm/v4/objects/tickets'

    response = requests.get(URL, headers={
        'Authorization': f'Bearer {API_KEY}'
    })
    
    tickets = response.json()
    print(json.dumps(tickets, indent=2))
    
    tickets_csv = 'negocios.csv'
    """ with open(tickets_csv, mode='w', newline='') as file:
        fieldnames = ["id", "createdate", "dealname", "amount", "ticketstage", ]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
    
        for item in tickets['results']:
            row = {
                "id": item["id"],
                "createdate": item["properties"]["createdate"],
                "dealname": item["properties"]["dealname"],
                "amount": item["properties"]["amount"],
                "ticketstage": item["properties"]["ticketstage"]
            }
            
            writer.writerow(row)

    print(f'Arquivo {tickets_csv} criado com sucesso!') """
    
tickets_list(API_KEY)