from random import randint

def roll_die():
    return randint(1, 6)

class Mom():
    def __init__(self, name):
        self.name = name
        self.question_list = []
    
    def answer(self, question):
        answer_dictionary = {
            1: "Yes", 
            2: "No", 
            3: "Silence (I'm ignoring you because you ignore me)", 
            4: "Yes", 
            5: "...Chicken!", 
            6: "No way, Jose!"
        }

        if question in self.question_list:
            print(f"{self.name} says: Hey, you already asked me that question and I already gave you an answer.")
            return None
        
        self.question_list.append(question)
        number = roll_die()
        # print(f"Rolling die...we rolled a {number}")
        print(f"{self.name} says: {answer_dictionary[number]}")

class Son():
    def __init__(self, name):
        self.name = name
    
    def ask(self, question, person):
        print(f"{self.name} says: Hey {person.name}, {question}")
        person.answer(question)