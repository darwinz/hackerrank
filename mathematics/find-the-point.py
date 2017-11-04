"""
Consider two points, p = (p(x), p(y)) and q = (q(x), q(y)). We consider the inversion or point reflection, r = (r(x), r(y)), of point p across point q to be a 180 degree rotation of point p around q.

Given n sets of points p and q, find  for each pair of points and print two space-separated integers denoting the respective values of r(x) and r(y) on a new line.

Input Format

The first line contains an integer, n, denoting the number of sets of points.
Each of the n subsequent lines contains four space-separated integers describing the respective values of p(x), p(y), q(x), and q(y) defining points p = (p(x), p(y)) and q = (q(x), q(y)).

Constraints
1 <= n <= 15
-100 <= p(x), p(y), q(x), q(y) <= 100

Output Format

For each pair of points p and q, print the corresponding respective values of r(x) and r(y) as two space-separated integers on a new line.

Sample Input

2
0 0 1 1
1 1 2 2
Sample Output

2 2
3 3
Explanation

The graphs below depict points p, q, and r for the n = 2 points given as Sample Input:

https://s3.amazonaws.com/hr-challenge-images/128/1476208076-15f0f71f16-find-point-0011.png

Thus, we print r(x) and r(y) as 2 2 on a new line.

https://s3.amazonaws.com/hr-challenge-images/128/1476207535-debed1b871-find-point-1122.png

Thus, we print r(x) and r(y) as 3 3 on a new line.
"""


def findThePoint(ar):
    px, py, qx, qy = ar[0], ar[1], ar[2], ar[3]
    return "{} {}".format(2*qx-px, 2*qy-py)


n = int(raw_input().strip())
for __ in range(n):
    ar = map(int, raw_input().strip().split(' '))
    result = findThePoint(ar)
    print(result)
