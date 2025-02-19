def start_process(process_name):
    print(process_name)

    def roll_back_process():
        print("You have resigned")

    return roll_back_process()


start_process("Onboarding")


def add(num1, num2):

    def compute(num1, num2):
        print(f"The summation of {num1} and {num2} is: {num1 + num2}")

    return compute(num1, num2)

add(2, 3)
