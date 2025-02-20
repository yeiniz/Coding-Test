li = [i for i in range(1, 31)]

for i in range(28):
  n = int(input())
  li.remove(n)

print(min(li))
print(max(li))