import pygame

class Bullet:
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 255, 0)  # Yellow color
        self.speed = speed

    def update(self):
        self.rect.y -= self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
