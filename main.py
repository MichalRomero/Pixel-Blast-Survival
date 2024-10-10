import pygame
import sys
from player import Player

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

# Create a clock to control the frame rate
clock = pygame.time.Clock()

def draw_grid(surface):
    """Draw a grid on the background for movement reference."""
    grid_color = (50, 50, 50)
    for x in range(0, MAP_WIDTH, 50):  # Adjust spacing for grid size
        pygame.draw.line(surface, grid_color, (x, 0), (x, MAP_HEIGHT))
    for y in range(0, MAP_HEIGHT, 50):
        pygame.draw.line(surface, grid_color, (0, y), (MAP_WIDTH, y))

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

    # Display player position
    position_text = f"Player Position: {player.get_position()}"
    font = pygame.font.Font(None, 36)
    text_surface = font.render(position_text, True, (255, 255, 255))
    screen.blit(text_surface, (10, 10))

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)
