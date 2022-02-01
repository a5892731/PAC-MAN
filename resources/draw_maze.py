
# Code for chapter 05 - Debugging with print

from pygame import image, Surface
from resources.load_tiles import load_tiles, get_tile_rect, SIZE
from resources.generate_maze import create_maze
from resources.util import debug_print


def parse_grid(data):
    """Parses the string representation into a nested list"""
    return [list(row) for row in data.strip().split("\n")]


def draw_grid(data, tile_img, tiles):
    """Returns an image of a tile-based grid"""
    debug_print("drawing level", data)
    xsize = len(data[0]) * SIZE
    ysize = len(data) * SIZE
    img = Surface((xsize, ysize))
    for y, row in enumerate(data):
        for x, char in enumerate(row):
            rect = get_tile_rect(x, y)
            img.blit(tile_img, rect, tiles[char])
    return img


if __name__ == '__main__':
    tile_img, tiles = load_tiles(img_addr = '../images/tiles.xpm')
    level = create_maze(12, 7)
    print(level)
    level = parse_grid(level)
    print(level)
    maze = draw_grid(level, tile_img, tiles)
    image.save(maze, 'maze.png')
