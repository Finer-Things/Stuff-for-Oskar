import random
import time

class Times_Table_Game:
    def __init__(self, smallest_number = 2, largest_number = 9, drum_roll_time = 3, speed_up_factor = 1):
        self.smallest_number = smallest_number
        self.largest_number = largest_number
        self.drum_roll_time = drum_roll_time
        self.speed_up_factor = speed_up_factor
        self.score = 0
        self.number_attempted = 0
        self.practice_range = range(self.smallest_number, self.largest_number + 1)
        self.practice_list = [[i, j] for i in self.practice_range for j in self.practice_range if i <= j]
        print(f"Game set up with numbers {smallest_number} through {largest_number}. Use the .play() method to begin playing.")
    
    def play(self):
        input_string = ""
        if self.number_attempted == 0:
            print(f"There are {len(self.practice_list)} total questions. This means {len(self.practice_list)} is the maximum score.")
            for pair in self.practice_list:
                random.shuffle(pair)
            random.shuffle(self.practice_list)
        else:
            print(f"Picking up from where we left off, with {self.number_attempted} question(s) answered and a score of {self.score}.")
        print('Type "stop" or "s" to terminate the program early.')
        
        # Gameplay Steps
        while len(self.practice_list) > 0:
            question_pair = self.practice_list.pop()
            input_string = input(f"What is {question_pair[0]}x{question_pair[1]}? ")
            if not input_string.isnumeric():
                self.practice_list.append(question_pair)
                break
            else:
                self.number_attempted += 1
                print(f"{question_pair[0]}x{question_pair[1]} = {input_string}?", end = " ")
                time.sleep(1/self.speed_up_factor)
                num_pauses = 4
                for i in range(num_pauses):
                    print(".", end="")
                    time.sleep(self.drum_roll_time/(num_pauses*self.speed_up_factor))
                if int(question_pair[0])*int(question_pair[1]) == int(input_string):
                    self.score += 1
                    print(f" Correct! Your score is {self.score}.")
                else:
                    print(f"{input_string} is incorrect. {question_pair[0]}x{question_pair[1]} is {question_pair[0]*question_pair[1]}.")
                    # time.sleep(1.5/speed_up_factor)
                    # print(f"Your score is {number_correct}.", end="")
                time.sleep(1.5/self.speed_up_factor)
            
        if self.score == self.number_attempted and len(self.practice_list) == 0:
            print("CONGRATULATIONS!!!! YOU FINISHED EVERY QUESTION WITH 100% ACCURACY!")
        
        if self.number_attempted != 0:
            print(f"Thanks for playing! \n Questions Answered: {self.number_attempted} \t Score: {self.score} \t Accuracy: {int(self.score/self.number_attempted*100+.499)}%")
        
    
