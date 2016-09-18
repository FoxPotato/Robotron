import serial
from vision import Vision

class Program():
	def __init__(self):
		self.serial = serial.Serial()
		self.serial.baudrate = 115200
		self.serial.port = '/dev/ttyAMA0'

	def run(self):
		print("Start " + self.name + "\n")
		self.serial.open()

	def quit(self):
		print("\nStop " + self.name)
		self.serial.close()

	def observe(self):
		pass

class Guard(Program):
	def __init__(self):
		super().__init__()
		self.name = "Guard"

		self.vision = Vision()

	def run(self):
		super().run()

		

		while True:
			movement = self.vision.findMovement()

			if movement is None:
				print("No movement found")
			else:
				print("Movement found at " + str(movement[0]) + ", " + str(movement[1]))

			value = input("\nQuit? y/n ")
			if value == "y":
				break;

		self.quit()

	def quit(self):
		super().quit()
		self.vision.quit()

class Pet(Program):
	def __init__(self):
		super().__init__()
		self.name = "Pet"

	def run(self):
		super().run()

		while True:
			self.serial.write(b's1 45\n')

			value = input("Quit? y/n ")
			if value == "y":
				break;

		self.quit()
