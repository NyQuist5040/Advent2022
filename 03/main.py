import re

# Read input
file_in = '03/input.txt'
with open(file_in) as f:
    in_txt = f.read()

backpacks = []
for line in in_txt.split('\n'):
    first_half = line[:len(line)//2]
    second_half = line[len(line)//2:]
    backpacks.append([first_half, second_half])

bp_matches = []
match_priority = []
for bp in backpacks:
    match_left = f'[{bp[0]}]'

    # Assuming there is only one common item in both halves, only find the first match
    matching_item = re.search(match_left, bp[1]).group()

    # Check if the matching item is uppercase
    is_uppercase = bool(re.match('[A-Z]', matching_item))

    # Convert to the priority score
    if is_uppercase:
        priority = ord(matching_item) - 38
    else:
        priority = ord(matching_item) - 96

    bp_matches.append(matching_item)
    match_priority.append(priority)

# Question 1
print(sum(match_priority))

