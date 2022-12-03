def priority(letter: str) -> int:
    if letter == letter.lower():
        return ord(letter) - 96
    return ord(letter) - 64 + 26


def get_rucksacks_from_file(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f.readlines()]


def get_part_1_score(rucksacks):
    return sum([
        priority(set(rucksack[:len(rucksack) // 2]).intersection(set(rucksack[len(rucksack) // 2:])).pop())
        for rucksack
        in rucksacks
    ])


def get_part_2_score(rucksacks):
    groups = zip(*([iter(rucksacks)] * 3))
    badge_priority_sum = 0
    for group in groups:
        group_rucksacks_sorted = sorted(group, key=lambda rucksack: len(rucksack))
        letters_in_smallest_rucksack = set(sorted(group, key=lambda rucksack: len(rucksack))[0])
        badge = [
            letter for letter in letters_in_smallest_rucksack if
            letter in group_rucksacks_sorted[1] and letter in group_rucksacks_sorted[2]
        ][0]
        badge_priority_sum += priority(badge)
    return badge_priority_sum


def test():
    rucksacks = get_rucksacks_from_file('./sample.txt')
    assert get_part_1_score(rucksacks) == 157
    assert get_part_2_score(rucksacks) == 70


if __name__ == "__main__":
    test()
    actual_rucksacks = get_rucksacks_from_file('./input.txt')
    print(get_part_1_score(actual_rucksacks))
    print(get_part_2_score(actual_rucksacks))
