import requests
import json

def get_enedis_data():
    url = "https://data.enedis.fr/api/explore/v2.1/catalog/datasets/consommation-electrique-par-secteur-dactivite-commune/records"
    res = requests.get(url)
    res = res.json()
    #print(json.dumps(res.json(), indent=3))
    res = res["results"]
    for r in res:
        print(f"Annee --> {r['annee']}\n")

if __name__ == "__main__":
    get_enedis_data()
    