'''
def pr( ms):
    mx = [0 for _ in range(n)]
    for i in ms:
        mx[i] = 1


def gen(k, n0, prefix = set(), results = set()):
    if k == 0:
        results.add(prefix)
        return

    prefix.add(0)
    for i in range(n0):
        results.append()
        gen(k-1, n0, )



n, k = map(int, input().split())
gen(k, n)
'''

def gen(k, n):


n, k = map(int, input().split())

r = gen(n)