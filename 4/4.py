from functools import reduce
from operator import concat


def get_lines(path='input.txt') -> list:
    """Call readlines() on the file at the
    provided path."""
    with open(path) as f:
        return f.readlines()


def flatten(nested_list: list) -> list:
    return [*map(int, reduce(concat, nested_list))]


def parse_pairs(line: str) -> list:
    return flatten([*map(lambda x: x.split('-'),line.strip().split(','))])


def complete_overlap(nums: list) -> bool:
    return (nums[0] <= nums[2] and nums[1] >= nums[3]) or (
            nums[2] <= nums[0] and nums[3] >= nums[1])


def any_overlap(nums: list) -> int:
    #return bool(set(range(nums[0],nums[1]+1)).intersection(set(range(nums[2],nums[3]+1))))
    return (nums[2] <= nums[0] <= nums[3]) or (nums[0] <= nums[2] <= nums[1])

def part1(lines: list) -> int:
    return reduce(lambda x,y: x+y, map(complete_overlap, map(parse_pairs, lines)))


def part2(lines: list) -> int:
    return reduce(lambda x,y: x+y, map(any_overlap, map(parse_pairs, lines)))


def main() -> None:
    print(f'completely overlapping pair count: {part1(get_lines())}')
    print(f'partial overlapping pair count {part2(get_lines())}')


if __name__ == '__main__':
    main()
