import re
from functools import reduce

print("AOC Day 03")
print("==========")

f = open("day3real.txt", "r")
content = f.read()
f.close()

mul_enabled = True

def do():
    global mul_enabled
    mul_enabled = True
    return 0

def dont():
    global mul_enabled
    mul_enabled = False
    return 0

def mul(x, y):
    return x * y if mul_enabled else 0

string = content.replace("don't", "dont")

def sums(part1 = False):
    pattern = r"(mul\([0-9]{1,3},[0-9]{1,3}\))|(do\(\))|(dont\(\))"
    if part1:
        pattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"
    matches = re.findall(pattern, string)
    if part1:
        lmatches = matches
    else:
        lmatches = list(map(lambda x: list(filter(lambda y: len(y) > 0, list(x)))[0], list(matches)))

    muls = list(map(lambda x: eval(x), lmatches))
    return sum(muls)

print("Part 1, sums = ", sums(True))
print("Part 2, sums = ", sums(False))