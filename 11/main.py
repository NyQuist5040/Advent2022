import re

# Read the input
with open('11/input.txt') as f:
    monkeys_definitions = f.read().split('\n\n')

class Monkey:
    def __init__(self, items, operation, test, if_true, if_false, all_monkeys) -> None:
        self.items = items
        self.operation = operation
        self.test = test
        self.if_true = if_true
        self.if_false = if_false
        self.all_monkeys = all_monkeys

        self.n_inspected = 0

    def take_turn(self) -> None:
        # Inspect all items from left to right
        for item in self.items:
            old = item
            new = eval(self.operation) // 3

            # pass to the relevant monkey
            if new % self.test == 0:
                self.all_monkeys[self.if_true].items.append(new)
            else:
                self.all_monkeys[self.if_false].items.append(new)

            # iterate the number of inspected items
            self.n_inspected += 1
        
        # Empty my items
        self.items = []

    def __str__(self) -> str:
        return f'Inpected {self.n_inspected} items ; holding {self.items}'


monkeys = []
for definition in monkeys_definitions:
    _, items_line, operation_line, test_line, true_line, false_line = definition.split('\n')

    # Parse the starting items
    items = [int(a) for a in re.findall('\d+', items_line)]
    
    # Parse the operation
    operation = operation_line.split('= ')[1]
    
    # Parse the test
    test_divisible = int(re.search('\d+', test_line).group())
    
    # Parse the target if test is True or False
    if_true = int(re.search('\d+', true_line).group())
    if_false = int(re.search('\d+', false_line).group())

    monkeys.append(Monkey(items, operation, test_divisible, if_true, if_false, monkeys))

# Run 20 rounds
for _ in range(20):
    for mon in monkeys:
        mon.take_turn()

# Question 2
sorted_inspection_n = sorted([a.n_inspected for a in monkeys])
print(sorted_inspection_n[-1] * sorted_inspection_n[-2])