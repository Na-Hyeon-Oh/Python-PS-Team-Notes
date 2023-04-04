from copy import deepcopy

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def grouping(n):
    groupID = []
    groups = []
    visited = [[False] * n for _ in range(n)]

    def dfs(idx, i, j):
        if visited[i][j]: return
        if grid[i][j] == groupID[idx]: 
            if idx < len(groups): groups[idx].append((i, j))
            else: groups.append([(i, j)])
            visited[i][j] = True
            for k in range(4):  
                ni, nj = i + dy[k], j + dx[k]
                if ni >= 0 and ni < n and nj >= 0 and nj < n: dfs(idx, ni, nj)
    
    for i in range(n):
        for j in range(n):
            if not visited[i][j]: 
                groupID.append(grid[i][j])
                dfs(len(groupID) - 1, i, j)
    return groupID, groups

def combination(arr, r):
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

def score(g1, g2, a, b):
    return (len(g1) + len(g2)) * a * b * commonSide(g1, g2)

def commonSide(g1, g2):
    result = 0
    for y1, x1 in g1:
        for y2, x2 in g2:
            if (y1 == y2 and abs(x1 - x2) == 1) or (x1 == x2 and abs(y1 - y2) == 1): result += 1
    return result

def rotate(n):
    k = int(n / 2)                  # core idx
    # + 회전
    rotateCounterClockwise(n)      
    # ㅁ 회전
    rotateClockwise(0, 0, k - 1, k - 1)
    rotateClockwise(k + 1, 0, n - 1, k - 1)
    rotateClockwise(0, k + 1, k - 1, n - 1)
    rotateClockwise(k + 1, k + 1, n - 1, n - 1)

def rotateCounterClockwise(n):
    tmpGrid = deepcopy(grid)
    k = int(n / 2)                  
    for i in range(n):              
        grid[k][i] = tmpGrid[i][k]
        grid[i][k] = tmpGrid[k][n - 1 - i]

def rotateClockwise(x1, y1, x2, y2):
    tmpGrid = deepcopy(grid)
    sx, sy, ex, ey = x1, y1, x2, y2                 # 정사각형의 시작점, 끝점 좌표
    while ex > sx and ey > sy:
        for i in range(ex - sx  + 1): 
            grid[sy + i][ex] = tmpGrid[sy][sx + i]
            grid[ey][ex - i] = tmpGrid[sy + i][ex]
            grid[sy + i][sx] = tmpGrid[ey][sx + i]
            grid[sy][ex - i] = tmpGrid[sy + i][sx]
        sx, sy, ex, ey = sx + 1, sy + 1, ex - 1, ey - 1

n = int(input())                        # 3 ≤ n ≤ 29
grid = [list(map(int, input().split())) for _ in range(n)]

result = 0
for _ in range(4):
    groupID, groups = grouping(n)

    idxArr = combination(list(range(len(groupID))), 2)
    for a, b in idxArr:
        result += score(groups[a], groups[b], groupID[a], groupID[b])

    rotate(n)

print(result)
