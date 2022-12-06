

def window_is_unique(substring: str) -> bool:
    return len(substring) == len(set(substring))


def find_first_packet_index(string: str, window) -> int:
    for i in range(len(string.strip())-window):
        if window_is_unique(string[i:i+window]):
            return i+window


def part1(path='input.txt') -> int:
    with open(path) as f:
        return find_first_packet_index(f.read(), window=4)


def part2(path='input.txt') -> int:
    with open(path) as f:
        return find_first_packet_index(f.read(), window=14)


def main() -> None:
    print(part1())
    print(part2())


if __name__ == '__main__':
    main()
