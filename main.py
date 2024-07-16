import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

end_of_game = False

while not end_of_game:

    user_cards = random.choices(cards, weights= None, k = 2)
    user_score = sum(user_cards)
    dealer_cards = random.choices(cards, weights= None, k = 2)
    dealer_score = sum(dealer_cards)

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {dealer_cards[0]}")


    end_of_game = True

