import serial

class Actuator():
	def __init__(self):
		self.serial = serial.Serial()
		self.serial.baudrate(115200)
		self.serial.port("/dev/ttyAMA0")

	def start(self):
		self.serial.open()

	def stop(self):
		self.serial.close()

	def setServoAngle(index, angle):
		self.serial.write("s" + str(index + 1) + " " + str(angle) + "\n")
