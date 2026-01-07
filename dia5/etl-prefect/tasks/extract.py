from prefect import task
import requests

@task
def extract():
    #Extrarer de randomuser
    URL = "https://randomuser.me/api/?results=10"
    response = requests.get(URL)

    extracted_data = []
    if response.status_code == 200:
        extracted_data = response.json()['results']
    return extracted_data