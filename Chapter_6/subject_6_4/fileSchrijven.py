import datetime

# Sets up the vars
today = datetime.datetime.today()
date = today.strftime("%a %d %b %Y")
time = today.time().strftime("%H:%M:%S")
names = ['Kaedin', 'Linda', 'Marcel', 'Jarec', 'Themba']

# Open the file in write mode (hence the 'w')
f = open("pe_6_4_kaartnummers.txt", "w")
for name in names:
    f.write("{}, {}, {}\n".format(date, time, name))
f.close()
