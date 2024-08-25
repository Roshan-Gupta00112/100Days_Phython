print("Welcome to Rollercoaster!")

height = int(input("What is your height in cm?\n"))

bill = 0
photo_charge = 3

if height > 120:
    print("You can ride rollercoaster")
    age = int(input("What is your age?\n"))
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    else:
        bill = 12
        print("Adult tickets are $12.")

    wants_photo = input("Do you want to have a photo take? Type y for Yes and n for No.\n")

    if wants_photo == "y":
        # bill = bill + photo_charge
        bill += photo_charge

    print(f"Your final bill is: ${bill}.")
else:
    print("Sorry, You can't ride rollercoaster")