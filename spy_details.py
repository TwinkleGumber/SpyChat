# replace all dictionaries by classes.

from datetime import datetime

class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None
        self.chats_avg = [0,0]



class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Twinkle', 'Ms.', 20, 6.7)

friend_one = Spy('Arsh', 'Mr.',22 , 6.9)
friend_two = Spy('Aditi', 'Ms.', 21, 6.39)
friend_three = Spy('Shweta', 'Ms.', 30, 6.95)


friends = [friend_one, friend_two, friend_three]

