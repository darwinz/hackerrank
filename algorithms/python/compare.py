import sys

def solve(a0, a1, a2, b0, b1, b2):
    # Complete this function
    try:
        if all(i <= 100 for i in [a0, a1, a2, b0, b1, b2]) and \
           all(i >= 1 for i in [a0, a1, a2, b0, b1, b2]):
            pointsAlice = (a0 > b0) + (a1 > b1) + (a2 > b2)
            pointsBob = (a0 < b0) + (a1 < b1) + (a2 < b2)
            return [pointsAlice, pointsBob]
        else:
            print("Constraints unmet 1 <= a or b <= 100")
    except ValueError:
        print("Integer required for all arguments")
            

a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
join = " ".join(map(str, result))
print join
