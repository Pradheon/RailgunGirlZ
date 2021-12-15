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

        idleTuple = (('resources/images/kuroko_sprites/StandR-0.png', .1),
                     ('resources/images/kuroko_sprites/StandR-1.png', .1),
                     ('resources/images/kuroko_sprites/StandR-2.png', .1),
                     ('resources/images/kuroko_sprites/StandR-3.png', .1))
        runRightTuple = (('resources/images/kuroko_sprites/RunR-0.png', .1),
                         ('resources/images/kuroko_sprites/RunR-1.png', .1),
                         ('resources/images/kuroko_sprites/RunR-2.png', .1),
                         ('resources/images/kuroko_sprites/RunR-3.png', .1),
                         ('resources/images/kuroko_sprites/RunR-4.png', .1),
                         ('resources/images/kuroko_sprites/RunR-5.png', .1))
        runUpTuple = (('resources/images/kuroko_sprites/RunR-0.png', .1),
                      ('resources/images/kuroko_sprites/RunR-1.png', .1),
                      ('resources/images/kuroko_sprites/RunR-2.png', .1),
                      ('resources/images/kuroko_sprites/RunR-3.png', .1),
                      ('resources/images/kuroko_sprites/RunR-4.png', .1),
                      ('resources/images/kuroko_sprites/RunR-5.png', .1))
        runLeftTuple = (('resources/images/kuroko_sprites/RunL-0.png', .1),
                        ('resources/images/kuroko_sprites/RunL-1.png', .1),
                        ('resources/images/kuroko_sprites/RunL-2.png', .1),
                        ('resources/images/kuroko_sprites/RunL-3.png', .1),
                        ('resources/images/kuroko_sprites/RunL-4.png', .1),
                        ('resources/images/kuroko_sprites/RunL-5.png', .1))
        runDownTuple = (('resources/images/kuroko_sprites/RunL-0.png', .1),
                        ('resources/images/kuroko_sprites/RunL-1.png', .1),
                        ('resources/images/kuroko_sprites/RunL-2.png', .1),
                        ('resources/images/kuroko_sprites/RunL-3.png', .1),
                        ('resources/images/kuroko_sprites/RunL-4.png', .1),
                        ('resources/images/kuroko_sprites/RunL-5.png', .1))

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

        self.oEnemyAnimation = AnimationCollection(window, (self.x, self.y),
                                                   {IDLE: idleTuple,
                                                    RIGHT: runRightTuple,
                                                    LEFT: runLeftTuple,
                                                    UP: runUpTuple,
                                                    DOWN: runDownTuple},
                                                   IDLE, loop=True, autoStart=True)

        self.direction = IDLE
        self.isMoving = False

        self.health = 100

        '''self.faceLeft = False
        self.faceRight = False
        self.idle = True'''
        self.visible = True

        self.velocity = 0.3

    def update(self, playerRect):
        if playerRect.x >= self.x:
            self.x += self.velocity
            newDirection = RIGHT
        elif playerRect.x < self.x:
            self.x -= self.velocity
            newDirection = LEFT
        if playerRect.y > self.y:
            self.y += self.velocity
        elif playerRect.y < self.y:
            self.y -= self.velocity

        self.isMoving = True
        self.oEnemyAnimation.setLoc((self.x, self.y))
        if newDirection != self.direction:
            self.direction = newDirection
            self.oEnemyAnimation.replace(self.direction)
            self.oEnemyAnimation.start()

        self.oEnemyAnimation.update()
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
            self.oEnemyAnimation.draw()

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
