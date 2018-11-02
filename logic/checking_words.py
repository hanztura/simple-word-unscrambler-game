from common import read_file, check_words

filename = str(input())
dictionary = []

file = read_file(filename)
dictionary = file.split()

t = int(input())
for a in range(t):
    user_input = str(input())
    result = check_words(user_input, dictionary)
    print(result)
