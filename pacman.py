import pygame
from entities import draw_pixel_art, pacman_pattern

class PacMan:
    def __init__(self, display_w, display_h):
        self.x = display_w // 3
        self.y = display_h - 100
        self.speed = 4
        self.pattern = pacman_pattern
        self.pixel_scale = 5
        self.score = 0
        self.powerup = False

        self.width = len(self.pattern[0]) * self.pixel_scale
        self.height = len(self.pattern) * self.pixel_scale

        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)



        
        self.rect.topleft = (self.x, self.y)

    def move(self, wall_rects):
        keys = pygame.key.get_pressed()

        movimento_x = 0
        movimento_y = 0

        if keys[pygame.K_LEFT]:
            movimento_x = -self.speed
        elif keys[pygame.K_RIGHT]:
            movimento_x = self.speed
        if keys[pygame.K_UP]:
            movimento_y = -self.speed
        elif keys[pygame.K_DOWN]:
            movimento_y = self.speed
       
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
        self.change_sides()

    def change_sides(self):
        print(self.x)
        if self.x <= -30:
            self.x = 800
        elif self.x >= 805:
            self.x = -20

    def check_dot_collision(self, dot_rects):
        for dot in dot_rects[:]:
            if self.rect.colliderect(dot):
                dot_rects.remove(dot)
                self.score += 1
                print(self.score)
    
    def check_big_dot_collision(self, big_dot_rects):
        for big_dot in big_dot_rects[:]:
            if self.rect.colliderect(big_dot):
                big_dot_rects.remove(big_dot)
                self.score += 10
                print(self.score)
                self.activate_powerup()
    
    def check_enemy_collision(self, enemies):
        for enemy in enemies:
            if self.rect.colliderect(enemy.rect):
                if not self.powerup:
                    print("Colidiu com um inimigo!")
                else:
                    enemies.remove(enemy)
                    self.score += 20
                    print("matou o inimigo")

    def activate_powerup(self):
        self.powerup = True
        self.powerup_end_time = pygame.time.get_ticks() + 25000
        print('powerup active')

    def update(self):
        if self.powerup and pygame.time.get_ticks() >= self.powerup_end_time:
            self.powerup = False
            print("Powerup desativado")

    def call_funcs(self,DISPLAY_W, DISPLAY_H, wall_rects, dot_rects, big_dot_rects, enemies):
        self.move(wall_rects)
        self.check_dot_collision(dot_rects)
        self.check_big_dot_collision(big_dot_rects)
        self.update()
        self.check_enemy_collision(enemies)

    def draw(self, display):
        draw_pixel_art(self.pattern, self.x, self.y, self.pixel_scale, display)