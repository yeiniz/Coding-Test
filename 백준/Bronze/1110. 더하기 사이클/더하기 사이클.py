n = int(input())
re = n
cy = 0

while True:
	a = n // 10
	b = n % 10
	c = (a+b) % 10
	n = 10 * b + c
	
	cy += 1
	if (re == n):
		break
	
print(cy)