
import math
import pygame
import random
import GameData.Render.Text_Render
import Variable_space_render
import time
import GameData.Generate.Generate

Generate = GameData.Generate.Generate
TextRender = GameData.Render.Text_Render


parametre__proximite_centre_ecran = Variable_space_render.parametre__proximite_centre_ecran
parametre__eloignement_etoiles = Variable_space_render.parametre__eloignement_etoiles
parametre__vision_peripherique = Variable_space_render.parametre__vision_peripherique
parametre__taille_etoiles_proches = Variable_space_render.parametre__taille_etoiles_proches
parametre__britnesse = Variable_space_render.parametre__britnesse
size_of_distant_stars = Variable_space_render.size_of_distant_stars
parametre__max_back_render = Variable_space_render.parametre__max_back_render
parametre__text = Variable_space_render.parametre__text

start_time = time.time()

#Traitement de donner
parametre__britnesse = parametre__britnesse/1000000

def angle_de_rotation(initial_time, periode_revolution, warp):
    temps_actuel = time.time()
    temps_ecoule = temps_actuel - initial_time

    # Calculer le nombre de tours complets effectués
    tours_complets = temps_ecoule / periode_revolution

    # Calculer la vitesse de rotation en fonction de la distance et de la variable Warp
    vitesse_rotation = 1 / (warp)

    # Calculer l'angle en degrés (360 degrés par tour)
    angle_degrees = tours_complets * 360 * vitesse_rotation

    return angle_degrees

def rotate_points_around_camera1D(points, camera_position, rotation_angle_degrees):
    # Translation des points par rapport à la caméra
    translated_points = [points[0] - camera_position[0], points[1] - camera_position[1]]

    # Calcul du rayon (r) pour chaque point
    radius = math.hypot(*translated_points)

    # Calcul des nouvelles coordonnées x et y
    angle_radians = math.atan2(translated_points[1], translated_points[0])
    new_angle_radians = angle_radians + math.radians(rotation_angle_degrees)
    new_x = radius * math.cos(new_angle_radians)
    new_y = radius * math.sin(new_angle_radians)

    new_points = [round(new_x+camera_position[0], 2), round(new_y+camera_position[1], 2)]
    return new_points

def rotate_points_around_camera2D(X_etoile, Y_etoile, Z_etoile, x, y, z, r_x, r_y):
    new_position = rotate_points_around_camera1D([X_etoile, Z_etoile], [x, z], r_x)
    X_etoile = new_position[0]
    Z_etoile = new_position[1] 
    
    new_position = rotate_points_around_camera1D([Z_etoile, Y_etoile], [z, y], r_y)
    Y_etoile = new_position[1]
    Z_etoile = new_position[0]
    return X_etoile, Y_etoile, Z_etoile
    
def rotate_points_around_camera3D(X_etoile, Y_etoile, Z_etoile, x, y, z, r_x, r_y, r_e):
    new_position = rotate_points_around_camera1D([X_etoile, Z_etoile], [x, z], r_x)
    X_etoile = new_position[0]
    Z_etoile = new_position[1] 
    
    new_position = rotate_points_around_camera1D([Z_etoile, Y_etoile], [z, y], r_y)
    Z_etoile = new_position[0]
    Y_etoile = new_position[1]
    
    '''
    new_position = rotate_points_around_camera1D([X_etoile, Y_etoile], [z, y], r_e)
    X_etoile = new_position[0]
    Y_etoile = new_position[1]
    '''
    
    return X_etoile, Y_etoile, Z_etoile

def Calcul_distance(x, y, z, display_x_div, display_y_div):
    # Calcul de différences
    diff_x = abs(x - display_x_div)
    diff_y = abs(y - display_y_div)

    # Calcul des distances directes sans racine carrée
    distance_1 = diff_x ** 2 + z ** 2
    distance_2 = distance_1 + diff_y ** 2

    # Retourner la racine carrée de la somme des distances
    return distance_2 ** 0.5


