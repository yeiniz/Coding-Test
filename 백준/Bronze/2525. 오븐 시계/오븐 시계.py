h, m = map(int, input().split())
t = int(input())

tmp = h*60 + m + t

if tmp>=1440:
  print((tmp-1440)//60, (tmp-1440)%60)
else:
  print(tmp//60, tmp%60)