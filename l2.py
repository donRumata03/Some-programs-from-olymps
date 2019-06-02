import math

n = int(input())
k = int(input())

a = []

for i in range(0, n + 1):
    if k == 1 or k == 0:
        print(*(a + [1]*(n-i-1)))
        break
    z = math.factorial(n-i-1)
    a.append(math.ceil(k / z))
    k %= z

