import pygame

pygame.init()

import func
import graphic

dim = [500, 500]

SCREEN = pygame.display
plane = SCREEN.set_mode(dim)

graphic.loop(func.f, dim[0], dim[1], plane, SCREEN)