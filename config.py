# configurations of the game
from enum import Enum

DICTIONARY_FILENAME = 'dictionary.txt'
NUMBER_OF_RETRIES = 5
NUMBER_OF_RANDOM_WORDS = 3
SCORING_MATRIX = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4,
                  "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
                  "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
                  "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
                  "y": 4, "z": 10}


class GAME_MODES(Enum):
    retry = ('retry', 'Try and Try until you die.')
    retry_anagram = (
        'retry_anagram',
        'Try and Try until you die AGAIN.'
    )
    timed = ('timed', 'Time is Gold.')
    exit = ('exit', 'I dont want to play games right now.')

    @classmethod
    def get_value(cls, member):
        return cls[member].value[0]

    @classmethod
    def get_title(cls, member):
        return cls[member].value[1]

    @classmethod
    def has_value(cls, value):
        return any(value == mode.value[0] for mode in cls)

    @classmethod
    def keys(cls):
        return [mode.value[0] for mode in cls]


# https://stackoverflow.com/questions/287871/print-in-terminal-with-colors
class BCOLORS:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
