import mss
import numpy as np
import cv2 as cv
from threading import Thread,Lock


class WindowsCapture:

    screenshot = None
    stopped = True


    def __init__(self):
        self.lock = Lock()

    def get_screenshot(self):
        monitor = {"top": 57, "left": 25, "width": 765, "height": 500}
        img = np.array(mss.mss().grab(monitor))
        return img

    def start(self):
        self.stopped = False
        t = Thread(target=self.run)
        t.start()

    def stop(self):
        self.stopped = True

    def run(self):
        # TODO: you can write your own time/iterations calculation to determine how fast this is
        while not self.stopped:
            # get an updated image of the game
            screenshot = self.get_screenshot()
            # lock the thread while updating the results
            self.lock.acquire()
            self.screenshot = screenshot
            self.lock.release()