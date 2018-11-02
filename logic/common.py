def read_file(filename):
    with open(filename) as f:
        file = f.read()

    return file


def pick_words(word_positions, dictionary):
    array_word_positions = [int(word_positions) for word_positions in word_positions.split()]

    words = ''
    for j in range(len(array_word_positions)):
        if words != '':
            words += " " + str(dictionary[array_word_positions[j]])
        else:
            words += str(dictionary[array_word_positions[j]])

    return words


def search_anagrams(word, dictionary):
    sorted_array_word_string = (sorted(list(word)))

    anagrams = ''
    for j in dictionary:
        sorted_letters = sorted(j)

        if sorted_array_word_string == sorted_letters:
            if anagrams != '':
                anagrams += " " + str(j)
            else:
                anagrams += str(j)

    return anagrams


def combine_words(words):
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
