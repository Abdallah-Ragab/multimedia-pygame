import pygame
from sys import exit

# Initialize pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Running")

# Create a clock to control the frame rate
clock = pygame.time.Clock()

# Create a font object to render text
test_font = pygame.font.Font(None, 50)

# Render the text "the game" using the font object
test_text = test_font.render("the game", False, "Black")

# Create a surface object and fill it with green color
test_surface = pygame.Surface((100, 200))
test_surface.fill("green")

# Load the sky and ground images
sky_surface = pygame.image.load('images/sky.png').convert_alpha()
ground_surface = pygame.image.load('images/ground.jpg').convert_alpha()

# Load the snail image and set its initial position
snail_surface = pygame.image.load('images/snail.png').convert_alpha()
snail_x_position = 600

# Start the game loop
while True:
    # Update the display
    pygame.display.update()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Fill the screen with black color
    screen.fill((0, 0, 0))

    # Move the snail to the left
    snail_x_position -= 4

    # If the snail goes off the screen, reset its position
    if snail_x_position < -100:
        snail_x_position = 800

    # Draw the sky, ground, and snail on the screen
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(snail_surface, (snail_x_position, 250))

    # Control the frame rate
    clock.tick(60)