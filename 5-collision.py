# Importing the pygame module
import pygame

# Importing the exit function from the sys module
from sys import exit

# Initializing pygame
pygame.init()

# Creating a window with dimensions of 800x400 pixels
screen = pygame.display.set_mode((800, 400))

# Setting the caption of the window to "Running"
pygame.display.set_caption("Running")

# Creating a clock object to control the frame rate
clock = pygame.time.Clock()

# Creating a font object with a size of 20
test_font = pygame.font.Font(None, 20)

# Rendering the text "the game" using the font object
test_text = test_font.render("the game", False, "Black")

# Creating a surface object with dimensions of 100x200 pixels and filling it with green color
test_surface = pygame.Surface((100, 200))
test_surface.fill("green")

# Loading the sky image and converting it to a format that can be displayed on the screen
sky_surface = pygame.image.load("images/sky.png").convert_alpha()

# Loading the ground image and converting it to a format that can be displayed on the screen
ground_surface = pygame.image.load("images/ground.jpg").convert_alpha()

# Loading the snail image and converting it to a format that can be displayed on the screen
snail_surface = pygame.image.load("images/snail.png").convert_alpha()

# Getting the rectangle of the snail image and setting its position to the bottom right corner of the screen
snail_rect = snail_surface.get_rect(bottomright=(600, 300))

# Loading the player image and converting it to a format that can be displayed on the screen
player_surface = pygame.image.load("images/player.png").convert_alpha()

# Getting the rectangle of the player image and setting its position to the middle bottom of the screen
player_rect = player_surface.get_rect(midbottom=(80, 300))

# Setting the snail to be moving
snail_moving = True

# Starting the game loop
while True:

    # Handling events
    for event in pygame.event.get():

        # If the user clicks the close button, exit the game
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # If the user presses a key
        if event.type==pygame.KEYDOWN:

            # Get the position of the mouse
            mouse_position=event.pos # (x,y)

            # If the player rectangle collides with the mouse position, print "player pressed"
            if player_rect.collidepoint(mouse_position):
                print("player pressed")

    # Filling the screen with black color
    screen.fill((0, 0, 0))

    # Drawing the sky image on the screen
    screen.blit(sky_surface, (0, 0))

    # Drawing the ground image on the screen
    screen.blit(ground_surface, (0, 300))

    # Drawing the "the game" text on the screen
    screen.blit(test_text, (20,20))

    # If the snail is moving
    if snail_moving:

        # Move the snail to the left by 4 pixels
        snail_rect.x -= 4

        # If the snail goes off the left edge of the screen, move it to the right edge of the screen
        if snail_rect.right <= 0: snail_rect.left = 800

    # Drawing the snail image on the screen
    screen.blit(snail_surface, snail_rect)

    # Drawing the player image on the screen
    screen.blit(player_surface, player_rect)

    # If the player rectangle collides with the snail rectangle, stop the snail from moving
    if player_rect.colliderect(snail_rect):
        snail_moving = False

    # If the player rectangle does not collide with the snail rectangle, set the snail to be moving
    else:
        snail_moving = True

    # Get the position of the mouse
    mouse_position = pygame.mouse.get_pos()

    # If the player rectangle collides with the mouse position
    if player_rect.collidepoint(mouse_position):

        # If the left mouse button is pressed, print "mouse is on the player"
        if pygame.mouse.get_pressed()[0]: # (True,False,False)
            print("mouse is on the player")

    # Updating the display
    pygame.display.update()

    # Setting the frame rate to 60 frames per second
    clock.tick(60)
