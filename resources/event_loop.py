
# Code for chapter 04 - Debugging with the Scientific Method

# The program prints the codes of pressed keys. 

from pygame.locals import KEYDOWN
import pygame




def event_loop(handle_key, delay=1):
    """Processes events and updates callbacks."""
    while True:
        pygame.event.pump()
        event = pygame.event.poll()
        if event.type == KEYDOWN:
            handle_key(event.key)

        pygame.time.delay(delay)


if __name__ == '__main__':
    print('press ESC for exit')
    pygame.init()
    pygame.display.set_mode((640, 400))
    event_loop(print)

