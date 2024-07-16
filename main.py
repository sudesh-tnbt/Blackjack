import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

end_of_game = False

user_cards = random.choices(cards, weights=None, k=2)
user_score = sum(user_cards)
dealer_cards = random.choices(cards, weights=None, k=2)
dealer_score = sum(dealer_cards)

while not end_of_game:

    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {dealer_cards[0]}")

    prompt = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    user_decision = True if (prompt == 'y') else False if (prompt == 'n') else None

    if user_decision:
        user_cards += random.choices(cards, weights=None)
        user_score = sum(user_cards)


    end_of_game = True

