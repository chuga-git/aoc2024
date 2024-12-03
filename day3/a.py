import sys
import re

f = sys.stdin
text = f.read().strip()
lines = text.splitlines()

def mul(x, y): return x * y

def part1():
    return sum(eval(x) for x in re.findall(r"mul\(\d+,\d+\)", text))

def part2():
    total = 0
    state = True
    for x in re.findall(r"do\(\)|don't\(\)|mul\(\d+,\d+\)", text):
        if x == "don't()":
            state = False
        elif x == "do()":
            state = True
        else:
            if state == False:
                continue
            total += eval(x)
    return total

print("part 1:", part1())
print("part 2:", part2())
