## Player Character Object
import pygame
import random
import sys
import pygwidgets
from pygame.locals import *
from Player import *
import time
from Constants import *


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

    def getHitboxRect(self):
        hitboxRect = pygame.Rect(self.x + 22, self.y + 5, self.width - 45, self.height - 5)
        return hitboxRect

    # draw the player on the game screen
    def draw(self):
        if self.visible:
            pygame.draw.rect(self.window, RED, (self.x - 15, self.y - 20, 100, 10), 0)
            pygame.draw.rect(self.window, GREEN, (self.x - 15, self.y - 20, 100 - (1 * (100 - self.health)), 10), 0)
            pygame.draw.rect(self.window, BLACK, (self.x - 15, self.y - 20, 100, 10), 1)
            self.enemyAnimation.draw()

    # enemy takes shoot damage from player
    def shootHit(self):
        if self.health > 0:
            self.health -= 5
            # print('hit')
        else:
            self.visible = False

    def meleeHit(self):
        if self.health > 0:
            self.health -= 10
            # print('hit')
        else:
            self.visible = False

    def getHealth(self):
        return self.health
