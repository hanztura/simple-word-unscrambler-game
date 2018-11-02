from config import (
    DICTIONARY_FILENAME, GAME_MODES, NUMBER_OF_RETRIES, SCORING_MATRIX
)
from engine import (
    seed_words, pick_words, combine_words, check_words, compute_word_score
)

# seed dictionary
dictionary = seed_words(DICTIONARY_FILENAME)

game_mode = ''
game_mode_keys = GAME_MODES.keys()
while not GAME_MODES.has_value(game_mode):
    print('Select Game Mode by entering the number on the left:')
    for mode in GAME_MODES:
        value = mode.value[0]
        title = mode.value[1]
        value_index = game_mode_keys.index(value)
        print('({}) {}'.format(value_index, title))
    try:
        game_mode = game_mode_keys[int(input())]
    except Exception as e:
        print('=====')
        error_message = 'Please select a valid mode.'
        print(error_message)

is_continue = True

if game_mode == 'exit':
    print('See you next time!')
else:
    print('Playing in mode: {}'.format(GAME_MODES.get_title(game_mode)))
    invalid_answers = []
    valid_answers = []
    while is_continue:
        if game_mode == 'retry':
            # get a scrambled letter
            random_words = pick_words('14 30', dictionary)
            scrambled_letters = combine_words(random_words)

            # present to player to the scrambled letter
            print('Create a valid word out of these letters: {}'.format(
                scrambled_letters)
            )

            # get user answer. blank is not allowed
            user_answer = input('Your answer >> ').lower()
            while user_answer == '':
                user_answer = input('Blank answer is not allowed >> ').lower()

            # check if answer is valid
            string_for_checking_word = '{} {}'.format(
                scrambled_letters, user_answer
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
                valid_answers.append(data)
            else:
                invalid_answers.append(data)

            # check if invalid answers is within limit
            invalid_count = len(invalid_answers)
            if invalid_count >= NUMBER_OF_RETRIES:
                is_continue = False
            else:
                is_continue = True

        else:
            is_continue = False

    # on game over, print results
    total_score = 0
    for answer_data in valid_answers:
        user_answer = answer_data['user_answer']
        score = compute_word_score(user_answer, SCORING_MATRIX)
        total_score = total_score + score

    print(total_score)
