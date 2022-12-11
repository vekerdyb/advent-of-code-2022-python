import functools
import operator


def get_monkey_operation(monkey_operation_line_fragment):
    monkey_operator = monkey_operation_line_fragment[0]
    monkey_operand = monkey_operation_line_fragment[1:].strip()

    if monkey_operand == "old":
        get_operand = lambda old: old
    else:
        get_operand = lambda _: int(monkey_operand)

    # This will be super easy to expand when I definitely will need to that
    monkey_operator_map = {
        "+": operator.add,
        "*": operator.mul,
    }

    return lambda old: monkey_operator_map[monkey_operator](old, get_operand(old))


def get_monkey_specification(monkey_lines):
    return {
        "id": int(
            monkey_lines[0][7]
        ),  # there are no double digit monkeys, haha. Also, not actually used.
        "item_worries": [
            int(item) for item in monkey_lines[1].split(": ")[1].split(",")
        ],
        "operation": get_monkey_operation(monkey_lines[2][23:]),
        "test": lambda item_worry: item_worry % int(monkey_lines[3][21:]) == 0,
        "test_operand": int(monkey_lines[3][21:]),
        "if_true": int(monkey_lines[4][-1]),
        "if_false": int(monkey_lines[5][-1]),
        "inspected_items": 0,
    }


def get_monkey_specifications(filename):
    with open(filename, "r") as f:
        monkey_lines = [line.strip("\n") for line in f.readlines()]
    monkey_specifications = []
    for monkey_index in range(0, len(monkey_lines), 7):
        monkey_specifications.append(
            get_monkey_specification(monkey_lines[monkey_index: monkey_index + 7])
        )
    return monkey_specifications


def monkeys_be_throwing_things_around(
        monkey_specifications, rounds=20, divider_override=None
):
    for monkey_round in range(rounds):
        for active_monkey in monkey_specifications:
            for item_worry in active_monkey["item_worries"]:
                # inspect
                new_item_worry = active_monkey["operation"](item_worry)
                # relief
                if not divider_override:
                    new_item_worry = int(new_item_worry / 3)
                else:
                    new_item_worry = new_item_worry % divider_override
                # test
                mon_key = (
                    "if_true" if active_monkey["test"](new_item_worry) else "if_false"
                )
                monkey_specifications[active_monkey[mon_key]]["item_worries"].append(
                    new_item_worry
                )
                # keep track of number of items inspected
                active_monkey["inspected_items"] += 1
            # in the current data no-one throws to themselves
            active_monkey["item_worries"] = []
            # for monkey in monkey_specifications:
            #     print(f"Monkey {monkey['id']}: {monkey['item_worries']}")
    return monkey_specifications


def get_monkey_business(monkey_status):
    top2_monkeys = sorted([monkey["inspected_items"] for monkey in monkey_status])[-2:]
    return top2_monkeys[0] * top2_monkeys[1]


def get_part_1(filename):
    monkey_status_after_throwing_around = monkeys_be_throwing_things_around(
        get_monkey_specifications(filename)
    )
    return get_monkey_business(monkey_status_after_throwing_around)


def get_part_2(filename):
    monkey_specifications = get_monkey_specifications(filename)
    monkey_divider = functools.reduce(operator.mul, [monkey["test_operand"] for monkey in monkey_specifications])
    # we override dividing by the product of all test operands - this won't change the test results
    monkey_status_after_throwing_around = monkeys_be_throwing_things_around(
        monkey_specifications, rounds=10000, divider_override=monkey_divider,
    )
    return get_monkey_business(monkey_status_after_throwing_around)


def test():
    part_1_result = get_part_1("./sample.txt")
    expected_1 = 10605
    assert (
            part_1_result == expected_1
    ), f"Test error part 1: {part_1_result} != {expected_1}"
    part_2_result = get_part_2("./sample.txt")
    expected_2 = 2713310158
    assert (
            part_2_result == expected_2
    ), f"Test error part 1: {part_2_result} != {expected_2}"


if __name__ == "__main__":
    test()
    print(get_part_1("./input.txt"))
    print(get_part_2("./input.txt"))
