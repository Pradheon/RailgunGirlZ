# Background Object

import pygame
import random
import sys
import pygwidgets
from pygame.locals import *
import time
from Player import *


class Background():
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight

        self.backgroundImage = pygwidgets.Image(window, (0, 0), 'resources/images/bgLee.jpg')

        startingRect = self.backgroundImage.getRect()
        self.width = startingRect[2]
        self.height = startingRect[3]

        self.backgroundImage.setLoc((0, 0))  # (-450, 0)
        self.imageX = 0
        self.IMAGE_Y = 0
        self.MIN_X = windowWidth - self.width

    def update(self, leftOrRight):
        """
        if playerMovementX < self.width:
            self.backgroundImage.moveX(playerMovementX)
        else:
            pass
        self.imageX = self.imageX + playerMovementX
        if self.imageX < 0:
            self.imageX = 0
        """
        if leftOrRight == 'left':
            self.imageX = self.imageX + 2
            if self.imageX > 0:  # reached left edge of image
                self.imageX = 0  # show from left edge

        elif leftOrRight == 'right':
            self.imageX = self.imageX - 2
            if self.imageX < self.MIN_X:  # if player goes too far
                self.imageX = self.MIN_X  # show from proper X

        self.backgroundImage.setLoc((self.imageX, self.IMAGE_Y))

    def getRect(self):
        backgroundRect = pygame.Rect(0, 0, self.width, self.height)
        return backgroundRect

    def draw(self):
        self.backgroundImage.draw()
