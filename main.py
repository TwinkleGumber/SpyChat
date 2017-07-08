from spy_details import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
from termcolor import colored

STATUS_MESSAGES = ['You only fail when you stop trying', 'Find the fighter in you.', 'Less waiting, more living']


print "Hello! Let's get started"

# The app asks the user if they want to continue with the default user or create their own.
question = "Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? "
existing = raw_input(question)

# add_status function
def add_status():
    updated_status_message = None

    if spy.current_status_message != None:
        print 'Your current status message is %s \n' % (spy.current_status_message)       # the app displays the current status message
    else:
        print "You don't have any status update \n"

    default = raw_input("Do you want to select from the older status updates (y/n)? ")

    if default.upper() == "N":
        new_status_message = raw_input("What status message do you want to set? ")


        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

    elif default.upper() == 'Y':

        item_position = 1

        for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))

# ' condition' for cases when the message is empty
        if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]        # After the user selects from the older status updates set it as the current one

    else:
        print 'The option you choose is not valid! Press either y or n.'

    if updated_status_message:
        print 'Your updated status message is: %s' % (updated_status_message)       #  print the updated status message
    else:
        print "You current don't have a status update"

    return updated_status_message

# function add_friend for the case when user selects to add a friend
def add_friend():

    new_friend = Spy('','',0,0.0)
                                     # ask the user for the name, age and rating of their spy friend and convert them into required datatype
    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    #new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print "Sorry! Invalid entry. We can't add spy with the details you provided"

    return len(friends)                  # return the number of friends the user has


#  method called select_a_friend.
def select_a_friend():
    item_number = 0

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,friend.age,friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends\n")
    friend_choice_position = int(friend_choice) - 1
    return friend_choice_position


def send_message():
#  method called select_a_friend to choose friend from the list of spy friends added by the user.
    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")

# ' condition' for cases when the image contains no secret message
    if len(text)>0:
        Steganography.encode(original_image, output_path, text)
        new_chat = ChatMessage(text, True)
        friends[friend_choice].chats.append(new_chat)           # Append the chat message to 'chats' key for the friends list.
        print "\nYour secret message(image) is ready!"
    else:
        print "\tENTER YOUR MESSAGE FIRST"
        send_message()


# method called read_a_message.
def read_message():
    sender = select_a_friend()                                   #  call the select_a_friend method to get which friend is to be communicated with.
    output_path = raw_input("What is the name of the file?")     # Ask the user for the name of the image they want to decode the message from.
    secret_text = Steganography.decode(output_path)
    new_chat = ChatMessage(secret_text,False)
    friends[sender].chats.append(new_chat)

    words = secret_text.split("_")
#  Delete a spy from your list of spies if they are speaking too much i.e. more than 100 words
    if len(secret_text) <= 100:
            for word in words:
                if word == word.upper():  # If a spy send a message with special words such as SOS, SAVE ME etc. (i.e. message in capital letters) then app displays an appropriate message.
                    print "IMPORTANT MESSAGE: " + secret_text
                else:
                    print "\nRecieved secret message is: " + secret_text
                    print "Your secret message has been saved!"


    else:
        print friends[sender].salutation + friends[sender].name + " " + "is speaking too much."

        del friends[sender]
        print "Spy has been deleted."
        print "Now your friend list is:"
        item_number = 0
        for friend in friends:
            print '%d. %s %s' % (item_number + 1, friend.salutation, friend.name)
            item_number = item_number + 1


        # Maintain the average number of words spoken by a spy everytime you receive a message from a particular spy.
    words_in_message = secret_text.split()
    print "\n  Number of words the message contains: " + str(len(secret_text.split()))
    print "  The average of number of words spoken by your spy friend: %0.1f" %(sum(len(word) for word in words_in_message)/len(words_in_message))






# method to read the entire chat history of a particular friend
def read_chat_history():
    read_for = select_a_friend()  # call the select_a_friend method to get which friend is to be communicated with.

    for chat in friends[read_for].chats:
      if chat.sent_by_me:        # print the chat history for a particular friend in different colours
        print (colored('[%s]' % (chat.time.strftime("%d %B %Y")),'blue')+" "+colored('%s:' %('You said:'),'red')+" "+colored('%s'%(chat.message)))
      else:
            print (colored('[%s]'%(chat.time.strftime("%d %B %Y")),'blue')+" "+colored('%s said:'%(friends[read_for].name),'red')+" "+colored('%s'%(chat.message)))




def start_chat(spy):
    spy.name = spy.salutation + " " + spy.name

# The age of the user is greater than 12 and less than 50 otherwise the app displays an appropriate message and exit.
    if spy.age > 12 and spy.age < 50:
# Print an appropriate welcome message with the name, salutation, age and rating of the spy.
        print "Authentication complete. Welcome " + spy.name + " age: " + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard "

        show_menu = True
        while show_menu:
# The app displays a menu with some choices.
            menu_choices = "\n What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)
                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)         # print the number of friends the user has
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy'


if existing.upper() == "Y":       # For default user the app will import the details from spy_details.py
    start_chat(spy)

else:                             # For new user app will ask for the name of the user
    spy = Spy('','',0,0.0)
    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

# It checks that the user has not entered an invalid name as input
    if len(spy.name) > 0:
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")  # The app  ask for the salutaion the user wants to be used in front of their name

        spy.age = raw_input("What is your age?")                       # Ask the user for their age and convert it to integer type
        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating?")              # Ask the user for their rating and convert it to float
        spy.rating = float(spy.rating)

        start_chat(spy)

    else:
        print 'Please add a valid spy name'

# Whether the user chooses to use the default user or a new user the app will call the same function i.e. spy_chat function