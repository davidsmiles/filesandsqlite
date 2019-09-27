def save_to_file(contents, filename):
    with open(filename, 'w') as file:
        file.write(contents)


def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()


if __name__ == "__main__":
    print(read_file('data.txt'))