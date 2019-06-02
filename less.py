import math
u = {1, 2, 3, 4, 5}


def C(n, k):
    return int((math.factorial(n))/(math.factorial(k)*math.factorial(n-k)))


# n = int(input())
# количество тех, кто меньше 235

a = [2, 3, 5]
n = 5
k = 3
res = 0

for i in range(k):
    print(i, a[max(0, i-1)], a[i])
    for x in range(a[max(0, i-1)] + 1, a[i]):
        res += C(n-x, k-i-1)

print(res)
