"""
Created on Tue Mar 21 06:44:12 2023

@author: nathan barraud
"""




import imghdr
import os
from tkinter import *
from tkinter.messagebox import *
from PIL import Image, ImageTk


canvas_size = 300 #Taille des affichages
formats = ["jpeg","png"] # Formats d'images acceptés
previousPaths = []
max_historic_steps = 20 # Nombre de retours en arrière max: -1 pour infinité


images_names = []
RawFolderAdress = ""
joieFolderAdress = ""
tristeFolderAdress = ""
degoutFolderAdress = ""
colereFolderAdress = ""
peurFolderAdress = ""
displayed_image_index = -1

def recupereAdresses():
    if not askyesno('Warning', 'Attention, si des images ont déjà été déplacées par ce script l\'historique de ces déplacements sera perdue. Cela signifie qu\'il sera impossible d\'appuier sur le boutton \'Annuler le choix\' pour ces images \n continuer ?'):
        return
    global RawFolderAdress,joieFolderAdress,tristeFolderAdress,degoutFolderAdress,colereFolderAdress,peurFolderAdress
    RawFolderAdress = arow.get()
    joieFolderAdress = creer_rep('joie')
    tristeFolderAdress = creer_rep('triste')
    degoutFolderAdress = creer_rep('surprise')
    colereFolderAdress = creer_rep('colere')
    peurFolderAdress = creer_rep('peur')
    if(not (RawFolderAdress and joieFolderAdress and tristeFolderAdress and degoutFolderAdress and colereFolderAdress and peurFolderAdress)):
        showerror("Problème d'adresse", "Toutes les adresses ne sont pas remplies !")
    else:
        init()
        load_images()
        display_next_image()

def creer_rep(name):
    path = os.path.join(RawFolderAdress,name)
    os.makedirs(path, exist_ok=True)
    return path

def init():
    global images_names,displayed_image_index,previousPaths
    images_names = []
    displayed_image_index = -1
    previousPaths = []

def load_images():
    global images_names
    print("debut for")
    print(RawFolderAdress)
    for filename in os.listdir(RawFolderAdress):
        path = os.path.join(RawFolderAdress,filename)
        if os.path.isfile(path):
            if imghdr.what(path) in formats:
                images_names.append(filename)
            else:
                print(imghdr.what(path))
    print(len(images_names))

def display_next_image():
    global displayed_image_index,canvas,poster,previousPaths,history_canvas,history_poster
    if displayed_image_index < len(images_names) - 1:
        displayed_image_index += 1
        print(displayed_image_index)
        display_image(canvas,poster,os.path.join(RawFolderAdress,images_names[displayed_image_index]))
        if(len(previousPaths) > 0):
            print(previousPaths)
            display_image(history_canvas,history_poster,previousPaths[-1][1])
            hisctoric_category_label.config(text = "image enregistrée dans: \'" + previousPaths[-1][2] + "\'")
            fenetre.update_idletasks()
        else:
            display_image(history_canvas,history_poster,None)
            hisctoric_category_label.config(text = "Pas d'historique")
            fenetre.update_idletasks()
        img_count_label.config(text = str(len(images_names) - displayed_image_index) + " images restantes")
        fenetre.update_idletasks()
        print("next exit")

def revert_one_frame():
        global displayed_image_index,canvas,poster,previousPaths,history_canvas,history_poster
        if displayed_image_index > 0:
            displayed_image_index -= 1
            display_image(canvas,poster,os.path.join(RawFolderAdress,images_names[displayed_image_index]))
            if(len(previousPaths) > 0):
                print(previousPaths)
                display_image(history_canvas,history_poster,previousPaths[-1][1])
                hisctoric_category_label.config(text = "image enregistrée dans: \'" + previousPaths[-1][2] + "\'")
                fenetre.update_idletasks()
            else:
                display_image(history_canvas,history_poster,None)
                hisctoric_category_label.config(text = "Fin de l'historique")
                fenetre.update_idletasks()
            img_count_label.config(text = str(len(images_names) - displayed_image_index) + " images restantes")
            fenetre.update_idletasks()

def display_image(canvas_istance,image_holder,path):
    photo = load_image(path)
    canvas_istance.itemconfigure(image_holder, image=photo)
    canvas_istance.image = photo
    canvas_istance.update()

def load_image(path):
    if path == None:
        return None
    else:
        photo = Image.open(path)
        photo = resize(photo)
        photo = ImageTk.PhotoImage(photo)
        return photo

def resize(img):
    global canvas_size
    width, height = img.size
    coef = 0
    if(width < height):
        coef = canvas_size/height
        img=img.resize((int(coef * width),canvas_size),Image.LANCZOS)
    else:
        coef = canvas_size/width
        img=img.resize((canvas_size,int(coef * height)),Image.LANCZOS)
    return img

