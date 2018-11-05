import os
from collections import Counter
from random import randint

from config import BCOLORS


def get_terminal_width():
    width = os.get_terminal_size().columns
    return width


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


def print_with_color(color, message, center=False, width=0):
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

    formatted_message = '{}{}{}'.format(
        color,
        message,
        BCOLORS.ENDC
    )

    if center:
        if not width:
            width = get_terminal_width()

        formatted_message = formatted_message.center(width)

    print(formatted_message)


def print_divider(width, character='-'):
    divider = character * width
    print(divider)


def print_on_center(message, width):
    centered_message = message.center(width)
    print(centered_message)


def print_on_left_and_right(left_message, right_message, width):
    width_per_side = int(width / 2)
    left_message = '{message:{filler}<{n}}'.format(
        message=left_message,
        n=width_per_side,
        filler=''
    )
    right_message = '{message:{filler}>{n}}'.format(
        message=right_message,
        n=width_per_side,
        filler=''
    )
    print('{}{}'.format(left_message, right_message))


def filter_dictionary(dictionary, min_length, max_length):
    dictionary = [word for word in dictionary if len(word) >= min_length and len(word) <= max_length]
    return dictionary


def sort_letters(word, return_as_string=True):
    sorted_letters = sorted(word)
    if return_as_string:
        sorted_letters = ''.join(sorted_letters)
    return sorted_letters


def is_a_sub_anagram(word, base_word):
    # direct substring
    if word in base_word:
        return True

    word_letters_count = Counter(word)
    is_a_sub_anagram = True
    for i, (letter, count) in enumerate(word_letters_count.items()):
        if base_word.count(letter) < count:
            is_a_sub_anagram = False

    return is_a_sub_anagram
