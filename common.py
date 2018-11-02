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
