from seeding_words import seeding_words

filename = str(input())
dictionary = []
with open(filename) as f:
    dictionary = f.read().split()

testcase = int(input())
for i in range(testcase):
    word_positions = input()
    array_word_positions = [int(word_positions) for word_positions in word_positions.split()]

    words = ''
    for j in range(len(array_word_positions)):
        if words != '':
            words += " " + str(dictionary[array_word_positions[j]])
        else:
            words += str(dictionary[array_word_positions[j]])

    print(words)
