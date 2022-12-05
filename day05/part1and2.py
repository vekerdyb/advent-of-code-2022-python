from collections import defaultdict


def parse_lines(lines):
    crates = defaultdict(lambda: [])
    moves = []
    state = "c"
    for line in lines:
        if state == "c":
            for index, letter in enumerate(line):
                if letter.isalpha():
                    crate_number = ((index - 1) // 4) + 1
                    crates[crate_number] = [letter] + crates[crate_number]
        if state == "m":
            _, crates_to_move, _, from_stack, _, to_stack = line.split(" ")
            moves.append([int(item) for item in [crates_to_move, from_stack, to_stack]])
        if line == "":
            state = "m"
    return crates, moves


def execute_move(move, crates):
    if not move:
        return move, crates
    crates_to_move, from_stack, to_stack = move
    crate = crates[from_stack].pop()
    crates[to_stack].append(crate)
    if crates_to_move == 1:
        return [], crates
    return execute_move([crates_to_move - 1, from_stack, to_stack], crates)


def execute_move_2(move, crates):
    crates_to_move, from_stack, to_stack = move
    index_take_from = len(crates[from_stack]) - crates_to_move
    crates_moving = crates[from_stack][index_take_from:]
    crates[to_stack] += crates_moving
    crates[from_stack] = crates[from_stack][:index_take_from]
    return crates


def move_crates(crates, moves):
    for move in moves:
        _, crates = execute_move(move, crates)
    return crates


def move_crates_2(crates, moves):
    for move in moves:
        crates = execute_move_2(move, crates)
    return crates


def get_top_crates(crates):
    return "".join(
        [
            crates[index].pop() if len(crates[index]) else "0"
            for index in range(1, len(crates) + 1)
        ]
    )


def get_part_1(filename):
    lines = get_lines(filename)
    crates = move_crates(*parse_lines(lines))
    return get_top_crates(crates)


def get_part_2(filename):
    lines = get_lines(filename)
    crates = move_crates_2(*parse_lines(lines))
    return get_top_crates(crates)


def get_lines(filename):
    with open(filename, "r") as f:
        return [line.strip("\n") for line in f.readlines()]


def test():
    part_1_result = get_part_1("./sample.txt")
    expected_1 = "CMZ"
    assert (
        part_1_result == expected_1
    ), f"Test error part 1: {part_1_result} != {expected_1}"
    part_2_result = get_part_2("./sample.txt")
    expected_2 = "MCD"
    assert (
        part_2_result == expected_2
    ), f"Test error part 2: {part_2_result} != {expected_2}"


if __name__ == "__main__":
    test()
    print(get_part_1("./input.txt"))
    print(get_part_2("./input.txt"))
