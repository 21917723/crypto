# on stocke toutes les lettres du code secret (on se debarasse des chiffres et des symboles de ponctuation)
lettre_codeSecret = "famycuiowdknlvsoqxg"
# on construit astucieusement le string lettre_vrai pour faire correspondre les positions des lettres du code secret avec leur substitution
lettre_vrai = "mzgudtsrfniahcorpel"

Code_secret = "gx qosvlnkd wkvlkxo xiu vscx qno yd fsu cx qniix cx unkggx kdvsddyx xu vsdukxdu g'kdckvx. gxi gxuuoxi cy fsu cx qniix qxofxuuxdu cx cxvngxo gxi gxuuoxi cy fxiinmx sokmkdng fscygs 26. ixygxi gxi gxuuoxi cx n n a isdu vlkwwoxxi."

def decoder(code_secret):
    message_decoder = ""
    for caractere in code_secret:
        if caractere in lettre_codeSecret:
            # on remplace ce caractere par sa substitution c-a-d par la lettre se trouvant a la meme position dans le string lettre_vrai
            message_decoder += lettre_vrai[lettre_codeSecret.index(caractere)] # la methode .index() retourne l'indice de la valeur en argument dans le string
        else:
            # le caractere n'est donc pas une lettre, on ne le remplace pas (puisqu'il n'a pas été chiffré par substitution)
            message_decoder += caractere
    return message_decoder

print(decoder(Code_secret))