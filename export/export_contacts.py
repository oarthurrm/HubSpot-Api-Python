from dotenv import load_dotenv
import os
import requests
import csv

load_dotenv()

API_KEY = os.getenv('TOKEN')
print(API_KEY)

def contacts_list(API_KEY):
    
    URL = f'https://api.hubapi.com/crm/v4/objects/contacts'

    response = requests.get(URL, headers={
        'Authorization': f'Bearer {API_KEY}'
    })
    
    contacts = response.json()
    
    contacts_csv = 'contatos.csv'
    
    with open(contacts_csv, mode='w', newline='') as file:
        fieldnames = ["id", "email", "firstname", "lastname", "createdate", "lastmodifieddate"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
    
        for item in contacts['results']:
            row = {
                "id": item["id"],
                "email": item["properties"]["email"],
                "firstname": item["properties"]["firstname"],
                "lastname": item["properties"]["lastname"],
                "createdate": item["properties"]["createdate"],
                "lastmodifieddate": item["properties"]["lastmodifieddate"]
            }
            
            writer.writerow(row)

    print(f'Arquivo {contacts_csv} criado com sucesso!')
    
contacts_list(API_KEY)