def gen(n, prefix, n0):
    global t

    if n == 0:
        if t == 0:
            return
        t -= 1
        print(*prefix)
        return

    prefix.append(0)
    for i in range(1, n0 + 1):

        if i != len(prefix) and i not in prefix:
            prefix[-1] = i
            gen(n - 1, prefix, n0)
    prefix.pop()


n, t = map(int, input().split())
gen(n, [], n)
