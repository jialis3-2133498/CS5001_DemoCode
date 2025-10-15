class Hand:
    """
    A hand of cards
    """

    def __init__(self, BLACKJACK):
        self.BLACKJACK = BLACKJACK
        self.cards = []
        self.has_ace = False

    def receive_card(self, card):
        """
        Receive a card
        """
        if card.rank == "ace" and not self.has_ace:
            self.has_ace = True
        self.cards.append(card)

    def display(self):
        """
        Print out the hand
        """
        print("Player hand:")
        for card in self.cards:
            print(card)

    def score(self):
        """
        Calculate and return the score
        """
        score = sum([c.num_value() for c in self.cards])
        ACE_BOOST = 10
        if score <= self.BLACKJACK - 10:
            if self.has_ace:
                score += ACE_BOOST
        return score
