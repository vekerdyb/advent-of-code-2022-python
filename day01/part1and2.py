import heapq


def parse_input() -> list[int | None]:
    with open("./input.txt", "r") as f:
        return [int(line.strip()) if line.strip() else None for line in f.readlines()]


def get_calories_per_elf(lines: list[int | None]) -> list[int]:
    current_calories = []
    total_calories = []
    for line in lines:
        if line is None:
            heapq.heappush(total_calories, sum(current_calories))
            current_calories = []
        else:
            current_calories.append(line)
    return total_calories


def get_top_n_calories(calories: list[int], n: int) -> int:
    return sum(heapq.nlargest(n, calories_per_elf))


if __name__ == "__main__":
    calories_per_item = parse_input()
    calories_per_elf = get_calories_per_elf(calories_per_item)
    print(get_top_n_calories(calories_per_elf, 1))
    print(get_top_n_calories(calories_per_elf, 3))
