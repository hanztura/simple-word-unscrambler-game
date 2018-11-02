filename = str(input())
dictionary = []
with open(filename) as f:
    dictionary = f.read().split()

score = {"a": 1, "b": 3, "c": 3, "d": 2, "e": 1, "f": 4,
         "g": 2, "h": 4, "i": 1, "j": 8, "k": 5, "l": 1,
         "m": 3, "n": 1, "o": 1, "p": 3, "q": 10, "r": 1,
         "s": 1, "t": 1, "u": 1, "v": 4, "w": 4, "x": 8,
         "y": 4, "z": 10}

testcase = int(input())
for a in range(testcase):
    letter_string = str(input())
    sorted_letter_string = sorted(list(letter_string))
    unique_sorted_letter_string_count = []

    anagrams = ''
    for j in dictionary:
        sorted_letters = sorted(j)

        if sorted_letter_string == sorted_letters:
            anagrams += str(j)

        total_score = 0
        for letter in anagrams:
            total_score += score[letter]
        print(total_score)
