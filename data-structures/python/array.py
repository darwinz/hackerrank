import sys

def reversed_array(arr):
    r = list(reversed(arr))
    return ' '.join(map(str, r))


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
print(reversed_array(arr))
