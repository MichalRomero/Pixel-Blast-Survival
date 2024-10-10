import pygame

class Player:
    def __init__(self, x, y, width, height, speed):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 255, 0)
        self.speed = speed

    def handle_movement(self, keys_pressed, screen_width, screen_height):
        #when player pressed a, thier x coord goes down depending on the speed.
        if keys_pressed[pygame.K_a]:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_d]:
            self.rect.x += self.speed
        if keys_pressed[pygame.K_w]:
            self.rect.y -= self.speed
        if keys_pressed[pygame.K_s]:
            self.rect.y += self.speed

        # Keep player inside the screen boundaries
        self.rect.x = max(0, min(screen_width - self.rect.width, self.rect.x))
        self.rect.y = max(0, min(screen_height - self.rect.height, self.rect.y))
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)