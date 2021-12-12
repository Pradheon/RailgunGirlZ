# BUTTONS

import pygame
import pygwidgets
from pygame.locals import *

class AttackButton():
    STATE_IDLE = 'idle'
    STATE_SHOOT = 'shoot'
    STATE_DISARMED = 'disarmed'

    def __init__(self, window, loc, up, down):
        self.window = window
        self.loc = loc
        self.surfaceUp = pygwidgets.Image(window, self.loc, up)
        self.surfaceDown = pygwidgets.Image(window, self.loc, down)

        self.rect = self.surfaceUp.getRect()
        self.rect[0] = loc[0]
        self.rect[1] = loc[1]

        self.state = AttackButton.STATE_IDLE

    def handleEvent(self, event):
        if event.type not in (MOUSEMOTION, MOUSEBUTTONUP, MOUSEBUTTONDOWN):
            return False

        eventPointInButtonRect = self.rect.collidepoint(event.pos)

        if self.state == AttackButton.STATE_IDLE:
            if (event.type == MOUSEBUTTONDOWN) and eventPointInButtonRect:
                self.state = AttackButton.STATE_SHOOT

        elif self.state == AttackButton.STATE_SHOOT:
            if (event.type == MOUSEBUTTONUP) and eventPointInButtonRect:
                self.state = AttackButton.STATE_IDLE
                return True  # clicked!

            if (event.type == MOUSEMOTION) and (not eventPointInButtonRect):
                self.state = AttackButton.STATE_DISARMED

        elif self.state == AttackButton.STATE_DISARMED:
            if eventPointInButtonRect:
                self.state = AttackButton.STATE_SHOOT
            elif event.type == MOUSEBUTTONUP:
                self.state = AttackButton.STATE_IDLE

        return False

    def draw(self):
        # Draw the button's current appearance to the window.
        if self.state == AttackButton.STATE_SHOOT:
            self.window.blit(self.surfaceDown, self.loc)

        else:  # IDLE or DISARMED
            self.window.blit(self.surfaceUp, self.loc)