import sys
import os

def  oddNumbers(l, r):
    oddList = []
    for x in range(l,r+1):
        if x % 2 == 0:
            continue
        else:
            oddList.append(x)
    return oddList


f = open(os.environ['OUTPUT_PATH'], 'w')


_l = int(input());


_r = int(input());

res = oddNumbers(_l, _r)
for res_cur in res:
    f.write( str(res_cur) + "\n" )

f.close()