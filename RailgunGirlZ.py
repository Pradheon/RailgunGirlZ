# !/usr/bin/python3.9
#
# Railgun GirlZ
# Inspired by Gun GirlZ. Based on "A Certian Scientific Railgun" series by Kazuma Kamachi and Motoi Fuyukawa
# Railgun GirlZ developed by Joshan Rai
#
# Synopsis: This is a game taking elements from my other game "Neko Quest", miHoYo's Gun GirlZ, and the Railgun series and combining it all into one game.
#           Play as Mikoto Misaka as you fight your way through Academy City's toughest foes to save the city, once again, from the enemies that aim to
#           destroy Academy City.
# How to Play: Use arrow / WASD keys to move/navigate, spacebar to attack.
# Future Content: More characters, character selection.
#
# Released under the Creative Commons License 3.0
##############################################################################################################################################################

### 1 - Load Modules ###

from Background import *
from Constants import *
from Enemy import *
from Projectile import *

### 2 - Version, Screen, Clock, Sound Effects, and Music ###
## 2.1 - Version
VERSION = "0.1"

## 2- Constants

## 2.2 - Screen
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Railgun GirlZ")

## 2.3 - Clock
game_clock = pygame.time.Clock()

## 2.4 - Sound Effects and Music
pygame.mixer.init()
# 2.4.1 - Music
background_music_k = pygame.mixer.Sound('resources/sounds/kontrolle.mp3')
menu_music_s = pygame.mixer.Sound('resources/sounds/shopsation.mp3')
pygame.mixer.set_num_channels(3)
menu_music = pygame.mixer.Channel(0)
background_music = pygame.mixer.Channel(1)
background_music.play(background_music_k, loops=-1, fade_ms=5000)
menu_music.play(menu_music_s, loops=-1, fade_ms=5000)
menu_music.pause()
pygame.mixer.Sound.set_volume(menu_music_s, 0.1)
pygame.mixer.Sound.set_volume(background_music_k, 0.1)
# 2.4.2 - Sound Effects
# projectile_shoot_sound = pygame.mixer.Sound()
# projectile_hit_sound = pygame.mixer.Sound()
# player_damage_sound = pygame.mixer.Sound()
# enemyAI_damage_sound = pygame.mixer.Sound()


### 3 - Character Sprites / Images ###
## 3.1 - Background
oBackground = Background(window, WINDOW_WIDTH, WINDOW_HEIGHT)
#oBackground = pygwidgets.Image(window, (0, 0), 'resources/images/bgLee.jpg') # -660, 0

## 3.2 - Object Instantiation
oPlayer = Player(window, WINDOW_WIDTH, WINDOW_HEIGHT)
oProjectileMgr = ProjectileMgr(window, WINDOW_WIDTH, WINDOW_HEIGHT)
enemyList = []
oShootButton = pygwidgets.TextButton(window, (890, 590), 'Shoot')
oMeleeButton = pygwidgets.TextButton(window, (890, 530), 'Melee')


### 4 - Resource Handling Functions ###
## Redraw Screen
# def redraw_screen():
# window.fill()

## Fade Effect
# def fade_effect():


### Game Object Classes ###
## Main Menu Object

for enemyNum in range(0, N_ENEMIES):
    oEnemy = Enemy(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    enemyList.append(oEnemy)

### Main Program ###
while True:
    # Handle Events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        # Player movement checks
        elif event.type == pygame.KEYDOWN:
            oPlayer.handleMovement(event)
        elif event.type == pygame.KEYUP:
            oPlayer.handleMovement(event)

        # Button checks
        if oMeleeButton.handleEvent(event):
            if oEnemy.visible:
                if enemyPlayerCollide:
                    oEnemy.hit()

        if oShootButton.handleEvent(event):
            center = oPlayer.getCenterRect()
            direction = oPlayer.getDirection()
            oProjectileMgr.newProjectile(center, direction)


    keyPressedTuple = pygame.key.get_pressed()
    #playerMovementX = oPlayer.handleMovement(event)

    if keyPressedTuple[pygame.K_LEFT] or keyPressedTuple[pygame.K_a]:
        oBackground.update('left')
    if keyPressedTuple[pygame.K_RIGHT] or keyPressedTuple[pygame.K_d]:
        oBackground.update('right')

    playerRect = oPlayer.getRect()
    enemyRect = oEnemy.getRect()
    enemyPlayerCollide = enemyRect.colliderect(playerRect)

    for oEnemy in enemyList:
        oEnemy.update(playerRect)
        if oEnemy.visible:
            for oProjectile in reversed(oProjectileMgr.projectileList):
                projectileX = oProjectile.update()
                projectilePos = (projectileX, oProjectile.y)
                enemyProjectileCollide = enemyRect.collidepoint(projectilePos)
                if keyPressedTuple[pygame.K_j] or enemyProjectileCollide:
                    oEnemy.shootHit()
                    oProjectileMgr.removeProjectile()
            if enemyPlayerCollide:
                oPlayer.hit()
            if keyPressedTuple[pygame.K_k] and enemyPlayerCollide:
                oEnemy.meleeHit()

    oProjectileMgr.update()
    oPlayer.update()

    # Draw Screen Elements
    oBackground.draw()
    oPlayer.draw()
    for oEnemy in enemyList:
        oEnemy.draw()
    oShootButton.draw()
    oMeleeButton.draw()
    oProjectileMgr.draw()

    # Update Display
    pygame.display.update()

    # Slow things down a bit
    game_clock.tick(60)
