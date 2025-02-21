import random
from art import logo


def blackjack_game():
    print(logo)


    user_game_play_choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").strip().lower()[0]

    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    dealer_cards_collection = []
    user_cards_collection = []

    while user_game_play_choice == 'y':

        dealer_curr_card = random.choice(cards)
        dealer_cards_collection.append(dealer_curr_card)

        user_curr_card = random.choice(cards)
        user_cards_collection.append(user_curr_card)


        user_next_card_choice = input("Type 'y' to get another card, type 'n' to pass: ").strip().lower()[0]

        while user_next_card_choice == 'y':
            user_curr_card = random.choice(cards)
            user_cards_collection

blackjack_game()
