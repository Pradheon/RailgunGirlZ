## Player Character Object
import pygame
import random
import sys
import pygwidgets
from pygame.locals import *
import time


class Player(object):

    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.playerAnimation = pygwidgets.SpriteSheetAnimation(self.window, (0, 0),
                                                               'resources/images/RailgunMisaka.png', 34, 80, 80, 1)

        startingRect = self.playerAnimation.getRect()
        self.width = startingRect[2]
        self.height = startingRect[3]

        self.x = self.windowWidth / 2
        self.y = windowHeight - self.height - 20
        self.maxX = self.windowWidth - self.width
        self.maxY = self.windowHeight - self.height
        self.playerAnimation.setLoc((self.x, self.y))

        self.faceLeft = False
        self.faceRight = False
        self.idle = True

        self.velocity = 0.5

    def handleEvents(self):
        keyPressedTuple = pygame.key.get_pressed()
        self.playerAnimation.setLoc((self.x, self.y))
        if keyPressedTuple[pygame.K_LEFT or pygame.K_a] and (self.x > self.velocity):
            self.x -= self.velocity
            self.faceLeft = True
            self.idle = False
        elif keyPressedTuple[pygame.K_RIGHT or pygame.K_d] and (self.x < self.maxX - self.velocity):
            self.x += self.velocity
            self.faceRight = True
            self.idle = False
        elif keyPressedTuple[pygame.K_UP or pygame.K_w] and (self.y > (self.windowHeight / 1.7) - self.velocity):
            # TODO: Move player character in an upward direction
            self.y -= self.velocity
        elif keyPressedTuple[pygame.K_DOWN or pygame.K_s] and (self.y < self.maxY - self.velocity):
            # TODO: Move player character in a downward direction
            self.y += self.velocity
        else:
            # TODO: Player is idle
            self.idle = True
            pass

    def getRect(self):
        playerRect = pygame.Rect(self.x, self.y, self.width, self.height)
        return playerRect

    # draw the player on the game screen
    def drawPlayer(self):
        self.playerAnimation.draw()

    # player takes damage from enemy AI
    # def hit_player(self):
