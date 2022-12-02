def get_part_1_sample_score() -> int:
    return get_part_1_score('./sample.txt')


def get_part_1_score(filename: str) -> int:
    with open(filename, "r") as f:
        return sum([get_part_1_score_for_round(line.strip()) for line in f.readlines()])


def get_part_1_score_for_round(line: str) -> int:
    return ord(line[2]) - 87 + get_part_1_outcome_score(line[0], line[2])


def get_part_1_outcome_score(opponents_shape: str, my_shape: str) -> int:
    return get_score_from_diff((ord(opponents_shape) - 65) - (ord(my_shape) - 88))


def get_score_from_diff(diff: int) -> int:
    if diff == 0:
        return 3
    if diff in [-1, 2]:
        return 6
    return 0


def get_part_2_sample_score() -> int:
    return get_part_2_score('./sample.txt')


def get_part_2_score(filename: str) -> int:
    with open(filename, "r") as f:
        return sum([get_part_2_score_for_round(line.strip()) for line in f.readlines()])


def get_part_2_score_for_round(line: str) -> int:
    my_number = get_part_2_shape_to_play(opponents_shape=line[0], expected_outcome=line[2])
    return my_number + (ord(line[2]) - 88) * 3


def get_part_2_shape_to_play(opponents_shape: str, expected_outcome: str) -> int:
    opponents_number = ord(opponents_shape) - 64
    if expected_outcome == "Y":
        return opponents_number
    if expected_outcome == "X":
        return opponents_number - 1 if opponents_number > 1 else 3
    return opponents_number + 1 if opponents_number != 3 else 1


def test():
    assert get_part_1_sample_score() == 15
    assert get_part_2_sample_score() == 12


if __name__ == "__main__":
    test()
    print(get_part_1_score('./input.txt'))
    print(get_part_2_score('./input.txt'))
