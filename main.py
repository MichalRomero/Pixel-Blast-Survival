import pygame
import sys
from player import Player

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pixel Blast: Survival")

# Game settings
clock = pygame.time.Clock()


# Initialize player
player = Player(SCREEN_WIDTH // 2 - 25, SCREEN_HEIGHT - 60, 50, 50, 5)



# Main game loop
def game_loop():
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



        

        keys_pressed = pygame.key.get_pressed()

        # Player movement
        player.handle_movement(keys_pressed, SCREEN_WIDTH, SCREEN_HEIGHT)

        



        # Fill the screen with a background color
        screen.fill((0, 0, 0))  # Black background

        # Draw player
        player.draw(screen)

        # Update display
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Start the game loop
if __name__ == "__main__":
    game_loop()
