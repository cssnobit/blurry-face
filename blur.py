import cv2
from config import HEAD_RATIO

def blur_heads(frame, detections):

    for (x1, y1, x2, y2) in detections:
        height = y2 - y1

        head_y2 = int(y1 + height * HEAD_RATIO)

        roi = frame[y1:head_y2, x1:x2]

        if roi.size == 0:
            continue

        blur = cv2.GaussianBlur(roi, (99, 99), 30)

        frame[y1:head_y2, x1:x2] = blur

    return frame