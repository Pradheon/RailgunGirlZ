## Player Character Object
import pygame
import random
import sys
import pygwidgets
from pygame.locals import *
from Player import *
import time


class Enemy(object):

    def __init__(self, window, windowWidth, windowHeight, player):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.player = player

        self.enemyAnimation = pygwidgets.Image(window, (0, 0), 'resources/images/kuroko_sprites/StandR-0.png')

        startingRect = self.enemyAnimation.getRect()
        self.width = startingRect[2]
        self.height = startingRect[3]

        self.x = (self.windowWidth / 2) + 250
        self.y = windowHeight - self.height - 20
        self.maxX = self.windowWidth - self.width
        self.maxY = self.windowHeight - self.height
        self.enemyAnimation.setLoc((self.x, self.y))

        self.faceLeft = False
        self.faceRight = False
        self.idle = True

        self.velocity = 1

    def update(self):
        if self.player.width > self.width:
            self.width += self.velocity
        if self.player.width < self.width:
            self.width -= self.velocity
        if self.player.height > self.height:
            self.height += self.velocity
        if self.player.height < self.height:
            self.height -= self.velocity

    def getRect(self):
        enemyRect = pygame.Rect(self.x, self.y, self.width, self.height)
        return enemyRect

    # draw the player on the game screen
    def drawEnemy(self):
        self.enemyAnimation.draw()

    # player takes damage from enemy AI
    # def hit_player(self):
