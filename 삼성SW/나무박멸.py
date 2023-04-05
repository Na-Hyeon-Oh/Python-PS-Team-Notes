'''
[B_G4] 나무박멸
- 시뮬레이션
'''


# i. 재귀


# 5 ≤ n ≤ 20
# 1 ≤ m ≤ 1000
# 1 ≤ k ≤ 20, 1 ≤ c ≤ 10
n, m, k, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def inRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def isTree(x, y):
    return inRange(x, y) and graph[x][y] >= 1

def isBlank(x, y):
    return inRange(x, y) and graph[x][y] == 0

def treeGrowth(n):
    for i in range(n):
        for j in range(n):
            if isTree(i, j):                                            # 나무이면 상하좌우의 나무 탐색 후 성장
                cnt = 0
                for l in range(4):
                    ni, nj = i + dx[l], j + dy[l]
                    if isTree(ni, nj): cnt += 1
                graph[i][j] += cnt 

def treeBreeding(n):
    tmp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if isTree(i, j):                                            # 나무이면 상하좌우의 빈 칸 세고 번식
                breedingRange = []                                      # 번식 가능 영역
                for l in range(4):
                    ni, nj = i + dx[l], j + dy[l]
                    if isBlank(ni, nj): breedingRange.append((ni, nj))
                if len(breedingRange) > 0:
                    breedingTreeNo = graph[i][j] // len(breedingRange)      # 번식 가능 영역별 나무 그루
                    for x, y in breedingRange:
                        tmp[x][y] += breedingTreeNo
    for i in range(n):
        for j in range(n):
            if tmp[i][j] != 0: graph[i][j] = tmp[i][j]

def findKillTarget(n, k):
    x, y = 0, 0
    maxKilled = 0
    for i in range(n):
        for j in range(n):
            killed = getKilledTreeNo(n, i, j, k)
            if maxKilled < killed: x, y, maxKilled = i, j, killed
    return x, y, maxKilled

def getKilledTreeNo(n, x, y, k):
    global killedTreeNo
    killedTreeNo = 0

    def dfs(cnt, k, pos, d):
        global killedTreeNo
        if cnt >= k: return                                              # k 이상
        nx, ny = pos[0] + d[0], pos[1] + d[1]
        if not inRange(nx, ny) or graph[nx][ny] <= 0: return            # 범위 밖, 벽, 제초제
        killedTreeNo += graph[nx][ny]
        dfs(cnt + 1, k, [nx, ny], d)
        
    if isTree(x, y):
        killedTreeNo += graph[x][y]
        dfs(0, k, [x, y], [-1, -1])
        dfs(0, k, [x, y], [-1, 1])
        dfs(0, k, [x, y], [1, -1])
        dfs(0, k, [x, y], [1, 1])
        
    return killedTreeNo

def treeKill(n, x, y, k, c):
    global KEEP
    KEEP = -2 - c

    def dfs(cnt, k, pos, d):
        global KEEP
        if cnt >= k: return
        nx, ny = pos[0] + d[0], pos[1] + d[1]
        if not inRange(nx, ny): return
        
        if graph[nx][ny] <= 0: 
            if graph[nx][ny] != -1: graph[nx][ny] = KEEP                  # 전파 도중 벽/나무 x
        else:
            graph[nx][ny] = KEEP
            dfs(cnt + 1, k, [nx, ny], d)

    if isTree(x, y):
        # 제초제 위치 박멸
        graph[x][y] = KEEP
        # dfs 이용해 제초제 대각선 범위 구하기
        dfs(0, k, [x, y], [-1, -1])
        dfs(0, k, [x, y], [-1, 1])
        dfs(0, k, [x, y], [1, -1])
        dfs(0, k, [x, y], [1, 1])

def removeKill(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] < -2: graph[i][j] += 1
            elif graph[i][j] == -2: graph[i][j] = 0

result = 0
for _ in range(m):
    treeGrowth(n)
    treeBreeding(n)
    x, y, killed = findKillTarget(n, k)
    result += killed
    # 제초제 update
    treeKill(n, x, y, k, c)
    removeKill(n)
    
print(result)



# ii. for 반복문 -> 시간 성능 i보다 4배 빨라짐

# 5 ≤ n ≤ 20
# 1 ≤ m ≤ 1000
# 1 ≤ k ≤ 20, 1 ≤ c ≤ 10
n, m, k, c = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def inRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def isTree(x, y):
    return inRange(x, y) and graph[x][y] >= 1

def isWall(x, y):
    return inRange(x, y) and graph[x][y] == -1

def isBlank(x, y):
    return inRange(x, y) and graph[x][y] == 0

