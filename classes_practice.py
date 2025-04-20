'''
Create a class to represent a bank account. It will need to have a balance,
a method of withdrawing money, depositing money and displaying the balance to the screen.
'''

class BankAccount(object):

	'''
	Attributes:
		balance
	'''

	def __init__(self, balance):
		self.balance = balance
	'''
	Methods:
	-withdraw
	-deposit
	-displaybalance
	'''

	def withdraw(self, amount):
		if amount <= self.balance:
			self.balance -= amount
			print('Success!')
			print(f'The current balance is: {self.balance}')
		else:
			print('Insufficient funds!')
			print(f'The current balance is: {self.balance}')

	def deposit(self, amount):
		self.balance += amount
		print('Success!')
		print(f'The current balance is: {self.balance}')

	def display_balance(self):
		print(f'The current balance is: {self.balance}')

bank = BankAccount(0)

bank.display_balance()
bank.deposit(1200)
bank.withdraw(300)
bank.display_balance()

'''
Create a circle class that will take the value of a radius and return the area of the circle
'''

class CircleArea(object):
	'''
	Attributes:
		radius
	'''

	def __init__(self, rad):
		self.rad = rad
		from math import pi
		print(f'You have entered a radius of: {rad}')
		print(f'The area of a circle is: {round(pi*(rad**2),2)}')

CircleArea(2)