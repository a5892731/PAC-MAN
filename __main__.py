# author: a5892731
# date: 31.01.2022
# last update: 02.02.2022
# version: 1.0.0
#
# description:
# this is a simple game named "maze runner" or "PACK-MAN"
#
# source:
# book: "Python dla profesjonalistów" by Kristian Rother
# https://github.com/krother/maze_run



from resources.load_tiles import load_tiles
from resources.generate_maze import create_maze
from resources.event_loop import event_loop
from resources.draw_maze import draw_grid, parse_grid
from resources.moves import move, LEFT, RIGHT, UP, DOWN
from pygame import Rect
import pygame


# initialize display
pygame.init()
pygame.display.set_mode((800, 600))
display = pygame.display.get_surface()

# prepare the maze
maze = parse_grid(create_maze(12, 7))
maze[1][1] = '*'
maze[5][10] = 'x'

# draw the graphics
tile_img, tiles = load_tiles()
img = draw_grid(maze, tile_img, tiles)
display.blit(img, Rect((0, 0, 384, 224)), Rect((0, 0, 384, 224)))
pygame.display.update()

# start the game
DIRECTIONS = {
    276: LEFT,
    275: RIGHT,
    273: UP,
    274: DOWN,
    1073741904: LEFT,
    1073741903: RIGHT,
    1073741906: UP,
    1073741905: DOWN,
}


def handle_key(key):
    """Handles key events in the game"""
    direction = DIRECTIONS.get(key)
    if direction:
        move(maze, direction)
    img = draw_grid(maze, tile_img, tiles)
    display.blit(img, Rect((0, 0, 384, 224)), Rect((0, 0, 384, 224)))
    pygame.display.update()


if __name__ == '__main__':
    action = event_loop(handle_key)
