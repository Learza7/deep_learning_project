Petit programme qui permettant de trier rapidement les images

Pour le lancer il suffit de faire "python3 TrieurImages.py"

Pour l'utiliser:
- Mettre l'adresse du dossier contenant toutes les images non triées dans le champ prévu pour ça
	-> le script créera dans ce même dossier les dossiers dans lesquels seront enregistrées les images
 
- Trier les images avec les boutons: il est possible d'ignorer certaines images et de revenir en arrière au cas ou on se soit trompé de catégorie

Par défaut j'ai réglé le maximum d'annulation de choix à 20, mais vous pouvez le régler aussi haut que vous le souhaitez dans le script, c'est la variable "max_historic_steps"__
Vous pouvez aussi changer les formats pris en compte en les rajoutant dans la variable "formats", il faut les indiquer comme sur la doc suivante: https://docs.python.org/3/library/imghdr.html

![alt text](https://github.com/Learza7/deep_learning_project/blob/main/TrieurImages/Exemple.png)
