import pygame
import sys

# Initialize Pygame
pygame.init()

# Define screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pixel Blast: Survival")

# Set up clock to control the frame rate
clock = pygame.time.Clock()

# Main game loop
def game_loop():
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with a background color
        screen.fill((0, 0, 0))  # Black background

        # Update display
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(60)

    # Quit Pygame
    pygame.quit()
    sys.exit()

# Start the game loop
if __name__ == "__main__":
    game_loop()
