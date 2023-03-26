# [B_G2] 2048 (Easy)
# https://www.acmicpc.net/problem/12100
'''
N * N (1 <= N <= 20) 크기의 보드에서 
한 번의 이동으로 보드 위에 있는 전체 블록을 상하좌우 네 방향 중 하나로 이동시킬 때,
같은 값을 갖는 두 블록이 충돌하면 두 블록은 하나로 합쳐지고,
한 번의 이동에서 이미 합쳐진 블록은 또 다른 블록과 다시 합쳐질 수 없다.
보드 위의 숫자 블록이 주어질 때, 최대 5번 이동시켜서 얻을 수 있는 가장 큰 블록은?
* 시간 제한 1초
* 메모리 제한 512MB
'''

from collections import deque

def findMax(n, arr):
  global result
  for i in range(n):
    for j in range(n):
      result = max(result, arr[i][j])

def moveBoard(n, arr, dir):
  afterMove = [[0] * n for _ in range(n)]
  if dir == 0 or dir == 1:          # 좌, 우
    for i in range(n):
      row = []
      valid = True                  # 합칠 수 있는지
      for j in range(n):
        target = arr[i][j if dir == 0 else n - 1 - j]
        if valid and len(row) > 0 and row[-1] == target:          # 같은 수면 합치기
          row[-1] *= 2
          valid = False
        elif target > 0:                                          # 아니면 row에 더하기
          row.append(target)
          valid = True
      for k in range(len(row)):                                      # 결과에 반영
        afterMove[i][k if dir == 0 else n - 1 - k] = row[k]
  else:                              # 상, 하
    for i in range(n):
      col = []
      valid = True              
      for j in range(n):
        target = arr[j if dir == 2 else n - 1 - j][i] 
        if valid and len(col) > 0 and col[-1] == target:     
          col[-1] *= 2
          valid = False
        elif target > 0:                                                       
          col.append(target)
          valid = True
      for k in range(len(col)):                             
        afterMove[k if dir == 2 else n - 1 - k][i] = col[k]  
  return afterMove

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

result = 0
findMax(n, board)
boards1, boards2 = deque(), deque()
boards1.append(board)
for step in range(5):
  while boards1 if step % 2 == 0 else boards2:
    state = (boards1 if step % 2 == 0 else boards2).popleft()
    for i in range(4):          # 각 방향으로 이동시켰을 때 블록의 결과
      afterState = moveBoard(n, state, i)
      findMax(n, afterState)
      (boards2 if step % 2 == 0 else boards1).append(afterState)

print(result)


'''
- 전체 경우의 수 : 4 ^ 5 = 1024 => 완전 탐색 가능
- 각 방향(상하좌우)로 이동 결과를 stack을 이용해서 계산하고 그 결과를 initialized 배열(afterMove)에 반영하여 return
- 2차원 배열이 있을 때 (arr) => max(max(arr)) != for {for max=max(max, element)}
'''
