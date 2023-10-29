# Import necessary modules
import random
import pygame
from sys import exit



class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.bullets = 20
        self.gravity = 0
        self.initial_position = (80, 300)
        self.frame_index = 0
        self.walk_frames = [
            pygame.image.load("images/player.png").convert_alpha(),
            pygame.image.load("images/player_2.png").convert_alpha()
        ]
        self.jump_frame = pygame.image.load("images/player_jump_1.png").convert_alpha()
        self.image = self.walk_frames[self.frame_index]
        self.rect = self.image.get_rect(midbottom=self.initial_position)
        self.jump_sound = pygame.mixer.Sound("sounds/jump.mp3")
        self.jump_sound.set_volume(0.5)

    def update(self):
        self.check_input()
        self.apply_gravity()
        self.apply_animation()

    def check_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] or keys[pygame.K_UP]:
            if self.rect.bottom >= GroundGroup.sprite.rect.top:
                self.gravity = -15
                self.jump_sound.play()

    def apply_gravity(self):
        self.gravity += 0.6
        self.rect.y += self.gravity
        if self.rect.bottom >= GroundGroup.sprite.rect.top:
            self.gravity = 0
            self.rect.bottom = GroundGroup.sprite.rect.top

    def apply_animation(self):
        if self.rect.bottom < GroundGroup.sprite.rect.top:
            self.image = self.jump_frame
        else:
            self.walk_animation()

    def walk_animation(self):
        self.frame_index += 0.05
        if self.frame_index >= len(self.walk_frames):
            self.frame_index = 0
        self.image = self.walk_frames[int(self.frame_index)]

class Enemy(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.speed = 5
        if type == "snail":
            self.animation_speed = 0.05
            self.frames = [
                pygame.image.load("images/snail.png").convert_alpha(),
                pygame.image.load("images/snail_2.png").convert_alpha()
            ]
            self.y_pos = 300
        elif type == "fly":
            self.animation_speed = 0.1
            self.frames = [
                pygame.image.load("images/fly_2.png").convert_alpha(),
                pygame.image.load("images/fly_3.png").convert_alpha()
            ]
            self.y_pos = 200

        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(midbottom=(800, self.y_pos))

    def apply_animation(self):
        self.frame_index += self.animation_speed
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def apply_movement(self):
        self.rect.x -= self.speed
        if self.rect.right <= 0:
            self.kill()

    def update(self):
        self.apply_animation()
        self.apply_movement()

class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.speed = 10
        bullet_x = PlayerGroup.sprite.rect.right
        bullet_y = (PlayerGroup.sprite.rect.bottom + PlayerGroup.sprite.rect.top) / 2
        self.image = pygame.transform.scale_by(pygame.image.load("images/bullet.png"), 0.5)
        self.rect = self.image.get_rect(topleft=(bullet_x, bullet_y))

    def apply_movement(self):
        self.rect.x += self.speed
        if self.rect.right <= 0:
            self.kill()
    def update(self):
        self.apply_movement()


class Cloud(pygame.sprite.Sprite):
    def __init__(self, type):
        super().__init__()
        self.speed = random.randint(1, 3)
        self.y_pos = random.randint(-50, 50)
        if type == "small":
            self.image = pygame.image.load("images/cloud_small.png").convert_alpha()
        elif type == "large":
            self.image = pygame.image.load("images/cloud_large.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(800, self.y_pos))

    def apply_movement(self):
        self.rect.x -= self.speed
        if self.rect.right <= 0:
            self.kill()
    def update(self):
        self.apply_movement()

class Ground(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/ground.jpg").convert_alpha()
        self.rect = self.image.get_rect(topleft=(0, 300))

class Background(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("images/clear_sky.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(0, 0))

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

def display_bullets():
    number_of_bullets = PlayerGroup.sprite.bullets
    bullet_surface = small_font.render(f"Bullets: {number_of_bullets}", False, "Black")
    bullet_rect = bullet_surface.get_rect(center=(400, 100))
    screen.blit(bullet_surface, bullet_rect)

def check_collision():
    global game_active
    collision = pygame.sprite.spritecollide(PlayerGroup.sprite, EnemyGroup, True)

    if collision:
        game_active = False

    enemy_hit = pygame.sprite.groupcollide(EnemyGroup, BulletGroup, True, True)

# Initialize pygame and window
pygame.init()
screen = pygame.display.set_mode((800, 400))
clock = pygame.time.Clock()

background_music = pygame.mixer.Sound("sounds/loop.mp3")
background_music.play(loops=-1)

PlayerGroup = pygame.sprite.GroupSingle()
PlayerGroup.add(Player())

GroundGroup = pygame.sprite.GroupSingle()
GroundGroup.add(Ground())

BackgroundGroup = pygame.sprite.GroupSingle()
BackgroundGroup.add(Background())

EnemyGroup = pygame.sprite.Group()

BulletGroup = pygame.sprite.Group()

CloudGroup = pygame.sprite.Group()







# Set the game to active
game_active = True

# Set the start time to 0
start_time = 0

# Set the game window caption
pygame.display.set_caption("Team 7 test game")

# Set up fonts for displaying text
small_font = pygame.font.Font(None, 30)
large_font = pygame.font.Font(None, 50)


# Set the top of the ground surface
scaled_player = pygame.transform.scale_by(pygame.image.load("images/player_dead.png").convert_alpha(), 3)
scaled_player_rect = scaled_player.get_rect(midbottom=(400, 325))

# Set up timers for enemy spawning and enemy animation
enemy_timer = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_timer, 1500)

cloud_timer = pygame.USEREVENT + 2
pygame.time.set_timer(cloud_timer, 5000)

pygame.event.post(pygame.event.Event(cloud_timer))


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
            # spawn clouds
            if event.type == cloud_timer:
                CloudGroup.add(Cloud(random.choice(["small", "large"])))
            # Spawn enemies
            if event.type == enemy_timer:
                EnemyGroup.add(Enemy(random.choice(["snail", "fly"])))
            if event.type==pygame.MOUSEBUTTONDOWN:
                if PlayerGroup.sprite.bullets > 0 :
                    BulletGroup.add(Bullet())
                    PlayerGroup.sprite.bullets -= 1
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_x:
                    if PlayerGroup.sprite.bullets > 0 :
                        BulletGroup.add(Bullet())
                        PlayerGroup.sprite.bullets -= 1
        # Handle events if the game is not active
        else:
            # Restart the game if space is pressed
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True

    if game_active:
        # Fill the screen with black
        screen.fill((0, 0, 0))


        # Draw the Sprite
        BackgroundGroup.draw(screen)
        CloudGroup.draw(screen)
        GroundGroup.draw(screen)
        PlayerGroup.draw(screen)
        EnemyGroup.draw(screen)
        BulletGroup.draw(screen)

        # Display the score
        score = display_score()
        display_bullets()

        # Update the Sprite Groups
        CloudGroup.update()
        PlayerGroup.update()
        EnemyGroup.update()
        BulletGroup.update()

        # Check for collisions
        check_collision()

    # Handle game logic if the game is not active
    else:
        # Clear the list of enemies and reset the player position and gravity
        EnemyGroup.empty()
        PlayerGroup.empty()
        PlayerGroup.add(Player())
        CloudGroup.empty()
        BulletGroup.empty()

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
