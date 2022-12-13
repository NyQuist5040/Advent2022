from functools import cmp_to_key
import copy

# Read input file
with open('13/input.txt') as f:
    pairs_txt = f.read().split('\n\n')

packet_pairs = []
all_packets = []
for pair in pairs_txt:
    pair_left, pair_right = pair.split('\n')

    pair_left, pair_right = eval(pair_left), eval(pair_right)

    packet_pairs.append([pair_left, pair_right])

    all_packets.append(pair_left)
    all_packets.append(pair_right)


def compare_packets(packet_left: list, packet_right: list) -> str:
    # Returns 'right' if packet_right is "higher" than packet_left, 'left' for
    # the contrary and 'equal' if "equal".

    # Cases where at least one list is empty
    if not packet_left and not packet_right:
        return 'equal'
    if not packet_left:
        return 'right'
    if not packet_right:
        return 'left'

    element_left = packet_left.pop(0)
    element_right = packet_right.pop(0)

    # Case of list comparison
    if isinstance(element_left, list) or isinstance(element_right, list):

        # First convert one to a list if it was not already
        if not isinstance(element_left, list):
            element_left = [element_left]
        if not isinstance(element_right, list):
            element_right = [element_right]

        larger_element = compare_packets(element_left, element_right)

    # Case of int comparison
    else:
        if element_right > element_left:
            larger_element = 'right'
        elif element_right < element_left:
            larger_element = 'left'
        else:
            larger_element = 'equal'

    # Either recurse or return
    if larger_element == 'equal':
        return compare_packets(packet_left, packet_right)
    else:
        return larger_element


def compare_packets_wrapper(packet_left: list, packet_right: list) -> int:
    result_str = compare_packets(copy.deepcopy(packet_left), copy.deepcopy(packet_right.copy()))

    if result_str == 'right':
        return 1
    elif result_str == 'left':
        return -1
    else:
        return 0


pair_order = []
total_Q1 = 0
for i, pair in enumerate(packet_pairs):
    order = compare_packets_wrapper(pair[0], pair[1])
    pair_order.append(order)

    if order == 1:
        total_Q1 += i + 1

# Question 1
print(total_Q1)

# Question 2
divider_1 = [[2]]
divider_2 = [[6]]
all_packets.append(divider_1)
all_packets.append(divider_2)

all_packets.sort(key=cmp_to_key(compare_packets_wrapper), reverse=True)

# Question 2
print((all_packets.index(divider_1) + 1) * (all_packets.index(divider_2) + 1))