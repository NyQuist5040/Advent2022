import re

# Read input file
with open('16/input_demo.txt') as f:
    txt_lines = f.read().split('\n')


class Valve:
    def __init__(self, name, flow_rate, tunnels) -> None:

        self.name = name
        self.flow_rate = flow_rate
        self.tunnels = tunnels

    def __str__(self) -> str:
        return f'Valve {self.name} has flow rate={self.flow_rate}; tunnels lead to valves {self.tunnels}'

    def link_tunnels(self, indexing_dict) -> None:
        self.leads_to = []
        for tunnel_name in self.tunnels:
            self.leads_to.append(indexing_dict[tunnel_name])

    def compute_distances(self, indexing_dict):
        # builds the valve distances parameter, storing the distance from self to each valve in the graph
        self.valve_distances = {self.name: 0}
        distance = 0
        while True:
            valves_at_outer = [k for k, d in self.valve_distances.items() if d == distance]

            distance += 1

            for valve_name in valves_at_outer:
                for possible_valve in indexing_dict[valve_name].leads_to:
                    if not possible_valve.name in self.valve_distances.keys():
                        self.valve_distances[possible_valve.name] = distance

            # check if there are new valves added
            if not distance in self.valve_distances.values():
                break


class Explorer:
    def __init__(self, starting_valve, time_left=30) -> None:

        self.time_left = time_left
        self.position = starting_valve

        self.releasing_rate = 0
        self.total_released = 0
        self.opened_valves = []

    def __str__(self) -> str:
        full_str = f'Explorer at valve {self.position.name} with:\n' \
                   f'    . Time left: {self.time_left} minutes\n' \
                   f'    . Release rate: {self.releasing_rate} pressure units per minute\n' \
                   f'    . Total released: {self.total_released} pressure units\n' \
                   f'    . Valves opened: {[a.name for a in self.opened_valves]}\n'
        return full_str

    def copy(self):
        new_object = type(self)(self.position, self.time_left)

        new_object.releasing_rate = self.releasing_rate
        new_object.total_released = self.total_released

        # Just a shallow copy of valves, so we keep the same valve objects
        new_object.opened_valves = self.opened_valves.copy()

        return new_object

    def spend_minute(self, n_minutes=1) -> None:
        self.total_released += self.releasing_rate * n_minutes
        self.time_left -= n_minutes

    def find_valid_paths(self, indexing_dict):
        # Finds all paths that could lead to an optimal solution.
        # assumes that we start at a point with a useless valve (flow=0).
        # The only valid option at  each step is to choose a valve not yet opened and with non-0 flow,
        # then go there through the shortest path.

        possible_paths = []
        for name, valve in indexing_dict.items():
            # Check that the valve is useful
            if valve.flow_rate == 0 or valve in self.opened_valves:
                continue

            # Check that in the allowed time, we can walk to the valve and open it.
            if self.time_left < self.position.valve_distances[name] + 1:
                continue

            # Otherwise, this is a valid destination, we save the valve and the distance to this
            # valve as possibilities
            possible_paths.append((valve, self.position.valve_distances[name]))

        return possible_paths

    def follow_path(self, path):
        # Returns a new Explorer object that has followed path

        new_explorer = self.copy()

        # Time spent: distance + 1 (for valve opening)
        new_explorer.spend_minute(path[1] + 1)

        # Move to the destination
        new_explorer.position = path[0]

        # Open the valve
        new_explorer.releasing_rate += new_explorer.position.flow_rate
        new_explorer.opened_valves.append(new_explorer.position)

        return new_explorer

    def explore(self, indexing_dict):

        # Find all possible paths
        possible_paths = self.find_valid_paths(indexing_dict)

        # ending condition
        if not possible_paths:
            # Just wait here till the end
            self.spend_minute(self.time_left)
            return self

        # Explore all possible options, keep the one with the most total pressure released
        explorers = []

        for path in possible_paths:
            # New explorer that is a copy of self that has then explored the next path.
            new_explorer = self.follow_path(path)

            # Recursive explore from this point
            explorers.append(new_explorer.explore(indexing_dict))

        # Find the one with maximum total release and return it
        explorers_total_released = [a.total_released for a in explorers]
        return explorers[explorers_total_released.index(max(explorers_total_released))]


class ExplorerTandem:
    def __init__(self, starting_valve, time_left=26) -> None:
        self.explorer_1 = Explorer(starting_valve, time_left)
        self.explorer_2 = Explorer(starting_valve, time_left)

    def __str__(self) -> str:
        return f'Explorer tandem with two explorers:\n' + str(self.explorer_1) + str(self.explorer_2)

    def copy(self):
        new_object = type(self)(None, None)
        new_object.explorer_1 = self.explorer_1.copy()
        new_object.explorer_2 = self.explorer_2.copy()

    def follow_paths(self, path_1, path_2):
        # Returns a new ExplorerTandem where explorers 1 and 2 respectively followed paths 1 and 2

        new_tandem = type(self)(None, None)

        new_1 = self.explorer_1.follow_path(path_1)
        new_2 = self.explorer_1.follow_path(path_2)

        # Add to each explorer the valve opened by the other
        new_1.opened_valves.append(path_2[0])
        new_2.opened_valves.append(path_1[0])

        new_tandem.explorer_1 = new_1
        new_tandem.explorer_2 = new_2

        return new_tandem

    def explore(self, indexing_dict):
        # explore with both explorers at the same time

        # Find all possible paths for each explorer
        # both possible paths lists are the same length, refering to the same valves in the same order
        possible_paths_1 = self.explorer_1.find_valid_paths(indexing_dict)
        possible_paths_2 = self.explorer_2.find_valid_paths(indexing_dict)

        # ending condition
        if not possible_paths_1:
            # Just wait here till the end
            self.explorer_1.spend_minute(self.time_left)
            self.explorer_2.spend_minute(self.time_left)
            return self

        # If there is only one valve left
        if len(possible_paths_1) == 1:
            # Send the closest explorer to it
            if possible_paths_1[0][1] < possible_paths_2[0][1]:


# Parse input
all_valves = {}
for row in txt_lines:
    flow_rate = int(re.search(r'\d+', row).group())
    valve_names = re.findall(r'[A-Z]{2}', row)

    name = valve_names[0]
    tunnels = valve_names[1:]

    all_valves[name] = Valve(name, flow_rate, tunnels)


# Initialize the direct pointers to other valves in each valve
for valve in all_valves.values():
    valve.link_tunnels(all_valves)
# Compute the distance between valves
for valve in all_valves.values():
    valve.compute_distances(all_valves)


# Question 1
explorer = Explorer(all_valves['AA'], 30)
print(explorer.explore(all_valves))

# Question 2
tandem = ExplorerTandem(all_valves['AA'], 5)
print(tandem)