## Player Character Object
import pygame
import random
import sys
import pygwidgets
from pygame.locals import *
import time
from AnimationCollection import *

IDLE = 'idle'
RIGHT = 'right'
LEFT = 'left'
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)


class Player(object):

    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        idleTuple = (('resources/images/misaka_sprites/StandR-0.png', .1),
                     ('resources/images/misaka_sprites/StandR-1.png', .1),
                     ('resources/images/misaka_sprites/StandR-2.png', .1),
                     ('resources/images/misaka_sprites/StandR-0.png', .1))
        runRightTuple = (('resources/images/misaka_sprites/RunR-0.png', .1),
                         ('resources/images/misaka_sprites/RunR-1.png', .1),
                         ('resources/images/misaka_sprites/RunR-2.png', .1),
                         ('resources/images/misaka_sprites/RunR-3.png', .1),
                         ('resources/images/misaka_sprites/RunR-4.png', .1),
                         ('resources/images/misaka_sprites/RunR-5.png', .1))
        runLeftTuple = (('resources/images/misaka_sprites/RunL-0.png', .1),
                        ('resources/images/misaka_sprites/RunL-1.png', .1),
                        ('resources/images/misaka_sprites/RunL-2.png', .1),
                        ('resources/images/misaka_sprites/RunL-3.png', .1),
                        ('resources/images/misaka_sprites/RunL-4.png', .1),
                        ('resources/images/misaka_sprites/RunR-5.png', .1))
        self.playerAnimation = pygwidgets.Image(window, (0, 0), 'resources/images/misaka_sprites/StandR-0.png')

        startingRect = self.playerAnimation.getRect()
        self.width = startingRect[2]
        self.height = startingRect[3]

        self.x = self.windowWidth / 2
        self.y = windowHeight - self.height - 20
        self.maxX = self.windowWidth - self.width
        self.maxY = self.windowHeight - self.height
        self.playerAnimation.setLoc((self.x, self.y))

        self.healthText = pygwidgets.DisplayText(window, (10, 32), textColor=RED, fontSize=30)
        self.healthText.setValue('HP')
        self.oPlayerAnimation = AnimationCollection(window, (self.x, self.y),
                                                    {IDLE: idleTuple,
                                                     RIGHT: runRightTuple,
                                                     LEFT: runLeftTuple},
                                                    RIGHT, loop=True, autoStart=False)

        self.direction = RIGHT
        self.isMoving = False

        self.health = 100
        self.visible = True
        '''self.faceLeft = False
        self.faceRight = False
        self.idle = True'''

        self.velocity = 5

    def handleMovement(self, keyPressedTuple):
        xMovement = 0
        self.playerAnimation.setLoc((self.x, self.y))
        if (keyPressedTuple[pygame.K_LEFT] or keyPressedTuple[pygame.K_a]) and (self.x > self.velocity):
            self.x -= 2
            xMovement += self.velocity
            '''
            self.keysDownList.append(LEFT)
            self.direction = LEFT
            self.oPlayerAnimation.replace(LEFT)
            self.oPlayerAnimation.start()
            self.isMoving = True
            #self.faceLeft = True
            #self.idle = False'''
        elif (keyPressedTuple[pygame.K_RIGHT] or keyPressedTuple[pygame.K_d]) and (self.x < self.maxX - self.velocity):
            self.x += 2
            xMovement -= self.velocity
            '''
            self.keysDownList.append(RIGHT)
            self.direction = RIGHT
            self.oPlayerAnimation.replace(RIGHT)
            self.oPlayerAnimation.start()
            self.isMoving = True
            #self.faceRight = True
            #self.idle = False'''
        if (keyPressedTuple[pygame.K_UP] or keyPressedTuple[pygame.K_w]) \
                and (self.y > (self.windowHeight / 1.7) - self.velocity):
            self.y -= self.velocity
            '''
            self.keysDownList.append(RIGHT)
            self.direction = RIGHT
            self.oPlayerAnimation.replace(RIGHT)
            self.oPlayerAnimation.start()
            self.isMoving = True'''
        elif (keyPressedTuple[pygame.K_DOWN] or keyPressedTuple[pygame.K_s]) and (self.y < self.maxY - self.velocity):
            self.y += self.velocity
            '''
            self.keysDownList.append(RIGHT)
            self.direction = RIGHT
            self.oPlayerAnimation.replace(RIGHT)
            self.oPlayerAnimation.start()
            self.isMoving = True'''
        else:
            pass
        return xMovement

    def getRect(self):
        playerRect = pygame.Rect(self.x, self.y, self.width, self.height)
        return playerRect

    # draw the player on the game screen
    def draw(self):
        if self.visible:
            self.healthText.draw()
            pygame.draw.rect(self.window, RED, (40, 30, 350, 20), 0)
            pygame.draw.rect(self.window, GREEN, (40, 30, 350 - (5 * (100 - self.health)), 20), 0)
            pygame.draw.rect(self.window, BLACK, (40, 30, 350, 20), 1)
            self.playerAnimation.draw()

    # player takes damage from enemy AI
    def hit(self):
        if self.health > 0:
            self.health -= 1
            print('hit')
        else:
            self.visible = False
