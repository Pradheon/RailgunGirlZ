import pygame
import random
import sys
import pygwidgets
from pygame.locals import *
import time


class Projectile():
    def __init__(self, window, windowWidth, windowHeight, x, y, radius, color, facing):
        self.window = window
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.velocity = 8 * facing
        self.projectileList = []

    def update(self):
        for oProjectile in self.projectileList:
            if self.x > self.windowWidth:
                self.x += self.velocity
            else:
                self.projectileList.pop(self.projectileList.index(oProjectile))

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)
