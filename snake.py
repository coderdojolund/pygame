import pygame

class Snake(pygame.sprite.Sprite):
    """The class is the player-controlled sprite. """

    def __init__(self, x, y):
        """Constructor function"""
        # Call the parent's constructor
        super().__init__()

        self.image = pygame.image.load("pygame.png") # .convert_alpha()
        # Make our top-left corner the passed-in location.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
