import pygame
#import ship

black = (0,0,0)
white = (255,255,255)


pygame.init()

width = 1200
height = 1200

gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('MineCorp')


class Ship:

  def __init__(self, x, y, gameDisplay):
    self.x = x;
    self.y = y;
    self.velx = 0;
    self.vely = 0;
    self.display = gameDisplay
    self.accel_rate = 0.5

  def accel(self, dx, dy):
    self.velx += self.accel_rate * dx
    self.vely += self.accel_rate * dy

  def move(self):
    self.x += self.velx
    self.y += self.vely
    self.decellerate()

  def decellerate(self):
    self.velx = self.velx * 0.99
    self.vely = self.vely * 0.99

  def draw(self):
    pygame.draw.circle(gameDisplay, white, (int(self.x), int(self.y)), 20)


clock = pygame.time.Clock()

crashed = False

ship = Ship(width/2, height/2, gameDisplay)


def key_down_action(key):
  move_ship(key)

def move_ship(key):
  if key == pygame.K_LEFT:
    ship.accel(-1, 0)
  elif key == pygame.K_RIGHT:
    ship.accel(1, 0)
  elif key == pygame.K_UP:
    ship.accel(0, -1)
  elif key == pygame.K_DOWN:
    ship.accel(0, 1)


while not crashed: 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      crashed = True

    if (event.type == pygame.KEYDOWN):
      key_down_action(event.key)

  ship.move()
  gameDisplay.fill(black)
  ship.draw()

  pygame.display.update()
  clock.tick(60)

pygame.quit()
quit()