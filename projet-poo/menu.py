############## importation ###############
import random
import pygame
from elements import *
from terrain import *
from config import *
import config
##########################################

# Définir les couleurs
BLANC = (255, 255, 255)
NOIR = (0, 0, 0)
MARRON = (164, 82, 33)


#===============================================================================================================================

class Home:

    pygame.init()
    
    def __init__(self, background = pygame.image.load('image/home.png'), largeur_bouton =  380, hauteur_bouton = 69 ):
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.__background= pygame.transform.scale(background ,(WIDTH,HEIGHT))
        self.bouton=(largeur_bouton, hauteur_bouton)

    ####### récuperer les classes qui permettent d'afficher les pages #######
    def new_game(self):
        terrain = Terrain(120)
        return terrain
    
    def setting(self):
        setting = Setting()
        return setting
    
    def credit(self):
        credit = Credit()
        return credit
    
    
    ####### Ajout de la musique #######
    def music(self):
        if config.MUSIC_STATE:
            music = pygame.image.load('image/music_on.png')
            pygame.mixer.music.load("Volume Alpha 03. Subwoofer Lullaby.mp3")
            pygame.mixer.music.play(-1)        
        else:
            music=pygame.image.load('image/music_off.png')
            #pygame.mixer.music.stop()

        music = pygame.transform.scale(music ,(60,60))
        self.__screen.blit(music, (20,20))
        pygame.display.flip()
        return music


    def affiche_accueil(self):
        
        ####### Creation des boutons du menu principal #######
        self.__screen.blit(self.__background, (0,0))
        bouton_newgame = pygame.Rect(350, 300-2, self.bouton[0], self.bouton[1])
        bouton_settings = pygame.Rect(350, 400-2, self.bouton[0], self.bouton[1])
        bouton_credits = pygame.Rect(350, 500-2, self.bouton[0], self.bouton[1])
        bouton_exit = pygame.Rect(350, 600-2, self.bouton[0], self.bouton[1])

        ##### La music joue par défaut #####
        music = self.music()

        ####### Activation des boutons et music #######
        RUN=True
        while RUN:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUN = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        RUN = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:

                    ####### active/désactiver le bouton musique #######
                    if music.get_rect().collidepoint(event.pos):
                        print("bouton music !")
                        if config.MUSIC_STATE:
                            config.MUSIC_STATE=False
                            self.music()
                            pygame.mixer.music.set_volume(0)
                            
                        elif config.MUSIC_STATE==0:
                            config.MUSIC_STATE=True
                            self.music()
                            self.__screen.blit(self.__background, (0,0))
                            pygame.mixer.music.set_volume(5)
                        self.__screen.blit(music, (20,20))
                        
                    ####### commencer le jeu #######
                    if bouton_newgame.collidepoint(event.pos):
                        print("bouton New Game !")
                        RUN = False
                        new_game=self.new_game()
                        new_game.affichage()

                    ####### aller sur la page des options #######
                    if bouton_settings.collidepoint(event.pos):
                        print("bouton Settings !")
                        RUN = False
                        settings=Setting()
                        settings.affiche_setting()
                    
                    ####### aller sur la page credits #######
                    if bouton_credits.collidepoint(event.pos):
                        print("bouton credits !")
                        RUN = False
                        credit = Credit()
                        credit.affiche_credits()
                    
                    ####### sortir du jeu #######
                    if bouton_exit.collidepoint(event.pos):
                        RUN=False

            pygame.display.update()
    

    
#===============================================================================================================================


