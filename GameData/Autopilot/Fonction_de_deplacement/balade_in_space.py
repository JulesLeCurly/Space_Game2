import random
import math
import GameData.Audio.read
import time

class balade_in_space():
    def __init__(self):
        self.state = None
        self.state_fonction = ""
        puissance = 10
    
    def hyper_space(x, a, b):
        calcule = ((x/(a/2))-1)**2
        return (calcule*(-1)+1)*b
    def balade_in_space(self, r_y, r_x, x, y, z):
            if self.state == None or time.time() > self.state[0]:
                #temps, puissance, r_x, r_y, etat
                self.state = [time.time()+random.randint(20, 60),
                            random.randint(5, 30),
                            random.randint(-180, 180),
                            random.randint(-90, 90)]
                print("changement", self.state)
    
            r_y = self.hyper_space(r_y, self.state)
            if r_y > 90: r_y = 90
            if r_y < -90: r_y = -90
            
            if r_x < -180: r_x = 180
            if r_x > 180: r_x = -180
            
            puissance = self.state[1]
    
            yy = abs(r_y)/90
            yy = 1-yy
            z += math.cos(math.radians(r_x)) * puissance * yy
            x += math.sin(math.radians(r_x)) * puissance * yy
            y -= math.sin(math.radians(r_y)) * puissance
    
            return r_y, r_x, x, y, z