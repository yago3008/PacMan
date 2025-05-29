import pygame

DISPLAY_W = 800
DISPLAY_H = 600
SCREEN = pygame.display.set_mode((DISPLAY_W, DISPLAY_H))
CLOCK = pygame.time.Clock()
FPS = 60
pygame.display.set_caption("Forti-Pac")


pacman_map = [
        "############################",
        "#*...........##...........*#",
        "#.####.#####.##.#####.####.#",
        "#.#  #.#   #.##.#   #.#  #.#",
        "#.####.#####.##.#####.####.#",
        "#..........................#",
        "#.####.##.########.##.####.#",
        "#......##....##....##......#",
        "######.##### ## #####.######",
        "     #.##### ## #####.#     ",
        "     #.##          ##.#     ",
        "     #.## ###--### ##.#     ",
        "######.## #      # ##.######",
        "#......   #      #   ......#",
        "######.## #      # ##.######",
        "     #.## ######## ##.#     ",
        "     #.##          ##.#     ",
        "     #.## ######## ##.#     ",
        "######.## ######## ##.######",
        "#............##............#",
        "#.####.#####.##.#####.####.#",
        "#...##................##...#",
        "###.##.##.########.##.##.###",
        "#......##....##....##......#",
        "#.##########.##.##########.#",
        "#*........................*#",
        "############################"
    ]

def manage_screen(pacman_player, enemy,  wall_rects=None, dot_rects=None, big_dot_rects=None, first_run=False):
    SCREEN.fill((0, 0, 0))

    tile_width = DISPLAY_W // len(pacman_map[0]) + 1
    tile_height = DISPLAY_H // len(pacman_map)

    collision_margin = 8
    visual_margin = 4

    def create_wall_rect(x, y):
        return pygame.Rect(
            x + collision_margin,
            y + collision_margin,
            tile_width - 2 * collision_margin,
            tile_height - 2 * collision_margin
        )

    def create_dot_rect(x, y):
        center = (x + tile_width // 2, y + tile_height // 2)
        dot_radius = min(tile_width, tile_height) // 5
        return pygame.Rect(center[0] - dot_radius, center[1] - dot_radius, dot_radius * 2, dot_radius * 2)

    def create_big_dot_rect(x, y):
        center = (x + tile_width // 2, y + tile_height // 2)
        radius = min(tile_width, tile_height) // 3
        return pygame.Rect(center[0] - radius, center[1] - radius, radius * 2, radius * 2)

  

    if first_run:
        wall_rects = []
        dot_rects = []
        big_dot_rects = []

        for row_idx, row in enumerate(pacman_map):
            for col_idx, tile in enumerate(row):
                x = col_idx * tile_width
                y = row_idx * tile_height

                if tile == "#":
                    wall_rects.append(create_wall_rect(x, y))
                elif tile == ".":
                    dot_rects.append(create_dot_rect(x, y))
                elif tile == "*":
                    big_dot_rects.append(create_big_dot_rect(x, y))

    def draw_walls():
        for rect in wall_rects:
            visual_rect = pygame.Rect(
                rect.x - (collision_margin - visual_margin),
                rect.y - (collision_margin - visual_margin),
                rect.width + 2 * (collision_margin - visual_margin),
                rect.height + 2 * (collision_margin - visual_margin)
            )
            pygame.draw.rect(SCREEN, (0, 0, 255), visual_rect)

    def draw_dots():
        for dot in dot_rects:
            center = dot.center
            radius = dot.width // 2
            pygame.draw.circle(SCREEN, (255, 255, 255), center, radius)
            
    def draw_big_dot_at(rect):
        pygame.draw.circle(SCREEN, (255, 255, 255), rect.center, rect.width // 2)


    draw_walls()
    draw_dots()
    for rect in big_dot_rects:
        draw_big_dot_at(rect)


    pacman_player.draw(SCREEN)
    enemy.draw(SCREEN)
    
    pygame.display.flip()
    CLOCK.tick(FPS)

    return wall_rects, dot_rects, big_dot_rects



