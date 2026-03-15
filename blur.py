import cv2
from config import HEAD_WIDTH_RATIO, HEAD_HEIGHT_RATIO


def blur_heads(frame, detections):

    for (x1, y1, x2, y2) in detections:

        width = x2 - x1

        head_width = int(width * HEAD_WIDTH_RATIO)
        head_height = int(head_width * HEAD_HEIGHT_RATIO)

        center_x = x1 + width // 2

        head_x1 = int(center_x - head_width // 2)
        head_x2 = int(center_x + head_width // 2)

        head_y1 = y1
        head_y2 = y1 + head_height

        head_x1 = max(0, head_x1)
        head_y1 = max(0, head_y1)

        roi = frame[head_y1:head_y2, head_x1:head_x2]

        if roi.size == 0:
            continue

        blur = cv2.GaussianBlur(roi, (51, 51), 30)

        frame[head_y1:head_y2, head_x1:head_x2] = blur

    return frame
