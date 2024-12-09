####################
# Part 1
####################
import re


def read_input(path):
    with open(path) as input_file:
        return [line.strip() for line in input_file]


def process_instructions(corrupted_input):
    instruction_pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
    result = 0
    instructions = instruction_pattern.findall("".join(corrupted_input))

    # Convert the instructions to a list of tuples
    instructions = [
        tuple(map(int, instruction[4:-1].split(","))) for instruction in instructions
    ]

    # Get the result of the instructions
    for instruction in instructions:
        result += instruction[0] * instruction[1]

    return result


corrupted_input = read_input("python/day_3/input.txt")
instruction_pattern = re.compile(r"mul\(\d{1,3},\d{1,3}\)")
result = process_instructions(corrupted_input)

print("Uncorrputed output:", result)


####################
# Part 2
####################
do_pattern = re.compile(r"do\(\)", re.IGNORECASE)
dont_pattern = re.compile(r"don't\(\)", re.IGNORECASE)

with open("python/day_3/input.txt") as input_file:
    corrupted_input = input_file.read()

# Initially, don't ignore valid instructions
calculating_instructions = True
unignored_instructions_result = 0
index = 0

while index < len(corrupted_input):
    # Search for the next order in the remaining input
    do_match = re.search(do_pattern, corrupted_input[index:])
    dont_match = re.search(dont_pattern, corrupted_input[index:])

    # No more orders found, process remaining instructions if enabled
    if not do_match and not dont_match:
        if calculating_instructions:
            unignored_instructions_result += process_instructions(
                corrupted_input[index:]
            )
        break

    # Determine next order to process
    if do_match and (not dont_match or do_match.start() < dont_match.start()):
        # Process up to the next "do()" or EOF
        if calculating_instructions:
            unignored_instructions_result += process_instructions(
                corrupted_input[index : index + do_match.start()] # process starting from current index upto the next "do()"
            )

        index += do_match.end()
        calculating_instructions = True
    elif dont_match and (not do_match or dont_match.start() < do_match.start()):
        # Process up to the next "don't()" or EOF
        if calculating_instructions:
            unignored_instructions_result += process_instructions(
                corrupted_input[index : index + dont_match.start()] # process upto next "don't()"
            )

        index += dont_match.end()
        calculating_instructions = False

print("Unignored instructions result:", unignored_instructions_result)
