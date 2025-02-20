lst = []
for _ in range(9):
  lst.append(list(map(int, input().split())))

max = 0
max_i = 0
max_j = 0
for i in range(9):
  for j in range(9):
    if lst[i][j] > max:
      max = lst[i][j]
      max_i = i
      max_j = j
print(max)
print(max_i+1, max_j+1)