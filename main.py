from dotenv import load_dotenv
import os
from google_images_search import GoogleImagesSearch

load_dotenv()

def download_images(search_terms, num_images, output_dir, api_key, custom_cx):
    gis = GoogleImagesSearch(api_key, custom_cx)

    for term in search_terms:
        _search_params = {
            'q': term,
            'num': num_images,
            'imgSize': 'medium',
            'fileType': 'jpg|png',
            'imgType': 'face',
        }

        term_dir = os.path.join(output_dir, term)
        os.makedirs(term_dir, exist_ok=True)
        gis.search(search_params=_search_params,
                   path_to_dir=term_dir, width=128, height=128)

if __name__ == "__main__":
    search_terms = ['happy human face', 'sad human face',
                    'angry human face', 'surprised human face', 'fearful human face']
    num_images = 1
    output_dir = 'emotion_images'
    api_key = os.getenv('API_KEY')
    custom_cx = os.getenv('CX')

    download_images(search_terms, num_images, output_dir, api_key, custom_cx)
