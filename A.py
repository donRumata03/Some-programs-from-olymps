w = int(input())
l= int(input())
h= int(input())


def f(l, w, h):
    if min(l, w) >= 2 * h and max(l, h) <= 2 * min(l, w):
        return True


print("good" if f(l, w, h) else "bad")