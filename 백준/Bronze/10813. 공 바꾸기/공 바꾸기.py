n, m = map(int, input().split())
li = []

for i in range(n+1):
  li.append(i)

for x in range(m):
    i, j = map(int, input().split())
    sep = li[i]
    li[i] = li[j]
    li[j] = sep

for i in range(1, len(li)):
    print(li[i], end=' ')