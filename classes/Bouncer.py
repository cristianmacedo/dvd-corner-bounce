import random
import pygame

from constants import LIGHT_RED 
from constants import RED
from constants import BLUE

class Bouncer:

  def __init__(self, surface, x_max, y_max, animate=False):

    self.corners = [
      (0, 0),
      (x_max, 0),
      (0, y_max),
      (x_max, y_max)
    ]

    self.animate = animate

    self.starting_x = random.randint(1, x_max)
    self.starting_y = random.randint(1, y_max)

    self.collisions = 0

    self.x = self.starting_x
    self.y = self.starting_y

    self.x_speed = 1
    self.y_speed = 1

    self.x_max = x_max
    self.y_max = y_max

    self.next_position = (0, 0)

    self.surface = surface

    self.color = RED
    self.trail_color = LIGHT_RED
    self.path_color = BLUE

    self.trail = [(self.starting_x, self.starting_y), (self.x, self.y)]

    self.trail_size = 1
    self.path_size = 1

    self.rectangle_size = 15
    self.ball_size = 10

    self.update_remaining_collisions()


  def update(self):

    self.next_position = self.get_next_position()

    new_x = self.x + self.x_speed
    new_y = self.y + self.y_speed

    if(not self.animate):
      new_x, new_y = self.next_position

    self.x = new_x
    self.y = new_y

    self.trail[-1] = (self.x, self.y)    

    if(new_x >= self.x_max or new_x <= 0):
      self.x_speed = self.x_speed * -1
      self.trail.append((self.x, self.y))
      self.collisions = self.collisions + 1
    
    if(new_y >= self.y_max or new_y <= 0):
      self.y_speed = self.y_speed * -1
      self.trail.append((self.x, self.y))
      self.collisions = self.collisions + 1

  def reset(self):

    self.collisions = 0
    self.trail = [(self.x, self.y), (self.x, self.y)]

  def update_remaining_collisions(self):
    while not self.check_corner():
      self.update()
    self.remaining_collisions = self.collisions
    self.reset()

  def draw(self):

    next_position = self.get_next_position()

    pygame.draw.lines(self.surface, self.trail_color, False, self.trail, self.trail_size)
    pygame.draw.line(self.surface, self.path_color, self.trail[-1], next_position, self.path_size)
    
    pygame.draw.rect(self.surface, self.color, (self.x, self.y, self.rectangle_size, self.rectangle_size))
    pygame.draw.circle(self.surface, self.color, next_position, self.ball_size)

  def check_loop(self):

    if(self.x == self.starting_x and self.y == self.starting_y):
      return True
    
    return False

  def check_corner(self):

    for corner in self.corners:
      if(self.x == corner[0] and self.y == corner[1]):
        return True
    
    return False
  
  def get_next_position(self):

    r_dist = self.x_max - self.x
    l_dist = self.x
    t_dist = self.y
    b_dist = self.y_max - self.y  

    comparisons = []

    if (self.x_speed > 0):
      comparisons.append(r_dist)
    elif (self.x_speed < 0):
      comparisons.append(l_dist)
      
    if (self.y_speed > 0):
      comparisons.append(b_dist)
    elif (self.y_speed < 0):
      comparisons.append(t_dist)

    closest = min(comparisons)

    return (self.x + (closest * self.x_speed), self.y + (closest * self.y_speed))