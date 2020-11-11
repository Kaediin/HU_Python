import PySimpleGUI as sg
import Semester_1.Sprints.Sprint_4.gui_tweet as tweet
sg.theme('DarkAmber')

layout = [[sg.Text('NS-Twitterzuil Tweet service')],
          [sg.Text('Kies één van de onderstaande knoppen')],
          [sg.Button('Tweet!'), sg.Button('Add Moderator'), sg.Button('Add Screen')]]


window = sg.Window('NS Twitterzuil', layout)

while True:
    event, values = window.read()

    if event == 'Tweet!':
        tweet.start_tweet_gui()
        break

    if event == 'Add Moderator':
        print('2')
        break

    if event == 'Add Screen':
        print('3')
        break

    if event == sg.WIN_CLOSED:
        break
window.close()
