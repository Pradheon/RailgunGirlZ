# !/usr/bin/python3.9
#
# Railgun GirlZ
# Inspired by Gun GirlZ. Based on "A Certian Scientific Railgun" series by Kazuma Kamachi and Motoi Fuyukawa
# Railgun GirlZ developed by Joshn Rai
#
# Synopsis: This is a game taking elements from my other game "Neko Quest", miHoYo's Gun GirlZ, and the Railgun series and combining it all into one game.
#           Play as Mikoto Misaka as you fight your way through Academy City's toughest foes to save the city, once again, from the enemies that aim to
#           destory Academy City.
# How to Play: Use arrow keys to move/navigate, spacebar to attack.
# Future Content: More characters, character selection.
#
# Released under the Creative Commons License 3.0
##############################################################################################################################################################

### Load Modules ###
import sys
import os
import random
import math
import getopt
import pygame
import json
import pygame.locals import *
from pygame.sprite import sprite
from socket import *


### Version, Screen, Clock, Sound Effects, and Music ###
## Version
VERSION = "0.1"

## Screen
game_window = pygame.display.set_mode((1920, 1080))
pygame.display.set_caption("Railgun GirlZ")

## Clock
game_clock = pygame.time.Clock()

## Sound Effects and Music
pygame.mixer.init()
# Music
main_menu_music = pygame.mixer.music.load()
menu_music = pygame.mixer.music.load()
background_music = pygame.mixer.music.load()
pygame.mixer.music.play(-1)
# Sound Effects
projectile_shoot_sound = pygame.mixer.Sound()
projectile_hit_sound = pygame.mixer.Sound()
player_damage_sound = pygame.mixer.Sound()
enemyAI_damage_sound = pygame.mixer.Sound()


### Character Sprites and Images ###
## Mikoto Misaka Character Sprites
mikoto_look_left = [pygame.image.load()]
mikoto_look_right = [pygame.image.load()]
mikoto_run_left = [pygame.image.load()]
mikoto_run_right = [pygame.image.load()]
mikoto_jump_up = [pygame.image.load()]

## Enemey AI Character Sprites
enemyAI_look_left = [pygame.image.load()]
enemyAI_look_right = [pygame.image.load()]
enemyAI_run_left = [pygame.image.load()]
enemyAI_run_right = [pygame.image.load()]


### Resource Handling Functions ###
## Redraw Screen
def redraw_screen():
    game_window.fill()

## Fade Effect
def fade_effect():



### Game Object Classes ###
## Main Menu Object


## Player Character Object
class player(object):
    def __init__():


    # draw the player on the gaem screen
    def draw_player():

    # player takes damage from enemy AI
    def hit_player():


## Enemy AI Character Object
class enemyAI(object):
    def __init__():

    # draw the enemy onto the game screen
    def draw_enemyAI():

    # Enemy AI takes damage from player projectiles
    def hit_enemyAI():


## Projectile Object
class projectile(object):
    def __init__():

    # draw projectile on screen when prompted by player attack or enemy AI attack
    def draw_projectile():



### Main Program ###
