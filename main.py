import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

end_of_game = False

user_cards = random.choices(cards, weights=None, k=2)
user_score = sum(user_cards)
dealer_cards = random.choices(cards, weights=None, k=2)
dealer_score = sum(dealer_cards)


def status():
    return True


while not end_of_game:

    # Display stats
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {dealer_cards[0]}")

    # User Input
    prompt = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    user_decision = True if (prompt == 'y') else False if (prompt == 'n') else None

    if user_decision:  # If user decides to take a card
        user_cards += random.choices(cards, weights=None)  # Add card to the user_cards
        user_score = sum(user_cards)  # Compute cumulative score
        if user_score > 21:  # Check if the score crosses threshold
            print("You went over, you lose.")
            end_of_game = status()
        elif user_score == 21:  # Check if the score matches threshold
            print("You got 21, you win.")
            end_of_game = status()
        else:  # Continue if the score is less
            pass
    else:
        while not end_of_game:
            end_of_game = status()
