s = input().upper()
li = [0]*26

for i in s:
    li[ord(i)-65] += 1

if li.count(max(li))>= 2:
    print("?")
else:
    print(chr(li.index(max(li))+65))