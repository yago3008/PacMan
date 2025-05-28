import pygame
from pacman import PacMan
from enemy import Enemy
from screen import manage_screen, DISPLAY_W, DISPLAY_H, SCREEN

pygame.init()

pacman = PacMan(DISPLAY_W, DISPLAY_H)
enemy = Enemy(x=100, y=100)

def main():
    wall_rects, dot_rects, big_dot_rects = manage_screen(pacman, wall_rects=None, dot_rects=None, big_dot_rects=None, first_run=True)

    running = True
    while running and pacman.score < 230:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                running = False

        pacman.move(DISPLAY_W, DISPLAY_H, wall_rects)
        pacman.check_dot_collision(dot_rects)
        pacman.check_big_dot_collision(big_dot_rects)
        pacman.update()

        enemy.update(wall_rects, pacman.powerup)
        enemy.draw()

        manage_screen (pacman, wall_rects, dot_rects, big_dot_rects)

    pygame.quit()


if __name__ == '__main__':
    main()