import os
import time
import random
import sys
import argparse
from PIL import Image

def main(random_selection):
    wd = args.wallpaper 
    index = 0
    used_images = []
    interval = args.interval
    while True:
        images = detect_image_files_in_directory(wd)
        image_count = len(images)
        if image_count > 0 and random_selection:
            if len(used_images) == image_count:
                used_images = []
            i = random.randint(0, image_count - 1)
            while i in used_images:
                i = random.randint(0, image_count - 1)
            used_images.append(i)  
            os.system('feh --bg-scale ' + images[i])
            print(images[i])
        elif image_count > 0:
            os.system('feh --bg-scale ' + images[index % image_count])
            print(images[index % image_count])
            index += 1
        else:
            print('Given directory doesn\'t contain any images.')
            sys.exit()
        time.sleep(interval)


def detect_image_files_in_directory(directory_path):
    images = []
    if directory_path[-1] != '/':
        directory_path += '/'
    files_at_dir = []
    try:   
        files_at_dir = os.listdir(directory_path)
    except FileNotFoundError:
        print('Given directory doesn\'t exist.')
        sys.exit()  
    for f in files_at_dir:
        file_path = directory_path + str(f)
        try:
            if Image.open(file_path):
                images.append(file_path)
        except OSError:
            pass
        except FileNotFoundError:
            pass
    return images
    

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-w', '--wallpaper', required=True, help='Path of the wallpapers folder')
    parser.add_argument('-r', '--random', action='store_true', help='Randomly change wallpaper without following the sequence')
    parser.add_argument('-i', '--interval', default=300, type=int, help='Time period between wallpaper change (As seconds)')
    args = parser.parse_args()

    if args.random and args.wallpaper:
        main(True)
    elif args.wallpaper:
        main(False)
    else:
        parser.print_help()

