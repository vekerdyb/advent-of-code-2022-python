def get_instructions(filename):
    with open(filename, "r") as f:
        instructions = [line.strip("\n").split(" ") for line in f.readlines()]
    return [
        (instruction[0], None)
        if len(instruction) == 1
        else (instruction[0], int(instruction[1]))
        for instruction in instructions
    ]


def maybe_sample(cycle, register_value, cycles_to_sample, samples):
    if cycle in cycles_to_sample:
        samples.append(cycle * register_value)
    return samples


def get_part_1(filename):
    cycles_to_sample = [20] + list(range(60, 260, 40))
    samples = []
    instructions = get_instructions(filename)
    register_x = 1
    instruction_pointer = 0
    is_waiting_for_number = False
    for cycle in range(1, 221):
        command, param = instructions[instruction_pointer]
        samples = maybe_sample(cycle, register_x, cycles_to_sample, samples)
        if command == "noop":
            instruction_pointer += 1
        elif command == "addx" and not is_waiting_for_number:
            is_waiting_for_number = True
        elif command == "addx" and is_waiting_for_number:
            register_x += param
            is_waiting_for_number = False
            instruction_pointer += 1
    return sum(samples)


def get_pixel_output(cycle, register_x):
    horizontal_position = (cycle - 1) % 40
    return "#" if (register_x - 1 <= horizontal_position <= register_x + 1) else '.'


def get_part_2(filename):
    instructions = get_instructions(filename)
    register_x = 1
    cycle = 1
    output = ""
    for instruction in instructions:
        command, param = instruction
        output += get_pixel_output(cycle, register_x)
        cycle += 1
        if command == "addx":
            output += get_pixel_output(cycle, register_x)
            register_x += param
            cycle += 1
    return "\n".join(["".join(pixel) for pixel in list(zip(*([iter(output)] * 40)))])


def test():
    part_1_result = get_part_1("./sample.txt")
    expected_1 = 13140
    assert (
            part_1_result == expected_1
    ), f"Test error part 1: {part_1_result} != {expected_1}"
    part_2_result = get_part_2("./sample.txt")
    expected_2 = """##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######....."""
    assert (
            part_2_result == expected_2
    ), f"Test error part 2: {part_2_result} != {expected_2}"


if __name__ == "__main__":
    test()
    print(get_part_1("./input.txt"))
    print(get_part_2("./input.txt"))
