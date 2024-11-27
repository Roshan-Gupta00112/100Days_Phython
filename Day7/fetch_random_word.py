import random

words_list = ["applecompany", "iphone", "airpods", "applewatch", "rollsroyce"]

chosen_word = random.choice(words_list)

chosen_word_lower = chosen_word.lower()
# print(f"Guess word is: {chosen_word_lower}")

guess = input("Please Guess a Letter!\n")

guess_lower = guess.lower()

guess_length = len(guess_lower)


if guess_length == 0:
    print("You haven't guesses any letter. Please guess a Letter")
elif guess_length > 1:
    print("Please guess a letter not a word!")

is_guess = False
for letter in chosen_word:
    if letter == guess:
        is_guess = True

if is_guess:
    print(f"Chosen word was: {chosen_word_lower}. You are Wright!")
else:
    print(f"Chosen word was: {chosen_word_lower}. You are Wrong!")
