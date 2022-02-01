# author: a5892731
# date: 31.01.2022
# last update:
#
# description:
# this is a simple game named "maze runner" or "PACK-MAN"
#
# source:
# book: "Python dla profesjonalistów" by Kristian Rother
# https://github.com/krother/maze_run


from pygame import image, Surface
from resources.load_tiles import load_tiles, get_tile_rect, SIZE
from resources.generate_maze import create_maze
from resources.draw_maze import parse_grid, draw_grid
from resources.moves import move
from resources.maze_run import event_loop, handle_key


import random
from pygame import Rect
import pygame

LEFT = (-1, 0)
RIGHT = (1, 0)
UP = (0, -1)
DOWN = (0, 1)

DIRECTIONS = {
    276: LEFT, 275: RIGHT,
    273: UP, 274: DOWN
}


'''------------------------------------------------------------------------------------------------------------------'''
if __name__ == "__main__":

    # initialize display
    xsize = 12
    ysize = 7
    pygame.init()
    pygame.display.set_mode((800, 600))
    display = pygame.display.get_surface()

    # prepare the maze
    maze = parse_grid(create_maze(12, 7))
    maze[1][1] = '*'
    maze[ysize-2][xsize-2]  = 'x'

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
        274: DOWN
    }

    # loop
    event_loop(handle_key)