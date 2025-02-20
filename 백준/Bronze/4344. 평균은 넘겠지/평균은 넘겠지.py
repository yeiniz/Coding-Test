c = int(input())

for _ in range(c):
  li = list(map(int, input().split()))
  m = sum(li[1:len(li)])/li[0]

  n = li[0]  # 학생 수
  scores = li[1:]  # 점수들

  average = sum(scores) / n  # 평균 계산
  above_average = [score for score in scores if score > average]  # 평균 초과 점수 필터링
  percentage = (len(above_average) / n) * 100  # 비율 계산

  print(f"{percentage:.3f}%")