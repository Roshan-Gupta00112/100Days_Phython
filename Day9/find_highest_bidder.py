import sys
import os

sys.path.append(os.path.abspath("/Users/rohsankumar/PycharmProjects/pythonProject/100 Days of Code - "
                                "The Complete Python Pro Bootcamp/Day 9/Blind Auction Project"))
import art
print(art.logo)


name = input("What is your name?: ")
bid = int(input("What's your bid?: $"))

# bid_dic = {}
bid_dic = dict()


bid_dic[name] = bid

highest_bidder = name
old_name = name

next_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n")


while True:
    if next_bid.lower() == "no":
        break
    elif next_bid.lower() != 'yes' and next_bid.lower() != 'no':
        print("Please Provide the correct input!")
    else:
        print("\n"*25)

        new_name = input("What is your name?: ")
        price = int(input("What's your bid?: $"))

        bid_dic[new_name] = price

        if bid_dic[old_name] < bid_dic[new_name]:
            highest_bidder = new_name

        old_name = new_name

    next_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n")


print(f"The winner is {highest_bidder} with a bid of ${bid_dic[highest_bidder]}.")
print(f"The winner is {max(bid_dic, key=bid_dic.get)} with a bid of ${bid_dic[highest_bidder]}.")
