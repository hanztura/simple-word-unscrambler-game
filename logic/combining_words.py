from common import combine_words

filename = str(input())
t = int(input())
for a in range(t):
    words = str(input())
    combined_words = combine_words(words)

    print(combined_words)
