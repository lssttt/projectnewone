import cv2 as cv
import os

# fold_path='./Dataset/1'
# fold_path='./Dataset/Final_images'
fold_path='./Dataset/4'
file_list=os.listdir(fold_path)
print(file_list)
for i in file_list:
    single_file=os.path.join(fold_path,i)
    src=cv.imread(single_file)
    print(src.shape,i)