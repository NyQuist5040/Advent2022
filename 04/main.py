
file_in = '04/input.txt'
with open(file_in) as f:
    in_txt = f.read()

# Transform input
assignments = []
for line in in_txt.split('\n'):
    left_elf, right_elf = line.split(',')
    left_range = tuple(int(a) for a in left_elf.split('-'))
    right_range = tuple(int(a) for a in right_elf.split('-'))
    
    assignments.append((left_range, right_range))

### Question 1
def contains(range_a, range_b):
    # Returns True if the ranges define by range_a (2-tuple) contains the one defined by range_b
    return range_a[0] <= range_b[0] and range_a[1] >= range_b[1]

is_contained = []
for assignment_left, assignment_right in assignments:
    is_contained.append(contains(assignment_left, assignment_right) or contains(assignment_right, assignment_left))

print(sum(is_contained))

### Question 2
def overlaps(range_a, range_b):
    # Returns True if range_a and range_b overlap in any way
    partial_overlap = (range_a[0] <= range_b[0] <= range_a[1]) or (range_a[0] <= range_b[1] <= range_a[1])
    return partial_overlap or contains(range_a, range_b) or contains(range_b, range_a)

has_overlap = []
for assignment_left, assignment_right in assignments:
    has_overlap.append(overlaps(assignment_left, assignment_right))

print(sum(has_overlap))