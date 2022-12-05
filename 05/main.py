import re
import copy

# Read the input file
file_in = '05/input.txt'
with open(file_in) as f:
    crates_txt, moves_txt = f.read().split('\n\n')

# Parse the crate piles definition
piles = {}
crates_rows = crates_txt.split('\n')[:-1]
for i_pile, i_col in enumerate(range(1, len(crates_rows[0]), 4)):
    # Initialize the pile
    piles[i_pile + 1] = []
    # Fill the pile
    for row in reversed(crates_rows):
        if (crate := row[i_col]) != ' ':
            piles[i_pile + 1].append(crate)

piles_1 = copy.deepcopy(piles)
piles_2 = copy.deepcopy(piles)

# Move crates around
for instruction in moves_txt.split('\n'):

    # Parse the instruction
    n_moves, from_pile_i, to_pile_i = (int(a) for a in re.findall('\d+', instruction))

    for _ in range(n_moves):
        piles_1[to_pile_i].append(piles_1[from_pile_i].pop())

    piles_2[to_pile_i] += piles_2[from_pile_i][-n_moves:]
    del piles_2[from_pile_i][-n_moves:]

# Question 1
print(''.join(a[-1] for a in piles_1.values()))

# Question 2
print(''.join(a[-1] for a in piles_2.values()))


