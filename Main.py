#importation des fichiers
import GameData.inputs_and_coordonne.souris
import GameData.inputs_and_coordonne.All_coordonne_Player
import GameData.Render.Space_Render
import GameData.Render.FPS_module
import GameData.Render.Text_Render
import GameData.Generate.Generate
import GameData.Audio.musique
import GameData.Autopilot.Autopilot
import GameData.Save.Save_load
import Variable

save_module = GameData.Save.Save_load
audio_module = GameData.Audio.musique.SoundGame()
TextRender = GameData.Render.Text_Render
FPS = GameData.Render.FPS_module.FPS()
coordonnees = GameData.inputs_and_coordonne.All_coordonne_Player.Coordonnees()
mouse_tracker = GameData.inputs_and_coordonne.souris.MouseTracker()
Autopilot = GameData.Autopilot.Autopilot.Autopilot()

Generate = GameData.Generate.Generate
Space_Render = GameData.Render.Space_Render

# Importation des bibliothèques nécessaires
import pygame
import time
import ast

# Initialisation de Pygame
pygame.init()

# Définition des dimensions de l'écran
display_x_div, display_y_div = int(Variable.display_x / 2), int(Variable.display_y / 2)
pygame.display.set_caption("space_game2")
screen = pygame.display.set_mode((Variable.display_x, Variable.display_y))
pygame.mouse.set_visible(True)

# Liste des étoiles
'''
etoile = []
etoile2 = [[
[0, 0, 100], 'Test', (255, 255, 255), ["r"],

[
[[0, 0, 10], 'P_Test', (255, 0, 0), ["r"]], [[0, 0, 100], 'P_Test2', (0, 255, 0), ["r"]], [[1000, 0, 1000], 'P_Test2', (0, 255, 0), ["r"]]
]
]]
'''

# Configuration des paramètres de suivi de la souris
mouse_tracker.stress = 0.1

# Configuration de la puissance des coordonnées
coordonnees.puissance = 10

# Initialisation de la variable de chunk
chunk = ()
All_data_etoile = {}
Taille_chunk_moitier = int(Variable.Taille_chunk / 2)

time_save_screen = 0

Calcul_etoile_dict = {}
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
    # Calcul du nombre d'images par seconde (FPS)
    nb_fps = FPS.main()
    
    # Calcul du chunk actuel en fonction des coordonnées
    temp_chunk = (
        int((coordonnees.x) / Variable.Taille_chunk),
        int((coordonnees.y) / Variable.Taille_chunk),
        int((coordonnees.z) / Variable.Taille_chunk)
    )
    
    # Génération de nouveaux éléments du jeu si le chunk a changé
    if chunk != temp_chunk:
        etoile, All_data_etoile = Generate.main_generate_chunk(temp_chunk, All_data_etoile)
    
    chunk = temp_chunk
    
    # Mise à jour des coordonnées de la caméra en fonction du mouvement de la souris
    if False:
        coordonnees.r_y, coordonnees.r_x, coordonnees.x, coordonnees.y, coordonnees.z = Autopilot.main(etoile, coordonnees.r_y, coordonnees.r_x, coordonnees.x, coordonnees.y, coordonnees.z)

    coordonnees.r_x, coordonnees.r_y = mouse_tracker.main()
    coordonnees.deplacer()
    
    # Gestion du son
    audio_module.main(Variable.Pack)
    
    # Mise à jour de l'affichage graphique
    screen.fill((0, 0, 0))
    
    if Variable.Show_info:
        # Affichage du nombre d'images par seconde
        text = "FPS:" + str(nb_fps)
        TextRender.text(screen, text, (0, Variable.display_y - 50), (100, 100, 100), 50)
        
        # Affichage des coordonnées de la caméra et du chunk actuel
        text = "Camera Rotation: X:" + str(coordonnees.r_x) + " Y:" + str(coordonnees.r_y) + f"  /  XYZ: {round(coordonnees.x)} {round(coordonnees.y)} {round(coordonnees.z)}"
        TextRender.text(screen, text, (0, 0), (100, 100, 100), 50)
    
    # Affichage de la confiramtion de la sauvergarde
    if time_save_screen > time.time():
        text = "Sauvegarde..."
        produit = int(((time_save_screen-time.time())*255)/5)
        TextRender.text(screen, text, (0, 0), (produit, produit, produit), 100)
    
    # Calcul et affichage des étoiles à l'écran
    Calcul_etoile_dict, text_list, Planets = Space_Render.Calcul_etoile(display_x_div, display_y_div, coordonnees.x, coordonnees.y, coordonnees.z, coordonnees.r_x, coordonnees.r_y, etoile, coordonnees.warp)
    Space_Render.affichage(screen, Calcul_etoile_dict, text_list)
    
    # Rafraîchissement de l'écran
    pygame.display.flip()
    
    if pygame.key.get_pressed()[pygame.K_o]:
        print(chunk,"/", coordonnees.x, coordonnees.y, coordonnees.z,"r_x", coordonnees.r_x, coordonnees.r_y,"p",coordonnees.puissance)
        time.sleep(0.5)
    
    if pygame.key.get_pressed()[pygame.K_w] and time_save_screen < time.time():
        liste_a_sauvegarder = [coordonnees.x, coordonnees.y, coordonnees.z, coordonnees.r_x, coordonnees.r_y, coordonnees.puissance, Variable.seed]
        save_module.save(liste_a_sauvegarder)
        time_save_screen = time.time()+5
    if pygame.key.get_pressed()[pygame.K_x]:
        liste_a_sauvegarder = save_module.load()
        if liste_a_sauvegarder is not None:
            coordonnees.x, coordonnees.y, coordonnees.z, coordonnees.r_x, coordonnees.r_y, coordonnees.puissance, Variable.seed = (
                ast.literal_eval(str(liste_a_sauvegarder[0])),
                ast.literal_eval(str(liste_a_sauvegarder[1])),
                ast.literal_eval(str(liste_a_sauvegarder[2])),
                ast.literal_eval(str(liste_a_sauvegarder[3])),
                ast.literal_eval(str(liste_a_sauvegarder[4])),
                ast.literal_eval(str(liste_a_sauvegarder[5])),
                str(liste_a_sauvegarder[6])
            )
            time.sleep(0.1)