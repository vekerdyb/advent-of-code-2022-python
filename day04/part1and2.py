def is_some_overlap(first, second):
    first_from, first_to = map(int, first.split("-"))
    second_from, second_to = map(int, second.split("-"))
    return (first_from <= second_from <= first_to) or (second_from <= first_from <= second_to)


def is_full_overlap(first, second):
    first_from, first_to = map(int, first.split("-"))
    second_from, second_to = map(int, second.split("-"))
    return (first_from <= second_from and first_to >= second_to) or (
            first_from >= second_from and first_to <= second_to
    )


def overlap_count(lines, method):
    return len([line for line in lines if method(*line.split(","))])


def full_overlap_count(lines):
    return overlap_count(lines, is_full_overlap)


def some_overlap_count(lines):
    return overlap_count(lines, is_some_overlap)


def get_part_1_score(filename):
    return full_overlap_count(get_lines(filename))


def get_part_2_score(filename):
    return some_overlap_count(get_lines(filename))


def get_lines(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]


def test():
    score_1 = get_part_1_score("./sample.txt")
    expected_1 = 2
    score_2 = get_part_2_score("./sample.txt")
    expected_2 = 4
    assert score_1 == expected_1, f"Test error part 1: {score_1} != {expected_1}"
    assert score_2 == expected_2, f"Test error part 2: {score_2} != {expected_2}"


if __name__ == "__main__":
    test()
    print(get_part_1_score("./input.txt"))
    print(get_part_2_score("./input.txt"))
