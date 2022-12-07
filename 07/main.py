# open the file and read the input lines
with open('07/input.txt') as f:
  input = f.readlines()

# the outermost directory is represented by an empty dictionary
dirs = {'': {}}
current = ['']  # stack of current directories

def getitem_for(d, key):
    for level in key:
        d = d[level]
    return d

# iterate over the input lines
for i, line in enumerate(input):

  # only process lines starting with '$' as commands
  if line.startswith('$'):
    # split the input line into the command and its arguments
    parts = line.strip().split()
    cmd = parts[1]  # remove the leading '$' from the command
    args = parts[2:]

    if cmd == 'cd':
      # if the first argument is /, switch to the outermost directory
      if args[0] == '/':
        current = ['']

      # if the first argument is .., move to the parent directory
      elif args[0] == '..':
        current.pop()

      # otherwise, move into the directory with the given name
      else:
        name = args[0]
        if name not in getitem_for(dirs, current):
          getitem_for(dirs, current)[name] = {}
        current.append(name)

    elif cmd == 'ls':
      # loop over all the lines that follow the ls command and that are not themselves commands
      for line in input[i+1:]:
        if line.startswith('$'):
            break
        elif line.startswith('dir'):
            continue
        else:
          # add the size of the file to the current directory's size
          size, name = line.strip().split()
          if name not in getitem_for(dirs, current):
            getitem_for(dirs, current)[name] = 0
          getitem_for(dirs, current)[name] += int(size)

def get_total_size(directory):
    the_sum = 0
    for key, value in directory.items():
        if isinstance(value, dict):
            the_sum += get_total_size(directory[key])
        else:
            the_sum += value

    return the_sum

def sum_sizes_low(directory):
    total_size = get_total_size(directory)
    the_sum = total_size if total_size <= 100000 else 0
    for _, value in directory.items():
        if isinstance(value, dict):
            the_sum += sum_sizes_low(value)

    return the_sum

# Question 1
print(sum_sizes_low(dirs))

disk_space = 70000000
required_space = 30000000

space_to_free = required_space - (disk_space - get_total_size(dirs))

def find_smallest_of_at_least(directory, size):
    # Finds the smallest subdirectory that is of at least size 'size'
    total_size = get_total_size(directory)
    if total_size < size:
        # Cannot find it here or in subdirs
        return None

    min_size = total_size
    for _, value in directory.items():
        if isinstance(value, dict):
            subdir_min_size = find_smallest_of_at_least(value, size)
            if subdir_min_size is not None:
                min_size = min(min_size, subdir_min_size)
    
    return min_size

# Question 2
print(find_smallest_of_at_least(dirs, space_to_free))