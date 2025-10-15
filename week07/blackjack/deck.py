from card import Card
from random import shuffle


class Deck:
    """
    A deck of cards
    """
    def __init__(self):
        """
        Construct a deck of card
        """
        suits = ["hearts",
                 "spcae",
                 "diammond",
                 "clubs"]
        ranks = ["ace", "2", "3", "4", "5"
                 "6", "7", "8", "9", "jack"
                 "queen", "king"]
        self.cards = [Card[suit, rank]
                      for suit in suits
                      for rank in ranks]
        shuffle(self.cards)

    def deal_one(self):
        """
        Deal one card from the dock
        """
        return self.cards.pop() 
        # pop() is the opposite of the append()
