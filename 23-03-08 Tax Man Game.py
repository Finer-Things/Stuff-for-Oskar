print("Welcome to The Tax Man. How many numbers will you be playing with today?")
number = int(input("Numbers:"))
number_list = list(range(1, number + 1))
print(number_list)
your_list = []
tax_man_list = []
while True:
    if number_list == []:
        break
    turn_input = int(input("Choose your number"))
    your_list.append(turn_input)
    tax_collection = [item for item in number_list if turn_input % item == 0 and item < turn_input]
    tax_man_list += tax_collection
    number_list = [item for item in number_list if item not in your_list and item not in tax_man_list]
    if tax_collection == []:
        break
    print(f"Your numbers are {sorted(your_list)}.")
    print(f"The Tax Man's numbers are {sorted(tax_man_list)}.")
    print(f"The remanining numbers are {sorted(number_list)}.")
tax_man_list += number_list
print(f"Your numbers are {sorted(your_list)}, with a sum of {sum(your_list)}.")
print(f"The Tax Man's numbers are {sorted(tax_man_list)}, with a sum of {sum(tax_man_list)}.")