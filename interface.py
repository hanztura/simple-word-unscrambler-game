from random import shuffle

from common import (
    get_random_numbers, print_with_color, print_on_center, print_divider,
    get_terminal_width, print_on_left_and_right, filter_dictionary
)
from config import (
    DICTIONARY_FILENAME, GAME_MODES, NUMBER_OF_RETRIES, SCORING_MATRIX,
    NUMBER_OF_RANDOM_WORDS, APP_NAME
)
from engine import (
    seed_words, pick_words, combine_words, check_words, compute_word_score,
    search_anagrams, compute_score, search_sub_anagrams_of_words
)

# seed dictionary
dictionary = seed_words(DICTIONARY_FILENAME)
dictionary = filter_dictionary(dictionary, 3, 9)
dictionary_max_index = len(dictionary) - 1
terminal_width = get_terminal_width()


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


def winner(message='You are a winner.'):
    print_with_color('green', message, True)


def game_over(message='Game over :('):
    print_with_color('red', message, True)


def mode_retry():
    """
    Call this when the user selects the Retry Game mode.
    After the game is over, this function will return valid answers,
    and invalid answers wrapped as a dictionary data type.
    """
    is_continue = True
    is_game_over = True
    invalid_answers = []
    valid_answers = []
    raw_valid_answers = []
    raw_invalid_answers = []
    user_answer_counter = 0
    max_possible_score = 0

    # initializing game
    print_on_center('Initializing please wait...', terminal_width)

    # get a scrambled letter
    random_numbers = get_random_numbers(
        NUMBER_OF_RANDOM_WORDS,
        dictionary_max_index,
        True
    )
    random_words = pick_words(random_numbers, dictionary)
    scrambled_letters = combine_words(random_words)
    shuffled_scrambled_letters = list(scrambled_letters)
    shuffle(shuffled_scrambled_letters)
    shuffled_scrambled_letters = ''.join(shuffled_scrambled_letters)

    anagrams_of_random_words = search_sub_anagrams_of_words(
        random_words,
        dictionary
    )
    max_possible_score = compute_score(
        anagrams_of_random_words,
        SCORING_MATRIX
    )

    while is_continue:
        if user_answer_counter > 0:
            print_on_center('*' * int(terminal_width / 4), terminal_width)

        # present to player to the scrambled letter
        left_message = 'Create a valid word out of these letters: {}'.format(
            shuffled_scrambled_letters
        )
        right_message = 'Retries: {}/{}'.format(
            len(invalid_answers),
            NUMBER_OF_RETRIES
        )
        print_on_left_and_right(left_message, right_message, terminal_width)

        # print possible number valid words
        print('Number of possible valid answers: {}'.format(
            len(anagrams_of_random_words)
        ))

        # print valid answers, and scores
        valid_answers_in_words = [answer['user_answer'] for answer in valid_answers]
        current_score = compute_score(valid_answers_in_words, SCORING_MATRIX)
        left_message = 'Correct answers: {}'.format(str(valid_answers_in_words))
        right_message = 'Score: {}/{}'.format(
            current_score,
            max_possible_score
        )
        print_on_left_and_right(left_message, right_message, terminal_width)

        # print invalid answers
        invalid_answers_in_words = [answer['user_answer'] for answer in invalid_answers]
        invalid_answers_in_words = list(set(invalid_answers_in_words))
        message = 'Invalid answers: {}'.format(str(invalid_answers_in_words))
        print(message)

        user_answer_counter = user_answer_counter + 1
        # get user answer. blank is not allowed
        user_answer = input('Your answer {} >> '.format(user_answer_counter))
        while user_answer == '':
            user_answer = input('Blank answer is not allowed >> ')

        lowered_user_answer = user_answer.lower()

        # check if answer is valid
        string_for_checking_word = '{} {}'.format(
            scrambled_letters, lowered_user_answer
        )
        print(random_words)

        user_answer_is_existing_already = False

        if lowered_user_answer in raw_valid_answers:
            user_answer_valid = True
            user_answer_is_existing_already = True
        elif lowered_user_answer in raw_invalid_answers:
            user_answer_valid = False
            user_answer_is_existing_already = True
        else:
            user_answer_valid = check_words(
                string_for_checking_word, anagrams_of_random_words
            )

        # record answer
        data = {
            'scrambled_letters': scrambled_letters,
            'user_answer': user_answer
        }
        if user_answer_valid:
            if user_answer_is_existing_already:
                _message = 'Your correct answer "{}" is already counted.'.format(user_answer)
                print_with_color('blue', _message)
            else:
                _message = 'Your answer "{}" is correct.'.format(user_answer)
                valid_answers.append(data)
                print_with_color('green', _message)
            raw_valid_answers.append(lowered_user_answer)
        else:
            _message = 'Your answer "{}" is wrong.'.format(user_answer)
            print_with_color('red', _message)
            invalid_answers.append(data)
            raw_invalid_answers.append(lowered_user_answer)

        current_score = compute_score(raw_valid_answers, SCORING_MATRIX)

        # check if invalid answers is within limit
        invalid_count = len(invalid_answers)
        if invalid_count >= NUMBER_OF_RETRIES:
            is_continue = False
        else:
            if current_score >= max_possible_score:
                is_continue = False
                is_game_over = False
            else:
                is_continue = True

    if is_game_over:
        game_over()
    else:
        winner()

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
    is_game_over = True
    invalid_answers = []
    valid_answers = []
    raw_valid_answers = []
    raw_invalid_answers = []
    user_answer_counter = 0

    while is_continue:
            # filter dictionary
            filtered_dictionary = [word for word in dictionary if len(word) >= 3]
            filtered_dictionary_max_index = len(filtered_dictionary) - 1

            # loading
            if user_answer_counter == 0:
                _message = 'Fetching you an awesome word...'
            else:
                print_on_center('*' * int(terminal_width / 4), terminal_width)
                _message = 'Fetching you another awesome word...'
            print_on_center(
                _message, terminal_width
            )

            # get a scrambled letter
            random_numbers = get_random_numbers(
                1,
                filtered_dictionary_max_index,
                True
            )
            random_word = pick_words(random_numbers, filtered_dictionary)
            anagrams = search_anagrams(random_word, filtered_dictionary)  # str
            anagrams = anagrams.split()  
            while len(anagrams) < 3:
                random_numbers = get_random_numbers(
                    1,
                    filtered_dictionary_max_index,
                    True
                )
                random_word = pick_words(random_numbers, filtered_dictionary)
                anagrams = search_anagrams(random_word, filtered_dictionary)
                anagrams = anagrams.split()  # array

            anagrams.remove(random_word)
            anagrams_count = len(anagrams)  # array
            max_possible_score = compute_score(
                anagrams,
                SCORING_MATRIX
            )

            # get user answer. blank is not allowed
            for i in range(anagrams_count):
                print_on_center('*' * int(terminal_width / 4), terminal_width)
                # present the word to get anagrams
                left_message = 'Please find {} possible anagrams for the word: {}'.format(
                    anagrams_count,
                    random_word
                )
                right_message = 'Retries: {}/{}'.format(
                    len(invalid_answers),
                    NUMBER_OF_RETRIES
                )
                print_on_left_and_right(left_message, right_message, terminal_width)

                # print valid answers, and scores
                valid_answers_in_words = [answer['user_answer'] for answer in valid_answers]
                current_score = compute_score(valid_answers_in_words, SCORING_MATRIX)
                left_message = 'Correct answers: {}'.format(str(valid_answers_in_words))
                right_message = 'Score: {}/{}'.format(
                    current_score,
                    max_possible_score
                )
                print_on_left_and_right(left_message, right_message, terminal_width)

                # print invalid answers
                invalid_answers_in_words = [answer['user_answer'] for answer in invalid_answers]
                invalid_answers_in_words = list(set(invalid_answers_in_words))
                message = 'Invalid answers: {}'.format(str(invalid_answers_in_words))
                print(message)

                current_answer_number = i + 1
                input_string = 'Your answer number {} of {} >> '.format(
                    current_answer_number, anagrams_count
                )
                user_answer = input(input_string)
                lowered_user_answer = user_answer.lower()
                user_answer_is_existing_already = False
                # check if user answer is valid
                if lowered_user_answer in raw_valid_answers:
                    user_answer_valid = True
                    user_answer_is_existing_already = True

                while user_answer == '' or user_answer_is_existing_already:
                    if user_answer == '':
                        user_answer = input('Blank answer is not allowed >> ')
                    else:
                        user_answer = input('Try another guess >> ')

                    lowered_user_answer = user_answer.lower()
                    user_answer_is_existing_already = False

                    # check if user answer is valid
                    if lowered_user_answer in raw_valid_answers:
                        user_answer_valid = True
                        user_answer_is_existing_already = True

                user_answer_counter += 1

                if lowered_user_answer in raw_invalid_answers:
                    user_answer_valid = False
                    user_answer_is_existing_already = True
                if not user_answer_is_existing_already:
                    user_answer_valid = lowered_user_answer in anagrams


                # record answer
                data = {
                    'question': random_word,
                    'user_answer': user_answer
                }
                if user_answer_valid:
                    if user_answer_is_existing_already:
                        _message = 'Your correct answer "{}" is already counted.'.format(user_answer)
                        print_with_color('blue', _message)
                    else:
                        _message = 'Your answer "{}" is correct.'.format(user_answer)
                        print_with_color('green', _message)
                        valid_answers.append(data)
                    raw_valid_answers.append(lowered_user_answer)
                else:
                    _message = 'Your answer "{}" is wrong.'.format(user_answer)
                    print_with_color('red', _message)
                    invalid_answers.append(data)

                    if not user_answer_is_existing_already:
                        raw_invalid_answers.append(lowered_user_answer)

                # print valid answers, and scores
                valid_answers_in_words = [answer['user_answer'] for answer in valid_answers]
                current_score = compute_score(valid_answers_in_words, SCORING_MATRIX)

                # check if invalid answers is within limit
                invalid_count = len(invalid_answers)
                if invalid_count >= NUMBER_OF_RETRIES:
                    is_continue = False
                    break
                else:
                    if current_score >= max_possible_score:
                        is_continue = False
                        is_game_over = False
                    else:
                        is_continue = True

    if is_game_over:
        game_over()
    else:
        winner()

    return {
        'valid_answers': valid_answers,
        'invalid_answers': invalid_answers
    }


