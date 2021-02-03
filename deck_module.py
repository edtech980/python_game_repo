#A deck of cards
#Kassi Kassino version 1

from hand_module import hand
from card_module import card

class deck(hand):
    """A deck of playing cards."""
    def populate(self):
        for suit in card.SUITS:
            for rank in card.RANKS:
                self.add(card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 10):
        
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Can't continue deal. Out of cards!")




