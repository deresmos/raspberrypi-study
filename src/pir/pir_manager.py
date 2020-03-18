import time

import RPi.GPIO as GPIO
from send_count import send_to_websocket
from video_recorder import start_camera

INTERVAL = 0.1
SLEEPTIME = 4
GPIO_PIN = 18

count = 0

recorder_thread = start_camera()


def detected():
    global count
    count += 1
    recorder_thread.record_video()

    #  send_to_websocket(count)
    print("ん？だれか通った？")
    time.sleep(SLEEPTIME)
    print("過ぎ去ったな。。。")


def start_rpi():
    while True:
        time.sleep(INTERVAL)

        # センサー感知
        if GPIO.input(GPIO_PIN) == GPIO.HIGH:
            detected()
            continue


def main():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(GPIO_PIN, GPIO.IN)

    try:
        print("End: Ctrl+c")
        start_rpi()
    except KeyboardInterrupt:
        print("処理終了中...")
    finally:
        GPIO.cleanup(GPIO_PIN)
        print(f"GPIO({GPIO_PIN}) clean完了")


if __name__ == "__main__":
    main()
