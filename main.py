import pygame
from pacman import PacMan
from enemy import spawn_enemies
from screen import manage_screen, DISPLAY_W, DISPLAY_H, MIDDLE_X, MIDDLE_Y

pygame.init()

pacman = PacMan(DISPLAY_W, DISPLAY_H)
enemies = spawn_enemies(MIDDLE_X, MIDDLE_Y)


def update_enemies(wall_rects, enemies):
    for enemy in enemies:
        enemy.update(wall_rects, pacman.powerup)

def main():
    wall_rects, dot_rects, big_dot_rects = manage_screen(pacman, enemies, wall_rects=None, dot_rects=None, big_dot_rects=None, first_run=True)

    running = True
    while running and pacman.score < 250 and len(enemies) > 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                running = False

        update_enemies(wall_rects, enemies)

        pacman.call_funcs(DISPLAY_W, DISPLAY_H, wall_rects, dot_rects, big_dot_rects, enemies)
        manage_screen (pacman, enemies, wall_rects, dot_rects, big_dot_rects)

    pygame.quit()


if __name__ == '__main__':
    main()