def position(x, y, z, display_x_div, display_y_div):
    x -= display_x_div
    y -= display_y_div
    
    try: x = x/(z/parametre__vision_peripherique)
    except: x = 0.001
    try: y = y/(z/parametre__vision_peripherique)
    except: y = 0.001
    
    x += display_x_div
    y += display_y_div

    return int(x), int(y), int(z)

def Calcul_Planets(distance_etoile, display_x_div, display_y_div, Etoile_XYZ, Planets, x, y, z, r_x, r_y, warp):
    nombre_etoile = len(Planets)
    Planets_list = []
    txt = []
    for index_etoile in range(0, nombre_etoile):
    
        X_Planet = Planets[index_etoile][0][0]+Etoile_XYZ[0]
        Y_Planet = Planets[index_etoile][0][1]+Etoile_XYZ[1]
        Z_Planet = Planets[index_etoile][0][2]+Etoile_XYZ[2]
        
        dist = (X_Planet**2+Y_Planet**2+Z_Planet**2)**0.5
        
        produit = 0
        X_Planet, Y_Planet, Z_Planet = rotate_points_around_camera3D(X_Planet, Y_Planet, Z_Planet, Etoile_XYZ[0], Etoile_XYZ[1], Etoile_XYZ[2], produit, 0, 0)

        
        X_Planet, Y_Planet, Z_Planet = rotate_points_around_camera2D(X_Planet, Y_Planet, Z_Planet, x, y, z, r_x, r_y)
        
        X_Planet += display_x_div - x
        Y_Planet += display_y_div - y
        Z_Planet -= z
        
        
        distance_Planet = Calcul_distance(X_Planet, Y_Planet, Z_Planet, display_x_div, display_y_div)*parametre__eloignement_etoiles
        
        X_Planet, Y_Planet, Z_Planet = position(X_Planet, Y_Planet, Z_Planet, display_x_div, display_y_div)
        if X_Planet < display_x_div*2 and X_Planet > 0 and Y_Planet > 0 and Y_Planet < display_y_div*2 and Z_Planet > 0:
        
            color_Planet = Planets[index_etoile][2]
            color_Planet = tuple(int(max(0, c - (distance_etoile**2) * parametre__britnesse*250)) for c in color_Planet)###################################################
            
            if sum(color_Planet) > 5:
                
                position_etoile_2D = (X_Planet+1, Y_Planet+1)
                
                Taille_cercle = (1000-distance_Planet)*parametre__proximite_centre_ecran
                Taille_cercle = int(Taille_cercle/distance_Planet/parametre__taille_etoiles_proches)/20############################################
                if Taille_cercle < 1:
                    Taille_cercle = 0
                
                Planets_list.append([distance_Planet, (color_Planet, position_etoile_2D, Taille_cercle)])
                #text
                if (distance_Planet*10) < parametre__text[0] and parametre__text[1] and (distance_Planet*20) > 20:
                    txt.append(["Type: Planet / Name: "+Planets[index_etoile][1]+" / "+str(round(distance_Planet/200, 2))+"années-lumière", position_etoile_2D, []])
                    
                if (distance_Planet*20) < 200 and parametre__text[1] and (distance_Planet*20) > 20:
                    txt.append(["Type: Planet / Name: "+Planets[index_etoile][1]+" / "+str(round(distance_Planet/200, 2))+"années-lumière", position_etoile_2D, Planets[index_etoile][3]])
    return Planets_list, txt


