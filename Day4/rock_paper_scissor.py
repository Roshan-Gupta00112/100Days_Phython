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

choice_list = [rock, paper, scissors]
your_choice = int(input("Please type 0 for rock, 1 for paper and 2 for scissors\n"))

if your_choice < 0 or your_choice > 2:
    print("You mistyped. You Lose!")


print(f"You Choose: {choice_list[your_choice]}")

computer_choice = random.randint(0, 2)
print(f"Computer Chose: {choice_list[computer_choice]}")

if your_choice == 0 and computer_choice == 2:
    print("You Win!")
elif your_choice == 1 and computer_choice == 0:
    print("You Win!")
elif your_choice == 2 and computer_choice == 1:
    print("You Win!")
elif your_choice == computer_choice:
    print("Match Draw!")
else:
    print("You Lose!")
