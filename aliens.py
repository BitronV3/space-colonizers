import pygame
import sys
import os

class ABullet():
    def __init__(self, x, y, texture, speed):
        self.x = x
        self.y = y
        self.height = 10
        self.width = 5
        self.texture = pygame.transform.scale(texture, (self.width, self.height))
        self.speed = speed
        self.hitbox= (self.x, self.y, self.width, self.height)
    
    def draw(self,window):
        window.blit(self.texture, (self.x, self.y))
        #- [DEBUG] Affiche la hitbox du projectile
        pygame.draw.rect(window, (255,0,0), self.hitbox,2)

    def update(self, window):
        #- Déplace le projectile
        self.y += self.speed
        self.hitbox= (self.x, self.y, self.width, self.height)
        
        #- Ré-affiche le projectile à sa nouvelle position
        self.draw(window)

class Alien():
    def __init__(self,x , y, textures):
        self.x = x
        self.y = y
        self.height = 30
        self.width = 30
        self.direction = 1
        self.speed = 5
        self.hitbox= (self.x, self.y, self.width, self.height)
        self.textures = textures
        self.texture = pygame.transform.scale(self.textures[0], (self.width, self.height))
        self.shooting = False
        self.shoot_count = 0

    def draw(self,window):
        window.blit(self.texture, (self.x, self.y))
        #- [DEBUG] Affiche la hitbox de l'alien
        pygame.draw.rect(window, (255,0,0), self.hitbox,2)
    
    def update(self,window):
        #- Déplacements de l'alien
        if self.x < window.get_width()*0.9:
            if self.direction == 1:
                self.x += self.speed
        else:
            self.direction = 0
        if self.x > window.get_width()*0.1:
            if self.direction == 0:
                self.x -= self.speed
        else:
            self.direction = 1
        self.hitbox = (self.x, self.y, self.width, self.height)

        #- Change de texture si l'alien tire
        if self.shooting:
            self.texture = pygame.transform.scale(self.textures[1], (self.width, self.height))
            self.shooting = False
        else:
            self.texture = pygame.transform.scale(self.textures[0], (self.width, self.height))
        
        self.shoot_count += 1

        #- Ré-affiche l'alien à sa nouvelle position
        self.draw(window)
            

class ABasic(Alien):
    def __init__(self, x, y, textures):
        super().__init__(x, y, textures)
        self.shoot_cool = 100 #- Prends 100 frames à tirer
    
    def shoot(self,bullets):
        bullets.append(ABullet(self.x+self.width/2,self.y+self.height,pygame.image.load(os.path.join("img", "test.jpg")),10))
        self.shoot_count = 0
        self.shooting = True