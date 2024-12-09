####################
# Part 1
####################
import re

# Initialize the lists
left_list = []
right_list = []
total_distance = 0

with open("./day_1/input.txt", "r") as input_file:
    for line in input_file:
        # Split the line into left and right with regex
        match = re.match(r"(\d+)\s+(\d+)$", line)

        if match:
            left = int(match.group(1))
            right = int(match.group(2))

            left_list.append(int(left))
            right_list.append(int(right))

# Sort the lists
left_list.sort()
right_list.sort()

# Calculate absolute distance
for left, right in zip(left_list, right_list):
    total_distance += abs(left - right)

# Print the result
print("Total distance:", total_distance)


####################
# Part 2
####################
similarity_score = 0
frequency_map = {}

for entry in right_list:
    if entry in frequency_map:
        frequency_map[entry] += 1
    else:
        frequency_map[entry] = 1

for entry in left_list:
    if entry in frequency_map:
        similarity_score += entry * frequency_map[entry]

print("Similarity score:", similarity_score)
