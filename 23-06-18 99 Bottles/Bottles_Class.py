class Song:
    def __init__(self):
        self.number_of_bottles = 99

    def sing_line(self):
        num = self.number_of_bottles
        print(f"{num} bottles of sparkling water on the wall, {num} bottles of sparkling water. \n Take one down, pass it around, {num - 1} bottles of sparkling water on the wall")
        self.number_of_bottles = self.number_of_bottles - 1