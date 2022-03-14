import cv2 as cv
import matplotlib
import os
path='./Dataset/test/'
file=os.listdir(path)
print(file)
test_video=cv.VideoCapture(os.path.join(path,file[0]))

init_number=0

if test_video.isOpened():
    val,frame=test_video.read()
else:
    val=False
time_diff=10000

name_number=1#图像开始的名字#############################################################################改名字

while val:
    print('第%s张图片转帧开始'%name_number)
    val,frame=test_video.read()
    if init_number%time_diff==0:
        cv.imwrite('./Dataset/test/%s_%s.png'%(file[0][:-4],name_number),frame)
        init_number+=1000000000
        name_number+=1
cv.waitkey(1)
test_video.release()