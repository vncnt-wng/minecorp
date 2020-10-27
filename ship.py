import pygame

class Ship:

  #TODO add "last known heading" as normalised vector set to north first, updated every call to accelerate
  #     fixes potential init of laser with 0 vector heading 


  def __init__(self, pos, gameDisplay):
    #vector 2 
    self.pos = pos
    self.vel = pygame.math.Vector2(0, 0.01)
    self.display = gameDisplay
    self.accel_rate = 0.5

  def accel(self, dx, dy):
    self.vel += pygame.math.Vector2(dx, dy) * self.accel_rate

  def move(self):
    self.pos += self.vel
    self.decellerate()

  def decellerate(self):
    self.vel = 0.99 * self.vel

  #returns a normalised direction vector
  def get_heading(self):
    return self.vel.normalize()

  def draw(self):
    pygame.draw.circle(self.display, (255, 255, 255), self.pos, 20)
