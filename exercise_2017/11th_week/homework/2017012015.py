#속성변수 : name,balance 
class BankAccount:
	__no_of_accounts = 0

	def __init__(self,n,b = 0):
		"""
		Hello! This is a DocString.
		n -> __name & b -> __balance
		__no_of_accounts -> numbers of accounts save in BankAccount Class
		"""
		self.__name = n
		self.__balance = b
		if self.__balance < 0:
			self.__balance = 0

		print("A bank account for " + self.__name + " is open.")
		print("Your current balance is " + str(self.__balance) + " won.")
		BankAccount.__no_of_accounts += 1
		


	def __str__(self):
		"""Shows not address but string"""
		return self.__name + "'s BankAccount object"


	@staticmethod
	def count_accounts():
		"""Prints number of accounts"""
		return BankAccount.__no_of_accounts

	
	def show_balance(self):
		"""Prints how much balance someone has."""
		print(self.__name + "'s balance is " + str(self.__balance) + " won.")
		


	def deposit(self,amount):
		"""Deposits money to someone's account"""
		if int(amount) >= 0:
			self.__balance += int(amount)
			print(str(amount) + " won has been successfully deposited.")
			self.show_balance()
		else:
			print("Deposit failed.")
			self.show_balance()


	def withdraw(self,amount):
		"""Withdraws money from someone's account"""
		if amount >= 0 and self.__balance >= amount:
			self.__balance -= amount
			print(str(amount) + " won has been successfully withdrawn.")
			self.show_balance()
		else:
			print("Withdraw failed.")
			self.show_balance()







