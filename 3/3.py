from functools import reduce


def add_two(x, y):
    return x + y


def sort_sack(rucksack: str) -> tuple:
    return set(rucksack[: len(rucksack) // 2]), set(rucksack[len(rucksack) // 2 :])


def get_priority(char_code: int) -> int:
    if 96 < char_code < 123:  # if upper case
        return char_code - 96
    else:  # else lower case
        return char_code - 38


def calculate_priority(char: str) -> int:
    return get_priority(ord(char))


def get_intersection(both: tuple) -> set:
    return both[0].intersection(both[1])


def process_sack(sack: set) -> int:
    return reduce(add_two, map(calculate_priority, get_intersection(sort_sack(sack))))


def part1(lines: list) -> int:
    return reduce(add_two, map(process_sack, lines))


#################################################################################


def three_way_intersection(set_tuple) -> set:
    return get_intersection([set(set_tuple[1]), set(set_tuple[2])]).intersection(
        set(set_tuple[0])
    )


def find_badge_priority(items: set) -> int:
    return reduce(add_two, map(get_priority, items))


def process_triplets(lines: list) -> list:
    return list(
        map(
            three_way_intersection,
            [
                [lines[i].strip(), lines[i + 1].strip(), lines[i + 2].strip()]
                for i in range(0, len(lines), 3)
            ],
        )
    )


def badge_priority(triplet_list: list) -> int:
    return calculate_priority(triplet_list.pop())


def part2(rucksacks) -> int:
    return reduce(add_two, map(badge_priority, process_triplets(rucksacks)))


#################################################################################


def main() -> None:
    rucksacks = []
    with open("input.txt") as f:
        rucksacks = f.readlines()
    print(f"total priority: {part1(rucksacks)}")
    print(f"badge priority {part2(rucksacks)}")


if __name__ == "__main__":
    main()
