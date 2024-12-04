print("AOC Day 04")
print("==========")

f = open("day4real.txt", "r")
content = f.read()
f.close()

lines = content.split('\n')

def search_direction_xmas(input, startx, starty, dirx, diry, maxx, maxy, step):
    newx = startx + dirx
    newy = starty + diry
    if newx >= maxx or newx < 0:
        return False
    if newy >= maxy or newy < 0:
        return False
    newchar = input[newy][newx]
    match step:
        case 2:
            if newchar == 'M':
                return search_direction_xmas(input, newx, newy, dirx, diry, maxx, maxy, step + 1)
            return False
        case 3:
            if newchar == 'A':
                return search_direction_xmas(input, newx, newy, dirx, diry, maxx, maxy, step + 1)
            return False
        case 4:
            return newchar == 'S'
        case _:
            return False # What is even going on here?

def find_xmas(input, xl, yl):
    num_xmas = 0
    for x in range(0, xl):
        for y in range(0, yl):
            char = input[y][x]
            if char == 'X':
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        found_xmas = search_direction_xmas(input, x, y, i, j, xl, yl, 2)
                        if found_xmas:
                            num_xmas += 1
    return num_xmas

def check_x_mas(char1, char2):
    return (char1 == 'M' and char2 == 'S') or (char1 == 'S' and char2 == 'M')

def find_x_mas(input, xl, yl):
    num_xmas = 0
    for x in range(0, xl):
        for y in range(0, yl):
            char = input[y][x]
            if char == 'A':
                if x > 0 and x < (xl - 1) and y > 0 and y < (yl - 1):
                    if check_x_mas(input[y-1][x-1], input[y+1][x+1]) and check_x_mas(input[y+1][x-1], input[y-1][x+1]):
                        num_xmas += 1
    return num_xmas

print("Number of XMAS, part 1: ", find_xmas(lines, len(lines[0]), len(lines)))
print("Number of X-MAS, part 2: ", find_x_mas(lines, len(lines[0]), len(lines)))