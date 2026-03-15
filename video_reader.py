import cv2
from config import PROCESS_FPS

class VideoReader:

    def __init__(self, video_path):

        self.cap = cv2.VideoCapture(video_path)

        if not self.cap.IsOpened():
            raise Exception("Erro ao abrir video")
        
        self.fps = self.cap.get(cv2.CAP_PROP_FPS)
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

        self.frame_interval = max(1, int(self.fps / PROCESS_FPS))

        self.frame_count = 0

    def read(self):

        ret, frame = self.cap.read()

        if not ret:
            return None
        
        self.frame_count += 1

        process = self.frame_count % self.frame_interval == 0

        return frame, process
    
    def release(self):
        self.cap.release()