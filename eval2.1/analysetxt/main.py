from nettoyer_texte import nettoyer_texte
from compter_mots import compter_mots
from detecter_mot_suspect import detecter_mot_suspect


def analyser_texte():

    texte = input("Entrez un texte pour l'analyse : ")

    texte_nettoye = nettoyer_texte(texte)

    nb_mots = compter_mots(texte_nettoye)
    print(f"Le texte contient {nb_mots} mots.")

    mot_suspect = input("Entrez un mot a rechercher dans le texte")

    if detecter_mot_suspect(texte_nettoye, mot_suspect):
        print(f"Le mot '{mot_suspect}' est présent dans le texte")
    else:
        print(f"Le mot '{mot_suspect}' est pas présent dans le texte")
        
analyser_texte()