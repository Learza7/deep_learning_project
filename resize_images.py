# script to resize images in a folder
#
import os
from PIL import Image


def resize_images(input_dir, output_dir, size):
    for filename in os.listdir(input_dir):
        if filename.endswith('.jpg') or filename.endswith('.JPG') or filename.endswith('.png') or filename.endswith('.PNG') or filename.endswith('.jpeg') or filename.endswith('.JPEG'):
            img = Image.open(os.path.join(input_dir, filename))
            img = crop_square(img)
            img = img.resize((size, size), Image.ANTIALIAS)
            img.save(os.path.join(output_dir, filename))
            
def crop_square(current_image):
    w, h = current_image.size
    if(w > h):
        delta = (w - h)/2
        return current_image.crop((delta, 0, w - delta, h))
    else:
        delta = (h - w)/2
        return current_image.crop((0, delta, w, h - delta))

if __name__ == "__main__":
    input_dir = 'emotion_images/train/angry_no_processed'
    output_dir = 'emotion_images/train/angry'
    resize_images(input_dir, output_dir, 128)
