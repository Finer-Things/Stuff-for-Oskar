from random import choice

nickname_list = ["the Bosker", "the Greython", "the Dommy", "the Billy", "the Crabby", "the Grouchy", "the Banana-Face"]

class Person:
    def __init__(self, first_name: str = "", last_name: str = ""):
        self.first_name = first_name
        self.last_name = last_name
    
    def say_nickname(self):
        print(f"{self.first_name} {choice(nickname_list)} {self.last_name}")