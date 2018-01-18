from card import *
from hand import *
from reader import *

class BJController(object):
	"""docstring for BJController"""
	def __init__(self,name):
		self.__player = PlayerHand(name)
		self.__dealer = Hand()
		self.__deck = Deck()


	def play(self): 
    print("== new game ==") 
    player = self.__player 
    dealer = self.__dealer 
    deck = self.__deck 
    
    player.get(deck.next()) 
    dealer.get(deck.next()) 
    player.get(deck.next()) 
    dealer.get(deck.next(open=False)) 
    
    print("Dealer :", dealer) 
    print(player.name, ":", player) 
    if player.total == 21: 
        print("Blackjack!", player.name, "wins.") 
        player.earn_chips(2) 
    else: 
        while player.total < 21 and \
              Reader.ox(player.name + ": Hit?(o/x) "): 
            player.get(deck.next()) 
            print(player.name, ":", player) 
        if player.total > 21: 
            print(player.name, "busts!") 
            player.lose_chips(1) 
        else: 
            while dealer.total <= 16: 
                dealer.get(deck.next()) 
            if dealer.total > 21: 
                print("Dealer busts!") 
                player.earn_chips(1) 
            elif dealer.total == player.total: 
                print("We draw.") 
            elif dealer.total > player.total: 
                print(player.name, "loses.") 
                player.lose_chips(1) 
            else: 
                print(player.name, "wins.") 
                player.earn_chips(1) 
        dealer.open() 
        print("Dealer :", dealer) 
    player.clear() 
    dealer.clear()

    def main(): 
	   print("Welcome to SMaSH Casino!") 
	    name = Reader.register() 
	    game = BlackjackController(name) 
	    while True: 
	        game.play() 
	        if not Reader.ox("Play more, " + name + "? (o/x) "): 
	            break 
	    print("Bye, " + name + "!")
			
		
		
		
		
		
		
		
		