import cv2 as cv
import os

# fold_path='./Dataset/3'
fold_path='./Dataset/4'
file_list=os.listdir(fold_path)
print(file_list)
# index=1077
index=2510
for i in file_list:

    single_file=os.path.join(fold_path,i)
    src=cv.imread(single_file)
    # new_path=os.path.join('./Dataset/Final_images','%s.jpg'%index)
    new_path=os.path.join('./Dataset/4','3_%s.jpg'%index)
    cv.imwrite(new_path,src)
    index+=1
    print(src.shape,index)