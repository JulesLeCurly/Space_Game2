import pygame
import math

class Coordonnees:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0
        self.r_x = 0
        self.r_y = 0
        self.puissance = 1
        self.warp = 1

    def augmenter_puissance(self):
        self.puissance += self.puissance / 50
        if self.puissance > 200:
            self.puissance = 200

    def diminuer_puissance(self):
        self.puissance -= self.puissance / 50
        if self.puissance < 0.01:
            self.puissance = 0.01

    def augmenter_warp(self):
        self.warp += self.warp*0.01
        if self.warp > 10**10:
            self.warp = 10**10

    def diminuer_warp(self):
        self.warp -= self.warp*0.01
        if self.warp < 0.01:
            self.warp = 0.01
            
    def deplacer(self):
        touches = pygame.key.get_pressed()
        angle_y = abs(self.r_y) / 90
        angle_y = 1 - angle_y

        if touches[pygame.K_r]:
            self.augmenter_warp()
        if touches[pygame.K_f]:
            self.diminuer_warp()
            
        if touches[pygame.K_a]:
            self.augmenter_puissance()
        if touches[pygame.K_e]:
            self.diminuer_puissance()

        if touches[pygame.K_z]:
            self.z += math.cos(math.radians(self.r_x)) * self.puissance * angle_y
            self.x += math.sin(math.radians(self.r_x)) * self.puissance * angle_y
            self.y -= math.sin(math.radians(self.r_y)) * self.puissance
        if touches[pygame.K_s]:
            self.z -= math.cos(math.radians(self.r_x)) * self.puissance * angle_y
            self.x -= math.sin(math.radians(self.r_x)) * self.puissance * angle_y
            self.y += math.sin(math.radians(self.r_y)) * self.puissance

        if touches[pygame.K_d]:
            self.z -= math.sin(math.radians(self.r_x)) * self.puissance
            self.x += math.cos(math.radians(self.r_x)) * self.puissance
        if touches[pygame.K_q]:
            self.z += math.sin(math.radians(self.r_x)) * self.puissance
            self.x -= math.cos(math.radians(self.r_x)) * self.puissance

        if touches[pygame.K_LSHIFT]:
            self.y -= self.puissance
        if touches[pygame.K_LCTRL]:
            self.y += self.puissance
