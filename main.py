import pygame

pygame.init()

import func
import graphic

dim = [1280, 720]

SCREEN = pygame.display
plane = SCREEN.set_mode(dim)

graphic.loop([func.f, func.f0, func.f1, func.f2, func.f3, func.f4, func.f5], dim[0], dim[1], plane, SCREEN)