import random

XMAX, YMAX = 19, 16


def create_grid_string(dots, xsize, ysize):
    """
    Creates a grid of size (xx, yy)
    with the given positions of dots.
    rest poles with #
    """
    grid = ""
    for y in range(ysize):
        for x in range(xsize):
            grid += "." if (x, y) in dots else "#"
        grid += "\n"
    return grid

def get_all_dot_positions(xsize, ysize):
    """Returns a list of (x, y) tuples covering all positions in a grid"""
    return [(x, y) for x in range(1, xsize - 1) for y in range(1, ysize - 1)]

def get_neighbors(x, y):
    """Returns a list with the 8 neighbor positions of (x, y)"""
    '''    return [
            (x, y-1), (x, y+1), (x-1, y), (x+1, y),
            (x-1, y-1), (x+1, y-1), (x-1, y+1), (x+1, y+1)
            ]
    '''
    return [
        (x-1, y+1), (x, y+1), (x+1, y+1),
        (x-1, y),             (x+1, y),
        (x-1, y-1), (x, y-1), (x+1, y-1),
        ] # better for visualization coordinates of neighbours

def generate_dot_positions(xsize, ysize):
    """Creates positions of dots for a random maze"""
    positions = get_all_dot_positions(xsize, ysize) # all dots without margin wall
    dots = set()
    while positions != []: # while not empty list
        x, y = random.choice(positions) # chose random point from list
        neighbors = get_neighbors(x, y) # get coordinates of all neighbour poles ( 8 ) of our point
        free = [nb in dots for nb in neighbors] # check that all 8 poles are taken
        if free.count(True) < 5: # if no more than 4 poles are taken then add a dot in this place
            dots.add((x, y))
        positions.remove((x, y)) # remove generated point from list
    return dots


def create_maze(xsize, ysize):
    """Returns a xsize*ysize maze as a string"""
    dots = generate_dot_positions(xsize, ysize)
    maze = create_grid_string(dots, xsize, ysize)
    return maze


'''------------------------------------------------------------------------------------------------------------------'''
if __name__ == '__main__':
    #dots = set(((1, 1), (1, 2), (1, 3), (2, 2), (3, 1), (3, 2), (3, 3)))  #(y, x)
    xsize = 17
    ysize = 7

    #print(dots)
    #print(create_grid_string(dots, xsize, ysize)) # dots x, y

    #positions = get_all_dot_positions(xsize, ysize)
    #print(create_grid_string(positions, xsize, ysize))

    #neighbors = get_neighbors(2, 2)
    #print(create_grid_string(neighbors, 5, 5))


    maze = create_maze(xsize, ysize)
    print(maze)
