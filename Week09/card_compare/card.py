class Card:
    """A playing card"""
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Return a user friendly string for the card"""
        return self.rank + " of " + self.suit

    @property
    def num_value(self):
        """Return the numerical value for the card"""
        ACE_VALUE = 1
        FACE_CARD_VALUE = 10
        if self.rank == "ace":
            return ACE_VALUE
        elif (self.rank == "jack" or
              self.rank == "queen" or
              self.rank == "king"):
            return FACE_CARD_VALUE
        else:
            return int(self.rank)
