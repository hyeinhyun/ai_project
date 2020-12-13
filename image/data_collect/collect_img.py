import sys
import re
import os
#Arrays for video queue
match = []


if len(sys.argv) < 2:
     quit()

for videos in sys.argv:
    print(sys.argv)
    if re.findall(r'\d+', videos):
        match.append(re.findall(r'\d+', videos)[0])
                #print(match)
for video_id in match:
    if not os.path.exists(video_id):
        os.mkdir(video_id)
    video_infos = util.getVideoInfo(video_id)
    util.downloadVideo(video_id)

print( "Bye! ❤️" )