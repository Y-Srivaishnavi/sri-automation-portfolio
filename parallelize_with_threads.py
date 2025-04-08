import os
import re
from time import time
from threading import Thread


# Exercise 3: Can we parallelize this code?
## Approach 1: what if we used threads?
'''
A thread is a separate flow of execution. 
This means that your program will have two things happening at once. 
But for most Python 3 implementations the different threads do not actually execute at the same time: they merely appear to.
The threads may be running on different processors, but they will only be running one at a time.
Getting multiple tasks running simultaneously requires a non-standard implementation of Python-
writing some of your code in a different language, or using `multiprocessing` which comes with some extra overhead.
'''

start = time()

def move_to_dir(folder_path:str):
    image_files = os.listdir(folder_path)
    for i in range(len(image_files)):
        if "LUCID" not in image_files[i]:
            continue

        old_path = os.path.join(folder_path, image_files[i])
        new_path = os.path.join(folder_path, "camera_imgs\\"+image_files[i])

        try:
            os.rename(old_path, new_path)
            print(f"The file: {image_files[i]} has been moved to camera_imgs")
        except:
            os.makedirs("camera_imgs")
            os.rename(old_path, new_path)
            print(f"The file: {image_files[i]} has been moved to camera_imgs")

    print("Moved successfully!")

def rename_files(folder_path:str):
    for img_file in os.listdir(folder_path):
        if not re.search("png$", img_file):
            continue

        old_path = os.path.join(folder_path, img_file)
        new_img_file = img_file.replace("final", "stokes")
        new_path = os.path.join(folder_path, new_img_file)

        os.rename(old_path, new_path)
        print(f"Renamed Image {img_file[:6]} successfully!")

    print("Renamed successfully!")

folder_path = 'C:\\Users\\2003y\\OneDrive\\Desktop\\p-project\\'
t_move = Thread(None, target=move_to_dir, args=[folder_path])
t_rnme = Thread(None, target=rename_files, args=[folder_path+"\\images"])

t_move.start()
t_rnme.start()

t_move.join()
t_rnme.join()

thread_time = time()-start

print("Finished tasks!")
print(thread_time)  # 0.345928430557251

