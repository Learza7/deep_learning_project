import os
import shutil
import random


## folder containing the images
main_folder = "emotion_images/train"
emotion = "fearful"

# Move 10% of the images to the validation folder and 10% to the test folder, and leave the rest in the train folder
for filename in os.listdir(os.path.join(main_folder, emotion)):
    choice = random.random()
    if choice < 0.1:
        shutil.move(os.path.join(main_folder, emotion, filename), os.path.join("emotion_images/validation", emotion, filename))
    elif choice < 0.2:
        shutil.move(os.path.join(main_folder, emotion, filename), os.path.join("emotion_images/test", emotion, filename))

## count the number of images in each folder
for folder in ["emotion_images/train", "emotion_images/validation", "emotion_images/test"]:
    print(f"{folder}/{emotion}: {len(os.listdir(os.path.join(folder, emotion)))} images")