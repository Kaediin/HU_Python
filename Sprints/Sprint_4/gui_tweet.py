import PySimpleGUI as sg
import Sprints.Sprint_4.postgresql_db as db

def start_tweet_gui():
    sg.theme('DarkAmber')

    layout = [[sg.Text('NS-Twitterzuil Tweet service')],
              [sg.Text('Naam:')],
              [sg.InputText()],
              [sg.Text('Bericht:')],
              [sg.Multiline()],
              [sg.Button('Plaats Tweet!')]]


    window = sg.Window('NS Twitterzuil', layout)

    while True:
        event, values = window.read()
        name = values[0]
        message = values[1]

        if str(name) == "":
            name = 'Anonymous'

        if event == 'Plaats Tweet!':
            db.tweet_message(message, name)
            break
        if event == sg.WIN_CLOSED:
            break
    window.close()

