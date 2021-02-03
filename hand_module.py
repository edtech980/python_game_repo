#A hand playing cards
from collections import Counter

class hand(object):
    """A hand of playing cards."""
    def __init__(self, name = None):
        self.cards = []
        self.name = name
        
        
    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "<empty>" 
        return rep

    def name(self):
        return str(self.name)
    
    
    def is_empty(self):
        return self.cards == []
    
    def throw_down(self, card, table):
        self.cards.remove(card)
        table.add(card)
        
    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

    def card_num(self):
        if self.cards:
            rep = []
            for card in self.cards:
                if len(str(card)) == 3:
                    rep.append(str(card)[0:2])
                else:
                    rep.append(str(card)[0])
        else:
            rep = "0"
                
        rep = Counter(rep)
        return rep
