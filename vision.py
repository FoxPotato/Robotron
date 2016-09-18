import imutils
import cv2

class Vision():
	def __init__(self):
		# Initialize a videocapture using the webcam
		self.capture = cv2.VideoCapture(0)
		self.capture.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
		self.capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
		self.minArea = 1200
		self.maxArea = 25000
		print(str(self.capture.get(cv2.CAP_PROP_FRAME_WIDTH)));
		
		# Initialize the first frame
		self.firstFrame = self.getNextFrame()

		self.changedPosition = False

	def findMovementDebug(self):
		changedPosition = False

		while True:
			self.frame = self.getNextFrame()

			frameDelta = cv2.absdiff(self.firstFrame, self.frame)
			threshold = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
			threshold = cv2.dilate(threshold, None, iterations=2)

			(image, contours, hierarchy) = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

			for contour in contours:
				area = cv2.contourArea(contour)
				if area < self.minArea:
					continue
				elif area > self.maxArea:
					changedPosition = True
					continue

				(x, y, w, h) = cv2.boundingRect(contour)
				cv2.rectangle(self.frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

				position = (0.5 * (2 * x + w), 0.5 * (2 * y + h))
				cv2.putText(self.frame, str(position), (int(position[0]), int(position[1])), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))

			cv2.imshow("Frame", self.frame)
			cv2.imshow("Threshold", threshold)
			cv2.imshow("Delta", frameDelta)

			key = cv2.waitKey(1) & 0xFF
			if key == ord("q"):
				break

			if changedPosition:
				self.firstFrame = self.getNextFrame()
				changedPosition = False

		cv2.destroyAllWindows()

	def findMovement(self):
		#self.findMovementDebug()
		#pass

		if self.changedPosition:
			self.getNextFrame()
			self.changedPosition = False
                
		self.frame = self.getNextFrame()

		# Compute the difference 
		frameDelta = cv2.absdiff(self.firstFrame, self.frame)
		threshold = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
		threshold = cv2.dilate(threshold, None, iterations=2)

		(image, contours, hierarchy) = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

		for contour in contours:
			area = cv2.contourArea(contour)
			if area < self.minArea:
				return None
			elif area > self.maxArea:
				self.changedPosition = True
				return None

			(x, y, w, h) = cv2.boundingRect(contour)

			return (0.5 * (2 * x + w), 0.5 * (2 * y + h))

	def getNextFrame(self):
		# Get a frame from the capture
		(grabbed, frame) = self.capture.read()
		#frame = imutils.resize(frame, width=500)

		# Convert captured frame to grayscale and blur it
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		gray = cv2.GaussianBlur(gray, (21, 21), 0)		
		
		return gray

	def findFace(self):
		pass

	def quit(self):
		self.capture.release()
