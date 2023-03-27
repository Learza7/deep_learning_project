# script to resize images in a folder
#
import os
from PIL import Image


def resize_images(input_dir, output_dir, size):
    for filename in os.listdir(input_dir):
        if filename.endswith('.jpg') or filename.endswith('.JPG') or filename.endswith('.png') or filename.endswith('.PNG') or filename.endswith('.jpeg') or filename.endswith('.JPEG'):
            img = Image.open(os.path.join(input_dir, filename))
            img = img.resize((size, size), Image.ANTIALIAS)
            img.save(os.path.join(output_dir, filename))


if __name__ == "__main__":
    input_dir = 'emotion_images/train/angry_no_processed'
    output_dir = 'emotion_images/train/angry'
    resize_images(input_dir, output_dir, 128)