def get_moves(filename):
    with open(filename, "r") as f:
        moves = [line.strip("\n").split(" ") for line in f.readlines()]
    return "".join([move[0] * int(move[1]) for move in moves])


def get_tail_position(head_position, tail_position):
    hx, hy = head_position
    tx, ty = tail_position
    touching_or_same = ((-1 <= ty - hy <= 1) and (-1 <= tx - hx <= 1))

    if touching_or_same:
        return tail_position

    # straight move
    if hx == tx:
        if hy > ty:
            return (tx, hy - 1)
        return (tx, hy + 1)
    if hy == ty:
        if hx > tx:
            return (hx - 1, ty)
        return (hx + 1, ty)

    # diagonal move
    xdiff = hx - tx
    ydiff = hy - ty
    new_tx = tx + 1 if (xdiff > 0) else tx - 1
    new_ty = ty + 1 if (ydiff > 0) else ty - 1
    return (new_tx, new_ty)


def get_part_1(filename):
    moves = get_moves(filename)
    tail_visited = set()
    head_position = (0, 0)
    tail_position = (0, 0)
    for move in moves:
        match move:
            case "U":
                head_position = head_position[0], head_position[1] - 1
            case "R":
                head_position = head_position[0] + 1, head_position[1]
            case "D":
                head_position = head_position[0], head_position[1] + 1
            case "L":
                head_position = head_position[0] - 1, head_position[1]
        tail_position = get_tail_position(head_position, tail_position)
        tail_visited.add(tail_position)
    return len(tail_visited)


def get_part_2(filename):
    moves = get_moves(filename)
    tail_visited = set()
    number_of_knots = 10
    knots = [(0,0)] * number_of_knots
    for move in moves:
        match move:
            case "U":
                knots[0] = knots[0][0], knots[0][1] - 1
            case "R":
                knots[0] = knots[0][0] + 1, knots[0][1]
            case "D":
                knots[0] = knots[0][0], knots[0][1] + 1
            case "L":
                knots[0] = knots[0][0] - 1, knots[0][1]

        for index in range(1, len(knots)):
            knots[index] = get_tail_position(knots[index - 1], knots[index])
        tail_visited.add(knots[number_of_knots - 1])
    return len(tail_visited)


def test():
    part_1_result = get_part_1("./sample.txt")
    expected_1 = 13
    assert (
            part_1_result == expected_1
    ), f"Test error part 1: {part_1_result} != {expected_1}"
    part_2_result = get_part_2("./sample.txt")
    expected_2 = 1
    assert (
            part_2_result == expected_2
    ), f"Test error part 2: {part_2_result} != {expected_2}"
    part_2_result = get_part_2("./sample2.txt")
    expected_2 = 36
    assert (
            part_2_result == expected_2
    ), f"Test error part 2: {part_2_result} != {expected_2}"


if __name__ == "__main__":
    test()
    print(get_part_1("./input.txt"))
    print(get_part_2("./input.txt"))
