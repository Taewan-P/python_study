class Reader:
	@staticmethod
	def resister():
		return input("Enter your name : ")


	@staticmethod
	def ox(message):
		response = input(message).lower()
		while not (response == 'o' or response == 'x'):
			response = input(message).lower()
		return response == 'o'






		