import pygame
import random

class Animal:
    def __init__(self, life_max, name):
        self.id = id(self)
        self.__life_max = life_max
        self.__age = 0
        self.__gender = random.randint(0, 1)
        self.__bar_life = [life_max, life_max]

    def update(self):
        # Ajoutez ici le code pour mettre à jour votre sprite
        pass

    def detecter_collision(self, groupe_sprites):
        for sprite in groupe_sprites:
            if isinstance(sprite, Animal) and pygame.sprite.collide_rect(self, sprite) and self.id != sprite.id:
                return (self.id, sprite.id)
        return None
    
    # Création des animaux
animal1 = Animal(100, "Lion")
animal2 = Animal(80, "Zèbre")

# Ajout des animaux à un groupe de sprites
groupe_sprites = pygame.sprite.Group()
groupe_sprites.add(animal1, animal2)

# Appel de la méthode detecter_collision sur l'animal1
resultat_collision = animal1.detecter_collision(groupe_sprites)

if resultat_collision:
    id_animal1 = resultat_collision[0]
    id_animal2 = resultat_collision[1]
    print("Collision entre les animaux", id_animal1, "et", id_animal2)
else:
    print("Pas de collision")

