# Playing Cards

class Card(object):
    SUITS = ["Diamond", "Heart", "Spade", "Clover"]
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
        
    def __init__(self, suit, rank, face_up=True):
        if suit in Card.SUITS and rank in Card.RANKS:
            self.suit = suit
            self.rank = rank
            self.face_up = face_up
        else:
            print("Error: Not a right suit or rank")

    def __str__(self):
        if self.face_up:
            return self.suit + "." + self.rank
        else:
            return "XXX"
            
    def flip(self):
        self.face_up = not self.face_up


class Hand(object):
    def __init__(self):
        self.cards = []
        
    def __str__(self):
        if len(self.cards) == 0:
            show = "empty"
        else:
            show = ""
            for card in self.cards:
                show += str(card) + " "
        return show

    def clear(self):
        self.cards = []
    
    def add(self,card):
        self.cards.append(card)
        
    def give(self,card,hand):
        self.cards.remove(card)
        hand.add(card)

class Deck(Hand):
    def fresh_deck(self):
        self.cards = []
        for s in Card.SUITS:
            for r in Card.RANKS:
                self.cards.append(Card(s,r,False))
        import random
        random.shuffle(self.cards)
        
    def deal(self,hand,how_many=1,open=False):
        if self.cards == []:
            self.fresh_deck()
        for _ in range(how_many):
            card = self.cards[0]
            if open :
                card.flip()
            self.give(card,hand)
        


