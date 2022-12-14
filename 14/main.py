import numpy as np

# Read input
with open('14/input.txt') as f:
    blocks_txt = f.read().split('\n')

# Parse the input
blocks = []
for line_txt in blocks_txt:
    corners = line_txt.split(' -> ')
    new_block = []
    for corner in corners:
        new_block.append(eval(f'({corner})'))

    blocks.append(new_block)

class Cave:
    def __init__(self, blocks) -> None:

        # Find the rocks' limits
        min_h = np.inf
        max_h = - np.inf
        max_v = - np.inf
        for block in blocks:
            new_min_h = min(corner[0] for corner in block)
            new_max_h = max(corner[0] for corner in block)
            new_max_v = max(corner[1] for corner in block)

            min_h = min(min_h, new_min_h)
            max_h = max(max_h, new_max_h)
            max_v = max(max_v, new_max_v)

        # Add 1 to the left, right, and bottom
        min_h -= 1
        max_h += 1
        max_v += 1

        self.h_len = max_h - min_h + 1
        self.v_len = max_v

        self.h_offset = min_h
        self.entry_point = [0, 500 - self.h_offset]

        self.rocks = np.zeros((self.v_len, self.h_len), np.int8)
        self.sand = np.zeros((self.v_len, self.h_len), np.int8)

        # Create the rock blocks
        for block in blocks:
            for i in range(len(block) - 1):
                corner_1, corner_2 = block[i], block[i+1]

                if corner_1[0] == corner_2[0]:
                    # Vertical block
                    start_i, end_i = min(corner_1[1], corner_2[1]), max(corner_1[1], corner_2[1]) + 1

                    self.rocks[start_i:end_i, corner_1[0]-self.h_offset] = 1

                else:
                    # Horizontal block
                    start_j, end_j = min(corner_1[0], corner_2[0]) - self.h_offset, max(corner_1[0], corner_2[0]) - self.h_offset + 1
                    self.rocks[corner_1[1], start_j:end_j] = 1

    def __str__(self) -> str:
        full_str = ''
        for i in range(self.v_len):
            for j in range(self.h_len):
                if self.rocks[i, j]:
                    full_str += '#'
                elif self.sand[i, j]:
                    full_str += 'o'
                else:
                    full_str += '.'
            full_str += '\n'

        return full_str

    def add_sand(self) -> bool:
        # Adds a grain of sand to the cav, returns True if it was successfully added, False if it
        # fell from the end.

        new_sand_pos = self.entry_point.copy()

        blocked = self.rocks + self.sand

        while True:
            # Check wether the new sand reached the bottom
            if new_sand_pos[0] == self.v_len - 1:
                return False

            # Check the direct vertical
            if not blocked[new_sand_pos[0] + 1, new_sand_pos[1]]:
                new_sand_pos[0] += 1
            # Check bottom left
            elif not blocked[new_sand_pos[0] + 1, new_sand_pos[1] - 1]:
                new_sand_pos[0] += 1
                new_sand_pos[1] -= 1
            # Check bottom right
            elif not blocked[new_sand_pos[0] + 1, new_sand_pos[1] + 1]:
                new_sand_pos[0] += 1
                new_sand_pos[1] += 1
            # If no move is possible
            else:
                self.sand[new_sand_pos[0], new_sand_pos[1]] = 1
                return True


    def fill_sand(self, verbose=False) -> None:
        while True:
            success = self.add_sand()

            if verbose:
                print(self)

            if not success:
                break


# Question 1
cave = Cave(blocks)
cave.fill_sand()
print(np.sum(cave.sand))
