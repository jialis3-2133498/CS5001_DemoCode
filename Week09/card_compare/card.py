class Card:
    """A playing card"""
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        """Return a user friendly string for the card"""
        return self.rank + " of " + self.suit
    
    def __repr__(self):
        return (f"{self.__class__.__name__}:"  # Access the name of the object
                f"(suit: {self.suit}, rank: {self.rank})")
    # What is __repr__?

    def __eq__(self, other):
        """
        Return a boolean representing equality of cards
        Other is another card
        """
        return (self.rank == other.rank and self.suit == other.suit)

    def __lt__(self, other):
        """
        Return a boolean representing less than
        """
        return (self.num_value < other.num_value)
    
    def __gt__(self, other):
        """
        Return a boolean representing less than
        """
        return (self.num_value > other.num_value)
    
    def __hash__(self):
        """
        Define objects' hash function so that the object
        can be used as the key of the dictionary.
        """
        return hash((self.suit, self.rank))
        # make sure hash function is consistant with __eq__ 
    
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
