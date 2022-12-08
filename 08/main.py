import numpy as np

# Read the input grid from the file
with open('08/input.txt') as f:
  grid = np.array([list(map(int, line.strip())) for line in f])

grid_height, grid_width = grid.shape

count = 0
# Iterate through each row and column in the grid
for i in range(grid_height):
  for j in range(grid_width):
    # Check if the current tree is taller than all of the other trees in the directions of north, south, east, and west
    taller_than_west = all(grid[i][k] < grid[i][j] for k in range(j))
    taller_than_east = all(grid[i][k] < grid[i][j] for k in range(j+1, grid_width))
    taller_than_north = all(grid[k][j] < grid[i][j] for k in range(i))
    taller_than_south = all(grid[k][j] < grid[i][j] for k in range(i+1, grid_height))

    # If the current tree is taller than all of the others in the directions of north, south, east, and west, increment the count of visible trees
    if taller_than_west or taller_than_east or taller_than_north or taller_than_south:
      count += 1

# Question 1: Print the final count of visible trees
print(count)

def compute_steps_in_direction(grid, i, j, cardinal_direction):
  grid_height, grid_width = grid.shape
  steps = 0

  # Define the directions as vectors
  direction = {
  'north' : (-1, 0),
  'south' : (1, 0),
  'east' : (0, 1),
  'west' : (0, -1),
  }[cardinal_direction]

  # Iterate until we reach the edge of the grid or encounter a taller tree
  next_i, next_j = i, j
  while True:
    # Compute the next position based on the current position and the direction vector
    next_i += direction[0]
    next_j += direction[1]

    # Check if the next position is within the grid
    if 0 <= next_i < grid_height and 0 <= next_j < grid_width:
      # There is a tree at the next position
      steps += 1

      # Check if the tree at the next position is taller than the current tree
      if grid[next_i, next_j] >= grid[i, j]:
        # The tree at the next position is taller, so we stop iterating
        break
    else:
      # We reached the edge of the grid, so we stop iterating
      break

  return steps

scenic_scores = np.ones(grid.shape, np.int32) * -1
# Iterate through each row and column in the grid
for i in range(grid_height):
  for j in range(grid_width):
    # Compute the scenic score for the current tree by counting the number of steps that can be taken in each direction before encountering a tree that is taller
    steps_west = compute_steps_in_direction(grid, i, j, 'west')
    steps_east = compute_steps_in_direction(grid, i, j, 'east')
    steps_north = compute_steps_in_direction(grid, i, j, 'north')
    steps_south = compute_steps_in_direction(grid, i, j, 'south')

    scenic_score = steps_west * steps_east * steps_north * steps_south
    scenic_scores[i, j] = scenic_score

# Question 2
print(np.max(scenic_scores))