def treeGrowth(n):
    for i in range(n):
        for j in range(n):
            if isTree(i, j):                                            # 나무이면 상하좌우의 나무 탐색 후 성장
                cnt = 0
                for l in range(4):
                    ni, nj = i + dx[l], j + dy[l]
                    if isTree(ni, nj): cnt += 1
                graph[i][j] += cnt 

def treeBreeding(n):
    tmp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if isTree(i, j):                                            # 나무이면 상하좌우의 빈 칸 세고 번식
                breedingRange = []                                      # 번식 가능 영역
                for l in range(4):
                    ni, nj = i + dx[l], j + dy[l]
                    if isBlank(ni, nj): breedingRange.append((ni, nj))
                if len(breedingRange) > 0:
                    breedingTreeNo = graph[i][j] // len(breedingRange)      # 번식 가능 영역별 나무 그루
                    for x, y in breedingRange:
                        tmp[x][y] += breedingTreeNo
    for i in range(n):
        for j in range(n):
            if tmp[i][j] != 0: graph[i][j] = tmp[i][j]

def findKillTarget(n, k):
    x, y = 0, 0
    maxKilled = 0
    for i in range(n):
        for j in range(n):
            killed = getKilledTreeNo(n, i, j, k)
            if maxKilled < killed: x, y, maxKilled = i, j, killed
    return x, y, maxKilled

def getKilledTreeNo(n, x, y, k):
    killedTreeNo = 0   
    if isTree(x, y):
        killedTreeNo += graph[x][y]
        for i in range(1, k + 1):
            nx, ny = x - i, y - i
            if not inRange(nx, ny) or graph[nx][ny] <= 0: break
            elif isTree(nx, ny): killedTreeNo += graph[nx][ny]
        for i in range(1, k + 1):
            nx, ny = x + i, y - i
            if not inRange(nx, ny) or graph[nx][ny] <= 0: break
            elif isTree(nx, ny): killedTreeNo += graph[nx][ny]
        for i in range(1, k + 1):
            nx, ny = x - i, y + i
            if not inRange(nx, ny) or graph[nx][ny] <= 0: break
            elif isTree(nx, ny): killedTreeNo += graph[nx][ny]
        for i in range(1, k + 1):
            nx, ny = x + i, y + i
            if not inRange(nx, ny) or graph[nx][ny] <= 0: break
            elif isTree(nx, ny): killedTreeNo += graph[nx][ny]
        
    return killedTreeNo

def treeKill(n, x, y, k, c):
    KEEP = -2 - c

    def dfs(cnt, k, pos, d):
        global KEEP
        if cnt >= k: return
        nx, ny = pos[0] + d[0], pos[1] + d[1]
        if not inRange(nx, ny): return
        
        if graph[nx][ny] <= 0: 
            if not isWall(nx, ny): graph[nx][ny] = KEEP                  # 전파 도중 벽/나무 x
        else:
            graph[nx][ny] = KEEP
            dfs(cnt + 1, k, [nx, ny], d)

    if isTree(x, y):
        # 제초제 위치 박멸
        graph[x][y] = KEEP
        for i in range(1, k + 1):
            nx, ny = x - i, y - i
            if isTree(nx, ny): graph[nx][ny] = KEEP
            else:
                if not inRange(nx, ny) or isWall(nx, ny): break
                graph[nx][ny] = KEEP
                break
        for i in range(1, k + 1):
            nx, ny = x + i, y - i
            if isTree(nx, ny): graph[nx][ny] = KEEP
            else:
                if not inRange(nx, ny) or isWall(nx, ny): break
                graph[nx][ny] = KEEP
                break
        for i in range(1, k + 1):
            nx, ny = x - i, y + i
            if isTree(nx, ny): graph[nx][ny] = KEEP
            else:
                if not inRange(nx, ny) or isWall(nx, ny): break
                graph[nx][ny] = KEEP
                break
        for i in range(1, k + 1):
            nx, ny = x + i, y + i
            if isTree(nx, ny): graph[nx][ny] = KEEP
            else:
                if not inRange(nx, ny) or isWall(nx, ny): break
                graph[nx][ny] = KEEP
                break

def removeKill(n):
    for i in range(n):
        for j in range(n):
            if graph[i][j] < -2: graph[i][j] += 1
            elif graph[i][j] == -2: graph[i][j] = 0

result = 0
for _ in range(m):
    treeGrowth(n)
    treeBreeding(n)
    x, y, killed = findKillTarget(n, k)
    result += killed
    # 제초제 update
    treeKill(n, x, y, k, c)
    removeKill(n)
    
print(result)
