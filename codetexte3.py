import tkinter as tk 

def frequence2(message_chiffre):
    resultat=[]
    for c in message_chiffre :
        if 97 <= ord(c) <= 122 :
            exist=True
            for i in range(len(resultat)):
                if resultat[i][0]==c :
                    exist= False  
                    resultat[i][1]+=round(1/len(message_chiffre)*100,2)
            if exist :
                resultat.append([c, round(1/len(message_chiffre)*100,2)])

    return resultat 


def rang(lettre):
    return ord(lettre)-97

def decalage(lettre_message, lettre_cle):
    if 97 <= ord(lettre_message) <=122 :
        return chr((rang(lettre_message)+rang(lettre_cle))%26 + 97)
    else :
        return lettre_message

def dec_texte(texte,cle):
    taille_cle = len(cle)
    res = ""
    for i in range(len(texte)):
        res += decalage(texte[i],cle[i%taille_cle])
    return res

def chiffre():
    resultat.delete(0,tk.END)
    text=entree_texte.get()
    cle=entree_cle.get()
    if((len(text)>0) and (len(cle)>0)):
        res=dec_texte(text,cle)
        resultat.insert(0,res)
    else:
        resultat.insert(0,"Il manque quelque chose")



racine=tk.Tk()
racine.title("Cryptographie")

entree_texte = tk.Entry(racine, width = 50, font = ("helvetica", "20"))
entree_texte.grid(row = 0, column = 0)

entree_cle = tk.Entry(racine, width = 50, font = ("helvetica", "20"))
entree_cle.grid(row = 1, column = 0)

label_texte = tk.Label(racine,font = ("helvetica", "20"), text = "Entrer le message ici.")
label_texte.grid(row = 0, column = 1)

label_cle = tk.Label(racine,font = ("helvetica", "20"), text = "Entrer la clé ici.")
label_cle.grid(row = 1, column = 1)

label_dech = tk.Label(racine,font = ("helvetica", "20"), text = "Déchiffre ici")
label_dech.grid(row = 3, column = 1)


bouton_decoder=tk.Button(racine,text="Déchiffrer texte",fg="black",  width=15,command=chiffre)
bouton_decoder.grid(row=2, column=1)

resultat=tk.Entry(racine,width = 50, font = ("helvetica", "20"))
resultat.grid(row=3,column=0)


racine.mainloop()