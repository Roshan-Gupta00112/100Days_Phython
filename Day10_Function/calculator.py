from  art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2 if n2 != 0 else "Error! Division by ZERO."


def get_valid_number(prompt):
    """Function to safely get a valid number input."""
    while True:
        try:
            return float(input(prompt).strip())
        except ValueError:
            print("Invalid input! Please enter a valid number.")



# dict_operator = {
    #     "+":"add",
    #     "-":"subtract",
    #     "*":"multiply",
    #     "/":"divide"
    # }
    # This will store value as a String

dict_operator = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}
# This will store value as a parameter

def print_operator():
    print("Available operators:")
    for key in dict_operator:
        print(key)
    return

def check_valid_operator_and_return_corresponding_operations(prompt):
    while True:
        print_operator()

        user_operator = input(prompt).strip()[0]
        try:
            return user_operator, dict_operator[user_operator]
        # except ValueError:   # this will not work because dictionary throws a key error for an invalid key
        except KeyError:
            print("Invalid operator! Please choose from the available options.")




def clear_console():
    print("\n"*10)


def calculator():
    print(logo)

    first_number = get_valid_number("Enter first number.\n")

    while True:
        user_operator, user_operation = check_valid_operator_and_return_corresponding_operations("Pick any operation: ")

        second_number = get_valid_number("Enter second number.\n")

        result = user_operation(first_number, second_number)

        print(f"{first_number} {user_operator} {second_number} = {result}")

        user_choice = (input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")
                       .strip().lower())[0]

        if user_choice == 'y':
            first_number = result
        elif user_choice == 'n':
            clear_console()
            calculator()
        else:
            print("Exiting calculator. Goodbye!")
            break



calculator()