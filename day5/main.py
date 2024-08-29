import collections
import pathlib
import re
import sys

def parse(puzzle_input):
    sections = puzzle_input.read()
    return puzzle_input

def part1(input):
    INF = 10 ** 20
    blocks = input.read().split('\n\n')
    seeds = blocks[0]
    seeds = list(map(int, seeds[6:].split()))

    def getb(block, x):
        for line in block.splitlines()[1:]:
            dst, src, r = map(int, line.split())
            print(dst, src, r)

            if src <= x <= src + r - 1:
                return x - src + dst
            
        return x

    def get(seed):
        current = seed
        for block in blocks[1:]:
            print(current)
            current = getb(block, current)
        
        print()
        return current   

    ans = INF
    for seed in seeds:
        ans = min(ans, get(seed))

    print(ans)

def part2(input):
    pass

def solve(puzzle_input):
    pass

if __name__ == "__main__":
        path = "/Users/shubham/Desktop/Challenges/aoc-shubham/day5/input.txt"
        print(f"{path}:")
        input = []
        with open(path) as f:
            part1(f)
             
        solutions = solve(input)