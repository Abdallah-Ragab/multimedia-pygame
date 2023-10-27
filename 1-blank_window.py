import pygame
from sys import exit

pygame.init()

# Create a window with dimensions 800x600 and set the caption to "Running"
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Running")

# Create a clock object to control the frame rate
clock = pygame.time.Clock()

# Create a surface object with no dimensions and fill it with green color
test_surface = pygame.Surface(())
test_surface.fill("green")

# Main game loop
while True:
    # Update the display
    pygame.display.update()

    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Quit the game if the user closes the window
            pygame.quit()
            exit()

    # Control the frame rate
    clock.tick(60)
