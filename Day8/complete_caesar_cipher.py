import sys
import os

# Add the directory to sys.path
sys.path.append(os.path.abspath("/Users/rohsankumar/PycharmProjects/pythonProject/100 Days of Code - The Complete Python Pro Bootcamp/Day 8/Caesar Cipher 3"))

# Import the logo variable from the art module
from art import logo

def encrypt():
    original_text = input("Type Message to Encrypt:\n")
    shifted_amount = int(input("Type the shift number:\n"))
    shifted_text_list = list(original_text)
    original_text_size = len(original_text)

    cap_ascii_val = ord('A')
    small_ascii_val = ord('a')


    for i in range(original_text_size):
        char_at_i = shifted_text_list[i]
        curr_char_ascii_val = ord(char_at_i)
        if char_at_i.isupper():
            shifted_text_list[i] = chr((curr_char_ascii_val - cap_ascii_val + shifted_amount) % 26 + cap_ascii_val)
        else:
            shifted_text_list[i] = chr((curr_char_ascii_val - small_ascii_val + shifted_amount) % 26 + small_ascii_val)


    shifted_text = "".join(shifted_text_list)

    print(f"Encrypted Word is: {shifted_text}")



def decrypt():
    original_text = input("Type Message to Decrypt:\n")
    shift_amount = int(input("Type the shift number:\n"))
    decrypted_list = list(original_text)

    cap_letter_start_ascii_val = ord('A')
    small_letter_start_ascii_val = ord('a')

    len_of_word = len(original_text)

    for i in range(len_of_word):
        chr_at_i = decrypted_list[i]

        curr_letter_ascii_val = ord(chr_at_i)

        if chr_at_i.islower():
            decrypted_list[i] = chr((curr_letter_ascii_val - small_letter_start_ascii_val - shift_amount) % 26 +
                                    small_letter_start_ascii_val)
        else:
            decrypted_list[i] = chr((curr_letter_ascii_val - cap_letter_start_ascii_val - shift_amount) % 26 +
                                    cap_letter_start_ascii_val)

    decrypted_word = "".join(decrypted_list)

    print(f"Decrypted Word is: {decrypted_word}")

def caesar():
    player_choice_lower = input("Want to play Caesar Cipher? Type y for Yes or n or No!\n").lower()

    while True:
        if player_choice_lower == 'n' or player_choice_lower == 'no':
            print("Thank You. Come Again!")
            break
        elif player_choice_lower.lower() == 'y' or player_choice_lower == 'yes':
             encode_or_decode = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

             if encode_or_decode == 'encode' or encode_or_decode == 'decode':
                original_text = input("Type Your Message:\n")
                shift_amount = int(input("Type the shift number:\n"))

                if encode_or_decode == "decode":
                    shift_amount *= -1

                output_letter_list = list(original_text)
                len_of_original_text = len(original_text)

                cap_starting_alphabet_ascii_value = ord('A')
                small_starting_alphabet_ascii_value = ord('a')

                for i in range(len_of_original_text):
                    chr_at_i = output_letter_list[i]

                    if chr_at_i.isalpha():
                        if chr_at_i.islower():
                            output_letter_list[i] = chr((ord(chr_at_i) - small_starting_alphabet_ascii_value +
                                                         shift_amount) % 26 + small_starting_alphabet_ascii_value)
                        else:
                            output_letter_list[i] = chr((ord(chr_at_i) - cap_starting_alphabet_ascii_value +
                                                         shift_amount) % 26 + cap_starting_alphabet_ascii_value)

                output_result = "".join(output_letter_list)

                print(f"Here is the {encode_or_decode}d result: {output_result}")
             else:
                print(f"Oh oo! You provided Wrong Input! Type 'encode' to encrypt, type 'decode' to decrypt.")
        else:
            print("Sorry, you entered Wrong! Either type y for yes or n for No")

        player_choice_lower = input("Type y for Yes or n or No!\n").lower()


def start_game():
    print(logo)

    caesar()

start_game()


