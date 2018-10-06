#! python3
from optparse import OptionParser
from time import gmtime, strftime
import os
from helpers import resize_images
from pathlib import Path
import time

origin_directory = "assets/images/imagesToProcess"
dest_directory = "_posts/"


def main():
    usage = "usage: %prog [options] arg"
    parser = OptionParser(usage)
    parser.add_option("-t", "--title", dest="title",
                      help="set the title of the blog")
    parser.add_option("-i", "--image", dest="image",
                      help="set the image to be used as the thumbnail")
    parser.add_option("-l", "--alt", dest="alt_text",
                      help="set the image alt text")

    parser.add_option("-p", "--pics", dest="pictures",
                      help="Process the pictures in the '/assets/images/imagesToProcess' folder ",
                      default=False,
                  action="store_true",)

    parser.add_option("-a", "--author", dest="author",
                      help="Set the Author of the post")
    parser.add_option("-v", "--verbose",
                      action="store_true", dest="verbose")
    parser.add_option("-q", "--quiet",
                      action="store_false", dest="verbose")

   
    (options, args) = parser.parse_args()

    # print(options)
    # if len(args) == 0:
    #     parser.error("incorrect number of arguments")
    # if options.verbose:
    #     print("reading %s..." % options.filename)
    if options.pictures is not None:
        process_Images_only()
        return
    if options.title is None:
        print("\n\nYou need to supply a title for the blog use" +
              " -t or --title\n\n")
        return
    else:
        if check_if_blog_exists(options.title):
            return
    if options.image is None:
        print("\n\nAdd your first image added to the " +
              "'{}' folder to creates the thumbnail \n\n"
              .format(origin_directory))
        options.image = "001.jpg"
    if options.alt_text is None:
        options.alt_text = ""
    if options.author is None:
        options.author = "cosma"

    # print(options)
    write_text_to_file(options.title,
                       options.image,
                       options.alt_text,
                       options.author
                       )
    process_images_for_post(options.title)
    # process_image_folder = resize_images.ProcessFolder()
    # process_image_folder.start()
    # process_image_folder.join()

def process_Images_only():
    
    resize_images.processImages('png')
    resize_images.processImages('jpg')

def process_images_for_post(title):
    while True:
        data = resize_images.processImages('png')
        if len(data) > 0:
            print(data)
            add_images_to_blog(title, data)

        data = resize_images.processImages('jpg')
        if len(data) > 0:
            print(data)
            add_images_to_blog(title, data)
        time.sleep(1)


def add_images_to_blog(title, list_of_images):
    file_title = title.replace(" ", "-")
    file_path = os.path.join(dest_directory,strftime("%Y-%m-%d-", gmtime()) + file_title + '.md')
    f = open(file_path, 'a')
    for image in list_of_images:
        f.write("\n![alt Image text needs to be added]" +
                "(/assets/images/sz_large/{})" .format(image))
        f.write("\n![alt Image text needs to be added]" +
                "(/assets/images/sz_small/{})" .format(image))
    f.close()


def check_if_blog_exists(title):
    file_title = title.replace(" ", "-")
    file_path = os.path.join(dest_directory,strftime("%Y-%m-%d-", gmtime()) + file_title + '.md')
    fname = Path(file_path)
    if fname.is_file():
        print("\n\nA Post already exists with the title '{}'.\n\n"
              .format(title))
        return True
    else:
        return False


def write_text_to_file(title, thumbnail_image, thumbnail_alt, author):
    file_title = title.replace(" ", "-")
    file_path = os.path.join(dest_directory,strftime("%Y-%m-%d-", gmtime()) + file_title + '.md')
    if check_if_blog_exists(title):
        return

    f = open(file_path, 'x')
    today = strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " +0000"
    lines = ["---\n",
             "layout: post\n",
             "title:  \'" + title, "\'\n",
             "date:   ", today, "\n",
             "categories: blog\n",
             "excerpt_separator: <!--more-->", "\n",
             "thumbnail_file_name: \'" + thumbnail_image, "\'\n",
             "thumbnail_alt: \'" + thumbnail_alt, "\'\n",
             "author: ", author, "\n",
             "---", "\n", "\n",
             "Your summary goes here.", "\n""\n",
             "<!--more-->", "\n",
             "body text here.", "\n", 

             ]
    f.writelines(lines)
    f.close()


if __name__ == "__main__":
    main()
