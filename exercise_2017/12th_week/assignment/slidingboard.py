class SlidingBoard:
	"""docstring for SlidingBoard"""
	#init =>> constructor
	def __init__(self,size):
		self.__board = SlidingBoard.create_init_board(size)
		self.__empty = SlidingBoard.find_position(self,0)
		self.__size = size


	@property
	def board(self):
		return self.__board


	@staticmethod
	def create_init_board(size):
		import random

		grouped = []
		not_grouped = random.sample(range(0,size**2),size**2)

		for i in range(0,size):
			temp = []
			for j in range(0,size): #리스트 안에 리스트 넣는거
				temp.append(not_grouped[j])
			not_grouped = not_grouped[size:]
			grouped.append(temp)
		
		return grouped

	@staticmethod
	def create_goal_board(size):
		board_1 = []
		goal_board = []
		for i in range(1,(size**2)+1):
			board_1.append(i)

		for h in range(0,size):
			temp = []
			for j in range(0,size):
				temp.append(board_1[j])
			board_1 = board_1[size:]
			goal_board.append(temp)

		goal_board[size-1][size-1] = 0
		return goal_board


	def find_position(self,num):
		for i in range(len(self.__board)):
			for j in range(len(self.__board)):
				if num == self.__board[i][j]:
					return (i,j)

	def move(self,pos):
		(x,y) = pos
		if self.__empty == (x-1,y) or self.__empty == (x+1,y) or self.__empty == (x,y-1) or self.__empty==(x,y+1):
			self.__board[self.__empty[0]][self.__empty[1]] = self.__board[x][y]
			self.__board[x][y] = 0
			self.__empty = (x,y)
		else:
			print("Can't move! Try again.")

	def print_board(self):
		for row in self.__board:
			for num in row:
				if num == 0:
					print("  ",end = ' ')
				elif 10 <= num:
					print(num,end = ' ')
				else: #num 이 한자리 수인 경우
					print(str(num).rjust(2), end = ' ')
			print()




class SlidingPuzzleController:

	def __init__(self,size):
		self.__size = size
		self.__slider = SlidingBoard(size)
		self.__goal = SlidingBoard.create_goal_board(self.__size)
		


	def play(self):
		size = self.__size
		goal = self.__goal
		empty = self.__slider.find_position(0)
		while True:
			SlidingBoard.print_board(self.__slider)
			if self.__slider.board == self.__goal:
				print("Congratulations!")
				break
			num = Reader.get_number(self.__size)
			if num == 0:
				break
			pos = self.__slider.find_position(num)
			self.__slider.move(pos)
		print("Please come again.")





class Reader:
	@staticmethod
	def get_number(size):
		num = input("Type the number you want to move (Type 0 to quit): ")
		while not (num.isdigit() and 0 <= int(num) <= size * size - 1):
			num = input("Type the number you want to move (Type 0 to quit): ")
		return int(num)

def main():
	if __name__ == "__main__":
		import sys
		size = sys.argv[1]
		if size.isdigit() and int(size) > 1:
			SlidingPuzzleController(int(size)).play()
		else:
			print("Not a proper system argument.")

main()

















