from random import randint
from config import BCOLORS


def read_file(filename):
    """
    Read a given filename and returns it as a string.
    """
    with open(filename) as f:
        file = f.read()

    return file


def get_random_numbers(count, max_num, to_string=False):
    """
    Returns a random number(s).By default it returns the numbers in array
    but setting to_string into True with return it as space separated string.

    count determines the number of random numbers to be generated.
    max_num determines the maximum number allowed in generating random number.
    """
    random_numbers = []
    for i in range(count):
        random_number = randint(0, max_num)
        random_numbers.append(random_number)

    if to_string:
        # https://stackoverflow.com/questions/44778/how-would-you-make-a-comma-separated-string-from-a-list-of-strings
        random_numbers = ' '.join(map(str, random_numbers))

    return random_numbers


def print_with_color(color, message):
    """
    Print a message with a color.
    """
    colors = {
        'green': BCOLORS.OKGREEN,
        'blue': BCOLORS.OKBLUE,
        'orange': BCOLORS.WARNING,
        'red': BCOLORS.FAIL
    }
    if color in colors:
        color = colors[color]
    else:
        color = colors['blue']

    print('{}{}{}'.format(
        color,
        message,
        BCOLORS.ENDC
    ))
