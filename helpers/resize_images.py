#! python3
import os
import fnmatch
import time
from PIL import Image, ExifTags
from pathlib import Path
import threading
# pip3 install Pillow


origin_directory = "assets/images/imagesToProcess"


def processImages(fileExt):
    listOfFiles = os.listdir(origin_directory)
    pattern = "*." + fileExt
    list_of_processed_files = []
    for entry in listOfFiles:

        if fnmatch.fnmatch(entry, pattern):
            # print(list_of_processed_files)
            list_of_processed_files.append(entry)
            # print(entry)
            resizeImage("assets/images/sz_xSmall", entry, 200)
            resizeImage("assets/images/sz_small", entry, 600)
            resizeImage("assets/images/sz_large", entry, 1200)
            origin = os.path.join(origin_directory, entry)
            dest = os.path.join("assets/images/Processed", entry)
            # print("{} > {}".format(origin,dest))
            print("\n")
            my_image = Path(dest)
            # if it already exists just delete original
            if my_image.exists():
                try:
                    time.sleep(0.5)
                    os.remove(origin)
                except:
                    print("err: removing file ")
            # of move to new folder.
            else:
                os.rename(origin, dest)
    
    return list_of_processed_files


def clean():
    '''
     removes all files from the output paths.
     use this in development only as you will lose all your pics.
    '''
    clean_folder("assets/images/sz_xSmall")
    clean_folder("assets/images/sz_large")
    clean_folder("assets/images/sz_small")
    clean_folder("assets/images/Processed")
    clean_folder("assets/images/imagesToProcess")


def clean_folder(folder_path):
    '''
    removes all files from the output paths.
    use this in development only as you will lose all your pics.
    '''
    listOfFiles = os.listdir(folder_path)
    for entry in listOfFiles:
        origin = os.path.join(folder_path, entry)
        os.remove(origin)


def flip_horizontal(im): return im.transpose(Image.FLIP_LEFT_RIGHT)


def flip_vertical(im): return im.transpose(Image.FLIP_TOP_BOTTOM)


def rotate_180(im): return im.transpose(Image.ROTATE_180)


def rotate_90(im): return im.transpose(Image.ROTATE_90)


def rotate_270(im): return im.transpose(Image.ROTATE_270)


def transpose(im): return rotate_90(flip_horizontal(im))


def transverse(im): return rotate_90(flip_vertical(im))


orientation_funcs = [None,
                     lambda x: x,
                     flip_horizontal,
                     rotate_180,
                     flip_vertical,
                     transpose,
                     rotate_270,
                     transverse,
                     rotate_90
                     ]


def apply_orientation(im):
    """
    Extract the oritentation EXIF tag from the image, which should be a PIL Image instance,
    and if there is an orientation tag that would rotate the image, apply that rotation to
    the Image instance given to do an in-place rotation.

    :param Image im: Image instance to inspect
    :return: A possibly transposed image instance
    """

    try:
        kOrientationEXIFTag = 0x0112
        if hasattr(im, '_getexif'):  # only present in JPEGs
            e = im._getexif()       # returns None if no EXIF data
            if e is not None:
                # log.info('EXIF data found: %r', e)
                orientation = e[kOrientationEXIFTag]
                # print(orientation)
                f = orientation_funcs[orientation]
                return f(im)
        # else:
        #     print("no exif")
    except:
        # print("err no exif")
        # We'd be here with an invalid orientation value or some random error?
        pass  # log.exception("Error applying EXIF Orientation tag")
    return im


def resizeImage(saveDirectory, image, baseWidth):
    time.sleep(.2)
    # Open the image file.
    path = os.path.join(origin_directory, image)
    print("Processing image: {} to width: {}".format(path, baseWidth))
    img = Image.open(path)
    img = apply_orientation(img)

    # Calculate the height using the same aspect ratio
    widthPercent = (baseWidth / float(img.size[0]))
    height = int((float(img.size[1]) * float(widthPercent)))

    # Resize it.
    img = img.resize((baseWidth, height), Image.BILINEAR)

    # Save it back to disk in new location.
    img.save(os.path.join(saveDirectory, image))
    img.close()


class ProcessFolder(threading.Thread):
    '''
    just a loop waiting for images to be added to files
    '''

    def __init__(self):
        super().__init__()
        self.running = False

    def run(self):
        self.running = True
        while self.running:
            processImages("png")
            processImages("jpg")
            time.sleep(1)

    def stop_running(self):
        self.running = False


def main():
    
    
    while True:
        '''
        This will run every second to check if files have been added to
        the folder.
        '''
        # print("retry")
        processImages("png")
        processImages("jpg")
        time.sleep(1)


if __name__ == "__main__":
   pass
   
