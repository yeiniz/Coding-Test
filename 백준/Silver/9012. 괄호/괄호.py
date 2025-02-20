n = int(input())  # 테스트 케이스 수

for _ in range(n):
    s = input()
    balance = 0  # 괄호 균형을 위한 변수

    for char in s:
        if char == '(':
            balance += 1
        else:
            balance -= 1
            if balance < 0:  # 닫는 괄호가 여는 괄호보다 많아짐
                break

        # 문자열 순회 종료 후 균형이 0이어야 VPS
    if balance != 0:
        print("NO")
    else:
        print("YES")