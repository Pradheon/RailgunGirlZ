# !/usr/bin/python3.9
#
# Railgun GirlZ
# Inspired by Gun GirlZ. Based on "A Certian Scientific Railgun" series by Kazuma Kamachi and Motoi Fuyukawa
# Railgun GirlZ developed by Joshan Rai
#
# Synopsis: This is a game taking elements from my other game "Neko Quest", miHoYo's Gun GirlZ, and the Railgun series and combining it all into one game.
#           Play as Mikoto Misaka as you fight your way through Academy City's toughest foes to save the city, once again, from the enemies that aim to
#           destory Academy City.
# How to Play: Use arrow keys to move/navigate, spacebar to attack.
# Future Content: More characters, character selection.
#
# Released under the Creative Commons License 3.0
##############################################################################################################################################################

### 1 - Load Modules ###
import pygame
import pygwidgets
import random
import sys
import os
import math
import getopt
import json
from pygame.locals import *
from pygame.sprite import *
from socket import *

from pygame.transform import scale

from Player import *

### 2 - Version, Screen, Clock, Sound Effects, and Music ###
## 2.1 - Version
VERSION = "0.1"

## 2- Constants
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
WINDOW_WIDTH = 1920
WINDOW_HEIGHT = 660
FRAMES_PER_SECOND = 60

## 2.2 - Screen
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Railgun GirlZ")

## 2.3 - Clock
game_clock = pygame.time.Clock()

## 2.4 - Sound Effects and Music
pygame.mixer.init()
# 2.4.1 - Music
# main_menu_music = pygame.mixer.music.load()
# menu_music = pygame.mixer.music.load()
# background_music = pygame.mixer.music.load()
# pygame.mixer.music.play(-1)
# 2.4.2 - Sound Effects
# projectile_shoot_sound = pygame.mixer.Sound()
# projectile_hit_sound = pygame.mixer.Sound()
# player_damage_sound = pygame.mixer.Sound()
# enemyAI_damage_sound = pygame.mixer.Sound()


### 3 - Character Sprites / Images ###
## 3.1 - Background
oBackground = pygame.image.load('resources/images/bgLee.jpg').convert()
# oBackground = pygwidgets.Image(window, WINDOW_WIDTH, WINDOW_HEIGHT, 'images/bgLee.png')

## 3.2 - Mikoto Misaka Character Sprites
oPlayer = Player(window, WINDOW_WIDTH, WINDOW_HEIGHT)  # 100, 500

## 3.3 - Enemey AI Character Sprites
# enemyAI_look_left = [pygame.image.load()]
# enemyAI_look_right = [pygame.image.load()]
# enemyAI_run_left = [pygame.image.load()]
# enemyAI_run_right = [pygame.image.load()]


### 4 - Resource Handling Functions ###
## Redraw Screen
# def redraw_screen():
# window.fill()

## Fade Effect
# def fade_effect():


### Game Object Classes ###
## Main Menu Object


### Main Program ###
while True:
    # Handle Events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    oPlayer.handleEvents()

    # Draw Screen Elements
    window.blit(oBackground, (0, 0))
    oPlayer.drawPlayer()

    # Update Display
    pygame.display.update()
