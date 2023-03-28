# [B_G4] 뱀
# https://www.acmicpc.net/problem/3190
'''
N * N (2 <= N <= 100) 보드에서 길이가 1인 뱀이 최상단좌측에서 시작하여 기어다니며 사과를 먹으면 길이가 늘어난다.
뱀의 이동은 다음의 규칙을 따른다.
- 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
- 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
- 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이가 변하지 않는다.
- 만약 뱀이 벽이나 자기 자신의 몸과 부딪히면 게임이 끝난다.
사과의 위치(0 <= K(사과의 개수) <= 100)와 뱀의 이동 경로(1 <= L(뱀의 방향 변환 횟수) <= 100, X(게임 시작 시간으로부터의 시간) <= 10,000, C(X초 뒤에 회전 방) = L or D)가 주어질 때 게임이 몇 초에 끝나는지 계산하라.
* 시간 제한 1초
* 메모리 제한 128MB
'''

# 우, 하, 좌, 상
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n = int(input())
k = int(input())
board = [[False] * n for _ in range(n)]
for _ in range(k):
  i, j = map(int, input().split())
  board[i - 1][j - 1] = True
l = int(input())
move = dict()
for _ in range(l):
  x, c = input().split()
  move[int(x)] = c

t = 0
x, y = 0, 0             # head 위치
snakeBody = []          # head를 제외한 snake 몸통
dirIdx = 0
while True:
  t += 1
  # 뱀 이동
  x += dx[dirIdx]
  y += dy[dirIdx] 
  moveEnable = True
  for body in snakeBody:                                 # 자기 자신의 몸과 부딪히는 경우
    if x == body[0] and y == body[1]:
      moveEnable = False
      break
  if moveEnable and (x >= 0 and x < n and y >= 0 and y < n):
    if board[y][x]:                                       # 사과를 먹는 경우
      snakeBody.append([x - dx[dirIdx], y - dy[dirIdx]])
      board[y][x] = False
    else:                                                 # 사과를 안 먹어서 몸통을 불리지 않는 경우
      for i in range(len(snakeBody)):
        if i < len(snakeBody) - 1: snakeBody[i] = snakeBody[i + 1]
        else: snakeBody[-1] = [x - dx[dirIdx], y - dy[dirIdx]]
    if t in move:                                           # 방향 바꾸는 경우
      if move[t] == 'L': dirIdx = (dirIdx - 1) % 4          # 왼쪽
      else: dirIdx = (dirIdx + 1) % 4                       # 오른쪽
  else: break                                               # 벽에 부딪히는 경우
  
print(t)



'''
<구현, 자료구조, 시뮬레이션>
- head 기준으로 코드 설계 -> 72ms
- 뱀에 대한 리스트로 코드 수정하면 시간 덜 걸림 (4-50ms) 
- 1시간 30분 소요
'''
