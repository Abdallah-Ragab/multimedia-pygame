# Importing necessary modules
import pygame
from sys import exit

# Function to display score
def display_score():
    # Calculating current time
    current_time = pygame.time.get_ticks() - start_time
    # Creating score surface
    score_surface = small_font.render(f"Score: {int(current_time/1000)}", False, "Black")
    # Getting score surface rectangle
    score_rect = score_surface.get_rect(center=(400, 50))
    # Blitting score surface on screen
    screen.blit(score_surface, score_rect)
    # Returning current time
    return current_time

# Initializing pygame
pygame.init()

# Creating game window
screen = pygame.display.set_mode((800, 400))

# Creating game clock
clock = pygame.time.Clock()

# Setting game active flag
game_active = True

# Initializing start time
start_time = 0

# Setting game window caption
pygame.display.set_caption("Team 7 test game")

# Creating fonts
small_font = pygame.font.Font(None, 30)
large_font = pygame.font.Font(None, 50)

# Creating test text surface
test_text = small_font.render("the game", False, "Black")

# Loading game images
sky_surface = pygame.image.load("images/sky.png").convert_alpha()
ground_surface = pygame.image.load("images/ground.jpg").convert_alpha()
ground_top = 300
snail_surface = pygame.image.load("images/snail.png").convert_alpha()
snail_rect = snail_surface.get_rect(bottomright=(600, 300))
snail_moving = True
player_surface = pygame.image.load("images/player.png").convert_alpha()
player_rect = player_surface.get_rect(midbottom=(80, 300))
player_gravity = 0
scaled_player = pygame.transform.scale2x(player_surface)
scaled_player_rect = scaled_player.get_rect(midbottom=(400, 325))

# Game loop
while True:
    # Handling events
    for event in pygame.event.get():
        # Quitting game if close button is clicked
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        # Handling events if game is active
        if game_active:
            # Handling key press events
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    if player_rect.bottom>=ground_top:
                        player_gravity=-15
            # Handling mouse click events
            if event.type==pygame.MOUSEBUTTONDOWN:
                mouse_position=event.pos
                if player_rect.collidepoint(mouse_position):
                    if player_rect.bottom>=ground_top:
                        player_gravity=-15
        # Handling events if game is not active
        else:
            # Restarting game if space key is pressed
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                game_active=True
                player_rect.midbottom=(80,300)
                player_gravity=0
                snail_rect.bottomright=(600,300)
                snail_moving=True

    # Updating game screen if game is active
    if game_active:
        # Filling screen with black color
        screen.fill((0, 0, 0))
        # Blitting sky surface on screen
        screen.blit(sky_surface, (0, 0))
        # Blitting ground surface on screen
        screen.blit(ground_surface, (0, ground_top))
        # Displaying score and getting current time
        score = display_score()
        # Updating player gravity
        player_gravity += 0.6
        # Updating player position
        player_rect.y += player_gravity
        # Handling player collision with ground
        if player_rect.bottom >= ground_top:
            player_gravity = 0
            player_rect.bottom = ground_top
        # Blitting player surface on screen
        screen.blit(player_surface, player_rect)
        # Updating snail position
        if snail_moving:
            snail_rect.x -= 4
            if snail_rect.right <= 0: snail_rect.left = 800
        # Blitting snail surface on screen
        screen.blit(snail_surface, snail_rect)
        # Handling player collision with snail
        if player_rect.colliderect(snail_rect):
            game_active = False
    # Updating game screen if game is not active
    else:
        # Filling screen with white color
        screen.fill((255, 255, 255))
        # Displaying score
        score_surface = small_font.render(f"Score: {int(score/1000)}", False, "Black")
        score_rect = score_surface.get_rect(center=(400, 50))
        screen.blit(score_surface, score_rect)
        # Displaying game over message
        game_over_surface = large_font.render("Game Over", False, "Black")
        game_over_rect = game_over_surface.get_rect(center=(400, 100))
        screen.blit(game_over_surface, game_over_rect)
        # Blitting scaled player surface on screen
        screen.blit(scaled_player, scaled_player_rect)
        # Displaying restart message
        restart_surface = small_font.render("Press space to restart", False, "Black")
        restart_rect = restart_surface.get_rect(center=(400, 125))
        screen.blit(restart_surface, restart_rect)
        # Updating start time
        start_time = pygame.time.get_ticks()
    # Updating game display
    pygame.display.update()
    # Setting game clock tick rate
    clock.tick(60)
