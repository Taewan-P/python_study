#5월 11일 목요일 프기 이론시간
#Object-Oriented Programming => 객체지향 프로그래밍
#객체는 속성,행위,속성변수,메소드를 가지고 있다.

"""
docstring 사용법  : 따옴표 3개

"""
import random
class Card: # 클래스 이름은 대문자로 시작하는 것이 관례이다.
	"""defines Card class"""
	__suits = ("Diamond", "Heart", "Spade", "Clover") # 입력 안하고 이렇게 설정 가능하지만,
	__ranks = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K") # 값을 마음대로 바뀔 수 있다... 그래서 속성 변수 앞에 __ 를 붙여주면 비공개가 된다.
	
	def __init__(self, s, r, fup = True): #첫번째 무조건 self : 자기 자신을 참조
		self.__suit = s
		self.__rank = r
		self.__faceup = fup
		print("asdf" + self.__suit)

########보안용 코드 짤때 사용########
	
	@property # 이걸 안달면 원래 card.suit() 이여야 하는데 card.suit 으로도 속성변수 참조가 가능하게끔 한다. //() 쓰면 오류남 // 그리고 사실 값은 __변수이름 에 들어가있다 (고급기능)
	def suit(self): # 공개용 메소드 => 이 함수를 통해서만 속성변수 접근하게끔 하는것!
		return self.__suit

	#@property 는 자기 밑에 하나의 함수에만 적용

	
	def __str__(self):
		if self.__faceup:
			return self.__suit + ":" + self.__rank
		else:
			return "(hidden)"

	def flip(self):
		self.__faceup = not self.__faceup

########보안용 코드 짤때 사용########

	# @staticmethod : object 가 없어도 부를수 있게끔 한다.
	@staticmethod
	#바깥에서는 못보는데 fresh_deck 을 통해서 __suit 를 부르는데 실제로 밖에서는 fresh_deck안에서 무슨 일이 일어나는지는 알수 없는거.
	def fresh_deck(): # 얘 는 self 가 필요없다.
		deck = []
		for s in Card.__suits: # 못읽는거 아님???? => Class안에서는 호출이 가능하다. + staticmethod 사용
			for r in Card.__ranks:
				deck.append(Card(s, r)) # 일딴 앞면으로 만듦
		random.shuffle(deck)
		return deck

		
		
		
		

