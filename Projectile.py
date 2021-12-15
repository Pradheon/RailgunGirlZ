import pygame
import random
import sys
import pygwidgets
from pygame.locals import *
import time
from Constants import *


class Projectile():
    def __init__(self, window, windowWidth, windowHeight, x, y, facing):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.x = x
        self.y = y
        self.radius = 5
        self.color = BLACK
        if facing == RIGHT:
            self.velocity = 8
        else:
            self.velocity = -8

    def update(self):
        self.x += self.velocity
        return self.x

    def draw(self):
        pygame.draw.circle(self.window, self.color, (self.x, self.y), self.radius)


class ProjectileMgr():
    def __init__(self, window, windowWidth, windowHeight):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.projectileList = []

    def update(self):
        for oProjectile in reversed(self.projectileList):
            projectileX = oProjectile.update()
            if projectileX < 0 or projectileX > self.windowWidth:
                self.projectileList.remove(oProjectile)

    def removeProjectile(self):
        for oProjectile in reversed(self.projectileList):
            self.projectileList.remove(oProjectile)

    def newProjectile(self, loc, direction):
        oProjectile = Projectile(self.window, self.windowWidth, self.windowHeight, loc[0], loc[1], direction)
        self.projectileList.append(oProjectile)

    def draw(self):
        for oProjectile in self.projectileList:
            oProjectile.draw()
