####################
# Part 1
####################
import re


def read_input(path):
    with open(path) as input_file:
        return [line.strip() for line in input_file]


corrupted_input = read_input("python/day_3/input.txt")
instruction_pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
result = 0

# Find all the instructions by matching the pattern
instructions = instruction_pattern.findall("".join(corrupted_input))

# Convert the instructions to a list of tuples
instructions = [
    tuple(map(int, instruction[4:-1].split(","))) for instruction in instructions
]

# Get the result of the instructions
for instruction in instructions:
    result += instruction[0] * instruction[1]

print("Uncorrputed output:", result)
