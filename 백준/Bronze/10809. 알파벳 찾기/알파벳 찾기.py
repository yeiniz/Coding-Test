S = input()
l = [-1] * 26
c = []
for i in S:
  if i not in c:
    l[ord(i)-97] = S.index(i)
for i in range(len(l)):
  print(l[i], end=' ')