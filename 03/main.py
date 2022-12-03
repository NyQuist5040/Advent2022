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


def letter_priority(letter):
    # Receives a single letter and computes the priority score

    # Check if the letter is uppercase
    is_uppercase = bool(re.match('[A-Z]', letter))

    # Convert to the priority score
    if is_uppercase:
        priority = ord(letter) - 38
    else:
        priority = ord(letter) - 96

    return priority

# Question 1
match_priorities = []
for bp in backpacks:
    match_left = f'[{bp[0]}]'

    # Assuming there is only one common item in both halves, only find the first match
    matching_item = re.search(match_left, bp[1]).group()

    match_priorities.append(letter_priority(matching_item))

print(sum(match_priorities))

# Question 2
badge_priorities = []
for i in range(0, len(backpacks), 3):

    # Go back to the input for unsplit backpacks
    bp_group = in_txt.split('\n')[i:i+3]

    match_first_bp = f'[{bp_group[0]}]'

    # Find the elements of bp 2 and 3 that are in bp 1
    match_on_second = set(re.findall(match_first_bp, bp_group[1]))
    match_on_third = set(re.findall(match_first_bp, bp_group[2]))

    # Find the only element that is in both matches
    badge = match_on_second.intersection(match_on_third).pop()

    badge_priorities.append(letter_priority(badge))

print(sum(badge_priorities))

