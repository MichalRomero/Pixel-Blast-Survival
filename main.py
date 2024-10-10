import pygame
import sys
from player import Player
from bullet import Bullet

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Define map size
MAP_WIDTH = 1200
MAP_HEIGHT = 1200

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pixel Blast: Survival")

# Create a player instance
player = Player(100, 100, 50, 50, 5)

# Create a list to store bullets
bullets = []

# Create a clock to control the frame rate
clock = pygame.time.Clock()

def draw_grid(surface):
    """Draw a grid on the background for movement reference."""
    grid_color = (50, 50, 50)
    for x in range(0, MAP_WIDTH, 50):
        pygame.draw.line(surface, grid_color, (x, 0), (x, MAP_HEIGHT))
    for y in range(0, MAP_HEIGHT, 50):
        pygame.draw.line(surface, grid_color, (0, y), (MAP_WIDTH, y))

# Variable to track if the spacebar is pressed
space_pressed = False

while True:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Get the keys currently pressed
    keys_pressed = pygame.key.get_pressed()

    # Handle player movement
    player.handle_movement(keys_pressed, MAP_WIDTH, MAP_HEIGHT)

    # Fire bullet when space is pressed
    if keys_pressed[pygame.K_SPACE]:
        if not space_pressed:  # Check if space was not pressed last frame
            bullet_x = player.rect.centerx
            bullet_y = player.rect.centery
            
            # Set bullet dimensions based on the direction
            if player.direction in ("UP", "DOWN"):
                bullet = Bullet(bullet_x, bullet_y, 15, 50, 10, player.direction)  # Width: 15, Height: 50
            else:  # LEFT or RIGHT
                bullet = Bullet(bullet_x, bullet_y, 50, 15, 10, player.direction)  # Width: 50, Height: 15
            
            bullets.append(bullet)
            space_pressed = True  # Set the flag to True
    else:
        space_pressed = False  # Reset the flag if space is not pressed

    # Update bullets
    for bullet in bullets[:]:  # Iterate over a copy of the list
        bullet.update()
        # Remove bullet if it is off screen
        if bullet.is_off_screen(SCREEN_WIDTH, SCREEN_HEIGHT):
            bullets.remove(bullet)

    # Calculate the camera position based on the player's position
    camera_x = player.get_position()[0] - (SCREEN_WIDTH // 2)
    camera_y = player.get_position()[1] - (SCREEN_HEIGHT // 2)
    camera_rect = pygame.Rect(camera_x, camera_y, SCREEN_WIDTH, SCREEN_HEIGHT)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the grid for movement reference
    draw_grid(screen)

    # Draw the player (with camera offset)
    player.draw(screen, camera_rect)

    # Draw all bullets (with camera offset)
    for bullet in bullets:
        bullet.draw(screen, camera_rect)

    # Display player position
    position_text = f"Player Position: {player.get_position()}"
    font = pygame.font.Font(None, 36)
    text_surface = font.render(position_text, True, (255, 255, 255))
    screen.blit(text_surface, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
