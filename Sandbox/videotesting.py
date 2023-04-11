import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
Video_FILE = "videofile.mp4"


def get_frames(filename):
    video=cv2.VideoCapture(filename)
    count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    print('Total no of frames: ',count)
    while video.isOpened():
        print("Video is playing")
        rete,frame=video.read()
        if rete:
            yield frame
        else:
            break
        yield None

for f in get_frames(Video_FILE):
    if f is None:
        break
    cv2.imshow('frame',f)
    if cv2.waitKey(10) == 40:
        break
cv2.destroyAllWindows()




def get_frame(filename,index):
    counter=0
    video=cv2.VideoCapture(filename)
    while video.isOpened():
        rete,frame=video.read()
        if rete:
            if counter==index:
                return frame
            counter +=1
        else:
            break
    video.release()
    return None

"""



"""
frame = get_frame(Video_FILE,95)
print('shape is', frame.shape)
print('pixel at (60,21)',frame[60,21,:],)
print('pixel at (120,10)',frame[120,10,:])
plt.imshow(frame)
fix_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
plt.imshow(fix_frame[220:430,300:600])
