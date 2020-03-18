import datetime
import threading
import time
from collections import deque

import cv2


class VideoRecorderThread(threading.Thread):
    def __init__(self, device_id, fps, size, seconds):
        super().__init__()
        self.setDaemon(True)

        self.fps = fps
        self.size = size
        self.seconds = seconds

        self.cap = cv2.VideoCapture(device_id)
        self.frame_que = deque(maxlen=int(fps * seconds))

        self._is_saving_video = False

    def record_video(self):
        if self._is_saving_video:
            return

        time.sleep(self.seconds / 2)

        t = threading.Thread(target=self._save_video)
        t.start()

    def run(self):
        while self.cap.isOpened():
            ret, frame = self.cap.read()
            self.frame_que.append(frame)

        self.cap.release()

    def _save_video(self):
        self._is_saving_video = True
        video = self._make_video()

        frame_que = self.frame_que.copy()
        for frame in frame_que:
            video.write(frame)

        video.release()
        print("Video saved")
        self._is_saving_video = False

    def _make_video(self):
        fourcc = cv2.VideoWriter_fourcc(*"XVID")
        dt_now = datetime.datetime.now()
        video_time = dt_now.strftime("%Y-%m-%d_%H:%M:%S")
        video = cv2.VideoWriter(f"media/{video_time}.avi", fourcc, self.fps, self.size)

        return video


def start_camera():
    fps = 20
    size = (640, 480)
    seconds = 10

    t = VideoRecorderThread(0, fps, size, seconds)
    t.start()

    return t


if __name__ == "__main__":
    start_camera()
