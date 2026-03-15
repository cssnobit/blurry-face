import cv2

class VideoWriter:

    def __init__(self, output_path, fps, width, height):
        
        self.out = cv2.VideoWriter(
            output_path,
            cv2.VideoWriter_fourcc(*'mp4v'),
            fps,
            (width, height)
        )

    def write(self, frame):
        self.out.write(frame)

    def release(self):
        self.out.release()