####################
# Part 1
####################
def is_gradual(levels, mode):
    return all(
        (
            levels[i] <= levels[i + 1]
            if mode == "increasing"
            else levels[i] >= levels[i + 1]
        )
        for i in range(len(levels) - 1)
    )


def is_diff_within_limit(levels, limit=3):
    return all(
        0 < abs(levels[i] - levels[i + 1]) <= limit for i in range(len(levels) - 1)
    )


def is_safe(levels):
    return any(
        is_gradual(levels, mode) for mode in ["increasing", "decreasing"]
    ) and is_diff_within_limit(levels)


safe_reports = 0

with open("python/day_2/input.txt") as reports_file:
    for line in reports_file:
        levels = list(map(int, line.strip().split()))

        if is_safe(levels):
            safe_reports += 1

print("Safe reports found: ", safe_reports)


####################
# Part 2
####################
def can_be_made_safe(levels):
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i + 1 :] # Remove bad level
        if is_safe(modified_levels):
            return True
    return False


dampened_safe_reports = 0

with open("python/day_2/input.txt") as reports_file:
    for line in reports_file:
        levels = list(map(int, line.strip().split()))

        if can_be_made_safe(levels):
            dampened_safe_reports += 1

print("Safe reports found after Problem Dampener: ", dampened_safe_reports)
