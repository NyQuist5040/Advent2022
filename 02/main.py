# Read the input file
file_in = '02/input.txt'
with open(file_in) as f:
    in_txt = f.read()

# Rock paper scissors with A < B < C < A
translation = {
    'A' : 'Rock',
    'B' : 'Paper',
    'C' : 'Scissors',
    'X' : 'Rock',
    'Y' : 'Paper',
    'Z' : 'Scissors',
}

# Transform the input
in_lines = in_txt.split('\n')
elf_plays = [translation[line[0]] for line in in_lines]
my_plays = [translation[line[-1]] for line in in_lines]

shape_number = {
    'Rock' : 1,
    'Paper' : 2,
    'Scissors': 3,
}
vic_score = {
    1 : 6, # I win
    2 : 0, # elf wins
    0 : 3, # draw
}

### Question 1
def match_score(elf_choice, my_choice):
    victory = ( shape_number[my_choice] - shape_number[elf_choice] ) % 3
    vic_score = {
        1 : 6, # I win
        2 : 0, # elf wins
        0 : 3, # draw
    }

    total_score = vic_score[victory] + shape_number[my_choice]

    return total_score

final_score = sum(match_score(a,b) for a,b in zip(elf_plays, my_plays))
print(final_score)

### Question 2
new_translation = {
    'X' : 2, # loss
    'Y' : 0, # draw
    'Z' : 1, # win
}
target_victories = [new_translation[line[-1]] for line in in_lines]

def match_score_2(elf_choice, victory):

    my_choice_number = 1 + (shape_number[elf_choice] + victory - 1) % 3
    total_score = vic_score[victory] + my_choice_number

    return total_score

final_score_2 = sum(match_score_2(a,b) for a,b in zip(elf_plays, target_victories))
print(final_score_2)