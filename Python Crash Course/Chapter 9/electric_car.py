from car import Car

class Battery():

	def __init__(self,battery_size=70):
		self.battery_size = battery_size


	def describe_battery(self):
		print("This car has " + str(self.battery_size) +"-kWh battery.")

	def get_range(self):
		if self.battery_size == 70:
			range = 240
		elif self.battery_size == 80:
			range = 270

		msg = "This car can go about " + str(range) + " miles on a full charge."
		print(msg)



#创建子类时，superclass必须包含在当前文件中，且位于子类前面。
class ElectricCar(Car):

	def __init__(self, make, model, year):
		#让Python调用父类方法————__init__()，让ElectricCar实例包含父类的所有属性
		super().__init__(make, model, year)
		self.battery = Battery()