'''
[CD_G2] 코드트리 빵
# BFS
# 시뮬레이션
'''

from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
stores = [list(map(int, input().split())) for _ in range(m)]

# 상, 좌, 우, 하
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

basecamps = []              # basecamp 좌표
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1: basecamps.append([i + 1, j + 1])
locations = []              # 사람 위치
remains = []                # 남은 사람에 대한 idx

def distance(x1, y1, x2, y2):                   
    minDistance = 1e8
    queue = deque()             # bfs
    visited = [[False] * n for _ in range(n)]
    queue.append((x1, y1, 0))                                     # (경로 좌표, 거리) 
    while queue:
        x, y, cnt = queue.popleft()
        if visited[x - 1][y - 1]: continue
        visited[x - 1][y - 1] = True
        if x == x2 and y == y2:                                   # 종점일 경우 최단 거리 update
            minDistance = min(minDistance, cnt)
            continue
        for i in range(4):                                        # 상하좌우 탐색 후 가능한 경로이면 queue에 append
            nx, ny = x + dx[i], y + dy[i]
            if inRange(nx, ny) and graph[nx - 1][ny - 1] != -1: queue.append((nx, ny, cnt + 1))
    return minDistance          # 최단 거리

def minDistanceBaseCampCoor(x, y):                                # (x, y) 편의점에서 최단거리의 basecamp 위치
    minDistance = 1e8
    fromX, fromY = 0, 0
    for [r, c] in basecamps:
        if graph[r - 1][c - 1] < 0: continue                      # 이미 선점된 basecamp일 경우
        compareDistance = distance(r, c, x, y)
        if minDistance > compareDistance:                         # 편의점과 가까운 basecamp일 경우 update
            minDistance = compareDistance
            fromX, fromY = r, c
    graph[fromX - 1][fromY - 1] = -1                              # 최단 거리의 basecamp 접근 불가
    return [fromX, fromY]           # 선택된 basecamp 좌표

def inRange(x, y):
    return x > 0 and x <= n and y > 0 and y <= n

def move(curLoc, dest):
    candidate = []
    minDistance = 1e8
    for i in range(4):                                            # 상하좌우로 한 칸씩 이동한 좌표에서의 최단 거리
        nx, ny = curLoc[0] + dx[i], curLoc[1] + dy[i]
        if inRange(nx, ny) and graph[nx - 1][ny - 1] != -1:
            compareDistance = distance(nx, ny, dest[0], dest[1])
            if minDistance > compareDistance:                     # 다른 방향보다 거리가 짧을 경우 update
                minDistance = compareDistance
                candidate = [nx, ny]
    return candidate

t = 0
arrived = 0
while arrived < m:                                  # 모두 편의점에 도착할 때까지
    t += 1
    
    nextRemains = []
    for idx in remains:                           # 격자에 사람이 있는 경우
        locations[idx] = move(locations[idx], stores[idx])
        if locations[idx] == stores[idx]:                                  # 원하는 편의점에 도착
            arrived += 1
            graph[stores[idx][0] - 1][stores[idx][1] - 1] = -1             # 해당 편의점 접근 불가
        else: nextRemains.append(idx)
    remains = deepcopy(nextRemains)

    if t <= m:                                                                              # t <= m일 때, 
        locations.append(minDistanceBaseCampCoor(stores[t - 1][0], stores[t - 1][1]))       # 사람별로 가고 싶은 편의점과 가까운 Basecamp에 위치 시키기
        remains.append(t - 1)

print(t)
