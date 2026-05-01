import requests
from bs4 import BeautifulSoup
import yaml
import os

# 1. Fetch DBLP BibTeX (Automatically includes your latest papers like ASE 2025)
DBLP_BIB_URL = "https://dblp.org/pid/80/6093.bib"
print("Syncing DBLP...")
bib_data = requests.get(DBLP_BIB_URL).text
os.makedirs("assets", exist_ok=True)
with open("assets/ref.bib", "w") as f:
    f.write(bib_data)

## 2. Fetch Researchr Service
#RESEARCHR_URL = "https://conf.researchr.org/profile/pabloponzio"
#print("Syncing Researchr...")
#response = requests.get(RESEARCHR_URL)
#soup = BeautifulSoup(response.text, 'html.parser')
#
#service_list = []
#committees_section = soup.find('h2', string=lambda s: s and 'Committees' in s)
#if committees_section:
#    items = committees_section.find_next('ul').find_all('li')
#    for item in items:
#        text = item.get_text(separator=" ").strip()
#        if ":" in text:
#            event, role = text.split(":", 1)
#            service_list.append({'event': event.strip(), 'role': role.strip()})
#
#os.makedirs("_data", exist_ok=True)
#with open("_data/service.yml", "w") as f:
#    yaml.dump(service_list, f)
