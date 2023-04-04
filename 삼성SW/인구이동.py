# [B_G5] 인구 이동
# https://www.acmicpc.net/problem/16234
'''
N * N (1 <= N <= 50) 크기의 땅이 있고 각 땅에는 나라가 하나씩 존재하며 각 나라에는 A[r][c]명이 살고 있다.
하루동안 인구 이동이 다음과 같이 진행될 때 인구 이동이 며칠 동안 발생하는가?
1. 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면 (1 <= L <= R <= 100), 두 나라가 공유하는 국경선을 하루동안 연다.
2. 국경선이 모두 열렸다면 인구 이동을 시작한다.
3. 국경선이 열려있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안 연합이라 한다.
4. 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. (버림)
5. 연합을 해체하고, 모든 국경선을 닫는다.
* 시간 제한 2초
* 메모리 제한 512MB
'''

from collections import deque

def bfs(arr):
  global n, L, R
  queue = deque()
  visited = [[False] * n for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if visited[i][j] == False:
        # 연합국가 bfs로 생성
        queue.append((i, j))
        union = []
        while queue:
          r, c = queue.popleft()
          if visited[r][c]: continue       
          visited[r][c] = True
          union.append([r, c])
          for k in range(4):            # 국경선 인접국 탐색
            nr, nc = r + dr[k], c + dc[k]
            if nr >= 0 and nr < n and nc >= 0 and nc < n and visited[nr][nc] == False:
              populationDiff = abs(world[nr][nc] - world[r][c])
              if populationDiff >= L and populationDiff <= R: queue.append((nr, nc))
        arr.append(union)
      
# 상, 하, 좌, 우          
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

n, L, R = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(n)]

result = 0
while True:
  unions = []
  bfs(unions)
  if len(unions) == n * n: break                      # 연합국가가 없을 때 종료
  result += 1
  for union in unions:                                # 연합국가별로 인구 이동
    sum = 0
    for r, c in union: sum += world[r][c]
    population = int(sum / len(union))
    for r, c in union: world[r][c] = population
  
print(result)


'''
bfs로 탐색했을 때 연합국이 있을 때까지  반복하고 몇 번 반복했는지 
'''
