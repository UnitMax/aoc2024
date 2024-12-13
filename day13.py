from ortools.linear_solver import pywraplp
import re

print("AOC Day 13")
print("==========")

f = open("day13real.txt", "r")
content = f.read()
f.close()

def minimize(x, y, x1, y1, x2, y2):
    # SCIP not GLOP since we're using integers only
    solver = pywraplp.Solver.CreateSolver("SCIP")
    if not solver:
        return
    
    # vars
    a = solver.IntVar(0, solver.infinity(), "a")
    b = solver.IntVar(0, solver.infinity(), "b")

    # constraints
    solver.Add(x == a * x1 + b * x2)
    solver.Add(y == a * y1 + b * y2)

    # cost function (probably not necessary because they are linear equations and should intersect at one point only)
    solver.Minimize(3 * a + b)

    status = solver.Solve()

    if status == pywraplp.Solver.OPTIMAL:
        return a.solution_value(), b.solution_value()
    else:
        return 0, 0

def find_tokens(part2):
    tokens = 0
    for machine in content.split("\n\n"):
        xpattern_button = r"X\+([0-9]+),"
        ypattern_button = r"Y\+([0-9]+)$"
        xpattern_prize = r"X=([0-9]+),"
        ypattern_prize = r"Y=([0-9]+)$"
        button_a_x = re.search(xpattern_button, machine.split("\n")[0]).group(1) if re.search(xpattern_button, machine.split("\n")[0]) else None
        button_a_y = re.search(ypattern_button, machine.split("\n")[0]).group(1) if re.search(ypattern_button, machine.split("\n")[0]) else None
        button_b_x = re.search(xpattern_button, machine.split("\n")[1]).group(1) if re.search(xpattern_button, machine.split("\n")[1]) else None
        button_b_y = re.search(ypattern_button, machine.split("\n")[1]).group(1) if re.search(ypattern_button, machine.split("\n")[1]) else None
        prize_x = re.search(xpattern_prize, machine.split("\n")[2]).group(1) if re.search(xpattern_prize, machine.split("\n")[2]) else None
        prize_y = re.search(ypattern_prize, machine.split("\n")[2]).group(1) if re.search(ypattern_prize, machine.split("\n")[2]) else None

        if part2:
            a, b = minimize(10000000000000 + int(prize_x), 10000000000000 + int(prize_y), int(button_a_x), int(button_a_y), int(button_b_x), int(button_b_y))
        else:
            a, b = minimize(int(prize_x), int(prize_y), int(button_a_x), int(button_a_y), int(button_b_x), int(button_b_y))
        tokens += 3 * a + b
    return tokens

print("Part 1, fewest tokens =", int(find_tokens(False)))
print("Part 2, fewest tokens =", int(find_tokens(True)))

