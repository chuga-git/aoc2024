import os
import sys
import itertools
import re
import operator

f = sys.stdin

# this will fail unless golfed soln is commented out (or vice versa)
lines = f.read().strip().splitlines()

def ints(s: str) -> list[int]:
    return list(map(int, re.findall(r"-?\d+", s)))

def drop1(xs):
    return [xs[:i] + xs[i+1:] for i in range(len(xs))]

def safe(xs):
    # todo: figure out why rhs has to be a list comprehension but doesn't throw any errors when consuming when not
    return (lambda l:all(-3 <= x <= -1 for x in l) or all(1 <= x <= 3 for x in l))([x-y for x,y in zip(xs,xs[1:])])

def part1():
    return sum(map(safe,map(ints, lines)))

def part2():
    return sum(any(map(safe, drop1(x)))for x in map(ints, lines))

print("part 1:", part1())
print("part 2:", part2())

# mega golfed
# this is atrocious
s=lambda X:(lambda l:all(-3<=x<=-1 for x in l)or all(1<=x<=3 for x in l))([x-y for x,y in zip(X,X[1:])])
print((lambda l:(sum(map(s,l)),sum(any(map(s,[x[:i]+x[i+1:]for i in range(len(x))]))for x in l)))([[int(x)for x in l.split()]for l in sys.stdin.read().split('\n')]))