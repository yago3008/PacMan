import pygame
from pacman import PacMan
from screen import manage_screen, DISPLAY_W, DISPLAY_H, SCREEN

pygame.init()

PACMAN_PLAYER = PacMan(DISPLAY_W, DISPLAY_H) 



def main():
    wall_rects, dot_rects, big_dot_rects = manage_screen(PACMAN_PLAYER, wall_rects=None, dot_rects=None, big_dot_rects=None, first_run=True)

    running = True
    while running and PACMAN_PLAYER.score < 230:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                running = False

        PACMAN_PLAYER.move(DISPLAY_W, DISPLAY_H, wall_rects)
        PACMAN_PLAYER.check_dot_collision(dot_rects)


        manage_screen(PACMAN_PLAYER, wall_rects, dot_rects, big_dot_rects)

    pygame.quit()

        
            
    pygame.quit()

if __name__ == '__main__':
    main()