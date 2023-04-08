'''
[CT_G2] 색깔 폭탄
# BFS
# 시뮬레이션 
'''

from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 우, 하, 좌, 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def inRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def bfs():
    result = []
    queue = deque()
    visited = [[False] * n for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if not visited[n - 1 - i][j] and graph[n - 1 - i][j] > 0:               # 반드시 빨간 폭탄이 아닌 다른 색 폭탄이 포함되어야 함
                queue.append((n - 1 - i, j, graph[n - 1 - i][j]))                   # 행이 큰 것부터, 열이 작은 것부터
                result.append([])
                while queue:
                    x, y, color = queue.popleft()
                    if visited[x][y]: continue
                    visited[x][y] = True                  
                    result[cnt].append((x, y))
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if inRange(nx, ny) and not visited[nx][ny] and (graph[nx][ny] == color or graph[nx][ny] == 0): queue.append((nx, ny, color))
                # 폭탄 묶음인지 확인
                if len(result[cnt]) >= 2: cnt += 1
                else: result.pop()
                for k in range(n):                              # 빨간 폭탄은 중복하여 group에 포함될 수 있음
                    for l in range(n): 
                        if visited[k][l] and graph[k][l] == 0: visited[k][l] = False
    return result

def maximumGroup(groups):
    maxLen = max([len(group) for group in groups])
    maximumGroupIdx = 0
    minRed = maxLen
    for idx in range(len(groups)):
        if len(groups[idx]) == maxLen:                                              # 크기가 큰 group 중
            cnt = 0
            for x, y in groups[idx]:    
                if graph[x][y] == 0: cnt += 1
            if minRed > cnt: 
                maximumGroupIdx = idx                                               # 빨간 폭탄 개수 최소
                minRed = cnt                                                        # update
    return groups[maximumGroupIdx]        

def removeGroup(group):
    for x, y in group:
        graph[x][y] = -2                                                            # 빈칸 : -2
    return len(group)                                                               # 터지는 폭탄 개수 반환

def fall():
    for i in range(n):
        for j in range(n):
            if graph[i][j] == -2:                                                   # 빈칸일 경우 그 위의 폭탄들이 중력의 힘을 받음
                x, y = i - 1, j
                while inRange(x, y) and graph[x][y] != -1:
                    graph[x + 1][y] = graph[x][y]
                    graph[x][y] = -2
                    x -= 1

def rotate():
    tmpGraph = deepcopy(graph)
    for i in range(n // 2):
        for j in range(n - 2 * i):
            graph[i + j][i] = tmpGraph[i][n - 1 - i - j]
            graph[n - 1 - i][i + j] = tmpGraph[i + j][i]
            graph[n - 1 - i - j][n - 1 - i] = tmpGraph[n - 1 - i][i + j]
            graph[i][n - 1 - i - j] = tmpGraph[n - 1 - i - j][n - 1 - i]

score = 0
groups = bfs()
while len(groups) > 0:
    group = maximumGroup(groups)
    score += removeGroup(group) ** 2
    fall()
    rotate()
    fall()
    groups = bfs()

print(score)
