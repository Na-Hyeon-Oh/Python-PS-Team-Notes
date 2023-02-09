# 쉬운 최단거리
# https://www.acmicpc.net/problem/14940
'''
지도가 주어지면 모든 지점에 대해서 가로와 세로로만 움직일 수 있을 때, 목표지점(2)까지의 거리를 구하여라.
0은 갈 수 없는 땅이고, 1은 갈 수 있는 땅이다.
* 2 <= n, m <= 1,000
* 제한 시간 1초
'''

import sys
from collections import deque

def input():
  return sys.stdin.readline().rstrip()

# 너비 우선 탐색
# 탐색하면서 graph 값에 목표지점까지의 최단 거리 값으로 업데이트
def bfs(y, x):
  global n, m
  queue = deque([[y, x]])
  visited[y][x] = True
  graph[y][x] = 0        # 목표지점은 거리 0
  while queue:
    current = queue.popleft()
    for i in range(4):      # 상하좌우
      ny = current[0] + dy[i]
      nx = current[1] + dx[i]
      if 0 <= ny < n and 0 <= nx < m:
        if graph[ny][nx] == -1: 
          graph[ny][nx] = graph[current[0]][current[1]] + 1        # 해당 노드에서 목표지점까지의 최단 거리 = 이전 노드에서 목표지점까지의 최단 거리 + 1
          queue.append([ny, nx])
    
# 목표 지점 구하기 : 2인 값을 가진 graph 좌표 구하기
def findGoal():
  global n, m
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 2: return i, j

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

goalY, goalX = findGoal()
visited = [[False] * (m) for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
# 땅(1)이지만 도달할 수 없는 위치는 -1로 출력해야 하므로 땅인 경우 default(방문하지 않은 경우)로 -1을 치환하여 저장
for i in range(n):
  for j in range(m):
    if graph[i][j] == 1: graph[i][j] = -1        
# 목표지점에서 시작하여 최단 거리 구하기 -> bfs
bfs(goalY, goalX)

for i in range(n):
  for j in range(m):
    print(graph[i][j], end=" ")
  print()

'''

'''

