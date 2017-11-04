"""
You are given an array of integers of size . You need to print the sum of the elements in the array, keeping in mind that some of those integers may be quite large.

Input Format

The first line of the input consists of an integer . The next line contains  space-separated integers contained in the array.

Output Format

Print a single value equal to the sum of the elements in the array.

Constraints


Sample Input

5
1000000001 1000000002 1000000003 1000000004 1000000005
Output

5000000015
Note:

The range of the 32-bit integer is (-2^31) to (2^31 - 1) or [-2147483648, 2147483647].
When we add several integer values, the resulting sum might exceed the above range. You might need to use long long int in C/C++ or long data type in Java to store such sums.
"""

import sys

def aVeryBigSum(n, ar):
    try:
        if((n <= 10 and n >= 1) and \
          all(a <= 10 ** 10 and a >= 0 for a in ar)):
            sum = 0
            for l in range(n):
                sum += ar[l]
            return sum
        else:
            return None
    except:
        return None


n = int(raw_input().strip())
ar = map(long, raw_input().strip().split(' '))
result = aVeryBigSum(n, ar)
print(result)