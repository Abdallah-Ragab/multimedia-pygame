import pygame
from sys import exit

# Initialize pygame
pygame.init()

# Create a window
screen = pygame.display.set_mode((800, 600))
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

# Load the background image
sky_surface = pygame.image.load('images/background.jpg')

# Game loop
while True:
    # Update the display
    pygame.display.update()

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # Draw the background image, the green surface, and the text on the screen
    screen.blit(sky_surface, (0, 0))
    screen.blit(test_surface, (400, 200))
    screen.blit(test_text, (100, 50))

    # Control the frame rate
    clock.tick(60)
