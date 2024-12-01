print("AOC Day 01")
print("==========")

f = open("day1real.txt", "r")
content = f.read()
f.close()

l = content.split()
l1 = []
l2 = []
i = 0
for e in l:
    if i % 2 == 0:
        l1.append(int(e))
    else:
        l2.append(int(e))
    i = i + 1

l1.sort()
l2.sort()

total_dist = sum([abs(a[0] - a[1]) for a in list(zip(l1, l2))])
print("Total distance, part1: ", total_dist)

def count_occurences(input):
    counter_map = dict()
    for e in input:
        if e in counter_map:
            counter_map[e] += 1
        else:
            counter_map[e] = 1
    return counter_map

l2count = count_occurences(l2)

simlitarity_score = 0
for e in l1:
    if e in l2count:
        simlitarity_score += (e * l2count[e])

print("Similarity score, part 2: ", simlitarity_score)