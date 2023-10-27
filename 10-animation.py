# Import necessary modules
import random
import pygame
from sys import exit


# Define a function for player animation
def player_animation():
    # Use global variables for player_surf and player_index
    global player_surf, player_index
    # If the player is not on the ground, set the player_surf to the jump image
    if player_rect.bottom < ground_top:
        player_surf = player_jump
    else:
        # Increment the player_index by 0.05
        player_index += 0.05
        # If the player_index is greater than or equal to the length of the player_walk list, reset it to 0
        if player_index >= len(player_walk):
            player_index = 0
        # Set the player_surf to the image at the current player_index in the player_walk list
        player_surf = player_walk[int(player_index)]


# Define a function for displaying the score
def display_score():
    # Get the current time in milliseconds and subtract the start time to get the elapsed time
    current_time = pygame.time.get_ticks() - start_time
    # Render the score as text using the small_font and convert the time to seconds
    score_surface = small_font.render(f"Score: {int(current_time/1000)}", False, "Black")
    # Get the rectangle for the score surface and center it horizontally at the top of the screen
    score_rect = score_surface.get_rect(center=(400, 50))
    # Draw the score surface onto the screen at the score_rect position
    screen.blit(score_surface, score_rect)
    # Return the current time to be used for updating the score
    return current_time


# Define a function for enemy movement that takes a list of enemy rectangles as input
def enemy_movement(enemy_list):
    # Check if the enemy list is not empty
    if enemy_list:
        # Loop through each enemy rectangle in the enemy list
        for enemy_rect in enemy_list:
            # Move the enemy rectangle to the left by 5 pixels
            enemy_rect.x -= 5
            # Check if the enemy rectangle has moved off the left side of the screen
            if enemy_rect.right <= 0:
                # Remove the enemy rectangle from the enemy list
                enemy_list.remove(enemy_rect)


# Define a function for checking enemy collision with player
def enemy_collision(player, enemies):
    # Loop through each enemy rectangle in the enemy list
    for enemy in enemies:
        # Check if the player rectangle collides with the enemy rectangle and return True if there is a collision
        if player.colliderect(enemy):
            return True
    # Return False if there is no collision
    return False

# Initialize pygame
pygame.init()

# Set up the game window
screen = pygame.display.set_mode((800, 400))

# Set up the game clock
clock = pygame.time.Clock()

# Set the game to active
game_active = True

# Set the start time to 0
start_time = 0

# Set the game window caption
pygame.display.set_caption("Team 7 test game")

# Set up fonts for displaying text
small_font = pygame.font.Font(None, 30)
large_font = pygame.font.Font(None, 50)

# Create a test text surface
test_text = small_font.render("the game", False, "Black")

# Load images for the sky and ground
sky_surface = pygame.image.load("images/sky.png").convert_alpha()
ground_surface = pygame.image.load("images/ground.jpg").convert_alpha()

# Set the top of the ground surface
ground_top = 300

# Load images for the snail and fly enemies
snail_walk_1 = pygame.image.load("images/snail.png").convert_alpha()
snail_walk_2 = pygame.image.load("images/snail_2.png").convert_alpha()
snail_walk = [snail_walk_1, snail_walk_2]
snail_index = 0
snail_surf = snail_walk[snail_index]

fly_walk_1 = pygame.image.load("images/fly_2.png").convert_alpha()
fly_walk_2 = pygame.image.load("images/fly_3.png").convert_alpha()
fly_walk = [fly_walk_1, fly_walk_2]
fly_index = 0
fly_surf = fly_walk[fly_index]

# Set up a list of enemies with their starting positions
enemy_list = [
    (snail_walk_1, (800, 300)),
    (fly_walk_1, (800, 200))
]

# Set up an empty list for enemies in the game
enemies_in_game = []

# Load images for the player and set up player animation
player_walk_1 = pygame.image.load("images/player.png").convert_alpha()
player_walk_2 = pygame.image.load("images/player_2.png").convert_alpha()
player_walk = [player_walk_1, player_walk_2]

