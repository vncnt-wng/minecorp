import pygame
import copy

class Laser:

  def __init__(self, ship):
    self.ship = ship
    #makes the laser vector the current heading of the calling ship
    self.direction = copy.copy(self.ship.get_heading())
    self.pos = copy.copy(self.ship.pos)
    self.start_ticks = pygame.time.get_ticks()
    self.time = 3000
    self.speed = 5
    self.length = 20

  def draw(self):
    self.pos += self.speed * self.direction
    pygame.draw.line(self.ship.display,
                     (255, 255, 255),
                     self.pos,
                     self.pos + self.length * self.direction,
                     2)

  #TODO abstract this kind of behaviour into a *particle* class?
  #TODO maybe do this with an event?
  def dying(self):
    return self.start_ticks + self.time < pygame.time.get_ticks()