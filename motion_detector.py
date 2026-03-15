import cv2

class MotionDetector:

    def __init__(self, threshold=25):
        self.prev_frame = None
        self.threshold = threshold

    def detect(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        if self.prev_frame is None:
            self.prev_frame = gray
            return True
        
        frame_delta = cv2.absdiff(self.prev_frame, gray)

        thresh = cv2.threshold(frame_delta, 25, 255, cv2.THRESH_BINARY)[1]

        motion = thresh.sum() > self.threshold * 1000

        self.prev_frame = gray

        return motion