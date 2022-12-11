# read the instructions
with open('10/input.txt') as f:
    instructions = f.read().split('\n')

small_test = ['noop', 'addx 3', 'addx -5']

class Computer:
    def __init__(self, instructions) -> None:
        self.instructions = instructions
        self.instruction_n = 0

        self.register = 1
        self.cycle_n = 1

        self.waiting_add = None

        self.signal_strength_collect = [20, 60, 100, 140, 180, 220]
        self.signal_strength = []
        

    def cycle(self) -> None:

        # Collect the signal strength if necessary
        if self.cycle_n in self.signal_strength_collect:
            self.signal_strength.append(self.cycle_n * self.register)
        
        # Add the previous add operation if necessary
        if self.waiting_add is not None:
            self.register += self.waiting_add
            self.waiting_add = None

        else:
            # Parse the next instruction
            next_instr = self.instructions.pop(0) if self.instructions else 'noop'
            if next_instr == 'noop':
                pass
            else:
                # Only other possibility is addx
                add_val = int(next_instr.split(' ')[1])
                self.waiting_add = add_val

        self.cycle_n += 1

    def cycle_n_times(self, n) -> None:
        for _ in range(n):
            self.cycle()

    def cycle_all(self) -> None:
        while True:
            if self.instructions:
                self.cycle()
            else:
                break


computer = Computer(instructions)

# Question 1
computer.cycle_n_times(220)
print(sum(computer.signal_strength))
