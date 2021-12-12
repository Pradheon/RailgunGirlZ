## Player Character Object
import pygame
import random
import sys
import pygwidgets
from pygame.locals import *
from Player import *
import time


class Enemy(object):

    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.enemyAnimation = pygwidgets.Image(window, (0, 0), 'resources/images/kuroko_sprites/StandR-0.png')

        startingRect = self.enemyAnimation.getRect()
        self.width = startingRect[2]
        self.height = startingRect[3]

        #self.y = windowHeight - self.height - 20
        self.maxX = windowWidth - self.width
        self.maxY = windowHeight - self.height
        self.halfY = (windowHeight / 2) + self.height
        self.x = random.randrange(0, self.maxX)
        self.y = random.randrange(self.halfY, self.maxY)
        self.enemyAnimation.setLoc((self.x, self.y))

        self.health = 100

        self.faceLeft = False
        self.faceRight = False
        self.idle = True
        self.visible = True

        self.velocity = 0.3

    def update(self, playerRect):
        if playerRect.x > self.x:
            self.x += self.velocity
            self.enemyAnimation.setLoc((self.x, self.y))
        elif playerRect.x < self.x:
            self.x -= self.velocity
            self.enemyAnimation.setLoc((self.x, self.y))
        if playerRect.y > self.y:
            self.y += self.velocity
            self.enemyAnimation.setLoc((self.x, self.y))
        elif playerRect.y < self.y:
            self.y -= self.velocity
            self.enemyAnimation.setLoc((self.x, self.y))
        '''
        self.y = playerRect.y + 50
        self.x = playerRect.x + 50
        self.enemyAnimation.setLoc((self.x, self.y))
        '''

    def getRect(self):
        enemyRect = pygame.Rect(self.x, self.y, self.width, self.height)
        return enemyRect

    def getCenterRect(self):
        theRect = self.getRect()
        centerRect = theRect.center
        return centerRect

    # draw the player on the game screen
    def draw(self):
        if self.visible:
            pygame.draw.rect(self.window, RED, (self.x, self.y - 20, 80, 10), 0)
            pygame.draw.rect(self.window, GREEN, (self.x, self.y - 20, 80 - (5 * (100 - self.health)), 10), 0)
            pygame.draw.rect(self.window, BLACK, (self.x, self.y - 20, 80, 10), 1)
            self.enemyAnimation.draw()

    # player takes damage from enemy AI
    def hit(self):
        if self.health > 0:
            self.health -= 1
            print('hit')
        else:
            self.visible = False
