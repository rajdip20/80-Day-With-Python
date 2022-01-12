import random
from guessing_art import logo

print(logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
computer_guess = random.randint(1, 100)

print(f"Pssst, the correct answer is {computer_guess}")
user_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def easy():
    life = 10
    is_finished = True

    while is_finished:

        if life > 0:
            print(f"You have {life} attempts remaining to guess the number.")
            user_guess = int(input("Make a guess: "))

            if computer_guess == user_guess:
                print(f"You got it! The answer was {user_guess}.")
                is_finished = False

            elif computer_guess > user_guess:
                print("Too low.")
                life -= 1
                if life == 0:
                    print("You've run out of guesses, you lose.")
                    is_finished = False
                else:
                    print("Guess again.")

            elif computer_guess < user_guess:
                print("Too high.")
                life -= 1
                if life == 0:
                    print("You've run out of guesses, you lose.")
                    is_finished = False
                else:
                    print("Guess again.")



def hard():
    life = 5
    is_finished = True

    while is_finished:

        if life > 0:
            print(f"You have {life} attempts remaining to guess the number.")
            user_guess = int(input("Make a guess: "))

            if computer_guess == user_guess:
                print(f"You got it! The answer was {user_guess}.")
                is_finished = False

            elif computer_guess > user_guess:
                print("Too low.")
                life -= 1
                if life == 0:
                    print("You've run out of guesses, you lose.")
                    is_finished = False
                else:
                    print("Guess again.")

            elif computer_guess < user_guess:
                print("Too high.")
                life -= 1
                if life == 0:
                    print("You've run out of guesses, you lose.")
                    is_finished = False
                else:
                    print("Guess again.")



if user_choice == "easy":
    easy()
else:
    hard()