player_index = 0
player_jump = pygame.image.load('images/player_jump_1.png').convert_alpha()

player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom=(80, 300))
player_gravity = 0

# Scale the player image for display
scaled_player = pygame.transform.scale_by(pygame.image.load("images/player_dead.png").convert_alpha(), 3)
scaled_player_rect = scaled_player.get_rect(midbottom=(400, 325))

# Set up timers for enemy spawning and enemy animation
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 1500)

snail_animation = pygame.USEREVENT + 2
pygame.time.set_timer(snail_animation, 500)

fly_animation = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation, 100)

# Start the game loop
while True:
    # Handle events
    for event in pygame.event.get():
        # Quit the game if the window is closed
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Handle events if the game is active
        if game_active:
            # Handle player jumping
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom >= ground_top:
                        player_gravity = -15
            # Handle player jumping with mouse click
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = event.pos
                if player_rect.collidepoint(mouse_position):
                    if player_rect.bottom >= ground_top:
                        player_gravity = -15
            # Spawn enemies
            if event.type == enemy_timer:
                enemy_surface = random.choice(enemy_list)
                enemy_rect = enemy_surface[0].get_rect(midbottom=enemy_surface[1])
                enemies_in_game.append(enemy_rect)
            # Animate snail enemies
            if event.type == snail_animation:
                snail_index += 1
                if snail_index >= len(snail_walk):
                    snail_index = 0
                snail_surf = snail_walk[snail_index]
            # Animate fly enemies
            if event.type == fly_animation:
                fly_index += 1
                if fly_index >= len(fly_walk):
                    fly_index = 0
                fly_surf = fly_walk[fly_index]
        # Handle events if the game is not active
        else:
            # Restart the game if space is pressed
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True

    # Handle game logic if the game is active
    if game_active:
        # Fill the screen with black
        screen.fill((0, 0, 0))
        # Draw the sky and ground
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_surface, (0, ground_top))
        # Display the score
        score = display_score()
        # Move enemies
        enemy_movement(enemies_in_game)
        # Apply gravity to the player
        player_gravity += 0.6
        player_rect.y += player_gravity
        # Keep the player on the ground
        if player_rect.bottom >= ground_top:
            player_gravity = 0
            player_rect.bottom = ground_top
        # Animate the player
        player_animation()
        screen.blit(player_surf, player_rect)
        # Draw the enemies
        for enemy_rect in enemies_in_game:
            if enemy_rect.bottom == 300:
                enemy_surface = snail_surf
            elif enemy_rect.bottom == 200:
                enemy_surface = fly_surf
            screen.blit(enemy_surface, enemy_rect)
        # End the game if the player collides with an enemy
        if enemy_collision(player_rect, enemies_in_game):
            game_active = False
    # Handle game logic if the game is not active
    else:
        # Clear the list of enemies and reset the player position and gravity
        enemies_in_game.clear()
        player_rect.midbottom = (80, 300)
        player_gravity = 0
        # Fill the screen with white
        screen.fill((255, 255, 255))
        # Display the score
        score_surface = small_font.render(f"Score: {int(score/1000)}", False, "Black")
        score_rect = score_surface.get_rect(center=(400, 50))
        screen.blit(score_surface, score_rect)
        # Display "Game Over" text
        game_over_surface = large_font.render("Game Over", False, "Black")
        game_over_rect = game_over_surface.get_rect(center=(400, 100))
        screen.blit(game_over_surface, game_over_rect)
        # Display the scaled player image
        screen.blit(scaled_player, scaled_player_rect)
        # Display "Press space to restart" text
        restart_surface = small_font.render("Press space to restart", False, "Black")
        restart_rect = restart_surface.get_rect(center=(400, 125))
        screen.blit(restart_surface, restart_rect)
        # Set the start time to the current time
        start_time = pygame.time.get_ticks()
    # Update the display and set the game clock
    pygame.display.update()
    clock.tick(60)
