import pygame
from entities import draw_pixel_art, pacman_pattern

class PacMan:
    def __init__(self, display_w, display_h):
        self.x = display_w // 3
        self.y = display_h - 100
        self.velocidade = 4
        self.pattern = pacman_pattern
        self.pixel_scale = 4
        self.score = 0

        self.width = len(self.pattern[0]) * self.pixel_scale
        self.height = len(self.pattern) * self.pixel_scale

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)


    def apply_boundaries(self, display_w, display_h):
        if self.x < 0:
            self.x = 0
        if self.x > display_w - self.width:
            self.x = display_w - self.width
        if self.y < 0:
            self.y = 0
        if self.y > display_h - self.height:
            self.y = display_h - self.height
        
        self.rect.topleft = (self.x, self.y)

    def move(self, display_w, display_h, wall_rects):
        keys = pygame.key.get_pressed()

        movimento_x = 0
        movimento_y = 0

        if keys[pygame.K_LEFT]:
            movimento_x = -self.velocidade
        elif keys[pygame.K_RIGHT]:
            movimento_x = self.velocidade
        if keys[pygame.K_UP]:
            movimento_y = -self.velocidade
        elif keys[pygame.K_DOWN]:
            movimento_y = self.velocidade

       
        if movimento_x != 0:
            step_x = int(abs(movimento_x) / movimento_x)
            for _ in range(abs(movimento_x)):
                new_rect_x = self.rect.move(step_x, 0)
                if any(new_rect_x.colliderect(wall) for wall in wall_rects):
                    break
                else:
                    self.x += step_x
                    self.rect.topleft = (self.x, self.y)

        
        if movimento_y != 0:
            step_y = int(abs(movimento_y) / movimento_y)
            for _ in range(abs(movimento_y)):
                new_rect_y = self.rect.move(0, step_y)
                if any(new_rect_y.colliderect(wall) for wall in wall_rects):
                    break
                else:
                    self.y += step_y
                    self.rect.topleft = (self.x, self.y)

        self.apply_boundaries(display_w, display_h)


    def check_dot_collision(self, dot_rects):
        for dot in dot_rects[:]:
            if self.rect.colliderect(dot):
                dot_rects.remove(dot)
                self.score += 1
                print(self.score)

    def draw(self, display):
        draw_pixel_art(self.pattern, self.x, self.y, self.pixel_scale, display)