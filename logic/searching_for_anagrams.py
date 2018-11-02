from common import read_file, search_anagrams

filename = str(input())
dictionary = []

file = read_file(filename)
dictionary = file.split()

testcase = int(input())
for i in range(testcase):
    word = str(input())
    anagrams = search_anagrams(word, dictionary)
    print(anagrams)
