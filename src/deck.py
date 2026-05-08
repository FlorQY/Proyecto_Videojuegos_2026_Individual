import random
from src.card import Card

class Deck:

    def __init__(self):
        self.cards = []
        self.create_deck()
        self.shuffle()

    def create_deck(self):

        colors = ["Red", "Blue", "Green", "Yellow"]

        for color in colors:
            for number in range(10):
                self.cards.append(Card(color, str(number)))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):

        if len(self.cards) > 0:
            return self.cards.pop()

        return None