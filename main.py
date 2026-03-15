import sys

from video_reader import VideoReader
from video_writer import VideoWriter
from detector import PersonDetector
from blur import blur_heads
from config import DETECTION_INTERVAL

def main(input_video, output_video):
    frame_count = 0
    reader = VideoReader(input_video)

    writer = VideoWriter(
        output_video,
        reader.fps,
        reader.width,
        reader.height
    )

    detector = PersonDetector()

    last_detections = []

    while True:

        data = reader.read()

        if data is None:
            break

        frame, process = data

        if frame_count % DETECTION_INTERVAL == 0:
            detections = detector.detect([frame])[0]
            last_detections = detections

        frame = blur_heads(frame, last_detections)

        writer.write(frame)

        frame_count += 1

    reader.release()
    writer.release()


if __name__ == "__main__":

    if len(sys.argv) < 3:

        print("Uso:")
        print("python main.py input.mp4 output.mp4")
        sys.exit()

    input_video = sys.argv[1]
    output_video = sys.argv[2]

    main(input_video, output_video)
