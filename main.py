import cv2
import time
from WindowsCapture import WindowsCapture
from threading import Thread


wincap = WindowsCapture()
wincap.start()
while True:
    start_time = time.time()
    if wincap.screenshot is None:
        continue
    cv2.imshow("AI", wincap.screenshot)
    key = cv2.waitKey(1)
    if key == ord('q'):
        wincap.stop()
        cv2.destroyAllWindows()
    elif key == ord('f'):
        cv2.imwrite(f'images/{time.time()}.jpg',wincap.screenshot)
        print("screenshot taken")
    #print("FPS: ", round(1.0 / (time.time() - start_time)))

print('Done')