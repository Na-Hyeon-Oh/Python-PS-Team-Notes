# [B_G4] 연구소
# https://www.acmicpc.net/problem/14502
'''
N*M (3 <= N, M <= 8)크기의 연구소에서 바이러스가 유출되었는데 확산을 막기 위해 연구소에 벽을 세우려고 한다.
연구소의 한 칸은 빈 칸(0)이거나 벽(1), 바이러스(2)로 이루어져 있다.
바이러스는 상하좌우 인접한 빈칸으로 모두 퍼져나갈 수 있다.
벽을 3개 세울 때, 바이러스가 퍼질 수 없는 안전 영역의 크기의 최댓값을 구하시오.
* 시간 제한 2초
* 메모리 제한 512MB
'''

from copy import deepcopy
from collections import deque

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def combination(arr, r):              # 재귀 활용
  result = []
  if r > len(arr): return result
  if r == 1:
    for element in arr:
      result.append([element])
  elif r > 1:
    for i in range(len(arr) - r + 1):
      for j in combination(arr[i + 1:], r - 1):
        result.append([arr[i]] + j)

  return result

def bfs(arr):
  q = deque()
  visited = [[False] * m for _ in range(n)]
  for i in range(n):          # 바이러스 찾기 -> 큐
    for j in range(m):
      if arr[i][j] == 2: q.append((i, j))
  while q:                    # 바이러스 전파 영역
    x, y = q.popleft()
    if visited[x][y]: continue
    visited[x][y] = True
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if nx >= 0 and nx < n and ny >= 0 and ny < m and visited[nx][ny] == False:
        if arr[nx][ny] == 0: 
          arr[nx][ny] = 2
          q.append((nx, ny))

def safeZone(arr):
  cnt = 0
  for i in range(n):
    for j in range(m):
      if arr[i][j] == 0: cnt += 1
  return cnt

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 0 위치 찾기
zeroLocation = []
for i in range(n):
  for j in range(m):
    if arr[i][j] == 0: zeroLocation.append((i, j))
# 벽 설치 가능 조합
cases = combination(zeroLocation, 3)

maxResult = 0
for case in cases:
  possibleCase = deepcopy(arr)
  # 벽 설치
  for x, y in case:
    possibleCase[x][y] = 1
  bfs(possibleCase)        # 바이러스 전파  
  maxResult = max(maxResult, safeZone(possibleCase))        # 안전영역 크기

print(maxResult)

'''
n, m  범위가 작으므로 벽을 설치하는 모든 경우의 수에 대해서 바이러스를 전파 시키고, 안전영역의 크기를 계산하여 그 최댓값 출력
'''
