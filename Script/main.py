from dotenv import load_dotenv
import os
from google_images_search import GoogleImagesSearch
from googleapiclient.errors import HttpError
import argparse
import shutil

JPG = 'jpg'
PNG = 'png'
JPEG = 'jpeg'

load_dotenv()

def download_images(search_term, num_images, output_dir, api_key, custom_cx):
    gis = GoogleImagesSearch(api_key, custom_cx)

    _search_params = {
        'q': search_term,
        'num': num_images,
        'imgSize': 'medium',
        'fileType': JPG +'|'+ PNG +'|'+ JPEG,
        'imgType': 'face',
    }

    term_dir = os.path.join(output_dir, search_term)
    os.makedirs(term_dir, exist_ok=True)
    gis.search(search_params=_search_params,path_to_dir=term_dir, width=128, height=128)    
    
def rename_move_images(nom,input_dir,output_dir):
    img_nbr = 0
    for filename in os.listdir(input_dir):
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
            os.remove(os.path.join(input_dir,filename))

        if not remove :
            shutil.move(os.path.join(input_dir, filename), os.path.join(output_dir, nouveau_nom))

    os.rmdir(input_dir)

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument('emotion', type=str, help='Entrez une émotion : angry, fearful, happy, sad, surprised')
    parser.add_argument('dossier', type=str, help='Entrez le nom du dossier où enregistrer les images : test, train, validation')
    parser.add_argument('nbImages', type=int, help='Entrez le nombre d\'image à télécharger')
    args = parser.parse_args()
    
    search_term = args.emotion + ' human face'
    output_dir = 'emotion_images/' + args.dossier + '/' + args.emotion
    num_images = args.nbImages
    
    api_key = os.getenv('API_KEY')
    custom_cx = os.getenv('CX')

    try :
        download_images(search_term, num_images, output_dir, api_key, custom_cx)
    except HttpError as e:
        print('Erreur lors du téléchargement d\'une image : ')
        print(e)

    rename_move_images(nom=args.dossier + '_' + args.emotion, input_dir=output_dir + '/' + search_term, output_dir=output_dir)
