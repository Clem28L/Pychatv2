from tkinter import *
import firebase_admin
from firebase_admin import credentials 
from firebase_admin import firestore 
from datetime import datetime 

class Pychat:
    def __init__(self, nom):
        self.nom = nom
        cred = credentials.Certificate('Key_pychat.json')
        app = firebase_admin.initialize_app(cred)
        self.db = firestore.client()

        self.fen1 = Tk()
        self.fen1.title("Pychat V2 ")
        self.fen1.geometry("1080x720")
        couleur_principale = "#212E53"
        couleur_secondaire = "#4A919E"
        couleur_treciaire = "#BED3C3"
        couleur_text = "white"
        self.channels = ["general"]
        self.current_channel = 0

        self.frame_gauche = Frame(self.fen1)
        self.frame_gauche.place(x=0, y=0, width=300, height=720)

        self.list_channel = Listbox(self.frame_gauche, bg=couleur_secondaire)
        self.list_channel.insert(0, "#general")
        self.list_channel.pack(fill="both", expand="yes")

        self.frame_droite = Frame(self.fen1, bg=couleur_principale)
        self.frame_droite.place(x=300, y=0, width=780, height=720)

        self.message_list_box = Listbox(self.frame_droite)
        self.message_list_box.pack(fill="both", expand="yes")
        self.message_list_box.configure(background=couleur_principale,foreground="white",)

        self.mess_send = Button(self.frame_droite, text='Envoyer', bg=couleur_principale, command=self.envoyer_message)
        self.mess_send.place(x=700, y=690)

        self.valeur_entre = StringVar()
        self.valeur_entre.set("Entrer un message à envoyer")
        self.entrer_mess = Entry(self.frame_droite, bg=couleur_treciaire, width=100, textvariable=self.valeur_entre)
        self.entrer_mess.place(x=70, y=700)

        def perform_task():
            self.update_message(self.current_channel)
            self.fen1.after(3000, perform_task)

        self.update_message(0)
        perform_task()

        self.fen1.mainloop()

    def update_message(self, channel_id):
        self.message_list_box.delete(0, END)
        all_content = self.db.collection("Messages").order_by("date").get()
        for doc in all_content:
            data = doc.to_dict()
            if data['channel'] == channel_id:
                self.message_list_box.insert("end", f"{data['owner']}: {data['content']}\n")   

    def envoyer_message(self):
        contenu_mess = self.entrer_mess.get().rstrip()
        if contenu_mess:
            self.db.collection("Messages").add({
                "content": contenu_mess,
                "date": datetime.now(),
                "owner": self.nom,
                "channel": self.current_channel
            })
            self.update_message(self.current_channel)
            self.valeur_entre.set("")
