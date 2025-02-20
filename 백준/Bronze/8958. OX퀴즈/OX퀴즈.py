n = int(input())

for _ in range(n):
  score = 0
  sep = 0
  s = input()
  for i in s:
    if i=='O':
      sep += 1
      score += sep
    else:
      sep = 0
  print(score)