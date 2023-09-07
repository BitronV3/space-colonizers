import pygame
import sys
import os

from aliens import *
from spaceship import *

pygame.init()


#- Setup scenes -#
def scene_main_menu(events):
    #- Réinitialisation de la fenêtre
    window.fill((255,0,0))

    #- Check de changements de scene
    for event in events:
        if keydown(pygame.K_SPACE, event):
            return 1
    
    return 0

def scene_play(events):
    #- Réinitialisation de la fenêtre
    window.fill((0,0,0))

    #- On update tt les objets présents ds la frame
    #screen.blit(bg, (0, 0)) 
    for alien in aliens:
        alien.update(window)
        if alien.shoot_count >= alien.shoot_cool:
            alien.shoot(bullets)
    
    for spaceship in spaceships:
        spaceship.update(window)

    #- Update des projectiles
    for bullet in bullets:
        bullet.update(window)

    #- Check de changements de scene
    for event in events:
        if keydown(pygame.K_ESCAPE, event):
            return 2
    
    return 1

def scene_pause(events):
    #- Réinitialisation de la fenêtre
    window.fill((0,255,0))

    #- Check de changements de scene
    for event in events:
        if keydown(pygame.K_SPACE, event):
            return 1
        elif keydown(pygame.K_a, event):
            return 3
        elif keydown(pygame.K_b, event):
            return 0
    
    return 2

def scene_controls(events):
    #- Réinitialisation de la fenêtre
    window.fill((0,0,255))

    #- Check de changements de scene
    for event in events:
        if keydown(pygame.K_ESCAPE, event):
            return 2
        
    return 3


#- Setup variables globales -#
clock = pygame.time.Clock()
window = pygame.display.set_mode((0, 0))

bullets = []
spaceships = []
aliens = []
scene = 0

#- Check si une touche est enfoncée
def keydown(keycode, event):
    return (event.type==pygame.KEYDOWN and event.key==keycode)

#- Setup images -#
abullet_texture = pygame.image.load(os.path.join("img", "test.jpg"))
spaceship_textures = [pygame.image.load(os.path.join("img", "test.jpg"))]
shield_textures = [pygame.image.load(os.path.join("img", "test.jpg"))]
    #- Alien textures
abasic_textures = [pygame.image.load(os.path.join("img", "test.jpg"))]*2



aliens.append(ABasic(20,20,abasic_textures))

#- Boucle de jeu principale -#
while True:
    #- Max framerate
    clock.tick(60)
    events = pygame.event.get()

    if scene == 3: scene = scene_controls(events)
    elif scene == 2: scene = scene_pause(events)
    elif scene == 1: scene = scene_play(events)
    elif scene == 0: scene = scene_main_menu(events)
    

    #x, y = pygame.mouse.get_pos()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    #- Update l'affichage de la frame
    pygame.display.update()

#- Safety stop -#
pygame.quit()
sys.exit()
