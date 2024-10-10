import pygame

class Bullet:
    def __init__(self, x, y, width, height, speed, direction):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 255, 0)  # Yellow color
        self.speed = speed
        self.direction = direction  # Direction of the bullet

    def update(self):
        # Move the bullet based on its direction
        if self.direction == "UP":
            self.rect.y -= self.speed
        elif self.direction == "DOWN":
            self.rect.y += self.speed
        elif self.direction == "LEFT":
            self.rect.x -= self.speed
        elif self.direction == "RIGHT":
            self.rect.x += self.speed

    def draw(self, screen, camera_rect):
        # Draw the bullet with camera offset
        pygame.draw.rect(screen, self.color, self.rect.move(-camera_rect.x, -camera_rect.y))

    def is_off_screen(self, screen_width, screen_height):
        # Check if the bullet is off the screen with a threshold of 100 pixels
        return (
            self.rect.x < -1000 or 
            self.rect.x > screen_width + 1000 or 
            self.rect.y < -1000 or 
            self.rect.y > screen_height + 1000
        )
