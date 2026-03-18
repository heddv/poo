############## importation ###############
import random
import pygame
from elements import *
from config import *
##########################################

class Terrain:

    pygame.init()
    clock = pygame.time.Clock()

    def __init__(self, area_size, background=pygame.image.load('image/fond.png')):
        self.__screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.__background= pygame.transform.scale(background ,(WIDTH,HEIGHT))

        self.area_size = area_size
        NB_REGIONS_X = self.__screen.get_width() // self.area_size
        NB_REGIONS_Y = self.__screen.get_height() // self.area_size
        self.regions = {}
        for x in range(NB_REGIONS_X):
            for y in range(NB_REGIONS_Y):
                self.regions[(x, y)] = []


    def is_free_place(self, x, y, zone):
        rect = pygame.Rect(x, y, zone.rect.width, zone.rect.height)
        return zone.rect.colliderect(rect)
    
    def get_random_free_place(self,surface):
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if self.is_free_place(x,y,surface):
                    return x,y
        return None
    
    def get_random_place(self,zone):
        x= random.randint(zone[0][0],zone[0][1])
        y=random.randint(zone[1][0],zone[1][1])
        return x,y                  

    
    def create_groups(self):
        #creation des different groupes de elements
        peacefull_list = pygame.sprite.Group()
        savaged_list = pygame.sprite.Group()
        car_list = pygame.sprite.Group()
        human_list = pygame.sprite.Group()
        resource_list = pygame.sprite.Group()
        print(ELEMENTS_COUNT.keys())
        for key in ELEMENTS_COUNT.keys():
            for i in range(ELEMENTS_COUNT[key]):
                element=eval(f"{key}()")
                if element.type == "peacefull":
                    for i in range(ELEMENTS_COUNT[key]):
                        peacefull_list.add(element)
                elif element.type == "savaged":
                    for i in range(ELEMENTS_COUNT[key]):
                        savaged_list.add(element)
                elif type(element) == Car:
                    for i in range(ELEMENTS_COUNT[key]):
                        car_list.add(element)
                elif element.type == "resource":
                    for i in range(ELEMENTS_COUNT[key]):
                        resource_list.add(element)
                elif type(element) == Human:
                    for i in range(ELEMENTS_COUNT[key]):
                        human_list.add(element)

        return peacefull_list, savaged_list, car_list, human_list
        
    
    def place_elements(self, elements_list):

        for sprite in elements_list:
            if type(sprite) == Car:
                if sprite.color == 'Red':
                    sprite.rect.x,sprite.rect.y =(815, 0)
                else :
                    sprite.rect.x,sprite.rect.y =(750, 590)

            elif type(sprite)==Bear:
                sprite.rect.x,sprite.rect.y = self.get_random_place([[0,200],[0,200]])
            else :
                sprite.rect.x,sprite.rect.y = self.get_random_place([[200,WIDTH-100],[200,HEIGHT-100]])

            #print(sprite.rect.x,sprite.rect.y)
            x = sprite.rect.x // self.area_size
            y = sprite.rect.y // self.area_size
            self.regions[(x, y)].append(sprite)

    def update(self, sprite):        
        sprite.rect.x += sprite.vx
        sprite.rect.y += sprite.vy
        
        if type(sprite)==Bear:
            if sprite.rect.left < 0 or sprite.rect.right > 300:
                sprite.vx = -sprite.vx
            if sprite.rect.top < 0 or sprite.rect.bottom > 300:
                sprite.vy = -sprite.vy
        
        elif type(sprite) == Car:
            #print(self.__screen.get_height()+100,sprite.rect.bottom)
            if sprite.rect.top < 0 :
                sprite.rect.y = self.__screen.get_height()-sprite.image.get_height()
            elif sprite.rect.bottom > 900:
                sprite.rect.y = 0

        else:
            if sprite.rect.left < 0 or sprite.rect.right-100 > self.__screen.get_width():
                sprite.vx = -sprite.vx
            if sprite.rect.top < 0 or sprite.rect.bottom-100 > self.__screen.get_height():
                sprite.vy = -sprite.vy


    def detect_collisions(self, list_sprite):

        for sprite1 in list_sprite:
            for sprite2 in list_sprite:
                if sprite1 != sprite2 and sprite1.rect.colliderect(sprite2.rect):
                    print(f"||{type(sprite1)}|| --> ||{type(sprite2)}||")







    def affichage(self):
        clock = pygame.time.Clock()
        self.__screen.blit(self.__background, (0,0))


        #création des groups
        liste_elements = self.create_groups()
        liste_peacefull = liste_elements[0]
        liste_savaged = liste_elements[1]
        liste_car = liste_elements[2]
        human= liste_elements[3]
        all_sprites = pygame.sprite.Group(liste_peacefull, liste_savaged, liste_car, human)
        
        #placement des sprites
        self.place_elements(liste_peacefull)
        self.place_elements(liste_savaged)
        self.place_elements(liste_car)
        self.place_elements(human)
        

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                    
            self.__screen.blit(self.__background, (0,0))

            
            # affichage des sprites
            for sprite in all_sprites:
                self.update(sprite)
                self.__screen.blit(sprite.image, (sprite.rect.x, sprite.rect.y))
                
            self.detect_collisions(all_sprites)
                    
            
            
            pygame.display.flip()
            clock.tick(60)