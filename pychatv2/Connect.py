from tkinter import *
import firebase_admin
from firebase_admin import credentials 
from firebase_admin import firestore 
from datetime import datetime 
from main import Pychat

class Menu_Depart:
    def __init__(self):
        self.fenetre = Tk()
        self.fenetre.title("Ma Fenetre")
        self.fenetre.geometry("300x200")

        label = Label(self.fenetre, text="Pseudo")
        label.pack(pady=10)

        def lancer_fenetre():
            texte_entry = self.pseudo.get().rstrip()
            self.fenetre.destroy()
            Pychat(texte_entry)
            

        button = Button(self.fenetre, text="Se connecter", command=lancer_fenetre)
        button.place(x=110, y=125)

        self.pseudo = Entry(self.fenetre, width=25)
        self.pseudo.place(x=75, y=100)

        self.fenetre.mainloop()
        
Menu_Depart()
