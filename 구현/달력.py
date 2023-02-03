# 달력
# https://www.acmicpc.net/problem/20207
'''
1일부터 365일까지 표시된 달력이 있을 때, 연속된 일정은 하나의 직사각형 코팅지에 포함해 달력이 지워지는 것을 막고자 한다.
각 일정의 시작, 종료 날자가 주어질 때, 필요한 코팅지의 총 면적은?
* 1 <= 일정 개수 n <= 1000, 1 <= 시작날짜 s <= 종료날짜 e <= 365
* 제한 시간 1초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

calendar = [0 for _ in range(365)]

n = int(input())
for _ in range(n):
  s, e = map(int, input().split())
  for dayIdx in range(s - 1, e): calendar[dayIdx] += 1

result = 0
width = 0
height = 0
for day in calendar:
  if day != 0:
    width += 1
    height = max(height, day)  
  else:
    result += width * height
    width = 0
    height = 0
if width != 0 and height != 0: result += width * height

print(result)

'''
calendar의 각 일에 일정이 있으면 일정 수만큼 저장하는 리스트를 만든다. 하나의 일정당 1개의 칸을 차지하므로 단순히 해당 리스트를 저장하면 된다.
그리고 달력의 처음부터 끝까지 검사하면서 특정 일에 일정이 없을 때, 즉 하나의 연속된 일정이 끝날 때 코팅지를 만든다.
'''
