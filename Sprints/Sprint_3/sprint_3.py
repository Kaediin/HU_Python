import datetime


# Tweet messages
def tweet_messages():
    messages = 0
    file = open('messages_sprint3', 'w')
    file = open('messages_sprint3', 'a+')
    while messages < 10:
        message = str(input("Enter message (max 140 chars): "))

        if len(message) > 140:
            print('You have exceeded the amount of chars. You are allowed 140 and have {}'.format(len(message)))
            continue

        today = datetime.datetime.today()
        currentdateTime = today.strftime("%Y-%m-%d %H:%M:%S")

        file.write('{} - {}'.format(currentdateTime, message + '\n'))
        file.close()
        messages += 1


# Review messages
def review_messages():
    moderator_name = str(input("State your name: "))
    file = open('messages_sprint3', 'r')
    for line in file.readlines():
        dtime = line[0:19]
        message = line[22:].strip("\n")

        while True:
            print("{}: {}".format(dtime, message))
            result = str(input("Do you accept (a) or reject (r) this message? (a/r)"))
            if result == "r":
                currentdateTime = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
                reject_file = open('reject_sprint3', "a+")
                reject_file.write(
                    'Message: {}, posted at: {}, rejected at: {},  by Moderator: {}\n'.format(message, dtime, currentdateTime,
                                                                                     moderator_name))
                reject_file.close()
                break
            elif result == "a":
                print("Message Tweeted!")
                break
            else:
                print("Please choose a valid input ('a' to accept or 'r' to reject)")


# Show rejected messages
def show_rejected_messages():
    file = open('reject_sprint3', 'r')
    for line in file.readlines():
        print(line.strip("\n"))


tweet_messages()
review_messages()
show_rejected_messages()
