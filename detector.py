from ultralytics import YOLO
from config import MODEL_PATH

class PersonDetector:

    def __init__(self):
        self.model = YOLO(MODEL_PATH)

    def detect(self, frames):
        results = self.model(frames)

        detections = []

        for result in results:
            frame_detections = []

            for box in result.boxes:

                cls = int(box.cls.cpu().numpy()[0])

                if cls == 0:

                    x1, y1, x2, y2 = box.xyxy.cpu().numpy()[0]

                    x1 = int(x1)
                    y1 = int(y1)
                    x2 = int(x2)
                    y2 = int(y2)

                    frame_detections.append((x1, y1, x2, y2))
            
            detections.append(frame_detections)

        return detections