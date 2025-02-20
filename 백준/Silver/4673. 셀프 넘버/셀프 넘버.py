li = [0 for i in range(1, 10001)]

for i in range(1, 10001):
    li2 = list(map(int, str(i)))
    if i + sum(li2) < 10001: 
		    li[i + sum(li2) - 1] = 1
    
for i in range(0, 10000):
    if li[i] == 0: 
		    print(i+1)