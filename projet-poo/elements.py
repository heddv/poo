#### importation ######
import random
import pygame
import time

class Element(pygame.sprite.Sprite):

    __ids_counts=0

    @classmethod
    def get_ids_counts(cls):
        return cls.__ids_counts
    def incr_ids_counts(cls):
        cls.__ids_counts+=1

    
    def __init__(self ,name, image):
        super().__init__()
        self.name=name
        self.image = image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.__id=self.__ids_counts+1
        Element.incr_ids_counts(Element)
        
        
    def get_id(self):
        return self.__id
   


class Resource(Element):
   def __init__(self,name, durability, image):
        super().__init__(name, image)
        self.__durability=durability


class Three(Resource):
    def __init__(self,name="three", durability=6, image = pygame.image.load("image/three.png")):
        super().__init__(name, durability, image)
        self.type="resource"
        self.image=pygame.transform.scale(image, (image.get_width()*2, image.get_height()*2))     
        
class Plant(Resource):
    def __init__(self,name="plant", durability=2, image = pygame.image.load("image/plant.png")):
        super().__init__(name, durability, image)
        self.type="resource"
        self.image=pygame.transform.scale(image, (image.get_width()*2, image.get_height()*2))

class Stone(Resource):
    def __init__(self, name="stone", durability=10, image = pygame.image.load("image/stone.png")):
        super().__init__(name, durability, image)
        self.type="resource"
        self.image=pygame.transform.scale(image, (image.get_width()*2, image.get_height()*2))

class Iron(Resource):
    def __init__(self,name="iron", durability=12, image = pygame.image.load("image/stone.png")):
        super().__init__(name, durability, image)
        self.type="resource"
        self.image=pygame.transform.scale(image, (image.get_width()*2, image.get_height()*2))




class Animal(Element):

    def __init__(self, name, life_max, damage, image, vx = random.randint(-5, 5), vy = random.randint(-3, 3)):
        super().__init__(name ,image)
        self.__life_max=life_max
        self.__age=0
        self.__gender=random.randint(0, 1)
        self.__bar_life=[life_max,life_max]
        self.__damage = damage
        self.vx = vx
        self.vy = vy
        while self.vy == self.vx:
            self.vy = random.randint(-3, 3)


    ############# age/genre #############
    def get_age(self):
        return self.__age
    
    def ageing(self):
        self.__age+=1

    def get_gender(self):
        if self.__gender:
            return "mâle"
        else:   
            return "femelle"

    ############# interaction ###############

    def collide(self):
        pass
    
    def reproduction(self):
        #Faire apparaitre un nouveau sprite de la class Animal, de la meme espèce et les mêmes coordonnées(x, y) que le sprite parent, avec comme âge par défaut 1
        pass

    def fight(self, sprite1):
        return self.losing_life(sprite1.__damage) and sprite1.losing_life(self.__damage)

    ############# point de vie ###############
    def get_life_max(self):
        return self.__life_max
 
    def get_life(self):
        return self.__bar_life[0]
    
    def is_alive(self):
        if self.get_life(): return True
            
        else: return False
            
    def is_dead(self):
        if self.get_life(): return False
            
        else: return True
            
    def recovering_life(self,value):
        # variables temp
        life=self.get_life()
        life_max=self.get_life_max()

        if life<life_max:
            if life_max-life<value:
                self.__bar_life[0]=life_max
            else:
                self.__bar_life[0]=life+value

    def losing_life(self,value):
        # variable temp
        life=self.get_life()

        if life>0:
            if life<value:
                self.__bar_life[0]=0
            else:
                self.__bar_life[0]=life-value    


class Cow(Animal):
    def __init__(self, name="Cow", life_max=10, damage=0, image=pygame.image.load("image/cow.png")):
        super().__init__(name, life_max, damage, image)
        self.type="peacefull"
        self.image=pygame.transform.scale(image, (image.get_width()*0.5, image.get_height()*0.5))

class Pig(Animal):
    def __init__(self, name="Pig", life_max=8, damage=0, image = pygame.image.load("image/pig.png")):
        super().__init__(name, life_max, damage, image)
        self.type="peacefull"
        self.image=pygame.transform.scale(image, (image.get_width()*0.5, image.get_height()*0.5))

class Sheep(Animal):
    def __init__(self, name="Sheep", life_max=8, damage=0, image = pygame.image.load("image/sheep.png")):
        super().__init__(name, life_max, damage, image)
        self.type="peacefull"
        self.image=pygame.transform.scale(image, (image.get_width()*0.9, image.get_height()*0.9))

class Rabbit(Animal):
    def __init__(self, name="Bunny", life_max=1, damage=0, image = pygame.image.load("image/rabbit.png")):
        super().__init__(name, life_max, damage, image)
        self.type="peacefull"
        self.image=pygame.transform.scale(image, (image.get_width()*0.6, image.get_height()*0.6))

class Fish(Animal):
    def __init__(self, name="Fish", life_max=1, damage=0, image = pygame.image.load(f"image/fishBasile.png")):
        super().__init__(name, life_max, damage, image)
        self.type="peacefull"
        self.color=('Basile','Emile')
        self.color = random.choice(self.color)
        self.image = pygame.image.load(f"image/fish{self.color}.png")
        self.image = pygame.transform.scale(image, (image.get_width()*0.4, image.get_height()*0.4))

class Bear(Animal):
    def __init__(self, name="Bear", life_max=30, damage=5, image = pygame.image.load("image/bear.png")):
        super().__init__(name, life_max, damage, image)
        self.type="savaged"
        self.image = pygame.transform.scale(image, (image.get_width()*0.7, image.get_height()*0.7))

class Wolf(Animal):
    def __init__(self, name="Wolf", life_max=15, damage=3, image = pygame.image.load("image/wolf.png")):
        super().__init__(name, life_max, damage, image)
        self.type="savaged"
        self.image = pygame.transform.scale(image, (image.get_width()*0.6, image.get_height()*0.6))

class Snake(Animal):
    def __init__(self, name="Snake", life_max=2, damage=1, image = pygame.image.load("image/snake.png")):
        super().__init__(name, life_max, damage, image)
        self.type="savaged"
        self.image = pygame.transform.scale(image, (image.get_width()*0.5, image.get_height()*0.5))

    def poisoned():
        pass

class Falcon(Animal):
    def __init__(self, name="Falcon", life_max=2, damage=2, image = pygame.image.load("image/falcon.png")):
        super().__init__(name, life_max, damage, image)
        self.type="savaged"
        self.image = pygame.transform.scale(image, (image.get_width()*0.8, image.get_height()*0.8))
        

class Car(Animal):
    def __init__(self, name="Car", life_max=100, damage=50, image = pygame.image.load(f"image/carBlue.png"), vx=0):
        super().__init__(name, life_max, damage, image, vx)
        self.type = "car"
        self.color = ('Blue', 'Red')
        self.color = random.choice(self.color)
        if self.color == 'Red':
            self.vy = random.randint(2,5)
        else :
            self.vy = -5
        self.image = pygame.image.load(f"image/car{self.color}.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.4, self.image.get_height() * 0.4))
        print(self.image.get_rect())




class Human(Animal):
    def __init__(self, name="Gru", life_max=10, damage=2, image = pygame.image.load("image/gru.png")):
        super().__init__(name, life_max, damage, image)
        self.type="human"
        self.image = pygame.transform.scale(image, (image.get_width() * 0.3, image.get_height() * 0.3))
        self.__inventory = []
        self.arms=0
        self.tools=0

        
    def crafting():
        pygame.time.Clock()

