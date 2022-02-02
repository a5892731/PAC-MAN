
# Code for chapter 04 - Debugging with the Scientific Method

# The program prints the codes of pressed keys. 

from pygame.locals import KEYDOWN
import pygame

KEYS_DICT = {'ESC':27,
             'UP':1073741906, 'DOWN':1073741905, 'RIGHT':1073741903, 'LEFT':1073741904}


def event_loop(handle_key, delay=1):
    """Processes events and updates callbacks."""
    while True:
        pygame.event.pump()
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            handle_key(event.key)

            if event.key == KEYS_DICT['UP']:
                print('UP')
                #return 'UP'
            elif event.key == KEYS_DICT['DOWN']:
                print('DOWN')
                #return 'DOWN'
            elif event.key == KEYS_DICT['RIGHT']:
                print('RIGHT')
                #return 'RIGHT'
            elif event.key == KEYS_DICT['LEFT']:
                print('LEFT')
                #return 'LEFT'
            elif event.key == KEYS_DICT['ESC']:
                print('exit')
                break
            else:
                print("key number: " + str(event.key))

        pygame.time.delay(delay)


if __name__ == '__main__':
    print('press ESC for exit')
    pygame.init()
    pygame.display.set_mode((640, 400))
    event_loop(print)

