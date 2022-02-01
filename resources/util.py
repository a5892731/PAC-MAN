
from pprint import pprint
import sys

DEBUG = '-d' in sys.argv
#DEBUG = True
'''
-d
Turn on parser debugging output (for expert only, depending on compilation options). See also PYTHONDEBUG.

PYTHONDEBUG
If this is set to a non-empty string it is equivalent to specifying the -d option. If set to an integer, 
it is equivalent to specifying -d multiple times.

'''
def debug_print(*args, **kwargs):
    condition = kwargs.get('condition', True)
    if DEBUG and condition:
        for a in args:
            pprint(a)
