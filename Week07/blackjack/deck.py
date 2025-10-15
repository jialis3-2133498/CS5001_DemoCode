from card import Card
from random import shuffle


class Deck:
    """
    A deck of cards
    """

    def __init__(self):
        """
        Construct a deck of cards
        """
        suits = ['hearts', 'spades', 'diamonds', 'clubs']
        ranks = ['ace', '2', '3', '4', '5', '6', '7', '8', '9',
                 '10', 'jack', 'queen', 'king']
        self.cards = [Card(suit, rank)
                      for suit in suits
                      for rank in ranks]
        shuffle(self.cards)

    def deal_one(self):
        """
        Deal one card from the deck
        """
        return self.cards.pop()
