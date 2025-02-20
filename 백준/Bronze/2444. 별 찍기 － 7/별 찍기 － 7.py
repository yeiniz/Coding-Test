n = int(input())
length = 2*n-1
mid = n-1
for i in range(length):
  if i <= mid:
    print(' '*(mid-i)+'*'*(1+2*i))
  else:
    print(' '*(i-mid)+'*'*(2*(length-i)-1))