def greet():
    print_on_center(APP_NAME, terminal_width)
    print_divider(terminal_width)


def go():
    """
    This is the entry point of the game. This should be called to start
    the game.
    """
    greet()

    results = {}
    game_mode = ''
    game_mode_keys = GAME_MODES.keys()
    games_played = 0
    while game_mode != 'exit':
        game_mode = ''
        if games_played > 0:
            print_on_center('Having fun? Choose your next game mode.', terminal_width)
        while not GAME_MODES.has_value(game_mode):
            for mode in GAME_MODES:
                value = mode.value[0]
                title = mode.value[1]
                value_index = game_mode_keys.index(value)
                print('({}) {}'.format(value_index, title))
            try:
                game_mode = game_mode_keys[int(input(
                    'Select Game Mode by entering the number on the left>>> '
                ))]
            except Exception as e:
                print_divider(terminal_width)
                error_message = 'Please select a valid mode.'
                print(error_message)

        if game_mode == 'exit':
            print_divider(terminal_width)
            print('See you next time!')
        else:
            print_divider(terminal_width)
            message = 'Playing in: {}'.format(GAME_MODES.get_title(game_mode))
            print_on_center(message, terminal_width)
            # call game modes
            if game_mode == 'retry':
                results = mode_retry()

            elif game_mode == 'retry_anagram':
                results = mode_retry_anagram()

            games_played += 1
            print_divider(terminal_width)
            print_game_results(
                results['valid_answers'],
                results['invalid_answers']
            )
