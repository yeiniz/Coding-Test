li = []

for i in range(10):
  n = int(input())
  if n%42 not in li:
    li.append(n%42)

print(len(li))