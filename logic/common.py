def read_file(filename):
    with open(filename) as f:
        file = f.read()

    return file