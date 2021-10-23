import PySimpleGUI as psg
from src.app.logic import prep_data

# window theme
psg.theme('GreenTan')
# window content
layout = [[psg.Text('Choose category of crime:', size=(40, 1), font='Lucida', justification='left')],
          [psg.Combo(prep_data.prepare_dropdown_categories(), default_value='All crime', key='category')],
          [psg.Text('Choose locations:', font='Lucida', justification='left')],
          [psg.Listbox(prep_data.prepare_dropdown_locations(), select_mode='extended', size=(40, 5), key='locations')],
          [psg.Text('Choose time span (year/month):', font='Lucida', justification='left')],
          [psg.Spin(['2018', '2019', '2020', '2021'], key='year'),
           psg.Spin(['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'], key='month')],
          [psg.Checkbox('Show table of content', default=False, key='table')],
          [psg.Text('')],
          [psg.Button('Generate', font=('Lucida', 12)), psg.Button('Cancel', font=('Lucida', 12))]]

# create window
window = psg.Window('Graph Generator', layout)
# event loop to process events and get values of inputs
while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED or event == 'Cancel':  # if user closes window or clicks cancel
        break
    print('Category:', values['category'])
    print('Locations:', values['locations'])
    print('Year & month:', values['year'], values['month'])
    print('Show table of content:', values['table'])

window.close()
