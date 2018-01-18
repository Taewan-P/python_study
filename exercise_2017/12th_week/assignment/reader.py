class Reader:
	@staticmethod
	def get_number(size):
		num = input("Type the number you want to move (Type 0 to quit): ")
		while not (num.isdigit() and 0 <= int(num) <= size * size - 1):
			num = input("Type the number you want to move (Type 0 to quit): ")
		return int(num)

