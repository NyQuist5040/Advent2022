import numpy as np

# Read the input grid from the file
with open('08/input_demo.txt') as f:
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

scenic_scores = np.ones(grid.shape, np.int8) * -1
# Iterate through each row and column in the grid
for i in range(grid_height):
  for j in range(grid_width):
    # Compute the scenic score for the current tree by counting the number of steps that can be taken in each direction before encountering a tree that is taller
    steps_west = 0
    steps_east = 0
    steps_north = 0
    steps_south = 0

    for k in range(1, grid_width):
      # If the current tree is not on the edge of the grid, check the number of steps that can be taken to the west before encountering a taller tree
      if j - k >= 0:
        # There is a tree
        steps_west += 1
        if grid[i, j-k] >= grid[i,j]:
            # The tree stops the viw
            break
      else:
        # We reached the edge
        break

    for k in range(1, grid_width):
      # If the current tree is not on the edge of the grid, check the number of steps that can be taken to the east before encountering a taller tree
      if j + k < grid_width:
        # There is a tree
        steps_east += 1
        if grid[i, j+k] >= grid[i,j]:
            # The tree stops the view
            break
      else:
        # We reached the edge
        break

    for k in range(1, grid_height):
      # If the current tree is not on the edge of the grid, check the number of steps that can be taken to the north before encountering a taller tree
      if i - k >= 0:
        # There is a tree
        steps_north += 1
        if grid[i-k, j] >= grid[i,j]:
            # The tree stops the view
            break
      else:
        # We reached the edge
        break

    for k in range(1, grid_height):
      # If the current tree is not on the edge of the grid, check the number of steps that can be taken to the south before encountering a taller tree
      if i + k < grid_height:
        # There is a tree
        steps_south += 1
        if grid[i+k, j] >= grid[i,j]:
            # The tree stops the view
            break
      else:
        # We reached the edge
        break

    scenic_score = steps_west * steps_east * steps_north * steps_south
    scenic_scores[i, j] = scenic_score

# Question 2
print(np.max(scenic_scores))
print(scenic_scores)