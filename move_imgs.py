'''
Code to put images from camera into a directory 
'''
import os
import re

folder_path = 'C:\\Users\\2003y\\OneDrive\\Desktop\\p-project\\'

image_files = os.listdir(folder_path)

# Exercise 1: Move camera images to folder to save space
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
# Moved successfully

#  Exercise 2: Rename stokes images for more clarity
folder_path += "images\\"

for img_file in os.listdir(folder_path):
    if not re.search("png$", img_file):
        continue

    old_path = os.path.join(folder_path, img_file)
    new_img_file = img_file.replace("final", "stokes")
    new_path = os.path.join(folder_path, new_img_file)

    os.rename(old_path, new_path)
    print(f"Renamed Image {img_file[:6]} successfully!")
# Renamed successfully

print ("Moving complete!")