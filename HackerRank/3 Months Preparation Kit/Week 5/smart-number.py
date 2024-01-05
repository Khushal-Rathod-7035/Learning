import math


def is_smart_number(num):
    factors = []
    for i in range(1, num+1):
        if num % i == 0:
            factors.append(i)
    if len(factors) % 2 == 0:
        return False
    return True


for _ in range(int(input())):
    num = int(input())
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")
