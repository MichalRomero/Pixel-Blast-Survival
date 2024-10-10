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

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
