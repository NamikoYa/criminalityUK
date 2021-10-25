from src.app.data_processing import prep_data
import json


# calculates crime rate by category, location and date
def calculate_crime_rate_by_location_date(category, location, date):
    # sets starting 100% crime value (in case it is empty)
    all_crimes = 600000
    # gets json object with crime numbers (100%)
    with open(r'../json/crime_numbers_all.json') as numbers:
        fetched_numbers = json.load(numbers)
    for record in fetched_numbers:
        if record['date'] == date:
            all_crimes = record['crimes']

    # estimation of all crimes per category per location (data inaccurate)
    all_crimes = all_crimes / 14 / 25

    crimes_of_location = prep_data.prepare_crime_data(category, location, date)
    crime_rate = (crimes_of_location / all_crimes) * 100  # calculates crime rate

    return round(crime_rate, 8)  # returns crime rate
