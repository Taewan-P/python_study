#5월 18일 목요일 프기 이론시간

import random
class Card: 
	"""defines Card class"""
	__suits = ("Diamond", "Heart", "Spade", "Clover")
	__ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
	
	def __init__(self, s, r, fup = False): 
		if s in Card.__suits and r in Card.__ranks:
			self.__suit = s
			self.__rank = r
			self.__faceup = fup
		else:
			print("Error: Not a valid card")

		self.__value = Card.__ranks.index(self.__rank) + 1
		if self.__value > 10:
			self.__value = 10

	@property
	def suit(self): 
		return self.__suit

	@property
	def rank(self):
		return self.__rank

	@property
	def faceup(self):
		return self.__faceup

	
	def __str__(self):
		if self.__faceup:
			return self.__suit + ":" + self.__rank
		else:
			return "(hidden)"

	def flip(self):
		self.__faceup = not self.__faceup


	@staticmethod
	def fresh_deck(): # 얘 는 self 가 필요없다.
		deck = []
		for s in Card.__suits: 
				deck.append(Card(s, r))
		random.shuffle(deck)
		return deck


class Deck:
	def __init__(self):
		self.__deck = Card.fresh_deck()
		print("<< A brand-new deck of card! >>")

	def next(self,open = True):
		if self.__deck == []:
			self.__deck = Card.fresh_deck()
			print("<< A brand-new deck of card! >>")

		card = self.__deck.pop()
		if open:
			card.flip()
		return card

		
		
		
		
		
		
		

		
		
		
		

