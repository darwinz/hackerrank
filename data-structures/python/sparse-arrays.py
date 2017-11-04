"""
There is a collection of N strings ( There can be multiple occurences of a particular string ).
Each string's length is no more than 20 characters. There are also Q queries. For each query, you are given a string,
and you need to find out how many times this string occurs in the given collection of N strings.

Input Format

The first line contains N, the number of strings.
The next N lines each contain a string.
The N + 2nd line contains Q, the number of queries.
The following Q lines each contain a query string.

Constraints

* 1 <= N <= 1000
* 1 <= Q <= 1000
* 1 <= length of any string <= 20

Sample Input

4
aba
baba
aba
xzxb
3
aba
xzxb
ab
Sample Output

2
1
0
Explanation

Here, "aba" occurs twice, in the first and third string. The string "xzxb" occurs once in the fourth string,
and "ab" does not occur at all.
"""

N = int(input())
strArray, qArray = [], []
for _ in range(N):
    strArray.append(input().strip())
Q = int(input())
for _ in range(Q):
    query = input()
    qArray.append(strArray.count(query))

print("\n".join(map(str, qArray)))
