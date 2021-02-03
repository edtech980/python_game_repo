#Deck of playing cards for a kassino game
#Kassi Kassino Version 1

class card(object):
    """A playing card."""
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep
