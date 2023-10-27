import pygame
from sys import exit

pygame.init()

# Create a window with size 800x400 and set the caption to "Running"
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Running")

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Create a font object with size 20
test_font = pygame.font.Font(None, 20)

# Create a text surface with the text "the game" in black color
test_text = test_font.render("the game", False, "Black")

# Create a green surface with size 100x200
test_surface = pygame.Surface((100, 200))
test_surface.fill("green")

# Load the sky, ground, snail, and player images
sky_surface = pygame.image.load("images/sky.png").convert_alpha()
ground_surface = pygame.image.load("images/ground.jpg").convert_alpha()
snail_surface = pygame.image.load("images/snail.png").convert_alpha()
player_surface = pygame.image.load("images/player.png").convert_alpha()

# Set the initial position of the snail and player rectangles
snail_rect = snail_surface.get_rect(bottomright=(600, 300))
player_rect = player_surface.get_rect(midbottom=(80, 300))

while True:
    # Update the display
    pygame.display.update()

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Fill the screen with black color
    screen.fill((0, 0, 0))

    # Blit the sky, ground, and test text surfaces onto the screen
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(test_text, (20,20))

    # Move the snail rectangle to the left and wrap around to the right if it goes off screen
    snail_rect.x -= 4
    if snail_rect.right <= 0: snail_rect.left = 800

    # Blit the snail and player surfaces onto the screen
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)

    # Check for collision between the player and snail rectangles
    player_rect.colliderect(snail_rect)

    # Control the frame rate
    clock.tick(60)
