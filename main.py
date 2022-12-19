from tkinter import *
import serial
from categorie.views import CategorieView
from categorie.models import Categorie
from tkinter.ttk import *
from PIL import Image, ImageTk
from random import randint
from time import time
import time

class Main:

    def __init__(self):
        #________________________ création de la fenetre générale _________________________
        self.root = Tk()
        self.root.geometry('1000x800')
        self.root.config(bg="white")
        self.root.title('COTONWATE : GESTION DES STOCK')
        self.frame_categorie = None
        self.menu = Menu(self.root)
        self.root['menu'] = self.menu
        self.menu.add_command(label='vetement', command=self.show_categorie)

        #________________________ création du frame acceuil _____________________________
        page_acceuil = Frame(self.root)
        page_acceuil.grid(row=0, column=0)

        image_fond = Image.open("Mod1.jpg")
        image_logo = Image.open("logo.png")
        image_fond.paste(image_logo,(20,250))
        photo_fond = ImageTk.PhotoImage(image_fond)
        bloc1 = Canvas(page_acceuil,  width = 1480, height = 500)
        bloc1.create_image(0,0, anchor = NW, image=photo_fond)
        bloc1.pack()

        bloc3 = Canvas(page_acceuil, width=1480, height=500, bg="white")
        l = Label(bloc3, text = "GESTION DES STOCKS DES VETEMENTS")
        l.config(font =("Arial Black", 30), background="white")
        l.pack(padx=10, pady=20)
        bloc3.pack()

        im = PhotoImage (file = r"C:\Users\user\cotonwate_project\button2.png")
        l1 = Label(page_acceuil, text = "Suivre le robot")
        l1.config(font =("Arial Black", 16))
        l1.place(x=350, y=620)
        b=Button(page_acceuil,image=im,text ='Suivre le robot')
        b.pack(side = LEFT, fill = BOTH, padx=275, pady=50)

        l2 = Label(page_acceuil, text = "Gérer les stocks")
        l2.config(font =("Arial Black", 16))
        l2.place(x=950, y=620)
        b2=Button(page_acceuil,image=im,text ='Suivre le robot', command=self.show_categorie).pack(side = LEFT, fill = BOTH, pady=50)

        Message(self.root, text='Application de gestion de stock').grid(row=0, column=0, columnspan=4)
        self.root.mainloop()

    def show_categorie(self):
       if self.frame_categorie is not None: 
            self.frame_categorie.grid_forget()
            self.frame_categorie = None
       self.frame_categorie = Frame(self.root, width=1000, height=900)
       self.frame_categorie.place(x=0, y=0)
       #self.frame_categorie.grid(row=0, column=0)
       CategorieView(self.frame_categorie)

 


if __name__ == "__main__":
    Main()
    # method Categorie.create du fichier modèle pour inserer les données
