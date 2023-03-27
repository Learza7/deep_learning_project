import os
from PIL import Image

directory = 'emotion_images/train/happy' # Entrez le chemin absolu du dossier contenant les images

threshold = 50 # Seuil de différence entre deux images en niveaux de gris, à partir duquel les images sont considérées comme différentes

image_list = [] # Liste pour stocker les images

for filename in os.listdir(directory):
    if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'): # Vérifiez si le fichier est une image
        image = Image.open(os.path.join(directory, filename))
        gray_image = image.convert('L') # Convertir l'image en niveaux de gris
        pixels = gray_image.getdata()
        black_pixels = sum(pixel < threshold for pixel in pixels) # Compter le nombre de pixels noirs dans l'image
        image_list.append((filename, black_pixels)) # Stocker le nom de fichier et le nombre de pixels noirs

image_list.sort(key=lambda x: x[1]) # Trier la liste d'images par nombre de pixels noirs

duplicates = set() # Ensemble pour stocker les doublons d'images

for i in range(len(image_list)-1):
    for j in range(i+1, len(image_list)):
        if abs(image_list[j][1] - image_list[i][1]) > threshold: # Vérifier si la différence entre les deux images en niveaux de gris est supérieure au seuil
            break
        else:
            img1 = Image.open(os.path.join(directory, image_list[i][0]))
            img2 = Image.open(os.path.join(directory, image_list[j][0]))
            if img1.histogram() == img2.histogram(): # Comparer les histogrammes des deux images
                duplicates.add(image_list[j][0])

for duplicate in duplicates:
    os.remove(os.path.join(directory, duplicate)) # Supprimer les doublons d'images
