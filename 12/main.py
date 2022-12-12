import numpy as np

# Read input file
with open('12/input.txt') as f:
    map_rows = f.read().split('\n')

# Parse the elevation map
elevation = np.zeros((len(map_rows), len(map_rows[0])), np.int32)
for i, row in enumerate(map_rows):
    letters = list(row)
    for j, letter in enumerate(letters):
        if letter == 'S':
            # Start
            starting = (i, j)
            elevation[i, j] = ord('a') - 96
        elif letter == 'E':
            # End
            ending = (i,j)
            elevation[i, j] = ord('z') - 96
        else:
            elevation[i,j] = ord(letter) - 96

def explore_recursively(map, position, target, already_explored):

    if position in already_explored:
        return None

    if position == target:
        return already_explored

    already_explored.append(position)

    dim_i, dim_j = map.shape

    possible_steps = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]

    possible_paths = []
    for step in possible_steps:
        new_pos = (position[0] + step[0], position[1] + step[1])
        # Check within bounds
        if 0 <= new_pos[0] < dim_i and 0 <= new_pos[1] < dim_j:
            # Check that the elevation is at most 1 more than the current one
            if map[new_pos] <= map[position] + 1:
                recursive_path = explore_recursively(map, new_pos, target, already_explored.copy())
                if recursive_path is not None:
                    possible_paths.append(recursive_path)

    # If no path is valid from here
    if not possible_paths:
        return None

    min_path = possible_paths[0]
    for poss in possible_paths:
        if len(poss) < len(min_path):
            min_path = poss

    return min_path

def build_path_iteratively(map, target):
    # Builds iteratively a map of the minimal number of steps necessary to go to
    # target from anywhere.

    dim_i, dim_j = map.shape

    possible_steps = [
        (1, 0),
        (-1, 0),
        (0, 1),
        (0, -1),
    ]

    min_dist = np.ones_like(map, np.float32) * np.inf
    has_propagated = np.zeros_like(map, np.int8)

    min_dist[target] = 0
    number_inf = np.sum(np.isinf(min_dist))
    while True:
        

        # Find the minimal value that has not yet propagated, and its locations
        minimal_on_border = np.min(min_dist, initial=9999, where=(np.logical_not(has_propagated)))
        positions_minimal = np.where(min_dist == minimal_on_border)
        #position_minimal = (position_minimal[0][0], position_minimal[1][0])

        for i_min, j_min in zip(positions_minimal[0], positions_minimal[1]):
            # loop over neighbours 
            for step in possible_steps:
                new_pos = (i_min + step[0], j_min + step[1])
                # Check within bounds
                if 0 <= new_pos[0] < dim_i and 0 <= new_pos[1] < dim_j:
                    # Check that the new position's min_dist is inf and can walk to the current position
                    if np.isinf(min_dist[new_pos]) and map[i_min, j_min] <= map[new_pos] + 1:
                        # Update the new position
                        min_dist[new_pos] = minimal_on_border + 1

            has_propagated[i_min, j_min] = 1

        # Verify that the status has changed
        if np.sum(np.isinf(min_dist)) != number_inf:
            number_inf = np.sum(np.isinf(min_dist))
        else:
            break

    return min_dist

# Question 1
min_paths = build_path_iteratively(elevation, ending)
print(int(min_paths[starting]))

# Question 2

print(int(np.min(min_paths, initial=9999, where=(elevation==1))))