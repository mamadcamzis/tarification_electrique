import requests
import json
import pandas as pd

def get_enedis_data():
    url = "https://data.enedis.fr/api/explore/v2.1/catalog/datasets/consommation-electrique-par-secteur-dactivite-commune/records"
    print(f"Fetching Enedis data ...") 
    res = requests.get(url)
    res = res.json()
    enedis_df = pd.DataFrame(res)
    return enedis_df

def get_real_time_data():
    url = "https://odre.opendatasoft.com/api/explore/v2.1/catalog/datasets/eco2mix-regional-tr/records?limit=-1"
    print(f"Fetching Real time data from open data réseaux énergie (ODRE) ...") 
    res = requests.get(url)
    res = res.json()
    res = res["results"]
    odre_df = pd.DataFrame(res)
    return odre_df


if __name__ == "__main__":
    #get_enedis_data()
    enedis_df = get_enedis_data()
    odre_df = get_real_time_data()
    print(f"Enedis data {enedis_df}")
    
    