
import os
import cv2


pathOut = r"D:\Dataset\correct\8 494452288\v8"
count = 0
counter = 0
sec = 0
listing = os.listdir(r'D:/Dataset/videos/video7/720p30/')

for vid in listing:
    vid = r"D:/Dataset/videos/video7/720p30/" + vid
    cap = cv2.VideoCapture(vid)
    count = 0
    counter += 1
    success = True
    print(vid)
    while success:

        success,image = cap.read()
        #print('read a new frame:',success)
        if success == False:
            break
        if count%25 == 0 :
            #count%25 is for 25 fps videos, if fps is different - change fps
            sec +=1
            cv2.imwrite(pathOut + 's%d.jpg' % sec, image)
            print("Saving image %d" %sec)

        count+=1
