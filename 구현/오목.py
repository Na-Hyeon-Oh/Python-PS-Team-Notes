# 오목
# https://www.acmicpc.net/problem/2615
'''
19개의 가로, 세로줄이 있는 오목판 위에서 연속적으로 다섯 알이 놓이면 그 색이 이기는 게임인 오목 게임에서
바둑판의 상태가 주어졌을 때, 흑돌이 이겼는지(1), 흰돌이 이겼는지(2), 아직 승부가 결정되지 않았는지(0)를 판단하는 프로그램을 작성하시오.
승부가 결정되었다면 둘째 줄에 연속된 다섯 개의 바둑알 중 가장 왼쪽에 있는 바둑알의 가로줄, 세로줄 번호를 순서대로 출력하시오.
- 여섯 알 이상이 연속적으로 놓인 경우에는 이긴 것이 아니다.
- 검은색과 흰색이 동시에 이기거나, 검은색 또는 흰색이 두 군데 이상에서 동시에 이기는 경우는 입력으로 들어오지 않는다.
* 제한 시간 1초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

# 오른쪽으로, 아래로, 대각선 아래로, 대각선 위로
dx = [1, 0, 1, 1]
dy = [0, 1, 1, -1]
omokPan = [list(map(int, input().split())) for _ in range(19)]

for i in range(19):
  for j in range(19):
    if omokPan[i][j] != 0:
      who = omokPan[i][j]

      for k in range(4):
        check = 0
        ny = i + dy[k]
        nx = j + dx[k]
        while 0 <= ny < 19 and  nx < 19 and omokPan[ny][nx] == who:
          check += 1
          ny += dy[k]
          nx += dx[k]
          if check == 4:
            if (0 <= ny < 19 and nx < 19 and omokPan[ny][nx] == who) or (0 <= i - dy[k] < 19 and 0 <= j - dx[k] < 19 and omokPan[i - dy[k]][j - dx[k]] == who): break
            print(who)
            print(f'{i + 1} {j + 1}')
            sys.exit(0)
       
print(0)

'''
- 좌측의 돌도 육목이 아닌지 확인해주어야 한다.
'''
