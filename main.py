import pygame
import sys
from player import Player
from bullet import Bullet
from enemy import Enemy

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set up the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pixel Blast: Survival")

# Game settings
clock = pygame.time.Clock()


# Initialize player
player = Player(SCREEN_WIDTH // 2 - 25, SCREEN_HEIGHT // 2 - 25, 50, 50, 5)

# Initialize bullets and enemies
bullets = []
enemies = []


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


        # Shooting bullets (spacebar)
        if keys_pressed[pygame.K_SPACE]:
            bullet_x = player.rect.centerx - 2
            bullet_y = player.rect.y

            # Create a bullet based on the player's direction
            if player.direction == "UP":
                bullets.append(Bullet(bullet_x, bullet_y, 5, 10, 7, "UP"))
            elif player.direction == "DOWN":
                bullets.append(Bullet(bullet_x, bullet_y + player.rect.height, 5, 10, 7, "DOWN"))
            elif player.direction == "LEFT":
                bullets.append(Bullet(bullet_x - 5, bullet_y + (player.rect.height // 2) - 2.5, 10, 5, 7, "LEFT"))  # Adjust for vertical centering
            elif player.direction == "RIGHT":
                bullets.append(Bullet(bullet_x + player.rect.width, bullet_y + (player.rect.height // 2) - 2.5, 10, 5, 7, "RIGHT"))  # Adjust for vertical centering


        # Update bullets
        for bullet in bullets[:]:
            bullet.update()
            if bullet.rect.y < 0:
                bullets.remove(bullet)



        # Fill the screen with a background color
        screen.fill((0, 0, 0))  # Black background


        # Draw player
        player.draw(screen)

        # Draw bullets
        for bullet in bullets:
            bullet.draw(screen)


        # Update display
        pygame.display.flip()

        # Limit the frame rate
        clock.tick(60)

    pygame.quit()
    sys.exit()

# Start the game loop
if __name__ == "__main__":
    game_loop()
