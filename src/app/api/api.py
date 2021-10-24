import requests
import json

API = "https://data.police.uk/api/"


# fetch data for dynamic dropdowns
def fetch_categories():
    response_API = requests.get(f"{API}crime-categories")
    if response_API.status_code == 200:
        api_response_text = response_API.text
        data = json.loads(api_response_text)
    else:
        data = ''
    return data


# fetch data for visualization
def fetch_neighbourhoods_by_location(location):
    response_API = requests.get(f"{API}{location}/neighbourhoods")
    if response_API.status_code == 200:
        api_response_text = response_API.text
        data = json.loads(api_response_text)
    else:
        data = ''
    return data


def fetch_data_by_neighbourhood(location, neighbourhood):
    response_API = requests.get(f"{API}{location}/{neighbourhood}")
    if response_API.status_code == 200:
        api_response_text = response_API.text
        data = json.loads(api_response_text)
    else:
        data = ''
    return data


def fetch_data_by_cat_lat_lng_date(crime_type, lat, lng, date):
    response_API = requests.get(f"{API}crimes-street/{crime_type}?lat={lat}&lng={lng}&date={date}")
    if response_API.status_code == 200:
        api_response_text = response_API.text
        data = json.loads(api_response_text)
    else:
        data = ''
    return data
