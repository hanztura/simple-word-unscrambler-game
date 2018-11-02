filename = str(input())
dictionary = []
with open(filename) as f:
    dictionary = f.read().split()

testcase = int(input())
for i in range(testcase):
    word = str(input())
    sorted_array_word_string = (sorted(list(word)))

    anagrams = ''
    for j in dictionary:
        sorted_letters = sorted(j)

        if sorted_array_word_string == sorted_letters:
            if anagrams != '':
                anagrams += " " + str(j)
            else:
                anagrams += str(j)

    print(anagrams)
