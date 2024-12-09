import sys
import itertools as it

f = sys.stdin
lines = f.read().strip().splitlines()

def get(i, j):
    if i >= len(lines) or i < 0:
        return None
    if j >= len(lines[0]) or j < 0:
        return None
    return lines[i][j]

def match_dir(pos, d):
    i, j = pos
    word = "XMAS"
    for k in range(4):
        cur = get(i, j)
        if cur != word[k]:
            return False
        i+=d[0]
        j+=d[1]
    return True

def part1():
    count = 0
    DIRS = [(-1, -1), (-1, 0), (-1, 1), (0 , -1), (0 , 1), (1 , -1), (1,  0), (1,  1)]
    for i,row in enumerate(lines):
        for j,col in enumerate(row):
            for d in DIRS:
                if (i, j) == (9, 7) and d == (-1,-1):
                    print("hi")
                if match_dir((i, j), d):
                    count += 1
    return count
        

def part2():
    deltas = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
    total = 0
    for i, row in enumerate(lines):
        for j, ch in enumerate(row):
            if ch != 'A':
                continue
            topleft = get(i-1,j-1)
            botleft = get(i+1, j-1)
            topright = get(i-1,j+1)
            botright = get(i+1, j+1)
            match (topleft, botright, botleft, topright):
                case ('M','S','M','S')|('M','S','S','M')|('S','M','M','S')|('S','M','S','M'):
                    total += 1
    return total


print("part 1:", part1())
print("part 2:", part2())
