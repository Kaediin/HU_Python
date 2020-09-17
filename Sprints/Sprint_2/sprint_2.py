import datetime
message = input('Type your message (max 150 chars): ')
if len(message) > 150:
    print('Your character amount exceeded 150 chars. You had: {}'.format(len(message)))
else:
    today = datetime.datetime.today()
    currentdateTime = today.strftime("%a %d %b %Y %H:%M:%S")
    file = open('sprint2', 'a+')
    file.write('{} - {}'.format(currentdateTime, message+'\n'))