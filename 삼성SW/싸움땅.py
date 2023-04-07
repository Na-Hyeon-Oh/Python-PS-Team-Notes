'''
[CT_G2] 싸움땅
# 시뮬레이션
'''

n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
players = [list(map(int, input().split())) for _ in range(m)]               # [x, y, d, s]

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def inRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def playerMove(idx):
    [x, y, d, s] = players[idx]
    nx, ny = x + dx[d], y + dy[d]                               # player 방향으로 한 칸 이동
    if not inRange(nx, ny):                                     # 격자 밖으로 나가는 경우,
        d = (d + 2) % 4
        nx, ny = x + dx[d], y + dy[d]                           # player 방향 바꾸고 한 칸 이동
    players[idx] = [nx, ny, d, s]
    return [nx, ny]
    
def isPlayer(idx, pos):
    for i in range(m):
        if i != idx and players[i][0] == pos[0] and players[i][1] == pos[1]: return i            # player 있으면 해당 player index 반환
    return -1                                                                                    # player 없으면 -1 반환

def isGun(idx, pos):
    gun = grid[pos[0]][pos[1]]
    if len(gun) > 0:                                             # gun이 존재하면,
        if idx in playerGun:                                     # player가 gun을 가지고 있을 때,
            currentGun = playerGun[idx]
            if max(gun) > currentGun:                            # 기존 gun보다 셀 경우 바꿈
                playerGun[idx] = max(gun)
                grid[pos[0]][pos[1]].remove(max(gun))
                grid[pos[0]][pos[1]].append(currentGun)
        else:                                                    # player가 gun이 없을 때,
            playerGun[idx] = max(gun)                            # 총 획득
            grid[pos[0]][pos[1]].remove(max(gun))

def fighting(p1, p2):
    s1, s2 = players[p1][3], players[p2][3]                                                                 # 초기 능력치
    g1, g2 = playerGun[p1] if p1 in playerGun else 0, playerGun[p2] if p2 in playerGun else 0               # 총의 공격력
    power1, power2 = s1 + g1, s2 + g2
    winner, loser = p1, p2
    if (power1 < power2) or (power1 == power2 and s1 < s2): winner, loser = p2, p1                          # player2가 이기는 경우
    
    # winner: 공격력 차이만큼 포인트 획득
    winnerPoint = abs(power1 - power2)
    points[winner] += winnerPoint

    # loser
    [x, y, d, s] = players[loser]
    if loser in playerGun:
        gunPower = playerGun[loser]
        grid[x][y].append(gunPower)
        playerGun.pop(loser, None)                  # 총 반환
    nx, ny = x + dx[d], y + dy[d]
    playerExist = isPlayer(loser, [nx, ny])
    while not inRange(nx, ny) or playerExist >= 0:  # 이동 가능한 방향, 좌표 찾기
        d = (d + 1) % 4
        nx, ny = x + dx[d], y + dy[d]
        playerExist = isPlayer(loser, [nx, ny])
    players[loser] = [nx, ny, d, s]
    isGun(loser, [nx, ny])                          # 움직인 칸에서 총이 있는지 확인하고 있다면 가지기

    # winner: 총 바꾸기
    isGun(winner, [x, y])

for i in range(n):                      # 총이 있는 경우 list로 조정
    for j in range(n):
        if grid[i][j] > 0: grid[i][j] = [grid[i][j]]
        else: grid[i][j] = []
for i in range(m):                      # player 좌표 값 조정
    players[i][0] -= 1
    players[i][1] -= 1

playerGun = dict()
points = [0] * m
for j in range(k):          # simulate
    for i in range(m):              # player마다
        pos = playerMove(i)         # 한 칸 이동
        fight = isPlayer(i, pos)    
        if fight >= 0: fighting(i, fight)       # 이동한 칸에 player가 있다면, fight
        else: isGun(i, pos)                     # 이동한 칸에 player가 없다면, 총 확인 후 있다면 획득
                          
print(*points)


'''
# dict -> list
n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
players = [list(map(int, input().split())) for _ in range(m)]               # [x, y, d, s]

# 상, 우, 하, 좌
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def inRange(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def playerMove(idx):
    [x, y, d, s] = players[idx]
    nx, ny = x + dx[d], y + dy[d]                               # player 방향으로 한 칸 이동
    if not inRange(nx, ny):                                     # 격자 밖으로 나가는 경우,
        d = (d + 2) % 4
        nx, ny = x + dx[d], y + dy[d]                           # player 방향 바꾸고 한 칸 이동
    players[idx] = [nx, ny, d, s]
    return [nx, ny]
    
def isPlayer(idx, pos):
    for i in range(m):
        if i != idx and players[i][0] == pos[0] and players[i][1] == pos[1]: return i            # player 있으면 해당 player index 반환
    return -1                                                                                    # player 없으면 -1 반환

def isGun(idx, pos):
    gun = grid[pos[0]][pos[1]]
    if len(gun) > 0:                                             # gun이 존재하면,
        if playerGun[idx] != 0:                                  # player가 gun을 가지고 있을 때,
            currentGun = playerGun[idx]
            if max(gun) > currentGun:                            # 기존 gun보다 셀 경우 바꿈
                playerGun[idx] = max(gun)
                grid[pos[0]][pos[1]].remove(max(gun))
                grid[pos[0]][pos[1]].append(currentGun)
        else:                                                    # player가 gun이 없을 때,
            playerGun[idx] = max(gun)                            # 총 획득
            grid[pos[0]][pos[1]].remove(max(gun))

def fighting(p1, p2):
    s1, s2 = players[p1][3], players[p2][3]                                                                 # 초기 능력치
    g1, g2 = playerGun[p1], playerGun[p2]                                                                    # 총의 공격력
    power1, power2 = s1 + g1, s2 + g2
    winner, loser = p1, p2
    if (power1 < power2) or (power1 == power2 and s1 < s2): winner, loser = p2, p1                          # player2가 이기는 경우
    
    # winner: 공격력 차이만큼 포인트 획득
    winnerPoint = abs(power1 - power2)
    points[winner] += winnerPoint

    # loser
    [x, y, d, s] = players[loser]
    if playerGun[loser] != 0: 
        gunPower = playerGun[loser]
        grid[x][y].append(gunPower)
        playerGun[loser] = 0                 # 총 반환
    nx, ny = x + dx[d], y + dy[d]
    playerExist = isPlayer(loser, [nx, ny])
    while not inRange(nx, ny) or playerExist >= 0:
        d = (d + 1) % 4
        nx, ny = x + dx[d], y + dy[d]
        playerExist = isPlayer(loser, [nx, ny])
    players[loser] = [nx, ny, d, s]
    isGun(loser, [nx, ny])

    # winner: 총 바꾸기
    isGun(winner, [x, y])

for i in range(n):                      # 총이 있는 경우 list로 조정
    for j in range(n):
        if grid[i][j] > 0: grid[i][j] = [grid[i][j]]
        else: grid[i][j] = []
for i in range(m):                      # player 좌표 값 조정
    players[i][0] -= 1
    players[i][1] -= 1

playerGun = [0] * m
points = [0] * m
for j in range(k):          # simulate
    for i in range(m):              # player마다
        pos = playerMove(i)         # 한 칸 이동
        fight = isPlayer(i, pos)    
        if fight >= 0: fighting(i, fight)       # 이동한 칸에 player가 있다면, fight
        else: isGun(i, pos)                     # 이동한 칸에 player가 없다면, 총 확인 후 있다면 획득
                          
print(*points)
'''