class Setting:
    
    def __init__(self, background = pygame.image.load('image/settings.png') ):
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.__background= pygame.transform.scale(background ,(WIDTH,HEIGHT))
        self.__element_count = DEFAULT_COUNT.copy()  #Faire une copie du Default_count pour que __element_count ne prends pas la nouvelle valeur comme valeur maximale
                                                             

    ###### fonction pour ajouter/enlever un animal ######
    def get_nb_count(self,element):
        return self.__element_count[element]

    def add(self, element):
        if self.__element_count[element] >= 0 and self.get_nb_count(element) < DEFAULT_COUNT[element]:    #sans faire la copie, _element_count et Default_count pointe sur le même dictionnaire 
            self.__element_count[element]+=1
        
    def remove(self, element):
        if self.__element_count[element] > 0:
            self.__element_count[element]-=1


    ###### créer un bouton pour chaque animal ######
    def make_button_set(self, id, x, y):
        police = pygame.font.SysFont("Arial", 45)
        intervalle_b=240
        intervalle_nb=120
        bouton_add = pygame.Rect(x+intervalle_b, y, 30, 50)
        bouton_remove = pygame.Rect(x, y, 30, 50)
        nb_animal = police.render(f"{id}", True, NOIR)
        txt_rect = nb_animal.get_rect()
        txt_rect.centerx = (bouton_add.left + bouton_remove.right)//2
        txt_rect.centery = (bouton_add.top + bouton_remove.bottom)//2
        self.__screen.blit(nb_animal, txt_rect)

        #pygame.draw.rect(self.__screen, BLANC, bouton_add,1)
        #pygame.draw.rect(self.__screen, BLANC, bouton_remove,1)

        return bouton_add, bouton_remove #renvoie les boutons


    def affiche_setting(self):
        police = pygame.font.SysFont("Arial", 45)
        self.__screen.blit(self.__background, (0,0))
        bouton_quit = pygame.Rect(818, 44, 60, 60)


        ############################ Création des boutons #################################
        bouton_cow = self.make_button_set(self.__element_count["Cow"],245,194)
        bouton_pig = self.make_button_set(self.__element_count["Pig"], 245, 298)
        bouton_sheep = self.make_button_set(self.__element_count["Sheep"], 245, 400)
        bouton_rabbit = self.make_button_set(self.__element_count["Rabbit"], 245, 508)

        bouton_falcon = self.make_button_set(self.__element_count["Falcon"], 555, 194)
        bouton_snake = self.make_button_set(self.__element_count["Snake"], 555, 298)
        bouton_wolf = self.make_button_set(self.__element_count["Wolf"], 555, 400)
        bouton_fish = self.make_button_set(self.__element_count["Fish"], 555, 508)

        ok = self.make_button_set("OK", 398, 580)

        ##############################################################################


        RUN=True
        while RUN:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    RUN = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        RUN = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if bouton_quit.collidepoint(event.pos):
                        print("bouton Quit !")
                        RUN = False
                        game=Home() 
                        game.setting()
                        game.affiche_accueil()

                    ###### Ajouter un animal ######
                    if bouton_cow[0].collidepoint(event.pos): #detection du bouton animal 0 (le bouton add)
                        print("bouton cow add")
                        self.add("Cow")    
                        pygame.draw.rect(self.__screen, MARRON, pygame.Rect(350, 198, 80, 40)) # mettre un rectangle marron par dessus l'ecriture existante
                        pygame.display.flip()
                        self.make_button_set(self.__element_count["Cow"],245,194)

                    if bouton_pig[0].collidepoint(event.pos):
                        print("bouton pig add")
                        self.add("Pig")    
                        pygame.draw.rect(self.__screen, MARRON, pygame.Rect(350, 301, 80, 40))
                        pygame.display.flip()
                        self.make_button_set(self.__element_count["Pig"], 245, 298)
                        
                    if bouton_sheep[0].collidepoint(event.pos):
                        print("bouton sheep add")
                        self.add("Sheep")    
                        pygame.draw.rect(self.__screen, MARRON, pygame.Rect(350, 404, 80, 40))
                        pygame.display.flip()
                        self.make_button_set(self.__element_count["Sheep"], 245, 400)

                    if bouton_rabbit[0].collidepoint(event.pos):
                        print("bouton rabbit add")
                        self.add("Rabbit")    
                        pygame.draw.rect(self.__screen, MARRON, pygame.Rect(350, 511, 80, 40))
                        pygame.display.flip()
                        self.make_button_set(self.__element_count["Rabbit"], 245, 508)

                    if bouton_falcon[0].collidepoint(event.pos):
                        print("bouton falcon add")
                        self.add("Falcon")    
                        pygame.draw.rect(self.__screen, MARRON, pygame.Rect(650, 198, 80, 40))
                        pygame.display.flip()
                        self.make_button_set(self.__element_count["Falcon"], 555, 194)

                    if bouton_snake[0].collidepoint(event.pos):
                        print("bouton snake add")
                        self.add("Snake")    
                        pygame.draw.rect(self.__screen, MARRON, pygame.Rect(650, 301, 80, 40))
                        pygame.display.flip()
                        self.make_button_set(self.__element_count["Snake"], 555, 298)

                    if bouton_wolf[0].collidepoint(event.pos):
                        print("bouton wolf add")
                        self.add("Wolf")    
                        pygame.draw.rect(self.__screen, MARRON, pygame.Rect(650, 404, 80, 40))
                        pygame.display.flip()
                        self.make_button_set(self.__element_count["Wolf"], 555, 400)

                    if bouton_fish[0].collidepoint(event.pos):
                        print("bouton fish add")
                        self.add("Fish")    
                        pygame.draw.rect(self.__screen, MARRON, pygame.Rect(650, 511, 80, 40))
                        pygame.display.flip()
                        self.make_button_set(self.__element_count["Fish"], 555, 508)

                    ###### Enlever un animal ######
                    if bouton_cow[1].collidepoint(event.pos): #détection du bouton animal 1 (bouton remove)
                        print("bouton cow remove")
                        self.remove("Cow")
                        pygame.draw.rect(self.__screen, MARRON, pygame.Rect(350, 198, 80, 40))
                        pygame.display.flip()
                        self.make_button_set(self.__element_count["Cow"],245,194)
                            
                    if bouton_pig[1].collidepoint(event.pos):
                        print("bouton pig remove")
                        self.remove("Pig")    
                        pygame.draw.rect(self.__screen, MARRON, pygame.Rect(350, 301, 80, 40))
                        pygame.display.flip()
                        self.make_button_set(self.__element_count["Pig"], 245, 298)

                    if bouton_sheep[1].collidepoint(event.pos):
                        print("bouton sheep remove")
                        self.remove("Sheep")    
                        pygame.draw.rect(self.__screen, MARRON, pygame.Rect(350, 404, 80, 40))
                        pygame.display.flip()
                        self.make_button_set(self.__element_count["Sheep"], 245, 400)

                    if bouton_rabbit[1].collidepoint(event.pos):
                        print("bouton rabbit remove")
                        self.remove("Rabbit")    
                        pygame.draw.rect(self.__screen, MARRON, pygame.Rect(350, 511, 80, 40))
                        pygame.display.flip()
                        self.make_button_set(self.__element_count["Rabbit"], 245, 508)

                    if bouton_falcon[1].collidepoint(event.pos):
                        print("bouton falcon remove")
                        self.remove("Falcon")    
                        pygame.draw.rect(self.__screen, MARRON, pygame.Rect(650, 198, 80, 40))
                        pygame.display.flip()
                        self.make_button_set(self.__element_count["Falcon"], 555, 194)

                    if bouton_snake[1].collidepoint(event.pos):
                        print("bouton snake remove")
                        self.remove("Snake")    
                        pygame.draw.rect(self.__screen, MARRON, pygame.Rect(650, 301, 80, 40))
                        pygame.display.flip()
                        self.make_button_set(self.__element_count["Snake"], 555, 298)

                    if bouton_wolf[1].collidepoint(event.pos):
                        print("bouton wolf remove")
                        self.remove("Wolf")    
                        pygame.draw.rect(self.__screen, MARRON, pygame.Rect(650, 404, 80, 40))
                        pygame.display.flip()
                        self.make_button_set(self.__element_count["Wolf"], 555, 400)
                        
                    if bouton_fish[1].collidepoint(event.pos):
                        print("bouton fish remove")
                        self.remove("Fish")    
                        pygame.draw.rect(self.__screen, MARRON, pygame.Rect(650, 511, 80, 40))
                        pygame.display.flip()
                        self.make_button_set(self.__element_count["Fish"], 555, 508)
                        #nb_animal = police.render(f"{self.__element_count['Fish']}", True, NOIR)
                        #self.__screen.blit(nb_animal, (670, 511))
                         
            pygame.display.update()
   
   

