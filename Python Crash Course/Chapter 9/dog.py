class Dog():

	def __init__(self, name, age):
		self.name = name
		self.age = age

	def sit(self):
		print(self.name.title() + " is now sitting.")

	def roll_over(self):
		print(self.name.title() + " rolled over")


my_dog = Dog('Frank', 6)
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('Tom', 3)
your_dog.sit()
your_dog.roll_over()