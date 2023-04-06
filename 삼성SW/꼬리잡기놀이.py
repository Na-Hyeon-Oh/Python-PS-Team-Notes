'''
[CT_G1] 꼬리잡기놀이
# 시뮬레이션
# dfs
'''

n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

teams = [[] for _ in range(m)]            # dfs로 탐색한 팀 가능 범위 좌표
teamPopulation = [0] * m                  # 각 팀의 인원
teamHeaderIdx = [0] * m                   # 각 팀의 header idx

# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[False] * n for _ in range(n)]
def dfs(idx, x, y, value, order):         # (팀 idx, 탐색하려는 x,y 좌표, 이전 탐색 좌표의 grid 값, 몇번째 탐색인지)
    if visited[x][y] or idx >= m: return
    if order == 1 or (value == 1 and grid[x][y] == 2) or (value == 2 and grid[x][y] in [2, 3]) or (value == 3 and grid[x][y] == 4) or (value == 4 and grid[x][y] == 4):
        visited[x][y] = True
        teams[idx].append([x, y])
        if grid[x][y] <= 3: teamPopulation[idx] += 1
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < n: dfs(idx, nx, ny, grid[x][y], order + 1)

def findDirection(idx):                 # head -> tail 방향
    headIdx = teamHeaderIdx[idx]
    teamScope = len(teams[idx])
    a = (headIdx + 1) % teamScope
    [x, y] = teams[idx][a]
    return 1 if grid[x][y] == 2 else -1

def move():
    for idx in range(len(teams)):
        teamScope = len(teams[idx])
        direction = findDirection(idx)
        teamHeaderIdx[idx] = (teamHeaderIdx[idx] - direction) % teamScope         # header 위치 update
        for j in range(teamScope):                                                # grid update
            i = (teamHeaderIdx[idx] + direction * j) % teamScope                  # teams[idx] 상 idx
            [x, y] = teams[idx][i]
            if j == 0: grid[x][y] = 1             
            elif j < teamPopulation[idx] - 1: grid[x][y] = 2
            elif j == teamPopulation[idx] - 1: grid[x][y] = 3
            else: grid[x][y] = 4
            
def throwBall(throwDir, idx):
    for i in range(n):
        r, c = 0, 0
        if throwDir == 0: r, c = idx, i
        elif throwDir == 1: r, c = n - 1 - i, idx
        elif throwDir == 2: r, c = n - 1 - idx, n - 1 - i
        elif throwDir == 3: r, c = i, n - 1 - idx 
        if grid[r][c] > 0 and grid[r][c] < 4: return [r, c]                        # 해당 행/열에서 처음으로 공을 받은 사람 좌표
    return -1

def kth(pos):
    for idx in range(len(teams)):
        for [x, y] in teams[idx]:             # 포함된 team을 찾으면
            if [x, y] == pos:   
                direction = findDirection(idx)
                headIdx = teamHeaderIdx[idx]
                for i in range(len(teams[idx])):        # 해당 team에서 header로부터 몇 번째에 포함되어 있는지 탐색
                    j = (headIdx + direction * i) % len(teams[idx])
                    if pos == teams[idx][j]: return [i + 1, idx]
    return -1

def swapHeadTail(idx):
    direction = findDirection(idx)
    tailIdx = teamHeaderIdx[idx]
    headIdx = teamHeaderIdx[idx] = (tailIdx + direction * teamPopulation[idx] - direction) % len(teams[idx])
    [x1, y1], [x2, y2] = teams[idx][headIdx], teams[idx][tailIdx]   # teams[idx] update
    grid[x1][y1], grid[x2][y2] = 1, 3                               # grid update

# team 구성
cnt = 0
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            dfs(cnt, i, j, 1, 1)
            cnt += 1
            visited = [[False] * n for _ in range(n)]     # 팀 구성할 때마다 visitied initialize
    if cnt == m: break

score = 0
for i in range(k):
    move()                                                  # 팀마다 한 칸씩 움직이기
    receiver = throwBall((i // n) % 4, i % n)               # 공 던지고 받는 사람이 있는지 확인 
    if receiver != -1:                                      # 있다면 사람이 어떤 팀의 몇 번째인지 확인하여 score update
        receiverOrder = kth(receiver)
        if receiverOrder != -1:
            score += receiverOrder[0] ** 2 
            swapHeadTail(receiverOrder[1])                  # 해당 팀의 header tail 바꾸기
print(score)
