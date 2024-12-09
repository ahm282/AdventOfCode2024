####################
# Part 1
####################
def count_word_occurrences(text, pattern="XMAS"):
    total = 0
    # Check every possible starting position in the text
    for start_index in range(len(text) - len(pattern) + 1):
        # Sliding window
        current_substring = text[start_index : start_index + len(pattern)]

        # Horizontal match
        if current_substring == pattern:
            total += 1

        # Reversed horizontal match
        if current_substring == pattern[::-1]:
            total += 1

    return total


def extract_diagonals(grid, word, is_forward_diagonal=True):
    number_of_rows = len(grid)
    number_of_columns = len(grid[0])
    diagonal_lines = [] # Diagonal strings

    # Get diagonals -> first column
    for starting_column in range(number_of_columns):
        current_diagonal = ""
        current_row = 0
        current_column = starting_column

        # Move diagonally to build string
        while current_row < number_of_rows and 0 <= current_column < number_of_columns:
            current_diagonal += grid[current_row][current_column]
            current_row += 1

            # Move right or left based on direction
            if is_forward_diagonal:
                current_column += 1
            else:
                current_column -= 1

        # Only keep string if long enough
        if len(current_diagonal) >= len(word):
            diagonal_lines.append(current_diagonal)

    # Extract diagonals starting from first row
    for starting_row in range(1, number_of_rows):
        current_diagonal = ""
        current_row = starting_row

        # Start from leftmost or rightmost column based on diagonal direction
        current_column = 0 if is_forward_diagonal else (number_of_columns - 1)

        # Build diagonal line
        while current_row < number_of_rows and 0 <= current_column < number_of_columns:
            current_diagonal += grid[current_row][current_column]
            current_row += 1

            # Move diagonally right or left based on direction
            if is_forward_diagonal:
                current_column += 1
            else:
                current_column -= 1

        # Only keep diagonals long enough to search
        if len(current_diagonal) >= len(word):
            diagonal_lines.append(current_diagonal)

    return diagonal_lines


with open("day_4/input.txt", "r") as file:
    grid = file.readlines()

total_xmas_occurrences = 0
lookup_word = "XMAS"

# Horizontal search
for row in grid:
    total_xmas_occurrences += count_word_occurrences(row)

# Vertical search
number_of_columns = len(grid[0])

for column_index in range(number_of_columns):
    # Traverse each column
    vertical_line = "".join(
        grid[row_index][column_index] for row_index in range(len(grid))
    )

    total_xmas_occurrences += count_word_occurrences(vertical_line)

# Diagonal search
forward_diagonals = extract_diagonals(grid, lookup_word, is_forward_diagonal=True)
reverse_diagonals = extract_diagonals(grid, lookup_word, is_forward_diagonal=False)

# Count "XMAS" in diagonals
for diagonal in forward_diagonals:
    total_xmas_occurrences += count_word_occurrences(diagonal)

for diagonal in reverse_diagonals:
    total_xmas_occurrences += count_word_occurrences(diagonal)

print('"XMAS"s found:', total_xmas_occurrences)
