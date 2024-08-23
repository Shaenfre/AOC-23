# aoc201901.py

import collections
import pathlib
import re
import sys

def parse(puzzle_input):
    return puzzle_input

def part1(input):
    total = 0
    for line in input:
        game, rest = line.split(":")

        def get_id(game):
            id = int(re.match("Game (\d+)", game)[1])
            return id

        r = collections.Counter({
            "red":12,
            "green":13,
            "blue":14
        })

        def good(record):
            pattern = r"(\d+) (\w+)"
            for ball in record.split(","):
                ball = ball.strip()
                matches = re.match(pattern, ball)
                num , color = matches[1], matches[2]
                num = int(num)
                if r[color] < num:
                    return False
                
            return True

        g = True
        for record in rest.split(";"):
            if not good(record):
                g = False
        
        if g:
            total += get_id(game)
    
    print(total)
    

def part2(input):
    """Solve part 2."""
    game, rest = input.split(":")
     

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    input = parse(puzzle_input)
    solution1 = part1(input)
    # solution2 = part2(input)

    return solution1 

if __name__ == "__main__":
        path = "/Users/shubham/Desktop/Challenges/aoc-shubham/day1/input.txt"
        print(f"{path}:")
        input = []
        with open(path) as f:
            for line in f:
                input.append(line)
        
        solutions = solve(input)
        # print("\n".join(str(solution) for solution in solutions))