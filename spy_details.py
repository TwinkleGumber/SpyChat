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


class ChatMessage:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy('Twinkle', 'Ms.', 20, 6.7)

friend_one = Spy('Arsh', 'Mr.', 6.9, 22)
friend_two = Spy('Aditi', 'Ms.', 6.39, 21)
friend_three = Spy('Shweta', 'Ms.', 6.95, 30)


friends = [friend_one, friend_two, friend_three]
