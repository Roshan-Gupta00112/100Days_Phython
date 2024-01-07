print("Welcome to the tip calculator.")

bill_amount = float(input("What was the total bill? $"))

count_of_people = int(input("How many people to split the bill?\n"))

tip = int(input("What percentage tip would you like to give? 10, 12, or 15?\n"))

each_pay = round(((bill_amount * (100+tip)/100)/count_of_people), 2)
print(f"Each person should pay: ${each_pay}")

each_pay = "{:.2f}".format((bill_amount * (100+tip)/100)/count_of_people)

print(f"Each person should pay: ${each_pay}")

