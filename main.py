import pygame
pygame.init()

# création de la fenetre du jeu
pygame.display.set_mode((800, 600))
pygame.display.set_caption("Wassim Pygame - RPG")

# boucle du jeu
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


pygame.quit()
