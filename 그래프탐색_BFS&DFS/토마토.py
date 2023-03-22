# [B_G5] 토마토 
# https://www.acmicpc.net/problem/7576

from collections import deque

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(m)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
  q = deque()
  for i in range(m):
    for j in range(n):
      if graph[i][j] == 1: q.append((i, j))
  
  visited = [[False] * n for _ in range(m)]
  cnt = 0
  while q:
    for _ in range(len(q)):
      x, y = q.popleft()
      visited[x][y] = True
      for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < m and ny >= 0 and ny < n and visited[nx][ny] == False and graph[nx][ny] == 0:
          graph[nx][ny] = 1
          q.append((nx, ny))
    if len(q) > 0: cnt += 1

  isAll = True
  for i in range(m):
    for j in range(n):
      if graph[i][j] == 0: 
        isAll = False
        break
    if isAll == False: break
  if isAll: print(cnt)
  else: print(-1)

bfs()
