colors = {'H', 'S', 'C', 'D'}
CARDS = ['A', *[str(x) for x in range(1, 11)], 'J', 'K', 'Q']
VALUES = [1] + [i for i in range(1, 11)] + [10] * 3

cards = [color + value for color in colors for value in CARDS]

for card in zip(cards, VALUES):
    print(card)
