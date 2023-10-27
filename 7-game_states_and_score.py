# Importing the pygame library and the exit function from the sys module
import pygame
from sys import exit

# Function to display the score on the screen
def display_score():
    # Calculating the current time elapsed in the game
    current_time = pygame.time.get_ticks() - start_time
    # Creating a surface to render the score text
    score_surface = small_font.render(f"Score: {int(current_time/1000)}", False, "Black")
    # Getting the rectangle of the score surface and centering it horizontally at the top of the screen
    score_rect = score_surface.get_rect(center=(400, 50))
    # Blitting the score surface onto the screen
    screen.blit(score_surface, score_rect)

# Initializing pygame
pygame.init()
# Creating a window with dimensions 800x400 pixels
screen = pygame.display.set_mode((800, 400))
# Creating a clock object to control the frame rate of the game
clock = pygame.time.Clock()
# Setting the game_active flag to True
game_active = True
# Initializing the start_time variable to 0
start_time = 0
# Setting the caption of the game window
pygame.display.set_caption("Team 7 test game")

# Creating two font objects for rendering text on the screen
small_font = pygame.font.Font(None, 30)
large_font = pygame.font.Font(None, 50)
# Creating a surface to render the text "the game"
test_text = small_font.render("the game", False, "Black")

# Loading two images for the game background and ground
sky_surface = pygame.image.load("images/sky.png").convert_alpha()
ground_surface = pygame.image.load("images/ground.jpg").convert_alpha()
# Setting the y-coordinate of the top of the ground surface
ground_top = 300

# Loading two images for the player and the snail enemy
snail_surface = pygame.image.load("images/snail.png").convert_alpha()
snail_rect = snail_surface.get_rect(bottomright=(600, 300))
snail_moving = True

player_surface = pygame.image.load("images/player.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0

# Game loop
while True:
    # Handling events
    for event in pygame.event.get():
        # Quitting the game if the user closes the window
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Handling events when the game is active
        if game_active:
            # Handling events when the user presses the space bar
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    # Making the player jump if they are on the ground
                    if player_rect.bottom>=ground_top:
                        player_gravity=-15
            # Handling events when the user clicks the mouse
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_position=event.pos
                # Making the player jump if they are on the ground and the mouse is clicked on them
                if player_rect.collidepoint(mouse_position):
                    if player_rect.bottom>=ground_top:
                        player_gravity=-15
        # Handling events when the game is over
        else:
            # Restarting the game if the user presses the space bar
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                game_active=True
                player_rect.midbottom=(80,300)
                player_gravity=0
                snail_rect.bottomright=(600,300)
                snail_moving=True

    # Updating the game state if the game is active
    if game_active:
        # Filling the screen with black color
        screen.fill((0, 0, 0))
        # Blitting the sky and ground surfaces onto the screen
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, ground_top))
        # Displaying the score on the screen
        display_score()

        # Updating the player's position based on gravity
        player_gravity += 0.6
        player_rect.y += player_gravity

        # Keeping the player on the ground
        if player_rect.bottom >= ground_top:
            player_gravity = 0
            player_rect.bottom = ground_top

        # Blitting the player and snail surfaces onto the screen
        screen.blit(player_surface, player_rect)

        if snail_moving:
            snail_rect.x -= 4
            if snail_rect.right <= 0: snail_rect.left = 800

        screen.blit(snail_surface, snail_rect)

        # Checking for collision between the player and snail
        if player_rect.colliderect(snail_rect):
            # Ending the game if there is a collision
            game_active = False
            # Filling the screen with white color
            screen.fill((255, 255, 255))
            # Displaying the score on the screen
            display_score()
            # Displaying the "Game Over" text on the screen
            game_over_surface = large_font.render("Game Over", False, "Black")
            game_over_rect = game_over_surface.get_rect(center=(400, 150))
            screen.blit(game_over_surface, game_over_rect)

            # Displaying the "Press space to restart" text on the screen
            restart_surface = small_font.render("Press space to restart", False, "Black")
            restart_rect = restart_surface.get_rect(center=(400, 180))
            screen.blit(restart_surface, restart_rect)

            # Updating the start_time variable to the current time
            start_time = pygame.time.get_ticks()

        # Updating the display and limiting the frame rate to 60 fps
        pygame.display.update()
        clock.tick(60)