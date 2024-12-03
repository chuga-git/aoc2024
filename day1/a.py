import sys
import re

f = sys.stdin
text = f.read().strip()

def ints(s: str) -> list[int]:
    return list(map(int, re.findall(r"-?\d+", s)))

# golfing: figure out how to bind ints(text) to a shorter name
def part1():
    return sum(map(lambda x,y:abs(x-y),*map(sorted,(ints(text)[::2],ints(text)[1::2]))))


def part2():
    return(lambda l:sum(x*l[1].count(x)for x in l[0]))(list(map(sorted,(ints(text)[::2],ints(text)[1::2]))))


print("part 1:", part1())
print("part 2:", part2())
