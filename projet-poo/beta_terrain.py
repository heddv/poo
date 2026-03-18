
import random
import pygame
import threading
import config
import beta_menu 

pygame.init()

ecran = pygame.display.set_mode((config.WIDTH, config.HEIGHT))

clock = pygame.time.Clock()

class MonSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, hp, dmg):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.vx = random.randint(-5, 5)
        self.vy = random.randint(-5, 5)
        while self.vy == self.vx:
            self.vy = random.randint(-5, 5)
        self.hp=hp
        self.dmg=dmg
        self.alive = True

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.left < 0 or self.rect.right > ecran.get_width():
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > ecran.get_height():
            self.vy = -self.vy

    def update_v(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.left < 0 :
            self.rect.x = ecran.get_width()-self.image.get_width()
        elif self.rect.right > ecran.get_width():
            self.rect.x = 0
        if self.rect.top < 0 :
            self.rect.y = ecran.get_height()-self.image.get_height()
        elif self.rect.bottom > ecran.get_height():
            self.rect.y = 0

    def update_m(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.left < 880 or self.rect.right > ecran.get_width():
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > ecran.get_height():
            self.vy = -self.vy

    def update_o(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.left < 0 or self.rect.right > 350:
            self.vx = -self.vx
        if self.rect.top < 0 or self.rect.bottom > 350:
            self.vy = -self.vy

    def collision(self, other):
        self_vx,self_vy = self.vx,self.vy
        other_vx,other_vy = other.vx,other.vy
        """self.vx,self.vy = 0,0
        other.vx,other.vy = 0,0"""
        #self.rect.clamp_ip(other.rect)
        groupe_self= self.groups()
        groupe_other = other.groups()
        if groupe_self == groupe_other:
            pass
        else:
            self.fight(other)
        self.vx,self.vy = -self_vx,-self_vy
        other.vx,other.vy = -other_vx,-other_vy

    def fight(self,other):
        other.hp -= self.dmg
        if other.hp <= 0:
            other.kill()
            self.alive = False
        self.hp -= other.dmg
        if self.hp <= 0:
            self.kill()
            self.alive = False

def startGame():
    fond = pygame.image.load('image/fond.png')
    fond = pygame.transform.scale(fond ,(config.WIDTH,config.HEIGHT))
    ecran.blit(fond, (0,0))


    sprite1 = MonSprite(100, 100, 20,5)
    sprite2 = MonSprite(200, 100, 20,5)
    sprite3 = MonSprite(200, 300, 20,5)
    spriteM1 = MonSprite(900, 600, 10,0)
    spriteM2 = MonSprite(900, 300, 10,0)
    spriteV1 = MonSprite(820, 0, 100,100)
    spriteV2 = MonSprite(755, 710, 100,100)
    spriteV1.vx=0
    spriteV2.vx=0
    spriteO1 = MonSprite(200, 200, 50,15)

    liste_sprites = pygame.sprite.Group()
    liste_sprites.add(sprite1, sprite2, sprite3)
    liste_spritesV = pygame.sprite.Group()
    liste_spritesV.add(spriteV1, spriteV2)
    liste_spritesM = pygame.sprite.Group()
    liste_spritesM.add(spriteM1, spriteM2)
    liste_spritesO = pygame.sprite.Group()
    liste_spritesO.add(spriteO1)

    ##################################################
    ################### les régions ##################
    ##################################################

    # Définir la taille et le nombre de régions
    TAILLE_REGION = 120
    NB_REGIONS_X = ecran.get_width() // TAILLE_REGION
    NB_REGIONS_Y = ecran.get_height() // TAILLE_REGION

    # Initialiser les régions
    regions = {}
    nb_regions=0
    for x in range(NB_REGIONS_X):
        for y in range(NB_REGIONS_Y):
            regions[(x, y)] = []
            nb_regions+=1
    print(nb_regions)


    # Placer les sprites dans les régions correspondantes
    for sprite in liste_sprites:
        x = sprite.rect.x // TAILLE_REGION
        y = sprite.rect.y // TAILLE_REGION
        regions[(x, y)].append(sprite)
    for sprite in liste_spritesV:
        x = sprite.rect.x // TAILLE_REGION
        y = sprite.rect.y // TAILLE_REGION
        regions[(x, y)].append(sprite)
    for sprite in liste_spritesM:
        x = sprite.rect.x // TAILLE_REGION
        y = sprite.rect.y // TAILLE_REGION
        regions[(x, y)].append(sprite)
    for sprite in liste_spritesO:
        x = sprite.rect.x // TAILLE_REGION
        y = sprite.rect.y // TAILLE_REGION
        regions[(x, y)].append(sprite)

    """set_surface = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
    surface_cadrillage = pygame.Surface((config.WIDTH, config.HEIGHT), pygame.SRCALPHA)
    surface_cadrillage.convert_alpha()

    # Dessiner les lignes horizontales
    for y in range(TAILLE_REGION, config.HEIGHT, TAILLE_REGION):
        pygame.draw.line(surface_cadrillage, (255, 255, 255, 128), (0, y), (config.WIDTH, y), 2)

    # Dessiner les lignes verticales
    for x in range(TAILLE_REGION, config.WIDTH, TAILLE_REGION):
        pygame.draw.line(surface_cadrillage, (255, 255, 255, 128), (x, 0), (x, config.HEIGHT), 2)"""
        
    ##################################################
    ##################################################
    ##################################################

    ##################################################
    ################# boucle principal ###############
    ##################################################

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # Tester les collisions pour les sprites dans les régions adjacentes
        for sprite in liste_sprites:
            sprite.update()
        
            x = sprite.rect.x // TAILLE_REGION
            y = sprite.rect.y // TAILLE_REGION
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (x+dx, y+dy) in regions:
                        for other_sprite in regions[(x+dx, y+dy)]:
                            if sprite != other_sprite and sprite.rect.colliderect(other_sprite.rect):
                                groupe_self = sprite.groups()
                                print("Collision",groupe_self,"->",other_sprite.groups())
                                t = threading.Thread(sprite.collision(other_sprite))
                                t.start()

                                
                                
                                liste_sprites.update()
                                
                                
                        
        for sprite in liste_spritesV:
            sprite.update_v()
            x = sprite.rect.x // TAILLE_REGION
            y = sprite.rect.y // TAILLE_REGION
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (x+dx, y+dy) in regions:
                        for other_sprite in regions[(x+dx, y+dy)]:
                            if sprite!= other_sprite and sprite.rect.colliderect(other_sprite.rect):
                                print("Collision",sprite.groups(),"->",other_sprite.groups())
                                t2 = threading.Thread(sprite.collision(other_sprite))
                                t2.start()
                                liste_spritesV.update()
    
        for sprite in liste_spritesM:
            sprite.update_m()
            x = sprite.rect.x // TAILLE_REGION
            y = sprite.rect.y // TAILLE_REGION
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (x+dx, y+dy) in regions:
                        for other_sprite in regions[(x+dx, y+dy)]:
                            if sprite!= other_sprite and sprite.rect.colliderect(other_sprite.rect):
                                print("Collision",sprite.groups(),"->",other_sprite.groups())
                                t3 = threading.Thread(sprite.collision(other_sprite))
                                t3.start()
                                liste_spritesM.update()
                                

        for sprite in liste_spritesO:
            sprite.update_o()
            x = sprite.rect.x // TAILLE_REGION
            y = sprite.rect.y // TAILLE_REGION
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    if (x+dx, y+dy) in regions:
                        for other_sprite in regions[(x+dx, y+dy)]:
                            if sprite!= other_sprite and sprite.rect.colliderect(other_sprite.rect):
                                print("Collision",sprite.groups(),"->",other_sprite.groups())
                                t4 = threading.Thread(sprite.collision(other_sprite))
                                t4.start()
                                liste_spritesO.update()
                                

        
        
        ecran.fill((255, 255, 255))
        ecran.blit(fond, (0,0))
        #ecran.blit(surface_cadrillage, (0, 0))

        #### affichage des sprites ####
        for sprite in liste_sprites:
            if sprite in liste_sprites:
                pygame.draw.rect(ecran, (255, 0, 0), sprite.rect)
        for sprite in liste_spritesV:
            if sprite in liste_spritesV:
                pygame.draw.rect(ecran, (0, 0, 255), sprite.rect)
        for sprite in liste_spritesM:
            if sprite in liste_spritesM:
                pygame.draw.rect(ecran, (0, 255, 0), sprite.rect)
        for sprite in liste_spritesO:
            if sprite in liste_spritesO:
                pygame.draw.rect(ecran, (164, 82, 33), sprite.rect)
                
        


        pygame.display.flip()
        clock.tick(60)

    ##################################################
    ##################################################
    ##################################################


    #home_page()

if __name__ == "__main__":
    beta_menu.home_page()



































    
"""
import itertools

# Générer toutes les combinaisons possibles de chiffres entre 0 et 9
combinaisons = itertools.product(range(100), repeat=2)

# Afficher toutes les combinaisons possibles
i=0
for combinaison in combinaisons:
    print(combinaison)
    i+=1

print(i)
"""