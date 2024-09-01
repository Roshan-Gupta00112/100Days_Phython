import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


# 1st Approach: Using String
my_password = ''

for char in range(1, nr_letters+1):
    my_password += random.choice(letters)
for char in range(1, nr_symbols+1):
    my_password += random.choice(symbols)
for char in range(1, nr_letters+1):
    my_password += random.choice(numbers)

print(f"My Password created using string is: {my_password}")

my_updated_password = ''.join(random.sample(my_password, len(my_password)))
print(f"My Shuffled Password using string is: {my_updated_password}")


# 2nd Approach: Using List
my_password_list = []

for char in range(1, nr_letters+1):
    my_password_list.append(random.choice(letters))
for char in range(1, nr_symbols+1):
    my_password_list.append(random.choice(symbols))
for char in range(1, nr_numbers+1):
    my_password_list.append(random.choice(numbers))

my_password2 = ''
for char in my_password_list:
    my_password2 += char
print(f"My Password created using list is: {my_password2}")

random.shuffle(my_password_list)

my_updated_password2 = ''.join(my_password_list)
print(f"My Shuffled Password created using list is: {my_updated_password2}")

