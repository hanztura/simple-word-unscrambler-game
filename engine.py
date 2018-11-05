from common import read_file, is_a_sub_anagram


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


def search_anagrams(word, dictionary):
    """
    The player may have an
    option to choose a game mode. For example, one mode could be to get
    all anagrams of a certain word by unscrambling a word. This means that
    for every word in the dictionary, the program must be able to find all the
    anagrams of the word.
    """
    sorted_array_word_string = (sorted(list(word)))
    dictionary = [word for word in dictionary if len(word) == len(word)]

    anagrams = ''
    for j in dictionary:
        sorted_letters = sorted(j)

        if sorted_array_word_string == sorted_letters:
            if anagrams != '':
                anagrams += " " + str(j)
            else:
                anagrams += str(j)

    return anagrams


def search_anagrams_of_words(words, dictionary):
    """
    Returns a list of unique words by getting the anagrams of each word in
    words.

    words is an array of words.
    dictionary is an array of words in the dictionary.
    """
    anagrams_of_words = []
    for word in words:
            anagrams = search_anagrams(word, dictionary)
            anagrams = anagrams.split()
            anagrams_of_words = anagrams_of_words + anagrams

    anagrams_of_words = list(set(anagrams_of_words))
    return anagrams_of_words


# def search_sub_anagrams_of_a_word_2(word, dictionary, limit=2):
#     """
#     Same with normal search of anagram but it includes all sub anagrams of a
#     word with a length at least of the limit.

#     Returns a space separated string of anagrams.
#     """
#     if len(word) <= limit:
#         return ''
#     else:
#         return search_anagrams(word, dictionary) + ' ' + search_sub_anagrams_of_a_word(
#             word[0:-1],
#             dictionary
#         )


def search_sub_anagrams_of_a_word(word, dictionary, limit=2):
    """
    Same with normal search of anagram but it includes all sub anagrams of a
    word with a length at least of the limit.

    Returns a space separated string of anagrams.
    """
    word_length = len(word)
    anagrams = ''
    if word_length <= limit:
        return ''
    else:
        # filter dictionary with length not more than its own length
        # sample great has length of 5 so dictionary words 6 and above not ignored
        dictionary = [d_word for d_word in dictionary if len(d_word) <= word_length]
        for d_word in dictionary:
            if is_a_sub_anagram(d_word, word):
                anagrams += ' '
                anagrams += d_word

    return anagrams


def search_sub_anagrams_of_words(words, dictionary):
    """
    Utitlity of sub anagram of word where it searches the sub anagrams of one
    or more words (list).

    Returns a list of sub anagrams.
    """
    anagrams = ''
    anagrams += ' ' + words
    combined_words = combine_words(words)
    anagrams = anagrams + ' ' + search_sub_anagrams_of_a_word(
        combined_words,
        dictionary
    )

    anagrams = anagrams.split()
    anagrams = list(set(anagrams))
    return anagrams


def combine_words(words):
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
    words_in_string = words.replace(' ', '')
    array_of_words = words.split()
    unique_letters = set(words_in_string)
    sorted_unique_letters = sorted(unique_letters)
    sorted_unique_letters_count = []

    # populate letters count
    for j in sorted_unique_letters:
        sorted_unique_letters_count.append(0)

    for word in array_of_words:
        for (i, letter) in enumerate(sorted_unique_letters):
            count = word.count(letter)
            current_max_count = sorted_unique_letters_count[i]

            if count > current_max_count:
                sorted_unique_letters_count[i] = count

    result = ''
    for (i, letter) in enumerate(sorted_unique_letters):
        string = sorted_unique_letters[i] * sorted_unique_letters_count[i]
        result = result + string

    return result


def check_words(user_input, dictionary):
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
    user_input_as_array = user_input.split()
    base_string = user_input_as_array[0]
    player_string = user_input_as_array[1]

    sorted_base_string = ''.join(sorted(base_string))
    sorted_player_string = ''.join(sorted(player_string))

    unique_sorted_base_string = sorted(set(base_string))
    unique_sorted_player_string = sorted(set(player_string))

    unique_sorted_base_string_count = []
    unique_sorted_player_string_count = []

    # populate letters count
    for j in unique_sorted_base_string:
        unique_sorted_base_string_count.append(0)

    # populate letters count
    for j in unique_sorted_player_string:
        unique_sorted_player_string_count.append(0)

    # count occurence
    for (i, letter) in enumerate(unique_sorted_base_string):
        count = base_string.count(letter)
        current_max_count = unique_sorted_base_string_count[i]

        if count > current_max_count:
            unique_sorted_base_string_count[i] = count

    # count occurence
    for (i, letter) in enumerate(unique_sorted_player_string):
        count = player_string.count(letter)
        current_max_count = unique_sorted_player_string_count[i]

        if count > current_max_count:
            unique_sorted_player_string_count[i] = count

    result1 = True
    result2 = False

    # result1
    for (i, letter) in enumerate(unique_sorted_player_string):
        base_count = 0
        player_string_count = unique_sorted_player_string_count[i]
        if letter in unique_sorted_base_string:
            base_string_index = unique_sorted_base_string.index(letter)
            base_count = unique_sorted_base_string_count[base_string_index]

            if base_count < player_string_count:
                result1 = False
                break
        else:
            result1 = False
            break

    # result2
    if player_string in dictionary:
        result2 = True

    return (result1 and result2)


def compute_word_score(word, scoring_matrix):
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
    total_score = 0
    for letter in word:
        score = scoring_matrix[letter]
        total_score = total_score + score

    return total_score


def compute_score(words, scoring_matrix):
    """
    Utility of compute word score where it computes the total score of a given
    list of words.
    """
    total_score = 0

    for word in words:
        score = compute_word_score(word, scoring_matrix)
        total_score = total_score + score

    return total_score
