import pygame

class Player:
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 255, 0)
        self.speed = speed
        self.direction = "UP"  # Default facing direction

    def handle_movement(self, keys_pressed, map_width, map_height):
        # Move the player based on key presses
        if keys_pressed[pygame.K_a]:
            self.rect.x -= self.speed
            self.direction = "LEFT"
        if keys_pressed[pygame.K_d]:
            self.rect.x += self.speed
            self.direction = "RIGHT"
        if keys_pressed[pygame.K_w]:
            self.rect.y -= self.speed
            self.direction = "UP"
        if keys_pressed[pygame.K_s]:
            self.rect.y += self.speed
            self.direction = "DOWN"

        # Keep player inside the larger movement boundaries
        self.rect.x = max(0, min(map_width - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(map_height - self.rect.height, self.rect.y))
    
    def draw(self, screen, camera_rect):
        # Draw the player offset by the camera position
        pygame.draw.rect(screen, self.color, self.rect.move(-camera_rect.x, -camera_rect.y))

    def get_position(self):
        return self.rect.topleft
