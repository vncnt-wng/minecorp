import pygame

#abstract out into destroyable class or similar?
class Asteroid:

  def __init__(self, pos, gameDisplay, size):
    self.pos = pos
    self.size = size
    self.display = gameDisplay
    self.hitbox = pygame.Rect(pos - (size, size), (size * 2, size * 2))
    self.destroy_hits = size / 10
    self.accel = 20 / size
    self.vel = pygame.Vector2(0, 0)

  def hit(self, direction):
    self.destroy_hits -= 1
    if (self.destroy_hits == 0):
      self.destroy()
      return True
    self.vel += direction * self.accel
    return False

  def destroy(self):
    #TODO spawn children if destroyed
    return

  def movement(self):
    self.pos += self.vel
    self.vel = self.vel * 0.98
    self.hitbox = pygame.Rect(self.pos - (self.size, self.size), (self.size * 2, self.size * 2))

  def draw(self):
    self.movement()
    pygame.draw.circle(self.display, (255, 255, 255), self.pos, self.size)
