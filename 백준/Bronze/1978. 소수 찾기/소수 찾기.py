n = int(input())
li = list(map(int, input().split()))
count = 0

for i in li:
  for j in range(2, i+1):
    if i % j == 0:
      if i == j:
        count += 1
      break

print(count)