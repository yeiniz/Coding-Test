n, m = map(int, input().split())
li = [i for i in range(1, n+1)]

for x in range(m):
  i, j = map(int, input().split())
  tmp = li[i-1:j]
  tmp.reverse()
  li[i-1:j] = tmp

for i in range(n):
  print(li[i], end=' ')