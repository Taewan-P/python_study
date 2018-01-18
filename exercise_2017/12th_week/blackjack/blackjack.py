# Blackjack Contoller
import bjcards
from bjcards import *
from reader import *

class BJController(object):
    DEALER_NAME = "Smavi"
    def __init__(self,names):
        self.players = []
        for n in names:
            p = BJPlayer(n)
            self.players.append(p)
        self.dealer = BJDealer(BJController.DEALER_NAME)
        self.deck = BJDeck()
        self.deck.fresh_deck()
        
    def play(self):
        players = self.players
        dealer = self.dealer
        deck = self.deck
        # 카드 나눠주기
        for p in players:
            deck.deal(p,open=True)
        deck.deal(dealer,open=True)
        for p in players:
            deck.deal(p,open=True)
        deck.deal(dealer)
        # 카드 보여주기 & 원하면 더 주기
        print(BJController.DEALER_NAME, ":", dealer)
        print('---')
        for p in players:
            print(p.name, ":", p)
            while p.hit():
                deck.deal(p,open=True)
                print(p.name, ":", p)
            if p.blackjack():
                print("Blackjack!")
            elif p.busted():
                print("Bust!")
        while dealer.hit():
            deck.deal(dealer,open=True)
        print('---')
        # 보여주기
        dealer.open()
        print(dealer.name, ":", dealer)
        if dealer.busted():
            print("Bust!")
        for p in players:
            if p.blackjack():
                #print("Blackjack!")
                #p.win()
                p.earn_chips(2)
            else:
                if p.busted():
                    #p.bust()
                    p.lose_chips(1)
                else:
                    if dealer.busted():
                        p.earn_chips(1)
                    elif dealer.total == p.total:
                        pass
                        #print(p.name, "draws.")
                    elif dealer.total > p.total:
                        #p.lose()
                        p.lose_chips(1)
                    else:
                        #p.win()
                        p.earn_chips(1)
        for p in players:
            print(p.name, ":", p)
            p.print_chips()
            p.clear()
        dealer.clear()

def main():
    print("Welcome to SMaSH Casino!")
    head_count = Reader.get_number("How many players? (1-4) ",1,4)
    names = []
    for i in range(head_count):
        s = input("Guest #" + str(i+1) + ", Enter your name : ")
        names.append(s)
    game = BJController(names)
    while True:
        print("== new round ==")
        game.play()
        if not Reader.ox("Play more? (o/x) "):
            break
    print("Bye, everyone!")
    
main()
