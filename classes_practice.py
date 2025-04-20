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

# bank.display_balance()
# bank.deposit(1200)
# bank.withdraw(300)
# bank.display_balance()

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

# CircleArea(2)


class Student(object):
	# a class variable to keep track of the total number of students
	total_students = 0

	def __init__(self, name, age, major, gpa, year):
		self.name = name
		self.age = age
		self.major = major
		self.gpa = gpa
		self.year = year

		Student.total_students += 1  # Increment the total_students count

	def get_details(self):
		print(f'''Name: {self.name}
Age: {self.age}
Major: {self.major}
GPA: {self.gpa}
Year: {self.year}

Total number of students in class: {Student.total_students}''')

	def update_age(self):
		# increase the student's age by 1 each time it is called
		self.age += 1

	def update_major(self, new_major):
		# takes a single parameter new_major and updates the student's major attribute to a new value
		self.major = new_major


# instances of the Student class
student1 = Student(
	name="Aisha Khan",
	age=19,
	major="Biology",
	gpa=3.9,
	year=2
)

student2 = Student(
	name="Carlos Alvarez",
	age=21,
	major="Mechanical Engineering",
	gpa=3.5,
	year=3
)

student3 = Student(
	name="Maya Patel",
	age=18,
	major="Physics",
	gpa=3.7,
	year=1
)

# # all students
# print(f'''Student 1:
# Name: {student1.name}
# Age: {student1.age}
# Major: {student1.major}
# GPA: {student1.gpa}
# Year: {student1.year}''')
# print("")
# print(f'''Student 2:
# Name: {student2.name}
# Age: {student2.age}
# Major: {student2.major}
# GPA: {student2.gpa}
# Year: {student2.year}''')
# print("")
# print(f'''Student 3:
# Name: {student3.name}
# Age: {student3.age}
# Major: {student3.major}
# GPA: {student3.gpa}
# Year: {student3.year}''')
# print("")

# print(f"Total number of students: {Student.total_students}")

# print(student1.get_details())
# print('')
# student1.update_age()
# student1.update_major(new_major="Molecular Biology")
# print(student1.get_details())
# print('')
# print(student2.get_details())
# print('')
# print(student3.get_details())

# HonorsStudent class, inheriting from Student
class HonorsStudent(Student):

	def __init__(self, name, age, major, gpa, year, honors_program):
		self.honors_program = honors_program
		super().__init__(name, age, major, gpa, year)

	# updated
	def get_details(self):
		print(f'''Name: {self.name}
Age: {self.age}
Major: {self.major}
GPA: {self.gpa}
Year: {self.year}
Honors Program: {self.honors_program}

Total number of students in class: {Student.total_students}''')


# an instance of the HonorsStudent class
honor_student = HonorsStudent(
	name="David Kim",
	age=20,
	major="Computer Science",
	gpa=3.9,
	year="Junior",
	honors_program="STEM Honors"
)

# honor_student.update_age()
# honor_student.get_details()

class Patient(object):
	'''
		Attributes:
		name: Patient name
		age: Patient age
		conditions: Existing medical conditions
	'''

	status = 'patient'

	def __init__(self, name, age):
		self.name = name
		self.age = age
		self.conditions = []

	def get_details(self):
		print(f'Patient record: {self.name}, {self.age} years.' \
		      f' Current information: {self.conditions}.')

	def add_info(self, information):
		self.conditions.append(information)

# steve = Patient('Steven Hughes',48)
# abigail = Patient('Abigail Sandwick',32)

class Infant(Patient):
	'''
	Patient under 2 years
	'''

	def __init__(self, name, age):
		self.vaccinations = []
		super().__init__(name, age)

	def add_vac(self, vaccine):
		self.vaccinations.append(vaccine)

	def get_details(self):
		print(f'Patient record: {self.name}, {self.age} years.' \
		      f' Patient has had {self.vaccinations} vaccines.' \
		      f' Current information: {self.conditions}.' \
		      f'\n{self.name} IS AN INFANT, HAS HE HAD ALL HIS CHECKS?')


# archie = Infant('Archie Fittleworth',0)
# archie.add_vac('MMR')
