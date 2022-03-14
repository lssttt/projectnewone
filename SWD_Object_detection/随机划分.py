import os
import shutil
import random
path='./images/train'
files_list=os.listdir(path)
print(len(files_list))

print(files_list)
random.shuffle(files_list)
print(files_list)

for o,i in enumerate(files_list):
    if o<len(files_list)*0.7:
        old_path=os.path.join('./images/val',i)
        new_path=os.path.join('./images/backup',i)
        shutil.move(old_path,new_path)
    else:
        old_path = os.path.join('./images/train', i)
        new_path = os.path.join('./images/backup', i)
        shutil.move(old_path, new_path)