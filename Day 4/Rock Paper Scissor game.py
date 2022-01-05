# Make Rock Paper scissor game

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors."))
# print("\nYou Choose\n")
# print(game_images[user_choice])
computer_choice = random.randint(0,2)
# print("Computer Choose\n")
# print(game_images[computer_choice])

if (user_choice>=3) or (user_choice<0):
    print("You Typed an Invalid Number... You Lose!!")

elif (user_choice==0) and (computer_choice==2):
    print("\nYou Choose\n")
    print(game_images[user_choice])
    print("\nComputer Choose\n")
    print(game_images[computer_choice])
    print("\nYou Win!!")

elif (computer_choice == 0) and (user_choice == 2):
    print("\nYou Choose\n")
    print(game_images[user_choice])
    print("\nComputer Choose\n")
    print(game_images[computer_choice])
    print("\nYou Lose!!")

elif user_choice > computer_choice:
    print("\nYou Choose\n")
    print(game_images[user_choice])
    print("\nComputer Choose\n")
    print(game_images[computer_choice])
    print("\nYou Win!!")

elif computer_choice > user_choice:
    print("\nYou Choose\n")
    print(game_images[user_choice])
    print("\nComputer Choose\n")
    print(game_images[computer_choice])
    print("\nYou Lose!!")
    
elif computer_choice == user_choice:
    print("\nYou Choose\n")
    print(game_images[user_choice])
    print("\nComputer Choose\n")
    print(game_images[computer_choice])
    print("\nIt\'s a Draw")
