from tkinter import *
import firebase_admin
from firebase_admin import credentials 
from firebase_admin import firestore 
from datetime import datetime 
from Connect import menu_depart

def creer_menu_depart():
    fenetre = Tk()
    fenetre.title("Ma Fenetre")
    fenetre.geometry("300x200")

    label = Label(fenetre, text="Pseudo")
    label.pack(pady=10)

    def lancer_fenetre():
        texte_entry = pseudo.get().rstrip()
        create_chat_app(texte_entry)
        fenetre.destroy()
        
        

    button = Button(fenetre, text="Se connecter", command=lancer_fenetre)
    button.place(x=110, y=125)

    pseudo = Entry(fenetre, width=25)
    pseudo.place(x=75, y=100)

    fenetre.mainloop()
    
    
#-----------------------main-------------------------------------------


def create_chat_app(nom):
    def update_message(channel_id):
        message_list_box.delete(0, END)
        all_content = db.collection("Messages").order_by("date").get()
        for doc in all_content:
            data = doc.to_dict()
            if data['channel'] == channel_id:
                message_list_box.insert("end", f"{data['owner']}: {data['content']}\n")   

    def envoyer_message():
        contenu_mess = entrer_mess.get().rstrip()
        if contenu_mess:
            db.collection("Messages").add({
                "content": contenu_mess,
                "date": datetime.now(),
                "owner": nom,
                "channel": current_channel
            })
            update_message(current_channel)
            valeur_entre.set("")

    def choix_channel(event):
        global current_channel
        selection = event.widget.curselection()
        if selection:
            index = selection[0]
            current_channel = index 
            update_message(current_channel)

    cred = credentials.Certificate('Key_pychat.json')
    app = firebase_admin.initialize_app(cred)
    db = firestore.client()

    fen1 = Tk()
    fen1.title("Pychat V2 ")
    fen1.geometry("1080x720")
    couleur_principale = "#212E53"
    couleur_secondaire = "#4A919E"
    couleur_treciaire = "#BED3C3"
    couleur_text = "white"
    channels = ["general"]
    current_channel = 0
    frame_gauche = Frame(fen1)
    frame_gauche.place(x=0, y=0, width=300, height=720)

    list_channel = Listbox(frame_gauche, bg=couleur_secondaire)
    list_channel.insert(0, "#general")
    list_channel.pack(fill="both", expand="yes")

    frame_droite = Frame(fen1, bg=couleur_principale)
    frame_droite.place(x=300, y=0, width=780, height=720)

    message_list_box = Listbox(frame_droite)
    message_list_box.insert(0, "Bienvenue sur le chat")
    message_list_box.pack(fill="both", expand="yes")
    message_list_box.configure(background=couleur_principale)

    mess_send = Button(frame_droite, text='Envoyer', bg=couleur_principale, command=envoyer_message)
    mess_send.place(x=700, y=690)

    valeur_entre = StringVar()
    valeur_entre.set("Entrer un message à envoyer")
    entrer_mess = Entry(frame_droite, bg=couleur_treciaire, width=100, textvariable=valeur_entre)
    entrer_mess.place(x=70, y=700)

    def perform_task():
        update_message(current_channel)
        fen1.after(3000, perform_task)

    update_message(0)
    perform_task()

    fen1.mainloop()


f= creer_menu_depart()
 













