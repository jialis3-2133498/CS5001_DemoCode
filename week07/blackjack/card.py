class Card:
    """
    A playing card
    """
    def __init__(self, suit, rank):
        """
        Construct a card object
        """
        self.suit = suit
        self.rank = rank

    def __str__(self):
        # __str__ means a special method
        # It prints out the object Card
        # We need to call it by print()
        """
        Provide a string representation of a card object
        """
        return f"{self.rank} of {self.suit}"

    def num_value(self):
        """
        Return the card's numerical value
        """
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
