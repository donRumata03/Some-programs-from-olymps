def nod(a, b):
    while a != 0 and b != 0:
        if a >= b:
            a %= b
        else:
            b %= a
    return max(a, b)


def max_NOD(ms):
    low = 0
    NODs = []
    Nodics = []
    maxnod = 1
    for i in range(len(ms) - 2):
        NODs.append(nod(ms[i], ms[i + 1]))
    print(NODs)
    while low + k < len(ms):
        Nodics = NODs[low:low+k]
        Nodics_new = []
        while len(Nodics) > 1:
            for i in range(len(Nodics)-2):
                Nodics_new.append(nod(Nodics[i], Nodics[i + 1]))

        low += 1
        print(Nodics)
        Nodics = Nodics_new
        print(Nodics)

        maxnod = max(maxnod, Nodics[0])
    return maxnod


n, k = map(int, input().split())
ms = list(map(int, input().split()))

print(max_NOD(ms))
