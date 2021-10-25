from src.app.api.api import *


# get list of crimes per neighbourhood of one location
def prepare_crime_data(category, location, date):
    list_of_crimes_per_neighbourhood = []
    list_of_neighbourhoods = fetch_neighbourhoods_by_location(location)
    for neighbourhood in list_of_neighbourhoods:
        neighbourhood_data = fetch_data_by_neighbourhood(location, neighbourhood['id'])
        fetched_data = fetch_data_by_cat_lat_lng_date(
            category, neighbourhood_data['centre']['latitude'], neighbourhood_data['centre']['longitude'], date
        )
        if type(fetched_data) != str and fetched_data != []:
            list_of_crimes_per_neighbourhood.append(fetched_data.__len__())

    return sum(list_of_crimes_per_neighbourhood)


# prepares data for category dropdown on gui
def prepare_dropdown_categories():
    fetched_categories = fetch_categories()
    categories = [x['name'] for x in fetched_categories]
    return categories


# prepares data for locations dropdown on gui
def prepare_dropdown_locations():
    with open(r'../json/counties_uk.json') as counties:
        fetched_locations = json.load(counties)
    locations = [x['name'] for x in fetched_locations]
    return locations


# prepare category for graph calculation
def prepare_category_for_calculation(category):
    category_lowercase = category.lower()
    spaces_count = category_lowercase.count(' ')
    for space in range(spaces_count):
        index_of_space = category_lowercase.find(' ')
        category_lowercase = category_lowercase.replace(' ', '-', index_of_space)
    return category_lowercase


# prepare location for graph calculation
def prepare_location_for_calculation(location):
    location_lowercase = location.lower()
    return location_lowercase


# prepare date for graph calculation
def prepare_dates_for_calculation(year):
    dates = []
    for month in range(1, 13):
        if month > 9:
            dates.append(f'{year}-{month}')
        elif year != '2018' or month > 8:
            dates.append(f'{year}-0{month}')
    return dates


# prepare user input locations for table
def prepare_locations_for_table(locations):
    list_of_locations = []
    for location in locations:
        list_of_locations.append(f'{location}')
    return list_of_locations
