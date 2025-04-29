import os
from time import time
from multiprocessing import Process

def move_to_dir(folder_path: str):
    camera_img_dir = os.path.join(folder_path, "camera_imgs")   # Enhanced by GPT; alternative to concatentaion
    if not os.path.exists(camera_img_dir):
        os.makedirs(camera_img_dir)

    image_files = os.listdir(folder_path)
    for img_file in image_files:
        if "LUCID" not in img_file:
            continue

        old_path = os.path.join(folder_path, img_file)
        new_path = os.path.join(camera_img_dir, img_file)

        try:
            os.rename(old_path, new_path)
            print(f"The file: {img_file} has been moved to camera_imgs")
        except Exception as e:
            print(f"Error moving {img_file}: {e}")

    print("Moved successfully!")

def rename_files(folder_path: str):
    for img_file in os.listdir(folder_path):
        if not img_file.endswith(".png"):
            continue

        old_path = os.path.join(folder_path, img_file)
        new_img_file = img_file.replace("final", "stokes")
        new_path = os.path.join(folder_path, new_img_file)

        try:
            os.rename(old_path, new_path)
            print(f"Renamed Image {img_file[:6]} successfully!")
        except Exception as e:
            print(f"Error renaming {img_file}: {e}")

    print("Renamed successfully!")

if __name__ == "__main__":  # this is necessary to multiprocessing
    start = time()

    folder_path = r'C:\\Users\\2003y\\OneDrive\\Desktop\\p-project'
    images_path = os.path.join(folder_path, "images")

    t_move = Process(target=move_to_dir, args=(folder_path,))
    t_rnme = Process(target=rename_files, args=(images_path,))

    t_move.start()
    t_rnme.start()

    t_move.join()
    t_rnme.join()

    thread_time = time() - start

    print("Finished tasks!")
    print(f"Time taken: {thread_time} seconds")
    
    # Time taken: 0.709763765335083(?) seconds (fluctuates with rerun)
    # definitely longer than previous codes
