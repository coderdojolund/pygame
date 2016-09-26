"""
Sample Python/Pygame Programs
Simpson College Computer Science
http://programarcadegames.com/
http://simpson.edu/computer-science/
"""

import pygame
from snake import Snake

WHITE = (255, 255, 255)

# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])

# Set the title of the window
pygame.display.set_caption('Move Sprite With Keyboard')

player = Snake(50, 50)
all_sprites_list = pygame.sprite.Group()
all_sprites_list.add(player)

clock = pygame.time.Clock()
more = True

while more:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            more = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player.rect.x -= player.rect.width
            elif event.key == pygame.K_RIGHT:
                player.rect.x += player.rect.width
            elif event.key == pygame.K_UP:
                player.rect.y -= player.rect.height
            elif event.key == pygame.K_DOWN:
                player.rect.y += player.rect.height

    # -- Draw everything
    # Clear screen
    screen.fill(WHITE)

    # Draw sprites
    all_sprites_list.draw(screen)

    # Flip screen
    pygame.display.flip()

    # Pause
    clock.tick(40)

pygame.quit()
