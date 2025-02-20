from itertools import combinations
import sys

input = sys.stdin.read
data = input().splitlines()
    
# 첫 줄 입력 처리
N, M = map(int, data[0].split())
    
# 카드 리스트
cards = list(map(int, data[1].split()))
    
# 초기화
max_sum = 0
    
# 모든 3장 조합을 순회
for comb in combinations(cards, 3):
    current_sum = sum(comb)
    if current_sum <= M:
        max_sum = max(max_sum, current_sum)
    
print(max_sum)