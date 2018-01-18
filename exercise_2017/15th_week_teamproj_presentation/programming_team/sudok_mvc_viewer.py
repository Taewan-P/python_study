class Hogaeng:
	"""docstring for Hogaeng"""

		

	@staticmethod
	def get_level(): # 레벨 설정 >> 빈칸의 갯수로 난이도를 설정
		level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
		while level not in {"상", "중", "하"}:
			level = input("난이도 (상중하) 중에서 하나 선택하여 입력: ")
		if level == '상':
			return 40
		elif level == '중':
			return 34
		else:
			return 28

	@staticmethod
	def show_board(board): # modify for gui programming
		print()
		print('S', '|', '1', '2', '3', '4', '5', '6', '7', '8', '9')
		print('-', '+', '-', '-', '-', '-', '-', '-', '-', '-', '-')
		i = 1
		for row in board:
			print(i, end=' ')
			print('|', end=' ')
			for entry in row:
				if entry == 0:
					print('.', end=' ')
				else:
					print(entry, end=' ')
			print()
			i += 1
		print()


	@staticmethod #정수 입력 오류가 났을때에는 get_integer(여기) 를 수정해 볼것!
	def get_integer(message, i, j): #입력받은 값이 정수인지 확인하는 함수 
		number = input(message)
		while not (number.isdigit() and i <= int(number) <= j):
			number = input(message)
		return int(number)