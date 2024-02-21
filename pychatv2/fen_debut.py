from tkinter import * 

class menu_depart(Tk):
    def __init__(self):
        super().__init__()
        self.title("Ma Fenetre")
        self.geometry("300x200")  # Taille initiale de la fenêtre

        # Ajouter des widgets
        self.label = Label(self, text="Bonjour, Tkinter!")
        self.label.pack(pady=10)

        self.button = Button(self, text="Cliquez-moi!", command=self.clique)
        self.button.pack(pady=10)

    def clique(self):
        self.label.config(text="Vous avez cliqué!")

if __name__ == "__main__":
    app = menu_depart()
    app.mainloop()
