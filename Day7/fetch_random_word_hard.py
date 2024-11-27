import random

words_list = ["applecompany", "iphone", "airpods", "applewatch", "rollsroyce"]

chosen_word_lower = random.choice(words_list).lower()
# SC = O(N)


guess_lower = input("Please Guess a Letter!\n").lower()
# SC = O(N)

guess_length = len(guess_lower)


count = 0
# new_word = ""
# # print(f"Attempt word is: {new_word}")
# for i in range(0, len(chosen_word_lower)):
#     new_word += "_"
    # TC = O(N^2)

new_word = "_" * len(chosen_word_lower)
# TC = O(N)

letter_list = list(new_word)
# SC = O(N)

while True:
    count += 1
    if guess_length == 0:
        print("You haven't guesses any letter!")
    elif guess_length > 1:
        print("You guessed a word not a letter!")
    else:
        letter_match = False
        for i, char in enumerate(chosen_word_lower):
            if char == guess_lower and letter_list[i] == "_":
                letter_list[i] = char
                letter_match = True
        if not letter_match:
            print(f"Sorry, the guessed word didn't contain letter:{guess_lower}")
        # for i in range(0, len(chosen_word_lower)):
        #     if chosen_word_lower[i] == guess_lower and new_word[i] == "_":
        #         new_word = new_word[:i] + guess_lower + new_word[i+1:]
                #     TC = O(N^2)

    till_formed_word = "".join(letter_list)
    # TC = O(N)

    if till_formed_word == chosen_word_lower:
        break
    #     TC = O(N)

    guess_lower = input("Please chose next letter!\n").lower()

    guess_length = len(guess_lower)


print(f"Congratulation you guessed the word, {chosen_word_lower} in {count} attempts")

# Overall TC = O(count) * O(len(chosen_word)) = O(M) * O(N) = O(M*N)
# SC = O(N)
