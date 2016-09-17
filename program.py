import serial

class Program():
	def __init__(self):
		#self.serial = serial.Serial()
		pass

	def run():
		pass

class Guard(Program):
	def __init__(self):
		self.name = "Guard"

	def run(self):
		print("Start " + self.name)

		while True:
			value = input("Quit? y/n ")
			if value == "y":
				break;

		print("Stop " + self.name)

class Pet(Program):
	def __init__(self):
		self.name = "Pet"

	def run(self):
		print("Start " + self.name)

		while True:
			value = input("Quit? y/n ")
			if value == "y":
				break;

		print("Stop " + self.name)
