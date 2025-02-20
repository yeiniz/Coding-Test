n = int(input())

n_5 = n//5
re = n%5

while (n_5 >= 0):
	if re % 3 == 0:
		n_3 = re//3
		print(n_5 + n_3)
		break
	n_5 -= 1
	re += 5
else:
	print(-1)