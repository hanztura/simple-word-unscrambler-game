from common import read_file, pick_words

filename = str(input())
dictionary = []

file = read_file(filename)
dictionary = file.split()

testcase = int(input())
for i in range(testcase):
    word_positions = input()
    words = pick_words(word_positions, dictionary)

    print(words)
