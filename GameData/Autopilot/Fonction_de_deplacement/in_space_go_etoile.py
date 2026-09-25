import random
import math
import GameData.Audio.read

def in_space_go_etoile(self, etoile, r_y, r_x, x, y, z):
    if self.state == 0:
        #choisir
        choix = random.randint(0, (len(etoile)-1))
        etoile_choix_XYZ = etoile[choix][0]

        #parler
        txt = "En direction de l'étoile "+str(etoile[choix][1])+" ."
        print(txt)
        #read.text_to_speech(txt)
        #calculer
        O = etoile_choix_XYZ[1]
        A = (etoile_choix_XYZ[0]**2+etoile_choix_XYZ[2]**2)**0.5
        angle_degrees_target_y = math.degrees(math.atan(O/abs(A)))-r_y
        
        O = etoile_choix_XYZ[0]
        A = etoile_choix_XYZ[2]
        angle_degrees_target_x = r_x+math.degrees(math.atan(O/abs(A)))*-1
        
        angle_degrees_target = [angle_degrees_target_x, angle_degrees_target_y]
        self.in_space_go_etoile_info = [angle_degrees_target, 0]

        #changement d etat
        self.state = 1
    elif self.state == 1:
        r_y = r_y+self.in_space_go_etoile_info[0][1]
        r_x = r_x+self.in_space_go_etoile_info[0][0]
        self.state = 2
    
    return r_y, r_x, x, y, z