import pygame, random, time

display_W = 800
display_H = 600


enemy_pattern = [
    "  7 1  1 7  ",
    "   11  11   ",
    " 1 161161 1 ",
    " 1 121121 1 ",
    " 1111111111 ",
    "   117711   ",
    "   11  11   ",
    "  1      1  "
]

pacman_pattern_rigth = [
    "  8888  ",
    " 888888 ",
    "88888888",
    "888888  ",
    "88888888",
    " 888888 ",
    "  8888 "
]

pacman__pattern_left = [
    "  888  ",
    " 88888 ",
    "8888888",
    "  88888",
    "8888888",
    " 88888 ",
    "  888  "
]

pacman_pattern_up = [
    "  8 8  ",
    " 88 88 ",
    "8888888",
    "8888888",
    "8888888",
    " 88888 ",
    "  888  ",
]   

pacman_pattern_down = [
    "  888  ",
    " 88888 ",
    "8888888",
    "8888888",
    "8888888",
    " 88 88 ",
    "  8 8  ",
]



def color(op):
    colors = {
        'white': (235, 235, 235),
        'yellow': (255, 255, 102),
        'dyellow': (214, 153, 0),
        'black': (0, 0, 0),
        'red': (255, 50, 50),
        'lred': (255, 107, 25),
        'dred': (198, 0, 0),
        'blue': (133, 209, 255),
        'dblue': (134, 199, 255),
        'dblue1': (135, 189, 255),
        'dblue2': (136, 179, 255),
        'dblue3': (134, 169, 255),
        'gray': (128, 128, 128),
        'dgray': (108, 108, 108),
        'dgray1': (98, 98, 98),
        'dgray2': (88, 88, 88),
        'dgray3': (87, 78, 88),
    }
    return colors.get(op)


def draw_pixel_art(pattern, x, y, ps, display):
    for row_index, row in enumerate(pattern):
        for col_index, pixel in enumerate(row):
            if pixel == '0':
                pygame.draw.rect(display, color('black'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '1':
                pygame.draw.rect(display, color('red'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '2':
                pygame.draw.rect(display, color('white'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '3':
                pygame.draw.rect(display, color('blue'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '6':
                pygame.draw.rect(display, color('dblue'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '4':
                pygame.draw.rect(display, color('gray'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '5':
                pygame.draw.rect(display, color('dgray'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '7':
                pygame.draw.rect(display, color('dred'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '8':
                pygame.draw.rect(display, color('yellow'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == '9':
                pygame.draw.rect(display, color('dyellow'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == 'a':
                pygame.draw.rect(display, color('dgray1'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == 'b':
                pygame.draw.rect(display, color('dgray2'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == 'c':
                pygame.draw.rect(display, color('dblue1'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == 'd':
                pygame.draw.rect(display, color('dblue2'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == 'e':
                pygame.draw.rect(display, color('dblue3'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == 'f':
                pygame.draw.rect(display, color('dgray3'), (x + col_index * ps, y + row_index * ps, ps, ps))
            if pixel == 'g':
                pygame.draw.rect(display, color('lred'), (x + col_index * ps, y + row_index * ps, ps, ps))