#===============================================================================================================================

class Credit:

    def __init__(self, background = pygame.image.load('image/credits.png') ):
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.__background= pygame.transform.scale(background ,(WIDTH,HEIGHT))
    
    def affiche_credits(self):
        police = pygame.font.SysFont("Arial", 33)
        self.__screen.blit(self.__background, (0,0))
        position_bouton_quit = pygame.Rect(788, 95, 60, 60)


        music_source1 = police.render("Subwoofer Lullaby by C418", True, NOIR)
        music_source2 = police.render("From Minecraft-Volume Alpha n°03", True, NOIR)
        self.__screen.blit(music_source1, (290,460))
        self.__screen.blit(music_source2, (290,500))


        author1 = police.render("Tom Lebel", True, NOIR)
        author2 = police.render("Remy Leber", True, NOIR)
        author3 = police.render("Eliott Goubin", True, NOIR)
        author4 = police.render("Kheda Islamova", True, NOIR)
        self.__screen.blit(author1, (300,265))
        self.__screen.blit(author2, (300,305))
        self.__screen.blit(author3, (300,345))
        self.__screen.blit(author4, (300,385))
        pygame.display.flip()

    
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
                        game=Home() 
                        game.credit()
                        game.affiche_accueil() 
                        
            pygame.display.update()