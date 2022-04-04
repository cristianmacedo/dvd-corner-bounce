import pygame
import random

from constants import WIDTH
from constants import HEIGHT 
from constants import FPS
from constants import BLACK

from Bouncer import Bouncer 

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()  # For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncer")
clock = pygame.time.Clock()

# Game loop
running = True

bouncer = Bouncer(screen, WIDTH-1, HEIGHT-1)
time_intervals = [0]

while running:

    #1 Process input/events
    clock.tick(FPS) # Will make the loop run at the same speed all the time
    for event in pygame.event.get():  #Gets all the events which have occured till now and keeps tab of them.
        # Listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False

    #2 Update
    bouncer.update()

    #3 Draw/render
    screen.fill(BLACK)
    bouncer.draw()

    #4 Check if game has ended
    if(bouncer.check_corner()):
      time_interval = pygame.time.get_ticks() - time_intervals[-1]
      time_intervals.append(time_interval)
      print('Bounce! Time' + str(time_interval))
    
    #5 Display flip
    pygame.display.flip()       

pygame.quit()
