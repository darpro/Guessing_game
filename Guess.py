import random

(print("Phyton number guessing game "))
min_num = int(input("Enter the range minimum: "))
max_num = int(input("Enter the range maximum: "))
answer = random.randint(min_num, max_num)
game_running = True
guesses = 0
while game_running :
    guess = (input("Enter your guess: "))
    if guess.isdigit() :
        guess = int(guess)
        guesses += 1

        if guess < min_num or guess > max_num :
            print("That number is out of range")
        elif guess < answer :
            print("Too low")
        elif guess > answer :
            print("Too high")
        else :
            print(f"Correct!! The answer was {answer}")
            print(f"It took you {guesses} guesses")
            game_running = False
    else :
        print("Invalid answer")
