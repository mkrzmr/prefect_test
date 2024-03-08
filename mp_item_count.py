import requests
import json
from prefect import flow, task

@flow(log_prints=True)
def number_of_items():
    api_url = "https://marketplace-api.sshopencloud.eu/api/item-search?order=modified-on&advanced=false&includeSteps=false"
    response = requests.get(api_url)
    hits = response.json()['hits']
    print(f"There are {hits} item in the Marketplace")
    
if __name__ == "__main__":
    number_of_items()
