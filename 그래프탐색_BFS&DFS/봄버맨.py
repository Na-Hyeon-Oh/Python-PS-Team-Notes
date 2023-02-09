# 봄버맨
# https://www.acmicpc.net/problem/16918
'''
R*C 직사각형 격자판 위에 있을 때, 각 격자의 칸은 비어있거나(.) 폭탄(O)이 들어있다.
폭탄이 든 칸은 3초가 지난 후 폭발하고, 폭발한 이후에는 폭탄이 있던 칸과 인접한 4개의 칸은 파괴된다.
만약 폭탄이 폭발했을 때, 인접한 칸에 폭탄이 있는 경우에는 인접한 폭탄은 폭발 없이 파괴되므로 연쇄 반응은 없다.
봄버맨이 다음과 같이 행동할 때, 폭탄을 설치해놓은 초기 상태를 보고 N초가 흐른 후의 격자판 상태를 구하라.
1. 가장 처음에 봄버맨은 일부 칸에 폭탄을 설치해놓는다.
2. 다음 1초동안 아무것도 하지 않는다.
3. 다음 1초동안 폭탄이 설치되어 있지 않은 모든 칸에 폭탄을 설치한다.
4. 1초가 지난 후 3초 전에 설치된 폭탄이 모두 폭발한다.
5. 3, 4를 반복한다.
* 1 <= R, C, N <= 200
* 제한 시간 2초
'''

import sys
sys.setrecursionlimit(100000)

def input():
  return sys.stdin.readline().rstrip()

# 1 level만 탐색
def bomb(y, x):
  global r, c
  resultGrid[y][x] = 0
  for i in range(4):
    ny = y + dy[i]
    nx = x + dx[i]
    if ny < 0 or nx < 0 or ny >= r or nx >= c: continue
    if(resultGrid[ny][nx] == 2): bomb(ny, nx)
    resultGrid[ny][nx] = 0
  
r, c, n = map(int, input().split())
grid = [list(input()) for _ in range(r)]

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
resultGrid = []
for i in range(r):
  row = []
  for j in range(c):
    if grid[i][j] == 'O': row.append(1)
    else: row.append(0)
  resultGrid.append(row)

for t in range(2, n+1):
  for i in range(r):
    for j in range(c): 
      if t % 2 == 0:          # 3번 규칙
        resultGrid[i][j] += 1
      else:                   # 4번 규칙
        if resultGrid[i][j] == 2: bomb(i, j)
    
for i in range(r):
  for j in range(c):
    if resultGrid[i][j] != 0: print('O', end='')
    else: print('.', end='')
  print()

'''
폭탄이 있는 경우는 1, 없는 경우는 0로 grid를 저장한 resultGrid 2차원 배열로 저장한다.
1초가 지나면 자기 자신, 2초가 지나면 모두 폭탄이 차 있는 모습, 3초가 지나면 처음의 폭탄이 터진 결과, 4초가 지나면 모두 폭탄이 차 있는 모습... 이므로
짝수초일 때는 모두 폭탄이 차있고, 홀수초일 때는 3초 전에 존재한 폭탄이 터진 결과를 보여줄 수 있다.
모두 폭탄을 채울 때 생기는 폭탄과 이전에 넣은 폭탄을 구분하기 위해, 짝수초일 때는 resultGrid의 해당 값을 2로 바꾸어주었고, 홀수초일 때 2인 값을 가진 격자칸에서는 폭탄이 제거(bomb)되어야 한다.
제거 후에는 0으로 바꾸어 주는데, 이 때 만약 2의 값을 가지는 칸이 연속해서 존재할 경우, 해당 칸을 recursive하게 다시 bomb해줄 수 있도록 하였다.
'''

