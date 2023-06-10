from random import randint

class Game:
    def __init__(self):
        self.number = randint(1,101)
    
    def let_me_guess(self):
        print("Let's play! \n You have 7 guesses to guess my number. It is between 1 and 100.")
        for i in range(7):
            guess = int(input("Your guess "))
            if guess == self.number:
                print(f"That's right! Congratulations, you guessed the number in only {i+1} guesses!")
                return None
            elif self.number < guess:
                print(f"The number is lower. Try again.")
            else:
                print(f"The number is higher. Try again.")
        print(f"Unfortunately, there are no more guesses. The number was {self.number}.")

game = Game()
game.let_me_guess()