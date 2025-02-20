a = int(input())
b = int(input())
c = int(input())

pro = str(a*b*c)

for i in range(10):
	print(pro.count(str(i)))