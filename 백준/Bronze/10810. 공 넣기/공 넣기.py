n, m = map(int, input().split())
li = [0] * (n+1)

for x in range(m):
    i, j, k = map(int, input().split())
    for s in range(i, j+1):
        li[s] = k

for i in range(1, len(li)):
    print(li[i], end=' ')