def sendTo(dir):
    global previousPaths
    old_path = os.path.join(RawFolderAdress,images_names[displayed_image_index])
    if (dir == "J" and displayed_image_index < len(images_names)-1):
        transfert_file_to(joieFolderAdress,old_path,"Joie")
        display_next_image()
    elif (dir == "T" and displayed_image_index < len(images_names)-1):
        transfert_file_to(tristeFolderAdress,old_path,"Tristesse")
        display_next_image()
    elif (dir == "S" and displayed_image_index < len(images_names)-1):
        transfert_file_to(degoutFolderAdress,old_path,"Surprise")
        display_next_image()
    elif (dir == "C" and displayed_image_index < len(images_names)-1):
        transfert_file_to(colereFolderAdress,old_path,"Colère")
        display_next_image()
    elif (dir == "P" and displayed_image_index < len(images_names)-1):
        transfert_file_to(peurFolderAdress,old_path,"Peur")
        display_next_image()
    elif (dir == "ignore" and displayed_image_index < len(images_names)-1):
        previousPaths.append((old_path,old_path,"ignorée"))
        display_next_image()
    elif (dir == "revert" and len(previousPaths) > 0):
        old_path, new_path, _ = previousPaths.pop()
        if(old_path != None and new_path != None):
            os.rename(new_path,old_path)
        revert_one_frame()

def transfert_file_to(name,old_path,category_display_name):
    global previousPaths
    new_path = os.path.join(name,images_names[displayed_image_index])
    if max_historic_steps != -1:
        if len(previousPaths) >= max_historic_steps:
            previousPaths.pop(0)
    previousPaths.append((old_path,new_path,category_display_name))
    os.rename(old_path, new_path)

#Crétion de la fentere
fenetre = Tk(className="Trieur")

fenetre.resizable(False, False)

topPannel = PanedWindow(fenetre, orient=HORIZONTAL)
topPannel.pack(side=TOP, expand=Y, fill=NONE, pady=2, padx=2)


FrameAdresses = Frame(fenetre, borderwidth=2, relief=RIDGE)
Label(FrameAdresses, text="Adresse dossier non trié:",anchor=W).grid(column=0,row=0)
arow = Entry(FrameAdresses, width=30)
arow.grid(column=1,row=0)
Button(FrameAdresses, text ='Valider', command= lambda: recupereAdresses()).grid(column=1,row=1)
Label(FrameAdresses, text="Le script créera les dossiers dans lesquels les images\nseront triées dans le dossier des images non triées").grid(column=1,row=2)
topPannel.add(FrameAdresses)


FrameInstructions = Frame(fenetre, borderwidth=2, relief=FLAT)
Label(FrameInstructions, text="Instructions:").grid(column=2,row=0)
Label(FrameInstructions, text="-Indiquer l'adresse du dossier contenant toutes les images non triées \n -Utiliser les bouttons pour trier les images").grid(column=2,row=1)
img_count_label = Label(FrameInstructions, text="")
img_count_label.grid(column=2,row=3)
topPannel.add(FrameInstructions)

topPannel.pack()

p = PanedWindow(fenetre, orient=HORIZONTAL)
p.pack(expand=Y, fill=NONE, pady=2, padx=2)

FrameCenter = Frame(fenetre, borderwidth=2, relief=FLAT)
canvas = Canvas(FrameCenter, width=canvas_size, height=canvas_size, bg='ivory')
poster = canvas.create_image(0,0,anchor=NW)
canvas.pack(side=TOP, padx=5, pady=5)
buttonPannel = PanedWindow(FrameCenter, orient=HORIZONTAL)
buttonPannel.pack(fill=NONE, pady=2, padx=2)
buttonPannel.add(Button(buttonPannel, text ='Joie',command= lambda: sendTo("J")))
buttonPannel.add(Button(buttonPannel, text ='Tristesse',command= lambda: sendTo("T")))
buttonPannel.add(Button(buttonPannel, text ='Surprise',command= lambda: sendTo("S")))
buttonPannel.add(Button(buttonPannel, text ='Colère',command= lambda: sendTo("C")))
buttonPannel.add(Button(buttonPannel, text ='Peur',command= lambda: sendTo("P")))
buttonPannel.add(Button(buttonPannel, text ='Ignore',command= lambda: sendTo("ignore")))
p.add(FrameCenter)

FrameRigth = Frame(fenetre, borderwidth=2, relief=FLAT)
history_canvas = Canvas(FrameRigth, width=canvas_size, height=canvas_size, bg='ivory')
history_poster = history_canvas.create_image(0,0,anchor=NW)
history_canvas.pack(side=TOP, padx=5, pady=5)
hisctoric_category_label = Label(FrameRigth, text="")
hisctoric_category_label.pack(padx=5, pady=5)
Button(FrameRigth, text ='Annuler le choix', command= lambda: sendTo("revert")).pack(padx=5, pady=5)
p.add(FrameRigth)

p.pack()

fenetre.mainloop()
