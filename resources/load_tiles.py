from pygame import image, Rect, Surface

'''pozycje elementow w pliki tiles.xpm
0,0 1,0 2,0 
0,1 1,1 2,1'''

TILE_POSIIONS = [
    ('#', 0, 0),  # wall
    ('o', 1, 0),  # crate
    (' ', 0, 1),  # floor
    ('x', 1, 1),  # exit
    ('.', 2, 0),  # dot
    ('*', 3, 0),  # player
]

SIZE = 32

'''------------------------------------------------------------------------------------------------------------------'''
def get_tile_rect(x,y):
    '''konwertuje indeks kfelka na obiekt pygame.Rect'''
    """Converts tile indices to a pygame.Rect"""
    return Rect(x * SIZE, y * SIZE, SIZE, SIZE)

def load_tiles(img_addr = 'images/tiles.xpm'):
    '''zwraca słownik prostokątów kafelków'''
    """Load tiles and returns a tuple of (image, tile_dict) """
    tile_image = image.load(img_addr)
    tiles = {}
    for symbol, x, y in TILE_POSIIONS:
        tiles[symbol] = get_tile_rect(x, y)
    return tile_image, tiles

'''------------------------------------------------------------------------------------------------------------------'''
if __name__ == "__main__":
    tile_img, tiles = load_tiles(img_addr = '../images/tiles.xpm')
    m = Surface((96, 32))
    print(tiles)
    m.blit(tile_img, get_tile_rect(0, 0), tiles['#'])
    m.blit(tile_img, get_tile_rect(1, 0), tiles[' '])
    m.blit(tile_img, get_tile_rect(2, 0), tiles['*'])
    image.save(m, 'tile_combo.png')