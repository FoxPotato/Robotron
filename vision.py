import imutils
import cv2

class Vision():
	def __init__(self):
		# Initialize a videocapture using the webcam
		self.capture = cv2.VideoCapture(0)
		self.minArea = 0
		
		# Initialize the first frame
		self.firstFrame = self.getNextFrame()

	def findMovement(self):
		self.frame = self.getNextFrame()

		# Compute the difference 
		frameDelta = cv2.absdiff(self.firstFrame, self.frame)
		threshold = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
		threshold = cv2.dilate(threshold, None, iterations=2)

		(image, contours, hierarchy) = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

		for contour in contours:
			if cv2.contourArea(contour) < self.minArea:
				return None

			(x, y, w, h) = cv2.boundingRect(contour)
			cv2.rectangle(self.frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

			return (0.5 * (2 * x + w), 0.5 * (2 * y + h))

	def getNextFrame(self):
		# Get a frame from the capture
		(grabbed, frame) = self.capture.read()
		frame = imutils.resize(frame, width=500)

		# Convert captured frame to grayscale and blur it
		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		gray = cv2.GaussianBlur(gray, (21, 21), 0)		
		
		return gray

	def findFace(self):
		pass

	def quit(self):
		self.capture.release()
