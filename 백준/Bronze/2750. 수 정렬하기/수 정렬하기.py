n = int(input())
li = []

for _ in range(n):
  a = int(input())
  li += [a]

li.sort()
for i in li : print(i)