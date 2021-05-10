import tkinter as tk

code_secret = []
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
subtituant = ['z','b','d','n','x','m','l','h','s','j','i','h','g','a','o','p','p','o','o','t','t','c','f','e','u','z']

def frequence2(code_secret):
    resultat=[]
    for c in code_secret :
        if 97 <= ord(c) <= 122 :
            exist=True
            for i in range(len(resultat)):
                if resultat[i][0]==c :
                    exist= False  
                    resultat[i][1]+=round(1/len(code_secret)*100,2)
            if exist :
                resultat.append([c, round(1/len(code_secret)*100,2)])

    return resultat 


def decoder():
    substituant = alphabet
    for i in range(code_secret) and code_secret in range(substituant):
        print(alphabet)

    return alphabet
        
def chiffre():
    resultat.delete(0,tk.END)
    code_secret=entree_code_secret.get()
    substituant=entree_substituant.get()
    if((len(text)>0) and (len(cle)>0)):
        res=dec_texte(text,cle)
        resultat.insert(0,res)
    else:
        resultat.insert(0,"Il manque quelque chose")

  
        


racine= tk.Tk()
racine.title("Cryptographie")

entree_texte = tk.Entry(racine, width = 50, font = ("helvetica", "20"))
entree_texte.grid(row = 0, column = 0)

label_texte = tk.Label(racine,font = ("helvetica", "20"), text = "Entrer le code secret ici.")
label_texte.grid(row = 0, column = 1)

bouton_decoder=tk.Button(racine,text="Déchiffrer texte",fg="black",  width=15,command=decoder)
bouton_decoder.grid(row=2, column=1)

resultat=tk.Entry(racine,width = 50, font = ("helvetica", "20"))
resultat.grid(row=3,column=0)


racine.mainloop()
