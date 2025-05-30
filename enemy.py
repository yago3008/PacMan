import pygame
import random
from entities import draw_pixel_art, enemy_pattern
from screen import SCREEN

class Enemy:
    def __init__(self, x, y):
        self.width = 42
        self.height = 32
        self.x = x + 4
        self.y = y + 1
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

        
        self.speed = 2
        self.direction = "up"
        
        self.scared = False

    def update(self, wall_rects, player_powerup):
        self.scared = player_powerup
        
        dx, dy = 0, 0
        if self.direction == "up":
            dy = -self.speed
        elif self.direction == "down":
            dy = self.speed
        elif self.direction == "left":
            dx = -self.speed
        elif self.direction == "right":
            dx = self.speed

        next_rect = self.rect.move(dx, dy)

        if not any(next_rect.colliderect(wall) for wall in wall_rects):
            self.rect = next_rect
            self.x, self.y = self.rect.topleft
        else:
            self.direction = random.choice(["up", "down", "left", "right"])

    def draw(self, screen):
        draw_pixel_art(enemy_pattern, self.x, self.y, 4, screen)
    

def spawn_enemies(MIDDLE_X, MIDDLE_Y):
    enemies = [Enemy(MIDDLE_X, MIDDLE_Y) for i in range(2)]
    return enemies
        
