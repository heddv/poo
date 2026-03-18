import pygame

pygame.init()

# Définir les couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
GRIS_FONCE = (40, 40, 40)
GRIS_CLAIR = (100, 100, 100)

# Définir la taille de la fenêtre
taille_fenetre = (800, 600)
fenetre = pygame.display.set_mode(taille_fenetre)

# Définir le texte du bouton
font = pygame.font.Font(None, 36)
texte_bouton = font.render("Cliquez ici", True, BLANC)

# Obtenir les dimensions du texte pour centrer le bouton
largeur_texte, hauteur_texte = font.size("Cliquez ici")
position_x = (taille_fenetre[0] - largeur_texte) // 2
position_y = (taille_fenetre[1] - hauteur_texte) // 2

# Définir les dimensions et la position du bouton
largeur_bouton = largeur_texte + 20
hauteur_bouton = hauteur_texte + 20
position_bouton = pygame.Rect(position_x, position_y, largeur_bouton, hauteur_bouton)

# Dessiner le bouton
pygame.draw.rect(fenetre, GRIS_CLAIR, position_bouton)
pygame.draw.rect(fenetre, NOIR, position_bouton, 2)
fenetre.blit(texte_bouton, (position_x + 10, position_y + 10))

# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Vérifier si le clic est dans le bouton
            if position_bouton.collidepoint(event.pos):
                print("Le bouton a été cliqué !")
    
    pygame.display.update()
