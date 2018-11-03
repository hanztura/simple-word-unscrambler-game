from common import get_random_numbers, print_with_color
from config import (
    DICTIONARY_FILENAME, GAME_MODES, NUMBER_OF_RETRIES, SCORING_MATRIX,
    NUMBER_OF_RANDOM_WORDS
)
from engine import (
    seed_words, pick_words, combine_words, check_words, compute_word_score,
    search_anagrams
)

# seed dictionary
dictionary = seed_words(DICTIONARY_FILENAME)
dictionary_max_index = len(dictionary) - 1


def print_game_results(valid_answers, invalid_answers):
    """
    Print game results. Both valid_answers and invalid answers are
    presumed to be in list data type.
    """
    # on game over, print results
    total_score = 0
    for answer_data in valid_answers:
        user_answer = answer_data['user_answer']
        score = compute_word_score(user_answer, SCORING_MATRIX)
        total_score = total_score + score

    print('Total Score: {}'.format(total_score))


def mode_retry():
    """
    Call this when the user selects the Retry Game mode.
    After the game is over, this function will return valid answers,
    and invalid answers wrapped as a dictionary data type.
    """
    is_continue = True
    invalid_answers = []
    valid_answers = []
    while is_continue:
            # get a scrambled letter
            random_numbers = get_random_numbers(
                NUMBER_OF_RANDOM_WORDS,
                dictionary_max_index,
                True
            )
            random_words = pick_words(random_numbers, dictionary)
            scrambled_letters = combine_words(random_words)

            # present to player to the scrambled letter
            print('Create a valid word out of these letters: {}'.format(
                scrambled_letters)
            )

            # get user answer. blank is not allowed
            user_answer = input('Your answer >> ')
            while user_answer == '':
                user_answer = input('Blank answer is not allowed >> ')

            # check if answer is valid
            string_for_checking_word = '{} {}'.format(
                scrambled_letters, user_answer.lower()
            )
            user_answer_valid = check_words(
                string_for_checking_word, dictionary
            )

            # record answer
            data = {
                'scrambled_letters': scrambled_letters,
                'user_answer': user_answer
            }
            if user_answer_valid:
                _message = 'Your answer "{}" is correct.'.format(user_answer)
                print_with_color('green', _message)
                valid_answers.append(data)
            else:
                _message = 'Your answer "{}" is wrong.'.format(user_answer)
                print_with_color('red', _message)
                invalid_answers.append(data)

            # check if invalid answers is within limit
            invalid_count = len(invalid_answers)
            if invalid_count >= NUMBER_OF_RETRIES:
                is_continue = False
            else:
                is_continue = True

    return {
        'valid_answers': valid_answers,
        'invalid_answers': invalid_answers
    }


def mode_retry_anagram():
    """
    Call this when the user selects the Retry Anagram Game mode.
    After the game is over, this function will return valid answers,
    and invalid answers wrapped as a dictionary data type.

    This mode will let user get all possible anagrams of the word.
    For example, the word 'cat' will have the following anagrams:
    cat, act
    """
    is_continue = True
    invalid_answers = []
    valid_answers = []
    while is_continue:
            # filter dictionary
            filtered_dictionary = [word for word in dictionary if (len(word) >= 4 and len(word) <= 6)]
            filtered_dictionary_max_index = len(filtered_dictionary) - 1

            # get a scrambled letter
            random_numbers = get_random_numbers(
                1,
                filtered_dictionary_max_index,
                True
            )
            random_word = pick_words(random_numbers, filtered_dictionary)
            anagrams = search_anagrams(random_word, filtered_dictionary)  # str
            anagrams = anagrams.split()  # array
            while len(anagrams) < 4:
                random_numbers = get_random_numbers(
                    1,
                    filtered_dictionary_max_index,
                    True
                )
                random_word = pick_words(random_numbers, filtered_dictionary)
                anagrams = search_anagrams(random_word, filtered_dictionary)
                anagrams = anagrams.split()  # array

            anagrams.remove(random_word)
            anagrams_count = len(anagrams)

            # present the word to get anagrams
            print('Please find {} possible anagrams for the word: {}'.format(
                anagrams_count,
                random_word
            ))

            # get user answer. blank is not allowed
            for i in range(anagrams_count):
                current_answer_number = i + 1
                input_string = 'Your answer number {} of {} >> '.format(
                    current_answer_number, anagrams_count
                )
                user_answer = input(input_string)
                while user_answer == '':
                    user_answer = input('Blank answer is not allowed >> ')
                    user_answer = user_answer

                # check if user answer is valid
                user_answer_valid = user_answer.lower() in anagrams

                # record answer
                data = {
                    'question': random_word,
                    'user_answer': user_answer
                }
                if user_answer_valid:
                    _message = 'Your answer "{}" is correct.'.format(user_answer)
                    print_with_color('green', _message)
                    valid_answers.append(data)
                else:
                    _message = 'Your answer "{}" is wrong.'.format(user_answer)
                    print_with_color('red', _message)
                    invalid_answers.append(data)

                # check if invalid answers is within limit
                invalid_count = len(invalid_answers)
                if invalid_count >= NUMBER_OF_RETRIES:
                    is_continue = False
                    break
                else:
                    is_continue = True

    return {
        'valid_answers': valid_answers,
        'invalid_answers': invalid_answers
    }


def go():
    """
    This is the entry point of the game. This should be called to start
    the game.
    """
    results = {}
    game_mode = ''
    game_mode_keys = GAME_MODES.keys()
    while not GAME_MODES.has_value(game_mode):
        for mode in GAME_MODES:
            value = mode.value[0]
            title = mode.value[1]
            value_index = game_mode_keys.index(value)
            print('({}) {}'.format(value_index, title))
        try:
            game_mode = game_mode_keys[int(input('Select Game Mode by entering the number on the left>>> '))]
        except Exception as e:
            print('=====')
            error_message = 'Please select a valid mode.'
            print(error_message)

    if game_mode == 'exit':
        print('See you next time!')
    else:
        print('Playing in mode: {}'.format(GAME_MODES.get_title(game_mode)))
        # call game modes
        if game_mode == 'retry':
            results = mode_retry()

        elif game_mode == 'retry_anagram':
            results = mode_retry_anagram()

        valid_answers = results['valid_answers']
        invalid_answers = results['invalid_answers']
        print_game_results(valid_answers, invalid_answers)
