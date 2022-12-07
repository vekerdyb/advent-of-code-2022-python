from collections import defaultdict


def get_part_1(filename):
    sizes = parse_lines(get_lines(filename))
    return sum([size for size in sizes.values() if size <= 100000])


def get_part_2(filename):
    total = 70000000
    need_unused = 30000000
    sizes = parse_lines(get_lines(filename))
    current_unused = total - sizes['/']
    need_to_delete_at_least = need_unused - current_unused
    return [size for size in sorted(sizes.values()) if size >= need_to_delete_at_least][0]


def recursive_default_dict():
    return defaultdict(recursive_default_dict)


def parse_lines(lines):
    # stores the total size for each path
    sizes = defaultdict(lambda: 0)
    path = []

    for line in lines:
        if line.startswith("$"):
            command, *args = line[2:].split(" ")
            if command == "cd":
                directory = args[0]
                if directory == "..":
                    path.pop()
                else:
                    path.append(directory)
        elif line.startswith("dir"):
            pass
        else:
            size, name = line.split(" ")
            for index in range(len(path)):
                subpath = "/" + "/".join(path[1:len(path)-index])
                sizes[subpath] += int(size)
    return sizes


def get_lines(filename):
    with open(filename, "r") as f:
        return [line.strip("\n") for line in f.readlines()]


def test():
    part_1_result = get_part_1("./sample.txt")
    expected_1 = 95437
    assert (
            part_1_result == expected_1
    ), f"Test error part 1: {part_1_result} != {expected_1}"

    part_2_result = get_part_2("./sample.txt")
    expected_2 = 24933642
    assert (
            part_2_result == expected_2
    ), f"Test error part 2: {part_2_result} != {expected_2}"


if __name__ == "__main__":
    test()
    print(get_part_1("./input.txt"))
    print(get_part_2("./input.txt"))
