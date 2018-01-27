import os, fnmatch
from PIL import Image
from pathlib import Path

# This runs in  python 3.* 
## pip3 install Pillow
## run from the command line 
#  > python .\resizeImages.py


origin_directory = "images/imagesToProcess"


def processImages(fileExt):
    listOfFiles = os.listdir(origin_directory)  
    pattern = "*." + fileExt  
    for entry in listOfFiles:  
        if fnmatch.fnmatch(entry, pattern):
                resizeImage("images/sz_xSmall",entry,200)
                resizeImage("images/sz_small",entry,600)
                resizeImage("images/sz_large",entry,1200)
                origin = os.path.join(origin_directory,entry )
                dest = os.path.join("images/Processed",entry)
                my_image = Path(dest)
                if my_image.exists(): # if it already exists just delete original
                     os.remove(origin)
                
                else: # of move to new folder.
                    os.rename(origin,dest)




def resizeImage(saveDirectory, image, baseWidth):
    # Open the image file.
    path = os.path.join(origin_directory, image)
    print("Processing image: {} to width: {}".format(path,baseWidth))
    img = Image.open(path)
     
    # Calculate the height using the same aspect ratio
    widthPercent = (baseWidth / float(img.size[0]))
    height = int((float(img.size[1]) * float(widthPercent)))
     
    # Resize it.
    img = img.resize((baseWidth, height), Image.BILINEAR)
     
    # Save it back to disk in new location.
    img.save(os.path.join(saveDirectory, image))


processImages("png")
processImages("jpg")

print("#############################\n\n All Done \n\n#############################")