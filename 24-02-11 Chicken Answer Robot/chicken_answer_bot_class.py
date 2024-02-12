import random

class ChickenAnswerBot:
    def __init__(self):
        self.answer_list = [
            "Scrambled eggs, bagock!", 
            "Chicken strips.", 
            "Guacamole!", 
            "Rooster.", 
            "Fried egg with cheese.", 
            ":-"
        ]
    
    def ask(self):
        print("Ask me a question about food.")
        input("(type input here)")
        print(random.choice(self.answer_list))

    


