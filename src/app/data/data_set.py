from src.app.api.api import *


def create_dataframe(category, list_of_category, locations, list_of_locations, time_span, list_of_timesteps):
    data_frame = {
        category: [list_of_category],
        locations: [list_of_locations],
        time_span: [list_of_timesteps]
    }
    return data_frame


def prepare_data(category, locations, time_span):
    # initialize list of neighbourhood ids
    neighbourhood_ids = []
    # initialize list of crimes of each location
    crimes_per_location = []

    # loop through locations
    for location in locations:
        # append neighbourhood ids to list of neighbourhood ids
        neighbourhood_ids.append(location.id)

    # loop through locations
    for location_name in locations:
        # append location to list of crimes of each location
        crimes_per_location.append(location_name)
        # initialize list of crimes of each neighbourhood
        crimes_per_neighbourhood = []

        # loop through neighbourhood ids
        for current_id in neighbourhood_ids:
            # append id to list of crimes of each neighbourhood
            crimes_per_neighbourhood.append(current_id)
            # initialize list of crimes of current neighbourhood
            crimes_of_neighbourhood = []
            # fetch data for current neighbourhood
            data_of_neighbourhood = fetch_data_by_neighbourhood(location_name, current_id)
            # loop through data of current neighbourhood
            for record in data_of_neighbourhood:
                # loop through coordinates
                for coordinates in record:
                    # check if parameter category is not empty
                    if category:
                        # fetch data by category, coordinates and time span
                        crimes_of_neighbourhood = fetch_data_by_cat_lat_lng_date(category, coordinates.latitude, coordinates.longitude, time_span)
                    else:
                        # fetch data by coordinates and time span
                        crimes_of_neighbourhood = fetch_data_by_cat_lat_lng_date('all-crime', coordinates.latitude, coordinates.longitude, time_span)

            # loop through neighbourhood ids
            for item in neighbourhood_ids:
                # append current crimes of each neighbourhood to current neighbourhood id
                crimes_per_neighbourhood[current_id].append(crimes_of_neighbourhood)

        # loop though locations
        for items in locations:
            # append crimes of each neighbourhood of current location to current location name
            crimes_per_location[location_name].append(crimes_per_neighbourhood)

    # return list of crimes of each neighbourhood of each location
    return crimes_per_location
