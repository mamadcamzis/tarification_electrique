import requests
import json
import pandas as pd

def get_enedis_data():
    url = "https://data.enedis.fr/api/explore/v2.1/catalog/datasets/consommation-electrique-par-secteur-dactivite-commune/records"
    res = requests.get(url)
    res = res.json()
    #print(json.dumps(res.json(), indent=3))
    res = res["results"]
    for r in res:
        print(f"Annee --> {r['annee']}\n")

def get_real_time_data():
    url = "https://odre.opendatasoft.com/api/explore/v2.1/catalog/datasets/eco2mix-regional-tr/records?limit=-1&lang=fr&refine=libelle_region%3A%22Auvergne-Rh%C3%B4ne-Alpes%22&refine=libelle_region%3A%22Bourgogne-Franche-Comt%C3%A9%22&refine=libelle_region%3A%22Bretagne%22&refine=libelle_region%3A%22Centre-Val%20de%20Loire%22&refine=libelle_region%3A%22Grand%20Est%22&refine=libelle_region%3A%22Hauts-de-France%22&refine=libelle_region%3A%22%C3%8Ele-de-France%22&refine=libelle_region%3A%22Normandie%22&refine=libelle_region%3A%22Nouvelle-Aquitaine%22&refine=libelle_region%3A%22Occitanie%22&refine=libelle_region%3A%22Pays%20de%20la%20Loire%22&refine=libelle_region%3A%22Provence-Alpes-C%C3%B4te%20d%27Azur%22"
    print(f"Fetching Real time data from open data réseaux énergie (ODRE) ...") 
    res = requests.get(url)
    res = res.json()
    res = res["results"]
    odre_df = pd.DataFrame(res)
    return odre_df


if __name__ == "__main__":
    #get_enedis_data()
    df = get_real_time_data()
    print(df["code_insee_region"].unique())
    