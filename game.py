import pygame

from constants import WIDTH
from constants import HEIGHT 
from constants import FPS
from constants import BLACK

from classes.Bouncer import Bouncer 
from classes.Text import Text

# Initialize pygame and create window
pygame.init()
pygame.mixer.init()  # For sound
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Bouncer")
clock = pygame.time.Clock()

# Game loop
running = True

bouncer = Bouncer(screen, WIDTH-1, HEIGHT-1, animate=True)
bouncer.update_remaining_collisions()
text =  Text(screen, (WIDTH-1, HEIGHT-1), bgcolor=(0, 0, 0), fontsize=20)
ticks = [0]

while running:

    #1 Process input/events
    clock.tick(FPS) # Will make the loop run at the same speed all the time
    for event in pygame.event.get():  #Gets all the events which have occured till now and keeps tab of them.
        # Listening for the the X button at the top
        if event.type == pygame.QUIT:
            running = False

    #2 Update      
    bouncer.update()
    text.update_text(str(bouncer.remaining_collisions))

    #3 Draw/render
    screen.fill(BLACK)
    bouncer.draw()
    text.draw()

    #4 Check if game has ended
    if(bouncer.check_corner()):
      current_ticks = pygame.time.get_ticks()
      last_ticks = ticks[-1]
      ticks_diff = current_ticks - last_ticks
      ticks.append(current_ticks)
      print( \
        'Corner bounce!' + ' | ' + \
        'Time: ' + str(ticks_diff/1000) + ' seconds' + ' | ' +  \
        'Collisions with wall: ' + str(bouncer.collisions)
      )
      bouncer.update()
      bouncer.update_remaining_collisions()

    560
    #5 Display flip
    pygame.display.flip()

pygame.quit()
