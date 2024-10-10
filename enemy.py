import pygame

class Enemy:
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 0, 0)  # Red color
        self.speed = speed

    def update(self):
        self.rect.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
