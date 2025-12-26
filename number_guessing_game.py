import random
pick_range = input("Pick your range in positive digits: ")

if pick_range.isdigit():
    pick_range = int(pick_range)
    if pick_range == 0:
        print("Please pick your range greater than 0")
        quit()
    print("_"*65, "\bGAME  BEGAINS", "_"*65)
else:
    raise ValueError("Range should be greater than 0")

random_number = random.randint(0, pick_range)
count_guesses = 0
while True:
    count_guesses += 1
    user_input = input("\nGuess the number: ")
    if user_input.isdigit():
        user_input = int(user_input)
    else:
        print("Your guess should be a number!")
        continue
    if user_input == random_number:
        print("WOW!!! You got it")
        break
    elif user_input > random_number:
        print("Make a smaller guess next time")
    else:
        print("Make a bigger guess next time")

print(f"You got it in {count_guesses} guesses")