from random import randint


def read_file(filename):
    with open(filename) as f:
        file = f.read()

    return file


def get_random_numbers(count, max_num, to_string=False):
    random_numbers = []
    for i in range(count):
        random_number = randint(0, max_num)
        random_numbers.append(random_number)

    if to_string:
        # https://stackoverflow.com/questions/44778/how-would-you-make-a-comma-separated-string-from-a-list-of-strings
        random_numbers = ' '.join(map(str, random_numbers))

    return random_numbers
