## Player Character Object
import pygame
import random
import sys
import pygwidgets
from pygame.locals import *
import time
from AnimationCollection import *
from Constants import *

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
        runUpTuple = (('resources/images/misaka_sprites/RunR-0.png', .1),
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
                        ('resources/images/misaka_sprites/RunL-5.png', .1))
        runDownTuple = (('resources/images/misaka_sprites/RunL-0.png', .1),
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
                                                     LEFT: runLeftTuple,
                                                     UP: runUpTuple,
                                                     DOWN: runDownTuple},
                                                    IDLE, loop=True, autoStart=True)
        '''UP: runUpTuple,DOWN: runDownTuple'''

        self.direction = IDLE
        self.isMoving = False
        self.keysDownList = []

        self.health = 100
        self.visible = True
        self.facing = RIGHT
        '''self.faceLeft = False
        self.faceRight = False
        self.idle = True'''

        self.velocity = 5

    def handleEvent(self, event):
        if event.type == pygame.KEYDOWN:
            if (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
                self.keysDownList.append(LEFT)
                self.facing = LEFT
            elif (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
                self.keysDownList.append(RIGHT)
                self.facing = RIGHT
            elif (event.key == pygame.K_UP) or (event.key == pygame.K_w):
                self.keysDownList.append(UP)
            elif (event.key == pygame.K_DOWN) or (event.key == pygame.K_s):
                self.keysDownList.append(DOWN)

        if event.type == pygame.KEYUP:
            if (event.key == pygame.K_LEFT) or (event.key == pygame.K_a):
                self.keysDownList.remove(LEFT)
            elif (event.key == pygame.K_RIGHT) or (event.key == pygame.K_d):
                self.keysDownList.remove(RIGHT)
            elif (event.key == pygame.K_UP) or (event.key == pygame.K_w):
                self.keysDownList.remove(UP)
            elif (event.key == pygame.K_DOWN) or (event.key == pygame.K_s):
                self.keysDownList.remove(DOWN)

    def update(self):
        if (LEFT in self.keysDownList) and (self.x > self.velocity):
            self.x -= 2
            self.direction = LEFT
            self.oPlayerAnimation.replace(LEFT)
            self.oPlayerAnimation.start()
            self.isMoving = True
            # self.faceLeft = True
            # self.idle = False
            # print(self.x)
        elif (RIGHT in self.keysDownList) and (self.x < self.maxX - self.velocity):
            self.x += 2
            self.direction = RIGHT
            self.oPlayerAnimation.replace(RIGHT)
            self.oPlayerAnimation.start()
            self.isMoving = True
            # self.faceRight = True
            # self.idle = False
            # print(self.x)
        if (UP in self.keysDownList) and (self.y > (self.windowHeight / 1.7) - self.velocity):
            self.y -= self.velocity
            self.direction = UP
            self.oPlayerAnimation.replace(UP)
            self.oPlayerAnimation.start()
            self.isMoving = True
        if (DOWN in self.keysDownList) and (self.y < self.maxY - self.velocity):
            self.y += self.velocity
            self.direction = DOWN
            self.oPlayerAnimation.replace(DOWN)
            self.oPlayerAnimation.start()
            self.isMoving = True

        # print('keysDownList:', self.keysDownList)
        if len(self.keysDownList) == 0:
            self.direction = IDLE
            self.oPlayerAnimation.replace(IDLE)
            self.oPlayerAnimation.start()
            self.isMoving = False
        else:
            self.direction = self.keysDownList[0]
            self.oPlayerAnimation.replace(self.direction)
            self.oPlayerAnimation.start()
            self.isMoving = True

        self.oPlayerAnimation.update()
        self.oPlayerAnimation.setLoc((self.x, self.y))

    def getRect(self):
        playerRect = pygame.Rect(self.x, self.y, self.width, self.height)
        return playerRect

    def getCenterRect(self):
        theRect = self.getRect()
        centerRect = theRect.center
        return centerRect

    def getDirection(self):
        return self.direction

    def getFacing(self):
        return self.facing

    def getHitboxRect(self):
        hitboxRect = pygame.Rect(self.x + 22, self.y + 10, self.width - 45, self.height - 10)
        return hitboxRect

    def drawHealthbar(self):
        self.healthText.draw()
        pygame.draw.rect(self.window, RED, (40, 30, 350, 20), 0)
        pygame.draw.rect(self.window, GREEN, (40, 30, 350 - (1 * (100 - self.health)), 20), 0)
        pygame.draw.rect(self.window, BLACK, (40, 30, 350, 20), 1)

    # draw the player on the game screen
    def draw(self):
        if self.visible:
            self.drawHealthbar()
            self.oPlayerAnimation.draw()

    # player takes damage from enemy AI
    def hit(self):
        if self.health > 0:
            self.health -= .01
            #print('hit')
        else:
            self.visible = False
