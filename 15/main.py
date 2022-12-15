import re

# read file
with open('15/input.txt') as f:
    rows_txt = f.read().split('\n')


class Sensor:
    def __init__(self, sensor_position, beacon_position) -> None:
        self.sensor_position = sensor_position
        self.beacon_position = beacon_position

        self.distance_to_beacon = self.distance_to(self.beacon_position)

    def __str__(self) -> str:
        return f'Sensor at {self.sensor_position}: closest beacon is at {self.beacon_position} (distance of {self.distance_to_beacon})'

    def distance_to(self, position):
        # returns the distance between the sensor and the point at position=(x, y)
        return abs(self.sensor_position[0] - position[0]) + abs(self.sensor_position[1] - position[1])

    def covered_on_row(self, row_y) -> tuple:
        # Return the range of cells in row number row_y that cannot contain another beacon than
        # the one reported by this sensor. The tuple is empty if no cell is covered.
        # returns (min_x, max_x) where min_x is covered and max_x is not.

        # Projection of the sensor on row_y
        projection_on_row = (self.sensor_position[0], row_y)
        # Distance to the projection row_y
        distance_to_row = self.distance_to(projection_on_row)
        # number of steps that can be taken after walking to row_y, while staying in the range of the sensor-beacon distance
        remaining_steps = self.distance_to_beacon - distance_to_row

        if remaining_steps < 0:
            # The sensor is too far from row_y
            return ()

        min_x = projection_on_row[0] - remaining_steps
        max_x = projection_on_row[0] + remaining_steps + 1

        return (min_x, max_x)


all_sensors = []
for row in rows_txt:
    numbers = [int(a) for a in re.findall(r'-?\d+', row)]
    all_sensors.append(Sensor((numbers[0], numbers[1]), (numbers[2], numbers[3])))

# Question 1
row_y = 2000000
all_coverages = []
for sensor in all_sensors:
    coverage = sensor.covered_on_row(row_y)
    if coverage:
        all_coverages.append(coverage)

all_coverages.sort()

# Funstions from day 4
def contains(range_a, range_b):
    # Returns True if the ranges define by range_a (2-tuple) contains the one defined by range_b
    return range_a[0] <= range_b[0] and range_a[1] >= range_b[1]

def overlaps(range_a, range_b):
    # Returns True if range_a and range_b overlap in any way
    partial_overlap = (range_a[0] <= range_b[0] <= range_a[1]) or (range_a[0] <= range_b[1] <= range_a[1])
    return partial_overlap or contains(range_a, range_b) or contains(range_b, range_a)

def merge_tuples(left, right) -> tuple:
    # If left and right overlap, return a tuple that defines a range that exactly covers both.
    # If they don't overlap, returns ()
    if not overlaps(left, right):
        return ()

    return (min(left[0], right[0]), max(left[1], right[1]))

### merge all coverages that overlap
independent_coverages = []
new_independent_coverage = all_coverages[0]
for coverage in all_coverages[1:]:
    merged_with_next = merge_tuples(new_independent_coverage, coverage)

    # Successful merge
    if merged_with_next:
        new_independent_coverage = merged_with_next

    # If the independent coverage being built cannot be merged with the next coverage
    else:
        # Store it and initialise a new one
        independent_coverages.append(new_independent_coverage)
        new_independent_coverage = coverage
# Add the last one
independent_coverages.append(new_independent_coverage)

# Compute the number of covered tiles
total_covered = sum(a[1] - a[0] for a in independent_coverages)

# We have to exclude the beacons that are in these ranges from the final count
known_beacons_x = list(set([a.beacon_position[0] for a in all_sensors if a.beacon_position[1]==row_y]))
for x in known_beacons_x:
    for ind_coverage in independent_coverages:
        if ind_coverage[0] <= x < ind_coverage[1]:
            total_covered -= 1

print(total_covered)