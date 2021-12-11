import pygame
from pygame.locals import *
import pygwidgets


class AnimationCollection():
    """A collection of animations

    Parameters:
            window  The window to draw into
            loc  The starting location for the animation
            animationsTuplesDict - a dictionary of animation tuples
                      the keys in the dictionary represent the different animations
                      and are used to switch among the possible animations.
            startAnimationKey - the key of the starting animation tuple

        Optional parameters:
            autoStart - should the animation start automatically (defaults to False)
            loop - should the current animation loop (defaults to False)
            showFirstImageAtEnd - when the animation ends, show the first frame (defaults to True)
            nickname - any internal nickname to use (defaults to None)
            callBack - a function or object.method to call back when an animation completes (defaults to None)
            nIterations - number of times the animation should loop (defaults to 1)
    """

    def __init__(self, window, loc, animationsTuplesDict, startAnimationKey,
                 autoStart=False, loop=False, showFirstImageAtEnd=True,
                 nickname=None, callBack=None, nIterations=1):
        self.window = window
        self.loc = loc
        self.animationsDict = {}

        for key, animationTuple in animationsTuplesDict.items():
            oAnimation = pygwidgets.Animation(self.window, self.loc, animationTuple, autoStart,
                                              loop, showFirstImageAtEnd, nickname, callBack, nIterations)
            self.animationsDict[key] = oAnimation

        self.replace(startAnimationKey)

    def replace(self, key):
        """Selects a different animation to be shown.

        Parameters:
            | key - a key in the original dictionary that specifies which animation to show

        Raises KeyError if the key to use to replace an animation is not found in the dictionary

        """
        if not (key in self.animationsDict):
            message = 'AnimationCollection: The  key "' + key + '" was not found in the animations dictionary'
            raise KeyError(message)

        self.currentAnimationKey = key
        self.oCurrentAnimation = self.animationsDict[self.currentAnimationKey]

    def start(self):
        self.oCurrentAnimation.start()

    def stop(self):
        self.oCurrentAnimation.stop()

    def update(self):
        self.oCurrentAnimation.update()

    def getRect(self):
        return self.oCurrentAnimation.getRect()

    def draw(self, scrollOffsetX=0, scrollOffsetY=0):
        self.oCurrentAnimation.draw(scrollOffsetX, scrollOffsetY)