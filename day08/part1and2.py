from functools import partial


def get_forest(lines):
    return len(lines[0]), [int(tree) for line in lines for tree in line]


def get_tree_height(forest, size, column, row):
    return forest[row * size + column]


def is_covered_from(direction, forest, size, column, row):
    get_forest_tree_height = partial(get_tree_height, forest, size)
    current_tree_height = get_forest_tree_height(column, row)
    if direction == "left":
        for c in range(column):
            if get_forest_tree_height(c, row) >= current_tree_height:
                return True
    elif direction == "right":
        for c in range(column + 1, size):
            if get_forest_tree_height(c, row) >= current_tree_height:
                return True
    elif direction == "above":
        for r in range(row):
            if get_forest_tree_height(column, r) >= current_tree_height:
                return True
    elif direction == "below":
        for r in range(row + 1, size):
            if get_forest_tree_height(column, r) >= current_tree_height:
                return True
    return False


def get_invisible_trees(forest, size):
    invisible = []
    for column in range(size):
        is_covered_from_left = partial(is_covered_from, "left", forest, size, column)
        is_covered_from_right = partial(is_covered_from, "right", forest, size, column)
        is_covered_from_above = partial(is_covered_from, "above", forest, size, column)
        is_covered_from_below = partial(is_covered_from, "below", forest, size, column)
        for row in range(size):
            if not is_covered_from_left(row):
                continue
            if not is_covered_from_right(row):
                continue
            if not is_covered_from_above(row):
                continue
            if not is_covered_from_below(row):
                continue
            invisible.append((row, column))
    return invisible


def get_part_1(filename):
    size, forest = get_forest(get_lines(filename))
    invisible_tree_coords = get_invisible_trees(forest, size)
    return size * size - len(invisible_tree_coords)


def get_viewing_distance(direction, forest, size, column, row, viewing_height):
    get_forest_tree_height = partial(get_tree_height, forest, size)
    if direction == "left":
        if column == 0:
            return 0
        return (
            1
            if get_forest_tree_height(column - 1, row) >= viewing_height
            else (
                1
                + get_viewing_distance(
                    direction, forest, size, column - 1, row, viewing_height
                )
            )
        )
    elif direction == "right":
        if column == size - 1:
            return 0
        return (
            1
            if get_forest_tree_height(column + 1, row) >= viewing_height
            else (
                1
                + get_viewing_distance(
                    direction, forest, size, column + 1, row, viewing_height
                )
            )
        )
    elif direction == "above":
        if row == 0:
            return 0
        return (
            1
            if get_forest_tree_height(column, row - 1) >= viewing_height
            else (
                1
                + get_viewing_distance(
                    direction, forest, size, column, row - 1, viewing_height
                )
            )
        )
    elif direction == "below":
        if row == size - 1:
            return 0
        return (
            1
            if get_forest_tree_height(column, row + 1) >= viewing_height
            else (
                1
                + get_viewing_distance(
                    direction, forest, size, column, row + 1, viewing_height
                )
            )
        )
    return 0


def get_best_scenic_score(forest, size):
    best_scenic_score = 0
    for column in range(size):

        scenic_score_left = partial(get_viewing_distance, "left", forest, size, column)
        scenic_score_right = partial(
            get_viewing_distance, "right", forest, size, column
        )
        scenic_score_above = partial(
            get_viewing_distance, "above", forest, size, column
        )
        scenic_score_below = partial(
            get_viewing_distance, "below", forest, size, column
        )
        for row in range(size):
            current_tree_height = get_tree_height(forest, size, column, row)
            scenic_score = (
                scenic_score_left(row, current_tree_height)
                * scenic_score_right(row, current_tree_height)
                * scenic_score_above(row, current_tree_height)
                * scenic_score_below(row, current_tree_height)
            )
            best_scenic_score = max(scenic_score, best_scenic_score)
    return best_scenic_score


def get_part_2(filename):
    size, forest = get_forest(get_lines(filename))
    return get_best_scenic_score(forest, size)


def get_lines(filename):
    with open(filename, "r") as f:
        return [line.strip("\n") for line in f.readlines()]


def test():
    part_1_result = get_part_1("./sample.txt")
    expected_1 = 21
    assert (
        part_1_result == expected_1
    ), f"Test error part 1: {part_1_result} != {expected_1}"
    part_2_result = get_part_2("./sample.txt")
    expected_2 = 8
    assert (
        part_2_result == expected_2
    ), f"Test error part 2: {part_2_result} != {expected_2}"


if __name__ == "__main__":
    test()
    print(get_part_1("./input.txt"))
    print(get_part_2("./input.txt"))
