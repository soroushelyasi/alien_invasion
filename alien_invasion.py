import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
  
#  ---------------------------------------------------------------
# ****************************************************************   
 
  def __init__(self):
    pygame.init()
    self.settings = Settings()
    self.screen=pygame.display.set_mode(
       (self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    self.clock = pygame.time.Clock()
    self.bg_color = self.settings.bg_color
    self.ship = Ship(self)
#  ---------------------------------------------------------------
# ****************************************************************   

  def run_game(self):
    """Start the main loop for the game."""
 # Redraw the screen during each pass through the loop.
    while True:
        self._check_events()
        self._update()
        self.clock.tick(60)
#  ---------------------------------------------------------------
# ****************************************************************   

  def _check_events(self):
        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
#  ---------------------------------------------------------------
# ****************************************************************   
  def _update(self):
          # Redraw the screen during each pass through the loop.
        self.screen.fill(self.bg_color)
        self.ship.blitme()
        # Make the most recently drawn screen visible.
        pygame.display.flip()
#  ---------------------------------------------------------------
# ****************************************************************  

# ################################################################
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# ################################################################
if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()