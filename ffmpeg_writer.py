import subprocess

class FfmpegWriter:

    def __init__(self, output_path, width, height, fps):
        command = [
            "C:/ffmpeg/bin/ffmpeg.exe",
            "-y",
            "-f", "rawvideo",
            "-vcodec","rawvideo",
            "-pix_fmt","bgr24",
            "-s", f"{width}x{height}",
            "-r", str(fps),
            "-i","-",
            "-an",
            "-vcodec","libx264",
            "-preset","fast",
            "-pix_fmt","yuv420p",
            output_path
        ]

        self.process = subprocess.Popen(
            command,
            stdin=subprocess.PIPE
        )
    
    def write(self, frame):
        self.process.stdin.write(frame.tobytes())
    
    def release(self):
        self.process.stdin.close()
        self.process.wait()