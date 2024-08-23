# aoc201901.py

import collections
import pathlib
import re
import sys

def parse(puzzle_input):
    return puzzle_input

def part1(input):
   time_str = input[0]
   dist_str = input[1]

   time_r = re.findall(r'\d+', time_str)
   dist_r = re.findall(r'\d+', dist_str)

   time = [int(t) for t in time_r]
   dist = [int(d) for d in dist_r]

   ans = 1

   for t, d in zip(time, dist):
    total_ways = 0
    for i in range(t):
        curr_dist = (t - i) * i
        if curr_dist > d:
            total_ways += 1
    ans *= total_ways   

   print(ans) 

def part2(input):
   #TODO - Solve it using ternary search
   time_str = input[0]
   dist_str = input[1]

   time_r = re.findall(r'\d+', time_str)
   dist_r = re.findall(r'\d+', dist_str)

   time = int("".join(t for t in time_r)) 
   dist = int("".join(d for d in dist_r)) 

   print(time, dist)
   ans = 1

   total_ways = 0
   for i in range(time):
       curr_dist = (time - i) * i
       if curr_dist > dist:
           total_ways += 1
   ans *= total_ways   

   print(ans) 
     

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    input = parse(puzzle_input)
    solution1 = part1(input)
    solution2 = part2(input)

    return solution1 

if __name__ == "__main__":
        path = "/Users/shubham/Desktop/Challenges/aoc-shubham/day6/input.txt"
        print(f"{path}:")
        input = []
        with open(path) as f:
            for line in f:
                input.append(line)
        
        solutions = solve(input)