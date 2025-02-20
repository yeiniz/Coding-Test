n = int(input())

res = 0
paper = [[0] * 101 for _ in range(101)]

for _ in range(n):
    a, b = map(int, input().split())
    for i in range(a, a+10):
        for j in range(b, b+10):
            paper[i][j] = 1

res = 0
for i in paper: 
    res += sum(i)

print(res)