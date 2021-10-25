import PySimpleGUI as psg
import matplotlib.pyplot as plt
import numpy as np
from src.app.data_processing import prep_data
from src.app.logic import calculate_graph

# window theme
psg.theme('GreenTan')
# window content
list_of_all_locations = prep_data.prepare_dropdown_locations()
layout = [[psg.Text('Choose category of crime:', size=(40, 1), font=('Lucida', 12), justification='left')],
          [psg.Combo(prep_data.prepare_dropdown_categories(), default_value='All crime', key='category')],
          [psg.Text('Choose locations (max: 3):', font=('Lucida', 12), justification='left')],
          [psg.Listbox(list_of_all_locations, select_mode='multiple', size=(40, 5), key='locations')],
          [psg.Text('Choose year:', font=('Lucida', 12), justification='left')],
          [psg.Spin(['2018', '2019', '2020', '2021'], key='year')],
          [psg.Text('note: data of 2018 is not complete', font=('Lucida', 8), justification='right')],
          [psg.Checkbox('Show table of content', font=('Lucida', 11), default=False, key='table')],
          [psg.Text('')],
          [psg.Button('Generate', font=('Lucida', 12)), psg.Button('Cancel', font=('Lucida', 12))]]

# create window UI
window = psg.Window('Graph Generator', layout)
# event loop to process events and get values of inputs
while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break

    list_of_locations = prep_data.prepare_locations_for_table(values['locations'])
    dates = prep_data.prepare_dates_for_calculation(values['year'])

    if list_of_locations.__len__() != 0:  # checks if length of list of location is 0
        crime_rate_of_year = []
        category = prep_data.prepare_category_for_calculation(values['category'])
        if list_of_locations.__len__() > 3:  # checks if length of list of locations is bigger than 3
            list_of_locations = list_of_locations[:3]  # only keeps three first entries
        # loops through prepared dates
        for date in dates:
            crime_rate_of_month = []
            # loops through list of locations
            for location in list_of_locations:
                current_location = prep_data.prepare_location_for_calculation(location)
                crime_rate = calculate_graph.calculate_crime_rate_by_location_date(category, current_location, date)
                crime_rate_of_month.append(crime_rate)  # adds crime rate to monthly crime rates
            crime_rate_of_year.append(crime_rate_of_month)  # adds monthly crime rate to yearly crime rate

    try:
        crime_rate_of_year  # checks if yearly crime rate is undefined
    except NameError:
        print(f'crime_rate_of_year is {crime_rate}')
    else:
        data = np.array(crime_rate_of_year)  # transforms yearly crime rate list to numpy array

        number_of_months = data.shape[0]
        number_of_locations = data.shape[1]

        # loops through list of locations
        for i, location_name in enumerate(list_of_locations):
            # sets how many graphs
            plt.plot(np.linspace(0, 365, number_of_months), data[:, i], label=f'{location_name}')

        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        percentage = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

        # sets x-axis values
        plt.xticks(np.linspace(0, 365, number_of_months), months[-number_of_months:])
        # sets y-axis values
        plt.yticks(percentage)
        # sets title with category of user input
        plt.title(f"Category {values['category']}")
        # sets x-axis label with year of user input
        plt.xlabel(values['year'])
        # sets y-axis label
        plt.ylabel('Crime rate in %')
        # shows graph
        plt.show()

        if values['table']:
            # makes table the foreground element
            fig, ax = plt.subplots()
            # hide axes
            fig.patch.set_visible(False)
            ax.axis('off')
            columns = tuple(months[-number_of_months:])
            rows = list_of_locations
            cells = data.astype(str)
            # sets cells, columns and rows of table
            plt.table(cellText=cells, rowLabels=columns, colLabels=rows, loc='center')
            # shows table
            plt.show()

# closes windows
window.close()
