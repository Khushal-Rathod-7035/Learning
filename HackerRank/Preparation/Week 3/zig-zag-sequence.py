def findZigZagSequence(a, n):
    max_val = max(a)
    a.remove(max_val)
    a.sort()
    half_len = n // 2
    first_half = a[:half_len]
    last_half = a[half_len:]
    last_half = last_half[::-1]
    a = first_half + [max_val] + last_half
    a = [str(i) for i in a]
    print(' '.join(a))


test_cases = int(input())
for cs in range(test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)
