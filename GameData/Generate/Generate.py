import random as random2

import hashlib
import random
import Variable

def interpoler_couleur(couleur_debut, couleur_fin, t):
    rouge = int(couleur_debut[0] + (couleur_fin[0] - couleur_debut[0]) * t)
    vert = int(couleur_debut[1] + (couleur_fin[1] - couleur_debut[1]) * t)
    bleu = int(couleur_debut[2] + (couleur_fin[2] - couleur_debut[2]) * t)
    return (rouge, vert, bleu)

def couleur_par_nombre(nombre):
    v = 50
    bleu = (v, v, 255-v)
    blanc = (255-v, 255-v, 255-v)
    jaune = (255-v, 255-v, v)
    orange = (255-v, 165, v)
    rouge = (255-v, v, v)
    
    # Conversion du nombre en une valeur entre 0 et 1
    valeur_normalisee = nombre
    
    # Séparation en intervalles égaux
    intervalle = 1 / 4
    intervalle_bleu_blanc = intervalle
    intervalle_blanc_jaune = intervalle * 2
    intervalle_jaune_orange = intervalle * 3
    intervalle_orange_rouge = intervalle * 4
    
    if valeur_normalisee <= intervalle_bleu_blanc:
        # Entre bleu et blanc
        t = valeur_normalisee / intervalle_bleu_blanc
        couleur = interpoler_couleur(bleu, blanc, t)
    elif valeur_normalisee <= intervalle_blanc_jaune:
        # Entre blanc et jaune
        t = (valeur_normalisee - intervalle_bleu_blanc) / (intervalle_blanc_jaune - intervalle_bleu_blanc)
        couleur = interpoler_couleur(blanc, jaune, t)
    elif valeur_normalisee <= intervalle_jaune_orange:
        # Entre jaune et orange
        t = (valeur_normalisee - intervalle_blanc_jaune) / (intervalle_jaune_orange - intervalle_blanc_jaune)
        couleur = interpoler_couleur(jaune, orange, t)
    else:
        # Entre orange et rouge
        t = (valeur_normalisee - intervalle_jaune_orange) / (intervalle_orange_rouge - intervalle_jaune_orange)
        couleur = interpoler_couleur(orange, rouge, t)
    
    return couleur

def sha256_decimal(text):
        # Calculer le hachage SHA-256
        hash_object = hashlib.sha256(text.encode('utf-8'))
        hex_digest = hash_object.hexdigest()

        # Convertir le résultat hexadécimal en décimal
        decimal_value = int(hex_digest, 16)

        return decimal_value

def donnees_planete():
    Donnees = []
    
    # Type de planète
    type_planete = random2.choice(["Tellurique", "Gazeuse", "Naine", "Exoplanète"])
    Donnees.append("Type de planète : " + type_planete)
    
    # Masse
    masse = round(random2.uniform(0.01, 100), 2)  # Valeur aléatoire entre 0.01 et 100 masses terrestres
    Donnees.append("Masse : " + str(masse) + " masses terrestres")
    
    # Rayon
    rayon = round(random2.uniform(0.1, 100), 2)  # Valeur aléatoire entre 0.1 et 100 fois le rayon de la Terre
    Donnees.append("Rayon : " + str(rayon) + " rayons terrestres")
    
    # Distance par rapport à l'étoile hôte
    distance = round(random2.uniform(10, 100), 2)  # Valeur aléatoire en unités astronomiques (UA)
    Donnees.append("Distance par rapport à l'étoile hôte : " + str(distance*10) + " UA")
    
    # Période de révolution
    periode_revolution = round(distance, 2)  # Valeur aléatoire en jours
    Donnees.append("Période de révolution : " + str(periode_revolution) + " jours")
    
    # Composition atmosphérique
    composition_atmospherique = "Azote : " + str(random2.randint(1, 80)) + "%, Oxygène : " + str(random2.randint(1, 30)) + "%, Autres : " + str(random2.randint(1, 50)) + "%"
    Donnees.append("Composition atmosphérique : " + composition_atmospherique)
    
    # Température de surface
    temperature_surface = round(random2.uniform(-100, 500), 2)  # Valeur aléatoire en degrés Celsius
    Donnees.append("Température de surface : " + str(temperature_surface) + " °C")
    
    # Présence de vie
    presence_vie = "Oui" if random2.choice([True, False]) else "Non"
    Donnees.append("Présence de vie : " + presence_vie) # Si la présence de vie est détectée, générer des détails sur le type de vie
    if presence_vie == "Oui":
        type_vie = random2.choice(["Micro-organismes", "Plantes", "Animaux", "Civilisation intelligente"])
        Donnees.append("Type de vie : " + type_vie)
        
        if type_vie == "Civilisation intelligente":
            niveau_technologique = random2.choice(["Primitif", "Avancé", "Niveau Humain", "Hyper-avancé", "Ultra-avancé"])
            Donnees.append("Niveau technologique de la civilisation : " + niveau_technologique)
    
    
    return Donnees, distance


