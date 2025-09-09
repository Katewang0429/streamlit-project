import cv2

def frame_generator(video_path, stride=1):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise FileNotFoundError(f"Cannot open video: {video_path}")
    i = 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        if i % stride == 0:
            yield frame
        i += 1
    cap.release()

class VideoWriter:
    def __init__(self, out_path, fps, width, height, fourcc="mp4v"):
        self._writer = cv2.VideoWriter(
            out_path, cv2.VideoWriter_fourcc(*fourcc), fps, (width, height)
        )
    def write(self, frame):
        self._writer.write(frame)
    def release(self):
        self._writer.release()
