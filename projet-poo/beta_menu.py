import pygame
import config
from beta_terrain import *

pygame.init()
pygame.mixer.init()

# Définir les couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
MARRON = (164, 82, 33)

# Définir la taille de la fenêtre
WIDTH= config.WIDTH; HEIGHT= config.HEIGHT
taille_fenetre = (WIDTH, HEIGHT)
fenetre = pygame.display.set_mode(taille_fenetre)
pygame.display.set_caption("Jeu de la vie")

pygame.mixer.music.load("Volume Alpha 03. Subwoofer Lullaby.mp3")
pygame.mixer.music.play(-1)


    




def home_page():
    fond_home = pygame.image.load('image/home.png')
    fond_home = pygame.transform.scale(fond_home ,(WIDTH,HEIGHT))
    fenetre.blit(fond_home, (0,0))

    
    if config.MUSIC_STATE:
        music=pygame.image.load('image/music_on.png')
        music=pygame.transform.scale(music ,(60,60))
        fenetre.blit(music, (20,20))        
    else:
        music=pygame.image.load('image/music_off.png')
        music=pygame.transform.scale(music ,(60,60))
        fenetre.blit(music, (20,20))


    

    # Définir les dimensions et la position des boutons
    largeur_bouton =  380
    hauteur_bouton = 69
    position_bouton_NewGame = pygame.Rect(350, 300-2, largeur_bouton, hauteur_bouton)
    position_bouton_settings = pygame.Rect(350, 400-2, largeur_bouton, hauteur_bouton)
    position_bouton_credits = pygame.Rect(350, 500-2, largeur_bouton, hauteur_bouton)
    position_bouton_quit = pygame.Rect(350, 600-2, largeur_bouton, hauteur_bouton)

    # Dessiner le bouton
    pygame.draw.rect(fenetre, BLANC, position_bouton_NewGame,1)
    pygame.draw.rect(fenetre, BLANC, position_bouton_settings,1)

    RUN=True
    while RUN:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    RUN = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # Vérifier si le clic est dans le bouton
                if position_bouton_NewGame.collidepoint(event.pos):
                    print("bouton New Game !")
                    startGame()
                if position_bouton_settings.collidepoint(event.pos):
                    print("bouton Settings !")
                    RUN = False
                    setting_page()
                if music.get_rect().collidepoint(event.pos):
                    print("bouton music !")
                    if config.MUSIC_STATE:
                        config.MUSIC_STATE=False
                        music=pygame.image.load('image/music_off.png')
                        music=pygame.transform.scale(music ,(60,60))
                        fenetre.blit(music, (20,20))
                        pygame.mixer.music.set_volume(0)
                        
                    elif config.MUSIC_STATE==0:
                        config.MUSIC_STATE=True
                        music=pygame.image.load('image/music_on.png')
                        music=pygame.transform.scale(music ,(60,60))
                        fenetre.blit(music, (20,20))
                        pygame.mixer.music.set_volume(5)

                if position_bouton_credits.collidepoint(event.pos):
                    print("bouton Credits !")
                    RUN = False
                    credit_page()
                if position_bouton_quit.collidepoint(event.pos):
                    print("bouton Quit !")
                    RUN = False

        pygame.display.update()


def setting_page():
    fond_settings = pygame.image.load('image/settings.png')
    fond_settings= pygame.transform.scale(fond_settings ,(WIDTH,HEIGHT))
    fenetre.blit(fond_settings, (0,0))

    # Définir les dimensions et la position du bouton
    position_bouton_quit = pygame.Rect(818, 44, 60, 60)
    position_bouton_addSheep = pygame.Rect(490, 399, 30, 50)
    position_bouton_addCow = pygame.Rect(490, 193, 30, 50)
    position_bouton_removeCow = pygame.Rect(250, 193, 30, 50)
    
    pygame.draw.rect(fenetre, BLANC, position_bouton_quit,1)
    pygame.draw.rect(fenetre, BLANC, position_bouton_addSheep,1)
    pygame.draw.rect(fenetre, BLANC, position_bouton_addCow,1)
    pygame.draw.rect(fenetre, BLANC, position_bouton_removeCow,1)


    # Définir le texte des options
    police = pygame.font.SysFont("Arial", 50)
    nb_sheep = police.render(f"{config.SHEEP_COUNT}", True, NOIR)
    fenetre.blit(nb_sheep, (370, 410))
    nb_cow = police.render(f"{config.COW_COUNT}", True, NOIR)
    fenetre.blit(nb_cow, (370, 203))

    RUN=True
    while RUN:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    RUN = False

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if position_bouton_quit.collidepoint(event.pos):
                    print("bouton Quit !")
                    RUN = False
                if position_bouton_addSheep.collidepoint(event.pos):
                    config.SHEEP_COUNT+=1
                    pygame.draw.rect(fenetre, MARRON, pygame.Rect(350, 405, 70, 40))
                    pygame.display.flip()
                    nb_sheep = police.render(f"{config.SHEEP_COUNT}", True, NOIR)
                    fenetre.blit(nb_sheep, (370, 410))
                    #print(f"bouton mouton : {config.SHEEP_COUNT}")
                if position_bouton_addCow.collidepoint(event.pos):
                    config.COW_COUNT+=1
                    pygame.draw.rect(fenetre, MARRON, pygame.Rect(350, 198, 70, 40))
                    pygame.display.flip()
                    nb_cow = police.render(f"{config.COW_COUNT}", True, NOIR)
                    fenetre.blit(nb_cow, (370, 203))
                    #print(f"bouton mouton : {config.COW_COUNT}")
                if position_bouton_removeCow.collidepoint(event.pos):
                    if config.COW_COUNT>0:
                        config.COW_COUNT-=1
                        pygame.draw.rect(fenetre, MARRON, pygame.Rect(350, 198, 70, 40))
                        pygame.display.flip()
                        nb_cow = police.render(f"{config.COW_COUNT}", True, NOIR)
                        fenetre.blit(nb_cow, (370, 203))
                    
                    
        pygame.display.update()

    home_page()
    return config.SHEEP_COUNT

    
def credit_page():
    fond_settings = pygame.image.load('image/credits.png')
    fond_settings= pygame.transform.scale(fond_settings ,(WIDTH,HEIGHT))
    fenetre.blit(fond_settings, (0,0))

    position_bouton_quit = pygame.Rect(725, 140, 60, 60)
    
    pygame.draw.rect(fenetre, BLANC, position_bouton_quit,1)

    police = pygame.font.SysFont("Arial", 32)
    music_source1 = police.render("Subwoofer Lullaby by C418", True, NOIR)
    music_source2 = police.render("From Minecraft-Volume Alpha n°03", True, NOIR)
    fenetre.blit(music_source1, (355,460))
    fenetre.blit(music_source2, (355,490))


    RUN=True
    while RUN:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                RUN = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    RUN = False
 
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if position_bouton_quit.collidepoint(event.pos):
                    print("bouton Quit !")
                    RUN = False
                    
        pygame.display.update()

    home_page()


if __name__ == "__main__":
       home_page()



