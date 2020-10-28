import pygame
from ship import Ship
from laser import Laser
from asteroid import Asteroid

black = (0,0,0)
white = (255,255,255)


pygame.init()

width = 1200
height = 1200

gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption('MineCorp')

clock = pygame.time.Clock()

crashed = False

ship = Ship(pygame.math.Vector2(width/2, height/2), gameDisplay)
lasers = []
asteroids = []

asteroids.append(Asteroid(pygame.math.Vector2(width/5, height/3), gameDisplay, 40))
asteroids.append(Asteroid(pygame.math.Vector2(width * 3/5, height * 3/4), gameDisplay, 30))

def key_down_action(key):
  if key == pygame.K_s:
    laser = Laser(ship)
    lasers.append(laser)
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


def draw_all():
  ship.draw()

  for laser in lasers:
    laser.draw()

  for asteroid in asteroids:
    asteroid.draw()

#TODO make this not n^2?
def check_collisions():
  for asteroid in asteroids:
    for laser in lasers:
      if asteroid.hitbox.collidepoint(laser.pos):
        if (asteroid.hit(laser.direction)):
          asteroids.remove(asteroid)
        lasers.remove(laser)
        break

def kill_particles():
  for laser in lasers:
    if laser.dying():
      lasers.remove(laser)

while not crashed: 
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      crashed = True

    if (event.type == pygame.KEYDOWN):
      key_down_action(event.key)

  ship.move()
  gameDisplay.fill(black)
  
  check_collisions()

  draw_all()
  
  kill_particles()

  pygame.display.update()
  clock.tick(60)

pygame.quit()
quit()