from classes.Bouncer import Bouncer 

from constants import WIDTH
from constants import HEIGHT

running = True
bouncer = Bouncer(None, WIDTH-1, HEIGHT-1, animate=False)

while not bouncer.check_corner():
    bouncer.update()

print(                       \
  'Corner bounce!' + ' | ' + \
  'Collisions with wall: ' + str(bouncer.bounces)
)