def Calcul_etoile(display_x_div, display_y_div, x, y, z, r_x, r_y, etoile, warp):
    Calcul_etoile_dict = {}
    text_list = []
    nombre_etoile = len(etoile)
    Planets = []
    for index_etoile in range(0, nombre_etoile):
        TEST_X = abs(etoile[index_etoile][0][0]-x)
        TEST_Y = abs(etoile[index_etoile][0][1]-y)
        TEST_Z = abs(etoile[index_etoile][0][2]-z)
        
        if TEST_X < parametre__max_back_render and TEST_Y < parametre__max_back_render and TEST_Z < parametre__max_back_render:
            X_etoile = etoile[index_etoile][0][0] 
            Y_etoile = etoile[index_etoile][0][1]
            Z_etoile = etoile[index_etoile][0][2] 
            
            X_etoile, Y_etoile, Z_etoile = rotate_points_around_camera2D(X_etoile, Y_etoile, Z_etoile, x, y, z, r_x, r_y)
            X_etoile += display_x_div - x
            Y_etoile += display_y_div - y
            Z_etoile -= z
            
            distance_etoile = Calcul_distance(X_etoile, Y_etoile, Z_etoile, display_x_div, display_y_div)*parametre__eloignement_etoiles
            
            if distance_etoile < 1000:
                Planets_data, txt = Calcul_Planets(distance_etoile, display_x_div, display_y_div, etoile[index_etoile][0], Generate.generate_planet(str(etoile[index_etoile])), x, y, z, r_x, r_y, warp)
                text_list = text_list + txt
                stop = len(Planets_data)
                for k in range(0, stop):
                    Calcul_etoile_dict[Planets_data[k][0]] = Planets_data[k][1]
                
            X_etoile, Y_etoile, Z_etoile = position(X_etoile, Y_etoile, Z_etoile, display_x_div, display_y_div)
            if X_etoile < display_x_div*2 and X_etoile > 0 and Y_etoile > 0 and Y_etoile < display_y_div*2 and Z_etoile > 0:
            
                color_etoile = etoile[index_etoile][2]
                color_etoile = tuple(int(max(0, c - (distance_etoile**2) * parametre__britnesse)) for c in color_etoile)
                
                if sum(color_etoile) > 5:
                    
                    position_etoile_2D = (X_etoile, Y_etoile)
                    
                    Taille_cercle = (1000-distance_etoile)*parametre__proximite_centre_ecran
                    Taille_cercle = int(Taille_cercle/distance_etoile/parametre__taille_etoiles_proches)
                    if Taille_cercle < 1:
                        Taille_cercle = 0
                    
                    Calcul_etoile_dict[distance_etoile+(random.randint(0, 1000)/1000)] = (color_etoile, position_etoile_2D, Taille_cercle)
                #text
                if distance_etoile < parametre__text[0] and parametre__text[1] and distance_etoile > 20:
                    text_list.append(["Type: Etoile / Name: "+etoile[index_etoile][1]+" / "+str(round(distance_etoile/200, 2))+"années-lumière", position_etoile_2D, []])
                if distance_etoile < 200 and parametre__text[1] and distance_etoile > 20:
                    text_list.append(["Type: Etoile / Name: "+etoile[index_etoile][1]+" / "+str(round(distance_etoile/200, 2))+"années-lumière", position_etoile_2D, etoile[index_etoile][3]])
    Calcul_etoile_dict = {index: Calcul_etoile_dict[index] for index in sorted(Calcul_etoile_dict, reverse=True)}
    return Calcul_etoile_dict, text_list, Planets
    
def affichage(screen, Calcul_etoile_dict, text_list):
    for key, value in Calcul_etoile_dict.items():
        if value[2] < 1:
            pygame.draw.rect(screen, value[0], (value[1][0], value[1][1], size_of_distant_stars, size_of_distant_stars))
        else:
            pygame.draw.circle(screen, value[0], value[1], value[2], 0)
    
    stop = len(text_list)
    for i in range(0, stop):
        if text_list[i][0][:12] == "Type: Etoile":
            TextRender.text(screen, text_list[i][0], text_list[i][1], parametre__text[2], 50)
        else:
            TextRender.text(screen, text_list[i][0], text_list[i][1], parametre__text[3], 50)
            
        if text_list[i][2] != []:
            for d in range(len(text_list[i][2])):
                position_xy = (text_list[i][1][0]+50, text_list[i][1][1]+(d+1)*50)
                if text_list[i][0][:12] == "Type: Etoile":
                    TextRender.text(screen, "- "+text_list[i][2][d], position_xy, parametre__text[2], 50)
                else:
                    TextRender.text(screen, "- "+text_list[i][2][d], position_xy, parametre__text[3], 50)