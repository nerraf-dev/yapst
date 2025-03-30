import sys
from config import COLOUR

def print_error_exit(msg):
    """
    Prints an error message in red color and exits the program.
    """
    print(COLOUR["RED"], msg, COLOUR["ENDC"])
    sys.exit(1)
