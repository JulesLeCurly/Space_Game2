from datetime import datetime
import numpy as np
import os

def sauvegarder_liste_dans_fichier(nom_fichier, ma_liste):
    with open(nom_fichier, 'w') as fichier:
        for element in ma_liste:
            fichier.write(str(element) + '\n')
    print(f"Sauvegarde dans le fichier {nom_fichier}.")


def charger_liste_depuis_fichier(nom_fichier):
    ma_liste = []
    with open(nom_fichier, 'r') as fichier:
        lignes = fichier.readlines()
        for ligne in lignes:
            ma_liste.append(eval(ligne.strip()))  # Retirer les caractères de nouvelle ligne
    print(f"La liste a été chargée depuis le fichier {nom_fichier}.")
    return ma_liste


def save(liste_a_sauvegarder):
    # Obtenir la date et l'heure actuelles
    maintenant = datetime.now()
    
    # Formater la date et l'heure dans un string
    date_heure_string = "Save/"+(maintenant.strftime("%Y-%m-%d %H:%M:%S")+".txt").replace(" ", "_").replace(":", "H")
    
    date_heure_string = "Save/"+(maintenant.strftime("%Y-%m-%d %H:%M:%S")).replace(" ", "_").replace(":", "H")
    np.save(date_heure_string, np.array(liste_a_sauvegarder))
    #sauvegarder_liste_dans_fichier(date_heure_string, liste_a_sauvegarder)

def load():
    dossier = "Save"
    if not os.path.exists(dossier):
        os.makedirs(dossier)
        return None
    fichiers = [f for f in os.listdir(dossier) if f.endswith('.npy')]
    if not fichiers:
        print("Aucune sauvegarde trouvée.")
        return None
    path = os.path.join(dossier, sorted(fichiers)[-1])
    liste_a_sauvegarder = np.load(path).tolist()
    print(f"Sauvegarde chargée : {path}")
    return liste_a_sauvegarder