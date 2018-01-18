class Hand:
	def __init__(self, name = "Dealer"):
		self.__name = name
		self.__hand = []

	@property
	def name(self):
		return self.__name

	@property
	def total(self):
		point = 0
		number_of_ace = 0
		for card in self.__hand:
			if card.rank == 'A':
				point += 11
				number_of_ace += 1
			else:
				point += card.value
		while point > 21 and number_of_ace > 0:
			point -= 10
			number_of_ace -= 1
		return point

	def get(self,card):
		#important
		self.__hand.append(card)

	
	def clear(self):
		self.__hand = []

	
	def open(self):
		for card in self.__hand:
			if(not card.face_up)
			card.flip()

	def hand(self)

class PlayerHand(Hand): #괄호안에 들어가는게 superclass 
	
	def __init__(self,name):
		super().__init__(name) #부모 클래스의 init 을 불러오는것!
		self.__chips = 0

	# def __str__(self):
	# 	show = "[" + str(self.total) + "]"
	# 	for 


	def earn_chips(self,n):
		self.__chips += n
		print("You have" , self.__chips, "chips.")


	def lose_chips(self,n):
		self.__chips -= n
		print("You have ", self.__chips, "chips")








