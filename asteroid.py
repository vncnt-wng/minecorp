import pygame

#abstract out into destroyable class or similar?
class Asteroid:

  def __init__(self, pos, gameDisplay, size):
    self.pos = pos
    self.size = size
    self.display = gameDisplay

  def destroy(self):
    #TODO spawn children if destroyed
    return

  def draw(self):
    pygame.draw.circle(self.display, (255, 255, 255), self.pos, self.size)
