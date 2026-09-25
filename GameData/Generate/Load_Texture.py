import pygame
pygame.init()


class load(object):
	Fichier_texture = 'default'
	
	
	def load_image(self, chemin, taille):
		try:
			return pygame.transform.scale(pygame.image.load("Pack//"+self.Fichier_texture+"//"+chemin), taille)
		except:
			return pygame.transform.scale(pygame.image.load("Pack//default//"+chemin), taille)
		
	def rotate(self, s, g):
		return pygame.transform.rotate(s, g)
		
	def load_texture(self):
		block = {}
		block['escape_buton'] = self.load_image("Texture//ATH//escape_buton.png", (600,600))
		
		return block