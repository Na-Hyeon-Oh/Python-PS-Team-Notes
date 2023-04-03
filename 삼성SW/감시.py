# [B_G4] 감시
# https://www.acmicpc.net/problem/15683
'''
N*M (1 <= N, M <= 8) 크기의 사무실에 총 K개의 CCTV가 설치되어 있다.
CCTV(최대 8개)는 5가지 종류로 각각 한 쪽 방향, 양쪽(반대) 방향, 직각 방향, 세 방향, 네 방향에 있는 벽(6)이 아닌 칸 전체(0, 1~5)를 감시할 수 있다.
CCTV가 감시할 수 없는 영역은 사각지대라고 한다.
또 CCTV는 90도 방향으로 회전시킬 수 있다.
사각 지대의 최소 크기는?
* 시간 제한 1초
* 메모리 제한 512MB
'''

from copy import deepcopy

# 북, 동, 남, 
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# cctv 종류에 따른 감시 방향
direction = {
  1: [[0], [1], [2], [3]],
  2: [[0, 2], [1, 3]],
  3: [[0, 1], [1, 2], [2, 3], [3, 0]],
  4: [[0, 1, 2], [1, 2, 3], [2, 3, 0], [3, 0, 1]],
  5: [[0, 1, 2, 3]]
} 

def watch(x, y, dir, candidate):
  for d in dir:
    nx, ny = x, y
    while True:        # 이동할 수 있을 때까지 이동
      nx += dx[d]
      ny += dy[d]
      if nx < 0 or nx >= n or ny < 0 or ny >= m or candidate[nx][ny] == 6: break
      if candidate[nx][ny] == 0: candidate[nx][ny] = '#'

def dfs(n, graph):
  global result
  candidate = deepcopy(graph)

  if n == len(cctv):              # 존재하는 cctv 모두 검사한 경우
    count = 0
    for row in candidate:      
      count += row.count(0)       # 사각지대 개수 세기
    result = min(result, count)
    return

  x, y, type = cctv[n]
  for dir in direction[type]:      # 종류에 따른 감시 구역 검사
    watch(x, y, dir, candidate)
    dfs(n + 1, candidate)
    candidate = deepcopy(graph)

n, m = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

# cctv 위치 저장
cctv = []
for i in range(n):
  for j in range(m):
    target = room[i][j]
    if target != 0 and target != 6:
      cctv.append([i, j, target])
# 사각지대 개수
result = 1e9
dfs(0, room)

print(result)

'''
* 다시 풀어보기
Greedy가 아닌 완전 탐색으로 풀어야 함
- CCTV의 순서와 관계 없이 CCTV의 종류에 따른 각 방향 별로 모든 경우를 DFS 이용해 탐색
'''
