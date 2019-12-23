import cv2, time
import pandas as pd

first_frame = None
status_list = [None,None]
times = []
df = pd.DataFrame(columns = ['Start','End'])


video = cv2.VideoCapture(0)

while True:
    check,frame = video.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21,21),0)
    if first_frame is None:
        first_frame = gray
        continue
