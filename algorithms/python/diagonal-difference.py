"""
given a square matrix of size , calculate the absolute difference between the sums of its diagonals.

input format

the first line contains a single integer, . the next  lines denote the matrix's rows, with each line containing space-separated integers describing the columns.

constraints

 - -100 <= Elements in the matrix <= 100

output format

print the absolute difference between the two sums of the matrix's diagonals as a single integer.

sample input

3
11 2 4
4 5 6
10 8 -12
sample output

15
explanation

the primary diagonal is:

11
   5
     -12
sum across the primary diagonal: 11 + 5 - 12 = 4

the secondary diagonal is:

     4
   5
10
sum across the secondary diagonal: 4 + 5 + 10 = 19
difference: |4 - 19| = 15

note: |x| is absolute value function
"""


def diagonal_difference(matrix):
    l = sum(row[i] for i, row in enumerate(matrix))
    difference = sum(row[i] - row[-i-1] for i, row in enumerate(matrix))
    return abs(difference)


n = int(raw_input().strip())
a = []
for _ in range(n):
    a.append(map(int, raw_input().split()))

print diagonal_difference(a)
