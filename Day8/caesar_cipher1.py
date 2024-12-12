text = input("Type your message:\n")
shift = int(input("Type the shift number:\n"))


def encrypt(original_text, shift_amount):
    encrypted_text_list = list(original_text)

    for i in range(len(encrypted_text_list)):
        char_at_i = encrypted_text_list[i]
        char_ascii_val = ord(char_at_i)
        if char_at_i.isupper():
            start_ascii_val = ord('A')
        else:
            start_ascii_val = ord('a')

        if char_at_i == 'z' or char_at_i == 'Z':
            encrypted_text_list[i] = chr((char_ascii_val - start_ascii_val + 9) % 26 + start_ascii_val)
        else:
            encrypted_text_list[i] = chr((char_ascii_val - start_ascii_val + shift_amount) % 26 + start_ascii_val)

    encrypted_text = "".join(encrypted_text_list)

    print(f"Encrypted letter is: {encrypted_text}")

encrypt(text, 1)