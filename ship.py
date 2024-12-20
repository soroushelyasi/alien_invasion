import pygame

class Ship:

#  ---------------------------------------------------------------
# ****************************************************************   
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/ship.bmp')
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*4, self.image.get_height()*5)) 
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
#  ---------------------------------------------------------------
# ****************************************************************   

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
#  ---------------------------------------------------------------
# ****************************************************************  