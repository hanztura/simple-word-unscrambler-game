from common import read_file


def seed_words(filename):
    """
    When the program starts, it must get
    the words to be unscrambled from a dictionary that is external to the
    program. Given the file name of the dictionary, the program must be able
    to load its contents. Loading the dictionary must be performed only once
    during the run time of the program.
    """
    file = read_file(filename)
    words = file.split()
    return words


def pick_words(word_positions, dictionary):
    """
    For every round of the game, the program
    must pick a word/a set of words to be unscrambled from the dictionary.
    This leads you to the problem of retrieving a word from a dictionary given
    its position in the dictionary.
    """
    array_word_positions = [int(word_positions) for word_positions in word_positions.split()]

    words = ''
    for j in range(len(array_word_positions)):
        if words != '':
            words += " " + str(dictionary[array_word_positions[j]])
        else:
            words += str(dictionary[array_word_positions[j]])

    return words


def search_anagrams():
    """
    The player may have an
    option to choose a game mode. For example, one mode could be to get
    all anagrams of a certain word by unscrambling a word. This means that
    for every word in the dictionary, the program must be able to find all the
    anagrams of the word.
    """
    pass


def combine_words():
    """
    Another game mode could be to get
    all the words from a random sequence of characters, and not from a word.
    To ensure that at least one word can be generated from the random sequence
    of characters, the random sequence of characters must be generated
    from one or more words in the dictionary. Given a set of words, one
    approach to generate a random sequence of characters is by getting the
    shortest string containing the characters that are required to unscramble
    each word (for the sequence to be random, the words must be randomly
    picked by our program). The program must be able to generate the shortest
    string containing the characters that are required to unscramble a set
    of words.
    """
    pass


def check_words():
    """
     From the string of letters that the
    program generated, the player will get points by entering a word whose
    letters are found in the string. Note that the word may not be in the
    set of words that the program picked (along with their anagrams) when
    generating the string. This means that a player will only get points if the
    the word that he/she entered contains letters that are found in the string
    of letters AND the word is found in the dictionary. The program must be
    able to check the two conditions.
    """
    pass


def compute_word_score():
    """
    When a player unscrambles a word,
    the program must give points to the user. One way to compute scores is
    to give one point for every valid word unscrambled, where the total score
    is the total number of words. Another way is to compute the scrabble
    points of a word. In this approach, the total score is the sum of the scrabble
    points of all words.
    The program must be able to compute the scrabble points of all words.
    Moreover, given a string of letters, the program must be able to compute
    the highest score that can be achieved by unscrambling words from the
    string
    """
    pass
