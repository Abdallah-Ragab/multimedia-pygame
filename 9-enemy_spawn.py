# Importing necessary modules
import random
import pygame
from sys import exit

# Function to display the score
def display_score():
    # Calculating the current time
    current_time = pygame.time.get_ticks() - start_time
    # Creating a surface to display the score
    score_surface = small_font.render(f"Score: {int(current_time/1000)}", False, "Black")
    # Getting the rectangle of the score surface and centering it
    score_rect = score_surface.get_rect(center=(400, 50))
    # Blitting the score surface onto the screen
    screen.blit(score_surface, score_rect)
    # Returning the current time
    return current_time

# Function to move the enemies
def enemy_movement(enemy_list):
    # Checking if there are any enemies in the list
    if enemy_list:
        # Looping through each enemy in the list
        for enemy_rect in enemy_list:
            # Moving the enemy to the left
            enemy_rect.x -= 5
            # Removing the enemy from the list if it goes off the screen
            if enemy_rect.right <= 0:
                enemy_list.remove(enemy_rect)

# Function to check for collision between the player and enemies
def enemy_collision(player, enemies):
    # Looping through each enemy in the list
    for enemy in enemies:
        # Checking if the player collides with the enemy
        if player.colliderect(enemy):
            # Returning True if there is a collision
            return True
    # Returning False if there is no collision
    return False

# Initializing pygame
pygame.init()

# Creating the game window
screen = pygame.display.set_mode((800, 400))

# Creating the game clock
clock = pygame.time.Clock()

# Setting the game to active
game_active = True

# Setting the start time to 0
start_time = 0

# Setting the game window caption
pygame.display.set_caption("Team 7 test game")

# Creating fonts for displaying text
small_font = pygame.font.Font(None, 30)
large_font = pygame.font.Font(None, 50)

# Creating a test text surface
test_text = small_font.render("the game", False, "Black")

# Loading the sky and ground images
sky_surface = pygame.image.load("images/sky.png").convert_alpha()
ground_surface = pygame.image.load("images/ground.jpg").convert_alpha()

# Setting the top of the ground surface
ground_top = 300

# Loading the enemy images
snail_surface = pygame.image.load("images/snail.png").convert_alpha()
fly_surface = pygame.image.load("images/fly.png").convert_alpha()

# Creating a list of enemies with their starting positions
enemy_list = [
    (snail_surface, (800, 300)),
    (fly_surface, (800, 200))
]

# Creating an empty list for enemies in the game
enemies_in_game = []

# Loading the player image
player_surface = pygame.image.load("images/player.png").convert_alpha()

# Setting the player rectangle to the bottom left of the screen
player_rect = player_surface.get_rect(midbottom=(80, 300))

# Setting the player gravity to 0
player_gravity = 0

# Scaling the player image
scaled_player = pygame.transform.scale2x(player_surface)

# Setting the scaled player rectangle to the bottom center of the screen
scaled_player_rect = scaled_player.get_rect(midbottom=(400, 325))

# Creating an enemy timer event
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 1500)

# Game loop
while True:
    # Handling events
    for event in pygame.event.get():
        # Quitting the game if the window is closed
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Handling events if the game is active
        if game_active:
            # Handling key presses
            if event.type == pygame.KEYDOWN:
                # Handling spacebar presses to make the player jump
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom >= ground_top:
                        player_gravity = -15
            # Handling mouse clicks
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = event.pos
                if player_rect.collidepoint(mouse_position):
                    if player_rect.bottom >= ground_top:
                        player_gravity = -15
            # Spawning enemies at regular intervals
            if event.type == enemy_timer:
                enemy_surface = random.choice(enemy_list)
                enemy_rect = enemy_surface[0].get_rect(midbottom=enemy_surface[1])
                enemies_in_game.append(enemy_rect)
        # Handling events if the game is not active
        else:
            # Restarting the game if the spacebar is pressed
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True

    # Updating the screen if the game is active
    if game_active:
        # Filling the screen with black
        screen.fill((0, 0, 0))
        # Blitting the sky and ground surfaces onto the screen
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, ground_top))
        # Displaying the score and getting the current time
        score = display_score()
        # Moving the enemies
        enemy_movement(enemies_in_game)
        # Applying gravity to the player
        player_gravity += 0.6
        player_rect.y += player_gravity
        # Handling collisions with the ground
        if player_rect.bottom >= ground_top:
            player_gravity = 0
            player_rect.bottom = ground_top
        # Blitting the player onto the screen
        screen.blit(player_surface, player_rect)
        # Blitting the enemies onto the screen
        for enemy_rect in enemies_in_game:
            if enemy_rect.bottom == 300:
                enemy_surface = snail_surface
            elif enemy_rect.bottom == 200:
                enemy_surface = fly_surface
            screen.blit(enemy_surface, enemy_rect)
        # Checking for collisions between the player and enemies
        if enemy_collision(player_rect, enemies_in_game):
            game_active = False
    # Updating the screen if the game is not active
    else:
        # Clearing the list of enemies in the game
        enemies_in_game.clear()
        # Resetting the player position and gravity
        player_rect.midbottom = (80, 300)
        player_gravity = 0
        # Filling the screen with white
        screen.fill((255, 255, 255))
        # Displaying the score
        score_surface = small_font.render(f"Score: {int(score/1000)}", False, "Black")
        score_rect = score_surface.get_rect(center=(400, 50))
        screen.blit(score_surface, score_rect)
        # Displaying the game over message
        game_over_surface = large_font.render("Game Over", False, "Black")
        game_over_rect = game_over_surface.get_rect(center=(400, 100))
        screen.blit(game_over_surface, game_over_rect)
        # Blitting the scaled player onto the screen
        screen.blit(scaled_player, scaled_player_rect)
        # Displaying the restart message
        restart_surface = small_font.render("Press space to restart", False, "Black")
        restart_rect = restart_surface.get_rect(center=(400, 125))
        screen.blit(restart_surface, restart_rect)
        # Setting the start time to the current time
        start_time = pygame.time.get_ticks()

    # Updating the display and setting the game clock
    pygame.display.update()
    clock.tick(60)
