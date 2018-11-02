from common import read_file, check_words, search_anagrams, compute_word_score

filename = str(input())
dictionary = []

file = read_file(filename)
dictionary = file.split()

scoring_matrix = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4,
                  "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
                  "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
                  "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
                  "y": 4, "z": 10}

testcase = int(input())
for a in range(testcase):
    letter_string = str(input())
    sorted_letter_string = sorted(list(letter_string))
    anagrams = []
    total_score = 0

    # loop every word in dictionary and check if word is valid with test case
    for word in dictionary:
        word_for_check_words = '{} {}'.format(letter_string, word)
        word_is_valid = check_words(word_for_check_words, dictionary)
        word_anagrams = []

        # get anagrams of the valid word
        if word_is_valid:
            word_anagrams = search_anagrams(word, dictionary).split()

        anagrams = anagrams + word_anagrams

    # make sure no duplicates
    anagrams = set(anagrams)

    # compute score of every word
    for word in anagrams:
        score = compute_word_score(word, scoring_matrix)
        total_score = total_score + score

    print(total_score)
