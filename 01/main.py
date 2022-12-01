
# Read the input file
file_in = '01/input.txt'
with open(file_in) as f:
    in_txt = f.read()

# Transform the input
split_by_elf = in_txt.split('\n\n')
backpacks = [[int(cal) for cal in elf.split('\n')] for elf in split_by_elf]

### Question 1
cal_by_elf = [sum(bp) for bp in backpacks]
max_cal = max(cal_by_elf)
print(max_cal)

### Question 2
cal_by_elf.sort()
top_3_cal = sum(cal_by_elf[-3:])
print(top_3_cal)