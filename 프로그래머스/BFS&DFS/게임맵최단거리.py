'''
# L2. 게임 맵 최단거리
N * M 맵에서 벽은 0, 길은 1로 표시되어 있을 때, 
1행 1열에서 시작하여 N행 M열까지 도달하는 최단 거리를 구하시오.
* 존재하지 않는다면 -1 출력
'''

from collections import deque

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def solution(maps):
    n, m = len(maps), len(maps[0])
    queue = deque()
    queue.append((0, 0))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m and maps[nx][ny] != 0 and maps[nx][ny] == 1:           # 방문하지 않은 길
                maps[nx][ny] = maps[x][y] + 1                             # 길은 1로부터 시작하므로 바로 다음 길은 이전 길의 + 1
                queue.append((nx, ny))
    if maps[n - 1][m - 1] == 1: return -1
    return maps[n - 1][m - 1]    
    
'''
** 가장 처음 maps[n - 1][m - 1] 에 도달하는 경우가 최단 거리 
'''
