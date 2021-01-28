
import random
import time

low = 0
high = 100
max_guesses = 7
remaining_guesses = max_guesses
secret_number = int(random.randint(low,high))

print(f"Welcome to guess a number game. "
      f"The secret number is from {low} to {high}! "
      f"You have {max_guesses} guesses available!")
time.sleep(0.5)


while remaining_guesses > 0:
    guess = int(input("Enter a number: "))
    if guess == secret_number:
        time.sleep(0.5)
        print(f"Congrats, you won! The correct number was {secret_number}!")
        break
    elif guess > secret_number:
        remaining_guesses -= 1
        print("Incorrect!")

        if remaining_guesses > 0:
            print("Correct number is lower!")
            print(f"You have {remaining_guesses} left")
            print("Try again!")
            time.sleep(0.5)
    elif guess < secret_number:
        remaining_guesses -= 1
        print("Incorrect!")

        if remaining_guesses > 0:
            print("Correct number is higher!")
            print(f"You have {remaining_guesses} guesses left")
            print("Try again!")
            time.sleep(0.5)
if remaining_guesses == 0:
    print("Game over")
    print(f"The correct number was {secret_number}!")
    print("The program will terminate in 10 seconds!")
    time.sleep(10)
quit()