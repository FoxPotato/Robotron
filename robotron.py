from program import Guard, Pet

class Robotron():
	def __init__(self):
		self.VERSION_MAIN = 0
		self.VERSION_SUB = 1
		self.VERSION_DEBUG = 0

		self.program = None

		print("Robotron v" + str(self.VERSION_MAIN) + "." + str(self.VERSION_SUB) + "." + str(self.VERSION_DEBUG))

	def queryProgram(self):
		while True:
			program = input("Select program: ")

			if program == "shutdown":
				return 0
			elif program == "guard":
				self.program = Guard()
				return
			elif program == "pet":
				self.program = Pet()
				return

			print("Program does not exist.")
			print("Available programs: guard, pet, shutdown")

	def runProgram(self):
		self.program.run()
		return

	def quit(self):
		print("Robotron shutting down.")

robotron = Robotron()

while (True):
	program = robotron.queryProgram()

	if program == 0:
		break
	else:
		robotron.runProgram()

robotron.quit()
