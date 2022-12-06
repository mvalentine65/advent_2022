def split_rations(calorie_list: str) -> list:
    return map(int, filter(bool, calorie_list.split('\n')))


def parse_input(path='input.txt') -> list:
    with open(path) as f:
        return map(split_rations, f.read().split('\n\n'))


def part1() -> int:
    return max(map(sum, parse_input()))


def part2() -> list:
    return sum(sorted([*map(sum, parse_input())], reverse=True)[0:3])


def main():
    print(f'highest calorie couunt: {part1()}')
    print(f'highest three sum: {part2()}')


if __name__ == '__main__':
    main()


