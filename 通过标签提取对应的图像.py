import os
import cv2 as cv
import random
import shutil
path='./Dataset/labels_my-project-name_2021-12-06-05-12-08'
label_list=os.listdir(path)
print(label_list)
print(len(label_list))
random.shuffle(label_list)
print(label_list)
for o,i in enumerate(label_list):

    src_path='./Dataset/Final_images/%s.jpg'%i[:-4]
    if o <len(label_list)*0.7:
        new_path='./Dataset/Face_Object_detection/images/train/%s.jpg'%i[:-4]
    else:
        new_path = './Dataset/Face_Object_detection/images/val/%s.jpg' % i[:-4]
    shutil.copy(src_path,new_path)
