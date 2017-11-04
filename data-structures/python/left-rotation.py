"""
n - integer input
d - integer input
a list of integers

rotate the list a by d positions to the left
e.g.
n = 4
a = [1, 2, 3, 4]
d = 2

answer:
[3, 4, 1, 2]

"""

from collections import deque

def leftRotation(a, d):
    a = deque(a)
    a.rotate(-d)
    return a

if __name__ == "__main__":
    n, d = input().strip().split(' ')
    n, d = [int(n), int(d)]
    a = list(map(int, input().strip().split(' ')))
    result = leftRotation(a, d)
    print (" ".join(map(str, result)))
