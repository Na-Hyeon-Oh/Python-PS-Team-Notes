# 지뢰 찾기
# https://www.acmicpc.net/problem/4396
'''
n * n의 격자 위에서 지뢰 찾기가 이루어질 때, m개의 지뢰가 숨겨져 있다.
지뢰가 없는 지점을 건드리면, 그 곳의 상하좌우, 혹은 대각선으로 인접한 8개의 칸에 지뢰가 몇 개 있는지 알려주는 0~8 숫자가 함께 나타난다.
해당 지뢰찾기 게임의 플레이된 게임 정보를 읽어 해당하는 격자를 출력하라.
* n <= 10
* 제한 시간 1초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

n = int(input())
pan = [list(str(input())) for _ in range(n)]
player = [list(str(input())) for _ in range(n)]

dirX = [-1, 0, 1, -1, 1, -1, 0, 1]
dirY = [-1, -1, -1, 0, 0, 1, 1, 1]

result = []
isFail = False
for i in range(n):
  row = []
  for j in range(n):
    if player[i][j] == 'x':
      if pan[i][j] == '*': isFail = True
      check = 0
      for k in range(8):
        x = j + dirX[k]
        y = i + dirY[k]
        if x >= 0 and x < n and y >= 0 and y < n and pan[y][x] == '*': check += 1
      row.append(str(check))  
    else: row.append('.')
  result.append(row)

if isFail != False: 
  for i in range(n):
    for j in range(n):
      if pan[i][j] == '*': print('*', end='')
      else: print(result[i][j], end='')
    print()
else:
  for row in result: print(''.join(row))


'''

'''

# 빙고, 지뢰 찾기, 단어 뒤집기 2, 오목, 배열 돌리기 1, 달력
# 상어 초등학교, 홀수 홀릭 호석, 빗물, ZOAC, 트리 순회, 폴더 정리(small), HTML 파싱, 마법사 상어와 블리자드
