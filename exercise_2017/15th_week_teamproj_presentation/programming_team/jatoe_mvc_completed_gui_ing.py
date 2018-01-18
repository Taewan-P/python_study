# 수독 9x9
import random
from tkinter import *

#Model

class Board:
	@staticmethod
	def create_board():
		"""create initial board"""
		seed = [1, 2, 3, 4, 5, 6, 7, 8, 9]
		random.shuffle(seed)
		n1 = seed[0]
		n2 = seed[1]
		n3 = seed[2]
		n4 = seed[3]
		n5 = seed[4]
		n6 = seed[5]
		n7 = seed[6]
		n8 = seed[7]
		n9 = seed[8]
		return [[n1, n2, n3, n4, n5, n6, n7, n8, n9],
				[n4, n5, n6, n7, n8, n9, n1, n2, n3],
				[n7, n8, n9, n1, n2, n3, n4, n5, n6],
				[n2, n3, n1, n5, n6, n4, n8, n9, n7],
				[n5, n6, n4, n8, n9, n7, n2, n3, n1],
				[n8, n9, n7, n2, n3, n1, n5, n6, n4],
				[n3, n1, n2, n6, n4, n5, n9, n7, n8],
				[n6, n4, n5, n9, n7, n8, n3, n1, n2],
				[n9, n7, n8, n3, n1, n2, n6, n4, n5]]

	def shuffle_ribbons(self, board):
		"""한줄씩 가로로 세칸을 서로 섞기"""
		self.sboard=board
		top = self.sboard[:3]
		middle = self.sboard[3:6]
		bottom = self.sboard[6:]
		random.shuffle(top)
		random.shuffle(middle)
		random.shuffle(bottom)
		self.sboard=top+middle+bottom
		return self.sboard

	def transpose(self, board):
		"""우하향 대각선을 기준으로 히오스"""
		self.tboard=board
		self.transposed = []
		for _ in range(len(self.tboard)):
		    self.transposed.append([])
		for row in self.tboard:
		    i = 0
		    for entry in row:
		        self.transposed[i].append(entry)
		        i += 1
		return self.transposed

	def create_solution_board(self):
		"""스독을 만드는 방법으로 만들기"""
		self.board = Board.create_board()
		Board.shuffle_ribbons(self, self.board)
		Board.transpose(self, self.sboard)
		Board.shuffle_ribbons(self, self.tboard)
		Board.transpose(self, self.sboard)
		self.board=self.tboard
		return self.board

	def copy_board(self, board):
		"""게임을 진행할 보드를 복제하기"""
		board_clone = []
		for row in board :
		    row_clone = row[:]
		    board_clone.append(row_clone)
		return board_clone

	def make_holes(self, board, no_of_holes):
		"""make a holes by level"""
		hboard=board
		holeset = set()
		while no_of_holes > 0:
			i = random.randint(0, 8)
			j = random.randint(0, 8)
			if hboard[i][j] != 0:
				hboard[i][j] = 0
				holeset.add((i, j))
				no_of_holes -= 1 
		return (hboard, holeset)

#View

class Hogaeng:
	@staticmethod
	def get_level():
		"""빈칸의 갯수로 난이도를 설정"""
		Label(self, text='Level:').grid(sticky=W)
		self.level=StrigVar()
		self.level.set(None)
		Radiobutton(self, text='Hard', variable=Hard, value='H').grid()
		Radiobutton(self, text='Normal', variable=Normal, value='N').grid()
		Radiobutton(self, text='Easy', variable=Easy, value='E').grid()

		if self.level.get() == 'H':
			return 40
		elif self.level.get() == 'N':
			return 34
		elif self.level.get()=='E':
			return 28

	@staticmethod
	def show_board(board):
		"""modify for gui programming"""
		print()
		print('S', '|', '1', '2', '3', '4', '5', '6', '7', '8', '9')
		print('-', '+', '-', '-', '-', '-', '-', '-', '-', '-', '-')
		i = 1
		for row in board:
			print(i, end=' ')
			print('|', end=' ')
			for entry in row:
				if entry == 0:
					print(' ', end=' ')
				else:
					print(entry, end=' ')
			print()
			i += 1
		print()

	@staticmethod
	def get_integer(message, i, j): 
		"""입력받은 값이 정수인지 확인하는 함수"""
		number = input(message)
		while not (number.isdigit() and i <= int(number) <= j):
			number = input(message)
		return int(number)

#Controllor
class SudokControllor:
	def __init__(self):
		"""set a initial attribute"""
		self.sudok=Board()  # object
		self.solution = self.sudok.create_solution_board()
		self.no_of_holes = Hogaeng.get_level()
		self.puzzle = self.sudok.copy_board(self.solution)
		(self.puzzle, self.holeset) = self.sudok.make_holes(self.puzzle, self.no_of_holes)

		window=Tk()
		window.title("jatoe")
		window.geometry()
		window.mainloop()

	def play(self):
		"""play sudok game"""
		Hogaeng.show_board(self.puzzle)
		while self.no_of_holes > 0:
			i = Hogaeng.get_integer("row number(1~9): ", 1, 9) - 1
			j = Hogaeng.get_integer("column number(1~9): ", 1, 9) - 1
			if (i, j) not in self.holeset:
				print("It already has a number.")
				continue
			n = Hogaeng.get_integer("number(1~9): ", 1, 9)
			sol = self.solution[i][j]
			if n == int(sol):
				self.puzzle[i][j] = sol
				Hogaeng.show_board(self.puzzle)
				self.holeset.remove((i, j))
				self.no_of_holes -= 1
			else:
				print(n, "is a wrong number. HAHAHAHA! Try again.")
		print("Good job. Never come back!")


SudokControllor().play()