n = int(input())

k = 0

while n > 0:
    if n >= (k+1)**2:
        n -= (k + 1)**2
        k += 1
    else:
        break
print(k)
