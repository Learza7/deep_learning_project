import argparse
import os
import shutil

JPG = 'jpg'
PNG = 'png'
JPEG = 'jpeg'

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('type_dir', type=str, help='Entrez le type du dossier : test, train, validation')
    parser.add_argument('dossier', type=str, help='Entrez une émotion : angry, fearful, happy, sad, surprised')
    args = parser.parse_args()

folder_path = 'emotion_images/' + args.type_dir + '/' + args.dossier

nom = args.type_dir + '_' + args.dossier

img_nbr = 0

for filename in os.listdir(folder_path):
    remove = False
    img_nbr += 1
    nouveau_nom = nom + '_' + str(img_nbr)
    if filename.endswith('.' + JPG) or filename.endswith('.JPG'):
        nouveau_nom += '.' + JPG
    elif filename.endswith('.' + PNG) or filename.endswith('.PNG'):
        nouveau_nom += '.' + PNG
    elif filename.endswith('.' + JPEG) or filename.endswith('.JPEG'):
        nouveau_nom += '.' + JPEG
    else :
        remove = True
        img_nbr -= 1
        os.remove(os.path.join(folder_path,filename))

    if not remove :
        shutil.move(os.path.join(folder_path, filename), os.path.join(folder_path, nouveau_nom))

    
    