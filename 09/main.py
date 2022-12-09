import numpy as np

# open the file and read the input lines
with open('09/input.txt') as f:
  instructions = f.read().split('\n')

def simulate_rope_movement_step(head_pos, tail_pos, direction):
  # Define a dictionary that associates a 2-tuple with each direction
  directions = {
    'U': np.array((0, 1), np.int32),
    'D': np.array((0, -1), np.int32),
    'L': np.array((-1, 0), np.int32),
    'R': np.array((1, 0), np.int32),
  }

  new_head_pos, new_tail_pos = head_pos.copy(), tail_pos.copy()

  # Update the position of the head
  new_head_pos += directions[direction]

  # Update the position of the tail
  is_adjacent = (abs(new_head_pos[0] - tail_pos[0]) <= 1) and (abs(new_head_pos[1] - tail_pos[1]) <= 1)
  if not is_adjacent:
      new_tail_pos[0] += np.sign(new_head_pos[0] - tail_pos[0])
      new_tail_pos[1] += np.sign(new_head_pos[1] - tail_pos[1])

  # Return
  return new_head_pos, new_tail_pos

def simulate_rope_movement(instructions):

  # Initialize the positions of the head and tail
  head_pos = np.array((0, 0), np.int32)
  tail_pos = np.array((0, 0), np.int32)

  # Initialize lists to keep track of the positions of the head and tail
  head_positions = [head_pos]
  tail_positions = [tail_pos]

  # Loop through each instruction
  for instruction in instructions:
    # Get the direction and number of steps from the instruction
    direction = instruction[0]
    steps = int(instruction[1:])

    for _ in range(steps):
        new_head_pos, new_tail_pos = simulate_rope_movement_step(head_positions[-1], tail_positions[-1], direction)
        head_positions.append(new_head_pos)
        tail_positions.append(new_tail_pos)

  # Return the final position of the tail
  return head_positions, tail_positions

head_positions, tail_positions = simulate_rope_movement(instructions)

# Question 1: count the number of unique positions of the tail
print(len(set(tuple(a) for a in tail_positions)))