def process_instructions(instructions, grid_size):
    r, c = grid_size
    x, y = 0, 0
    dirs = ('N', 'E', 'S', 'W')
    p = 0
    curr_dir = dirs[p]


    for i in instructions:

        if i == 'F':
            if curr_dir == 'N':
                y = y + 1
            elif curr_dir == 'E':
                x = x + 1
            elif curr_dir == 'S':
                y = y - 1
            elif curr_dir == 'W':
                x = x - 1
        elif i == 'L':
            p = p - 1
        elif i == 'R':
            p = p + 1

        if x < 0:
            x = 0
        elif x > c:
            x = c
        if y < 0:
            y = 0
        elif y > r:
            y = r

        curr_dir = dirs[p]

    pos = (x, y)
    return pos, curr_dir


instructions = "FFLFFRFL"
grid_size = (5, 5)
print(process_instructions(instructions, grid_size))
