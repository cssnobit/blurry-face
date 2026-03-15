import sys

from video_reader import VideoReader
from ffmpeg_writer import FfmpegWriter
from detector import PersonDetector
from blur import blur_heads
from config import DETECTION_INTERVAL
from motion_detector import MotionDetector
from tqdm import tqdm
import cv2

def main(input_video, output_video):
    frame_count = 0
    reader = VideoReader(input_video)
    motion_detector = MotionDetector()

    total_frames = int(reader.cap.get(cv2.CAP_PROP_FRAME_COUNT))

    pbar = tqdm(total=total_frames, desc="Processando vídeo", unit="frame")

    writer = FfmpegWriter(
        output_video,
        reader.width,
        reader.height,
        reader.fps
    )

    detector = PersonDetector()

    last_detections = []

    while True:
        data = reader.read()

        if data is None:
            break

        frame, process = data
        motion = motion_detector.detect(frame)

        if motion and frame_count % DETECTION_INTERVAL == 0:
            detections = detector.detect([frame])[0]
            last_detections = detections

        frame = blur_heads(frame, last_detections)

        writer.write(frame)

        frame_count += 1
        pbar.update(1)

    pbar.close()
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
