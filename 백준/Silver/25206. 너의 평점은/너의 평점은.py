gradeList = ['F', 'P', 'D0', 'D+', 'C0', 'C+', 'B0', 'B+', 'A0', 'A+']
creditSum = 0
gradeSum = 0

for i in range(20):
  course, credit, grade = input().split()
  credit = float(credit)
  if grade == 'P':
    continue
  else:
    creditSum += credit
    gradeSum += gradeList.index(grade) * 0.5 * credit
print(gradeSum / creditSum)