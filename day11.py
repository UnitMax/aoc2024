print("AOC Day 11")
print("==========")

f = open("day11real.txt", "r")
content = f.read()
f.close()

saved_rules = {}

def rules(input, iterations, max_iterations):
    key = str(input) + "_" + str(iterations) + "_" + str(max_iterations)
    if key in saved_rules:
        return saved_rules[key]
    if iterations == max_iterations + 1:
        return len(input)
    
    score = 0
    for stone in input:
        if stone == "0":
            score += rules(["1"], iterations + 1, max_iterations)
        elif len(stone) % 2 == 0:
            score += rules([str(int(stone[0:int(len(stone)/2)]))], iterations + 1, max_iterations) 
            score += rules([str(int(stone[int(len(stone)/2):]))], iterations + 1, max_iterations) 
        else:
            score += rules([str(int(stone) * 2024)], iterations + 1, max_iterations)

    saved_rules[key] = score
    return score

def transform_stones(input, iterations, max_iterations):
    score = 0
    for stone in input:
        score += rules([stone], iterations, max_iterations)
    return score

print("Part 1, blink score =", transform_stones(content.split(), 1, 25))
print("Part 2, blink score =", transform_stones(content.split(), 1, 75))