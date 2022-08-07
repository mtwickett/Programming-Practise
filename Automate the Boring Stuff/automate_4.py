grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

def attempt_one():
    one_dot = str(grid[0][0])
    one_zero = str(grid[1][1])

    line_one = one_dot * 2 + one_zero * 2 + one_dot + one_zero * 2 + one_dot * 2
    line_two = one_dot + one_zero * 7 + one_dot
    line_three = one_dot + one_zero * 7 + one_dot
    line_four = one_dot * 2 + one_zero * 5 + one_dot * 2
    line_five = one_dot * 3 + one_zero * 3 + one_dot * 3
    line_six = one_dot * 4 + one_zero + one_dot * 4

    print(line_one)
    print(line_two)
    print(line_three)
    print(line_four)
    print(line_five)
    print(line_six)

def attempt_two():
    line = []
    for i in range(0, 6):
        for j in range(0, 9):
            line.append(grid[j][i])
        print(''.join(line))
        line = []

def attempt_three():
    for i in range(len(grid[0])):
        for j in range(len(grid)):
            print(str(grid[j][i]), end='')
        print()

attempt_three()
