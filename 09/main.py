import numpy as np
import copy

# open the file and read the input lines
with open('09/input.txt') as f:
  instructions = f.read().split('\n')

def simulate_rope_movement_step(current_pos, direction):
  # Define a dictionary that associates a 2-tuple with each direction
  directions = {
    'U': np.array((0, 1), np.int32),
    'D': np.array((0, -1), np.int32),
    'L': np.array((-1, 0), np.int32),
    'R': np.array((1, 0), np.int32),
  }

  new_pos = copy.deepcopy(current_pos)

  # Update the position of the head
  new_pos[0] += directions[direction]

  for i in range(1, len(current_pos)):
    # Update the position of successive knots
    is_adjacent = (abs(new_pos[i-1][0] - current_pos[i][0]) <= 1) and (abs(new_pos[i-1][1] - current_pos[i][1]) <= 1)
    if not is_adjacent:
        new_pos[i][0] += np.sign(new_pos[i-1][0] - current_pos[i][0])
        new_pos[i][1] += np.sign(new_pos[i-1][1] - current_pos[i][1])

  # Return
  return new_pos

def simulate_rope_movement(instructions, n_knots):

  # Initialize the positions of all knots, head to tail
  knot_init_pos = [np.array((0, 0), np.int32) for _ in range(n_knots)]

  # Initialize lists to keep track of the positions of the head and tail
  past_positions = [knot_init_pos]

  # Loop through each instruction
  for instruction in instructions:
    # Get the direction and number of steps from the instruction
    direction = instruction[0]
    steps = int(instruction[1:])

    for _ in range(steps):
        new_positions = simulate_rope_movement_step(past_positions[-1], direction)
        past_positions.append(new_positions)

  # Return the final position of the tail
  return past_positions

# Question 1: count the number of unique positions of the tail with 2 knots
rope_positions = simulate_rope_movement(instructions, 2)
print(len(set(tuple(a[-1]) for a in rope_positions)))

# Question 2: count the number of unique positions of the tail with 10 knots
rope_positions = simulate_rope_movement(instructions, 10)
print(len(set(tuple(a[-1]) for a in rope_positions)))