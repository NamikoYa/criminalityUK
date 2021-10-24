from src.app.data_processing import prep_data
from src.app.api import api
import json
import numpy as np


def calculate_crime_rate_by_location_date(category, location, date):
    all_crimes = 600000
    with open(r'../json/crime_numbers_all.json') as numbers:
        fetched_numbers = json.load(numbers)
    for record in fetched_numbers:
        if record['date'] == date:
            all_crimes = record['crimes']

    all_crimes = all_crimes / 14 / 25

    crimes_of_location = prep_data.prepare_crime_data(category, location, date)
    crime_rate = (crimes_of_location / all_crimes) * 100

    return round(crime_rate, 8)
