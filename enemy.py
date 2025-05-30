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

    def draw(self, screen, pacman):
        if not pacman.powerup:
            draw_pixel_art(enemy_pattern, self.x, self.y, 4, screen)
        else:
            draw_pixel_art(self.ghost_mode(enemy_pattern), self.x, self.y, 4, screen)     
    
    def ghost_mode(self, pattern):
        possible_substitutes = list('123456789ABCDEFG')
        substitution_map = {}

        result = []

        for line in pattern:
            new_line = ''
            for char in line:
                if char == ' ' or char == '2':
                    new_line += char
                else:
                    if char not in substitution_map:
                        substitute = random.choice([c for c in possible_substitutes if c not in substitution_map.values()])
                        substitution_map[char] = substitute
                    new_line += substitution_map[char]
            result.append(new_line)

        return result

def spawn_enemies(MIDDLE_X, MIDDLE_Y):
    enemies = [Enemy(MIDDLE_X, MIDDLE_Y) for i in range(2)]
    return enemies
        
