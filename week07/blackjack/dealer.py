from deck import Deck
from random import randint


class Dealer:
    """
    A blackjack dealer
    """

    def __init__(self):
        DEALER_RANGE = (17, 21)
        self._score = randint(*DEALER_RANGE)  # randint takes two argvs, *?
        # * will unpack the tuple into the argument
        # _score is an info hiding
        # It means other objects could not access this data
        # It keeps it private
        self._deck = Deck()

    def deal_one(self):
        """
        Deal a single card from the deck
        """
        return self._deck.deal_one()
    
    property  # what does it mean?

    def score(self):
        """
        Getter for score
        """
        return self._score