def donnees_etoile():
    
    Donnees = []
    
    # Type spectral
    type_spectral = "MNO"[random.randint(0, 2)] + "ABCFGKM"[random.randint(0, 6)]
    Donnees.append("Type spectral : " + type_spectral)
    
    # Luminosité (magnitude apparente)
    magnitude_apparente = round(random.uniform(0, 10), 2)  # Valeur aléatoire entre 0 et 10
    Donnees.append("Luminosité : " + str(magnitude_apparente))
    
    # Masse
    masse = round(random.uniform(0.1, 100), 2)  # Valeur aléatoire entre 0.1 et 100 masses solaires
    Donnees.append("Masse : " + str(masse) + " masses solaires")
    
    # Taille (rayon)
    rayon = round(random.uniform(0.1, 1000), 2)  # Valeur aléatoire entre 0.1 et 1000 fois le rayon solaire
    Donnees.append("Taille (rayon) : " + str(rayon) + " rayons solaires")
    
    # Âge
    age = round(random.uniform(1, 13.8), 2)  # Valeur aléatoire entre 1 et 13.8 milliards d'années (âge de l'univers)
    Donnees.append("Âge : " + str(age) + " milliards d'années")
    
    # Composition chimique
    composition_chimique = "Hydrogène : " + str(random.randint(1, 100)) + "%, Hélium : " + str(random.randint(0, 100)) + "%, Autres : " + str(random.randint(0, 100)) + "%"
    Donnees.append("Composition chimique : " + composition_chimique)
    
    # Magnétisme
    magnetisme = "Oui" if random.choice([True, False]) else "Non"
    Donnees.append("Magnétisme : " + magnetisme)
    
    # Rotation
    vitesse_rotation = round(random.uniform(0, 500), 2)  # Valeur aléatoire entre 0 et 500 km/s
    Donnees.append("Vitesse de rotation : " + str(vitesse_rotation) + " km/s")
    
    # Activité stellaire
    activite_stellaire = random.choice(["Éruptions solaires", "Taches solaires", "Émissions de rayons X", "Aucune"])
    Donnees.append("Activité stellaire : " + activite_stellaire)
    
    # Évolution
    evolution = random.choice(["Naine blanche", "Supernova", "Étoile géante", "Autre"])
    Donnees.append("Évolution : " + evolution)
    
    return Donnees

def generate_etoile_name():
    characters = "abcdefghijklmnopqrstuvwxyz1234567890-"
    return ''.join(random.choice(characters) for _ in range(10))

def generate_etoile_position(name_chunk, Taille_chunk):
    Taille_chunk_moitier = int(Taille_chunk/2)
    X = random.randint(-Taille_chunk_moitier, Taille_chunk_moitier) + name_chunk[0] * Taille_chunk
    Y = random.randint(-Taille_chunk_moitier, Taille_chunk_moitier) + name_chunk[1] * Taille_chunk
    Z = random.randint(-Taille_chunk_moitier, Taille_chunk_moitier) + name_chunk[2] * Taille_chunk
    return [X, Y, Z]

def generate_planet(seed):
    random2.seed(sha256_decimal(seed))
    Planets = []
    stop = random2.randint(0, 5)
    for z in range(0, stop):
        Donnees, distance = donnees_planete()
        name = ''.join(random2.choice("abcdefghijklmnopqrstuvwxyz1234567890-") for _ in range(10))
        color = (random2.randint(10, 255), random2.randint(10, 255), random2.randint(10, 255))
        Planets.append([[0, 0, distance], name, color, Donnees])
    
    return Planets
def generate_etoile(name_chunk, seed, Taille_chunk, Nombre_etoile_chunk):
    seed_chunk = sha256_decimal(str(name_chunk)+str(seed))
    random.seed(seed_chunk)
    
    etoile = []
    for _ in range(0, Nombre_etoile_chunk):
        position = generate_etoile_position(name_chunk, Taille_chunk)
        name = generate_etoile_name()
        Donnees = donnees_etoile()
        etoile.append([position , name, couleur_par_nombre(random.randint(0, 10000)/10000), Donnees])
    
    return etoile

def main_generate_chunk(middle_chunk, All_data_etoile):
    
    nation = []
    
    for x in range(-1, 2):
        for y in range(-1, 2):
            for z in range(-1, 2):
                name_chunk = (middle_chunk[0] + x, middle_chunk[1] + y, middle_chunk[2] + z)
                
                nation.append(name_chunk)
    
    #nation = [(0, 0, 0)]
    stop = len(nation)
    for i in range(0, stop):
        if not nation[i] in All_data_etoile:
            All_data_etoile[nation[i]] = generate_etoile(nation[i], Variable.seed, Variable.Taille_chunk, Variable.Nombre_etoile_chunk)
    
    
    # Créez une copie du dictionnaire pour éviter de modifier le dictionnaire d'origine
    All_data_etoile_copie = All_data_etoile.copy()
    
    # Parcourez chaque clé du dictionnaire
    for key in All_data_etoile_copie.keys():
        # Si la clé n'est pas dans la liste nation, supprimez-la du dictionnaire
        if key not in nation:
            del All_data_etoile[key]
        
    
    liste_etoile = []
    for key, value in All_data_etoile.items():
        liste_etoile = liste_etoile + value
    
    return liste_etoile, All_data_etoile
