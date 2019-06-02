n, d, k = map(int, input().split())


ms = [(0, 0)]

len0 = d

ch = 0

x = 0
y = 0

num = 0

while num < n:
    if num + len0 < n:
        num += len0
        x += len0 if not ch else (-len0)

    else:
        if ch:
            x += num - n
        else:
            x += n - num
        num = n

    ms.append((x, y))

    if num == n:
        break

    if num + len0 < n:
        num += len0
        y += len0 if ch == 1 else (-len0)

    else:
        if ch:
            y += num - n
        else:
            y += n - num

        num = n
    ms.append((x, y))

    len0 *= k
    ch += 1
    if ch == 2:
        ch = 0

mx = my = mix = miy = 0

for i in ms:
    mx = max(mx, i[0])
    my = max(my, i[1])
    mix = min(mix, i[0])
    miy = min(miy, i[1])

h = my - miy + 1
w = mx - mix + 1

print(h, w)


########################################


len0 = d

ch = 0

x = -mix
y = -miy

mt = [["." for __ in range(w)] for _ in range(h)]
mt[x][y] = "*"


for i in range(1, len(ms)):
    if (i - 1) % 2:                               # Not chot, znach y
        while y != ms[i][1] - miy:

            if (i - 1) % 4 == 1:
                y -= 1
            else:
                y += 1
            mt[y][x] = "*"


    else:
        while x != ms[i][0] - mix:
            if (i - 1) % 4 == 0:
                x += 1
            else:
                x -= 1
            mt[y][x] = "*"



for i in range(h):
    print(*mt[i])

