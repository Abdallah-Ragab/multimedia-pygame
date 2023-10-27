# python 6-jumping.py

# Importing the necessary modules
import pygame
from sys import exit

# Initializing Pygame
pygame.init()

# Creating the game window
screen = pygame.display.set_mode((800, 400))

# Creating a clock object to control the frame rate
clock = pygame.time.Clock()

# Setting the caption of the game window
pygame.display.set_caption("Running")

# Creating a font object to display text
test_font = pygame.font.Font(None, 20)

# Creating a text object to display on the screen
test_text = test_font.render("the game", False, "Black")

# Loading the sky and ground images
sky_surface = pygame.image.load("images/sky.png").convert_alpha()
ground_surface = pygame.image.load("images/ground.jpg").convert_alpha()

# Setting the position of the ground
ground_top = 300

# Loading the snail and player images
snail_surface = pygame.image.load("images/snail.png").convert_alpha()
player_surface = pygame.image.load("images/player.png").convert_alpha()

# Setting the initial position of the snail and player
snail_rect = snail_surface.get_rect(bottomright=(600, 300))
player_rect = player_surface.get_rect(midbottom=(80, 0))

# Setting the initial gravity of the player
player_gravity = 0

# The game loop
while True:
    # Handling events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # Handling the space bar and mouse click events to make the player jump
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                if player_rect.bottom>=ground_top:
                    player_gravity=-15

        if event.type==pygame.MOUSEBUTTONDOWN:
            mouse_position=event.pos
            if player_rect.collidepoint(mouse_position):
                if player_rect.bottom>=ground_top:
                    player_gravity=-15

    # Drawing the sky, ground and text on the screen
    screen.fill((0, 0, 0))
    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, ground_top))
    screen.blit(test_text, (20,20))

    # Updating the position of the player based on gravity
    player_gravity += 0.5
    player_rect.y += player_gravity

    # Limiting the player's position to the ground
    if player_rect.bottom >= ground_top:
        player_gravity = 0
        player_rect.bottom = ground_top

    # Drawing the player and snail on the screen
    screen.blit(player_surface, player_rect)

    # Moving the snail and checking for collision with the player
    if snail_moving:
        snail_rect.x -= 4
        if snail_rect.right <= 0: snail_rect.left = 800

    if player_rect.colliderect(snail_rect):
        snail_moving = False
    else :
        snail_moving = True

    screen.blit(snail_surface, snail_rect)

    # Updating the display and controlling the frame rate
    pygame.display.update()
    clock.tick(60)
