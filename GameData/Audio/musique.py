import pygame
import os
import time
import random

class SoundGame(object):
    def __init__(self):
        self.musique_timer = 0
    
    def get_audio_duration(self, file_path):
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        return pygame.mixer.Sound(file_path).get_length()

        
    def jouer_musique(self, fichier_musique):
        pygame.mixer.init()
        pygame.mixer.music.load(fichier_musique)
        pygame.mixer.music.play()
    
    def arreter_musique(self):
        pygame.mixer.music.stop()
    
    def mettre_en_pause(self):
        pygame.mixer.music.pause()
    
    def reprendre_musique(self):
        pygame.mixer.music.unpause()
    
    def play_a_musique(self, texture_pack):
        # Définir le dossier de la musique en fonction du pack de textures
        dossier = os.path.join("Pack", texture_pack, "Sound", "Musique", "in space")
    
        fichiers = os.listdir(dossier)
        musique_path = []
        
        for fichier in fichiers:
            chemin_complet = os.path.join(dossier, fichier)
            if os.path.isfile(chemin_complet):
                print("audio_module: Musique charger:",fichier)
                musique_path.append(chemin_complet)
        
        musique_path = random.choice(musique_path)#choix aleatoire
        
        if musique_path:
            self.jouer_musique(musique_path)
            print("audio_module: Lecture:",musique_path)
            return self.get_audio_duration(musique_path)
        else:
            return 0  # Aucun fichier de musique trouvé
    
    def main(self, Pack):
        if self.musique_timer < time.time():
            # Jouer une musique aléatoire à partir du pack de textures "default"
            try:
                audio_duration = self.play_a_musique(Pack) + random.randint(5, 60)
            except:
                audio_duration = self.play_a_musique("default") + random.randint(5, 60)
            self.musique_timer = int(time.time() + audio_duration)
            print("audio_module: Changement de musique dans "+str(int(self.musique_timer-time.time()))+"s")