import cv2 as cv
import os

fold_path='./Dataset/3'
file_list=os.listdir(fold_path)

for i in file_list:
    print(i)
    single_file=os.path.join(fold_path,i)
    os.remove(single_file)