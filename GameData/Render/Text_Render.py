import pygame

def text(screen, text, position, color, size, police="Futura"):
    font = pygame.font.SysFont(police, size)
    screen.blit(font.render(str(text), 1, color), position)