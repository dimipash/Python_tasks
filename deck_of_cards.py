suits = ['H', 'S', 'C', 'D']  # Hearts, Spades, Clubs, Diamonds
cards = ['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']


def card_value(card):
    """
        This function returns the value of a card.

        Args:
            card (str): The card to get the value of.

        Returns:
            int: The value of the card.
    """
    return {'A': 1}.get(card, int(card) if card.isdigit() else 10)


def generate_deck():
    """
        This function generates a deck of cards.

        Returns:
            list: A list of tuples, where each tuple represents a card and its value.
    """
    deck = [(suit + card, card_value(card)) for suit in suits for card in cards]
    return deck


cards = generate_deck()
for card in cards:
    print(card)
