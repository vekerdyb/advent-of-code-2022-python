def get_part_1(filename):
    with open(filename, "r") as f:
        message = f.readline()
    for index in range(4, len(message)):
        if len(set(message[index - 4:index])) == 4:
            return index


def get_part_2(filename):
    with open(filename, "r") as f:
        message = f.readline()
    for index in range(14, len(message)):
        if len(set(message[index - 14:index])) == 14:
            return index


if __name__ == "__main__":
    print(get_part_1("./input.txt"))
    print(get_part_2("./input.txt"))
