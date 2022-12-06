from pprint import pprint
from itertools import combinations
from collections import deque


def strip_list(lines: list) -> list:
    return [line.rstrip('\n') for line in lines]


def transpose_line(lines: list, i: int):
    return [lines[x][i] for x in range(len(lines)-2,-1,-1) if lines[x][i] != " "]


def transpose_blob(lines: list) -> list:
    return [transpose_line(lines, i) for i in range(1, len(lines[0]), 4)]


def parse_crate_bytes(handle) -> list:
    handle.seek(0)
    return handle.read().split('\n\n')
    

def parse_move_bytes(byte_handle) -> list:
    byte_handle.readline()
    byte_handle.readline()
    return byte_handle.read().encode('ascii').split()


def find_move_numbers(line: str) -> list:
    return [int(x)-1 for x in line.split() if x.isdigit()]


def find_moves(lines: list) -> list:
    return deque([*map(find_move_numbers, filter(bool, lines.split('\n')))])


def execute_single_move(crates: list, move: list) -> list:
    for i in range(move[0]+1):
        crates[move[2]].append(crates[move[1]].pop())

def execute_all_moves(crates: list, moves: list) -> list:
    while moves:
        execute_single_move(crates, moves.popleft())
    return crates


def execute_move_same_order(crates, move):
    crates[move[2]].extend(reversed([crates[move[1]].pop() for _ in range(move[0]+1)]))


def execute_bulk_moves(crates: list, moves: list) -> list:
    while moves:
        execute_move_same_order(crates, moves.popleft())
    return crates


def part1(path='input.txt') -> list:
    with open(path) as handle:
        return ''.join(stack[-1] for stack in execute_all_moves(transpose_blob(strip_list(parse_crate_bytes(handle)[0].split('\n'))),
        find_moves(parse_crate_bytes(handle)[-1])))


def part2(path='input.txt'):
    with open(path) as handle:
        return ''.join(stack[-1] for stack in
                       execute_bulk_moves(transpose_blob(strip_list(parse_crate_bytes(handle)[0].split('\n'))),
                                         find_moves(parse_crate_bytes(handle)[-1])))


def main() -> None:
    # with open('input.txt') as handle:
        # pprint(transpose_blob(strip_list(parse_crate_bytes(handle)[0].split('\n'))))
        # handle.seek(0)
        # pprint(find_moves(parse_crate_bytes(handle)[-1]))
    # print(''.join([stack[-1] for stack in part1()]))
    print(part1())
    print(part2())
if __name__ == '__main__':
    main()
