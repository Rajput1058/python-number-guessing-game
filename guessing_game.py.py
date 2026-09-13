# Day4_guessing game
# Day 4 - Number Guessing Game - By Usman in Lisbon
import random
print("welcom to the number guessing game")
print("you only have maximum of 7 attempts")
secret_number = random.randint(1,99)
attempts = 0
maximum_attempts = 7
while attempts < maximum_attempts:
    guess = int(input("guess a number between 1 and 99: "))
    attempts += 1
    if guess < secret_number:
        print("too low")
    elif guess > secret_number:
        print("too high")
    else:
        print(f"congratulations! you guessed the number {secret_number} in {attempts} attempts.")
        break
else:
    print("GAME OVER")
    
