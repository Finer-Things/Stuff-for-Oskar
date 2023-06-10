import random
import time

#### Multiplication Function
def times_tables_game(smallest_number = 2, largest_number = 9, drum_roll_time = 1.5, speed_up_factor = 1):
    list = [str(i)+"x"+str(j) for i in range(smallest_number, largest_number+1) for j in range(smallest_number, largest_number+1) if i >= j]
    random_list = random.sample(list, len(list))

    number_correct = 0
    number_attempted = -1
    print(f"There are {len(list)} total questions. Ths means {len(list)} is the maximum score.")
    print('Type "stop" to terminate the program early.')
    for item in random_list:
        number_attempted += 1
        answer = input(f"What is {item}?")
        if answer.lower() in ["stop", "s"]:
            print(f"Thanks for playing! Program stopped after {number_attempted} questions.")
            if number_attempted != 0:
                print(f"You got {int(number_correct/number_attempted*100+.499)}% correct.")
            break
        # time.sleep(.5/speed_up_factor)
        print(f"{item} = {answer}?", end = " ")
        time.sleep(1/speed_up_factor)
        print("...", end=" ")
        time.sleep(drum_roll_time/speed_up_factor)
        if int(item[0])*int(item[2]) == int(answer):
            number_correct += 1
            print(f"Correct! Your score is {number_correct}.")
        else:
            print(f"{answer} is incorrect. {item} is {int(item[0])*int(item[2])}.")
            # time.sleep(1.5/speed_up_factor)
            # print(f"Your score is {number_correct}.", end="")
        time.sleep(1.5/speed_up_factor)
    if number_attempted == len(list): 
        print("\n" + f"Done! You answered {len(list)} questions and you got {number_correct} of them right. That's {int(number_correct/len(list)*100+.499)}% correct.")






times_tables_game(2,9, drum_roll_time = 5.5, speed_up_factor = 1.2)