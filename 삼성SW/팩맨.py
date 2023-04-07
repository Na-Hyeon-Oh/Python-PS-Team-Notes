'''
[CT_G1] 팩맨
# 시뮬레이션, 완전 탐색 
'''

from copy import deepcopy

m, t = map(int, input().split())
packman = []                                                            # r, c
monsters = [[[] for _ in range(4)] for _ in range(4)]                   # r, c: [d]
killed = [[[] for _ in range(4)] for _ in range(4)]                     # r, c: [t]

# 상, 좌상, 좌, 좌하, 하, 우하, 우, 우상
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def initialize():
    r, c = map(int, input().split())
    packman.extend([r - 1, c - 1])         
    for i in range(m):
        r, c, d = map(int, input().split())
        monsters[r - 1][c - 1].append(d - 1)

def inRange(x, y):
    return x >= 0 and x < 4 and y >= 0 and y < 4

def isPackman(x, y):
    return [x, y] == packman

def isKilled(x, y):
    return len(killed[x][y]) > 0

def moveMonster():
    newMonsters = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            element = monsters[i][j]
            for k in range(len(element)):                                                           # 모든 몬스터에 대해
                r, c, d = i, j, element[k]
                for l in range(8):                                                                  # 각 방향별로
                    moveDir = (d + l) % 8
                    nr, nc = r + dx[moveDir], c + dy[moveDir]
                    if inRange(nr, nc) and not isPackman(nr, nc) and not isKilled(nr, nc):          # 몬스터 시체가 없고, 팩맨이 없고, 격자를 벗어나지 않을 때, 즉시 이동
                        r, c, d = nr, nc, moveDir
                        break
                newMonsters[r][c].append(d)
    return newMonsters

def movePackman():
    [r, c] = packman
    maxMonsterWay = [0, 0, 0]                                               # 각 한 칸의 이동 방향
    maxMonster = 0
    for i in range(4):                                                      # 몬스터를 최대로 먹을 수 있는 경로 탐색
        x1, y1 = r + dx[i * 2], c + dy[i * 2]
        if not inRange(x1, y1): continue
        eat1 = len(monsters[x1][y1])
        for j in range(4):
            x2, y2 = (x1 + dx[j * 2]) % 8, (y1 + dy[j * 2]) % 8
            if not inRange(x2, y2): continue     # 격자 밖의 경우
            eat2 = len(monsters[x2][y2]) if not (x1 == x2 and y1 == y2) else 0    # 지나온 경로이면 몬스터 추가하지 않기
            for k in range(4):
                x3, y3 = (x2 + dx[k * 2]) % 8, (y2 + dy[k * 2]) % 8
                if not inRange(x3, y3): continue
                eat3 = len(monsters[x3][y3]) if not ((x1 == x3 and y1 == y3) or (x2 == x3 and y2 == y3)) else 0                   
                if maxMonster < eat1 + eat2 + eat3:                         # 최대 몬스터 경로 update
                    maxMonsterWay = [i * 2, j * 2, k * 2]
                    maxMonster = eat1 + eat2 + eat3
    for move in range(3):                                                   # 3칸의 이동 중 몬스터 먹기
        r += dx[maxMonsterWay[move]]
        c += dy[maxMonsterWay[move]]                        
        killed[r][c].extend([2] * len(monsters[r][c]))                      # 시체 남기기
        monsters[r][c] = []                                                 
    packman[0], packman[1] = r, c                                           # 팩맨 최종 위치 update
        
def removeKilled():
    newKilled = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            element = killed[i][j]
            for k in range(len(element)):
                if element[k] > 0: newKilled[i][j].append(element[k] - 1)               # 1턴씩 빼기
    return newKilled                

def copyMonster(target):
    for i in range(4):
        for j in range(4):
            element = target[i][j]
            if len(element) > 0: monsters[i][j].extend(target[i][j])        # monster로 부화

def remainMonsters():
    result = 0
    for i in range(4):
        for j in range(4):
            result += len(monsters[i][j])
    return result

initialize()
for _ in range(t):                                   # simulate
    copiedMonster = deepcopy(monsters)               # 1. 몬스터 복제
    monsters = deepcopy(moveMonster())               # 2. 몬스터 이동
    movePackman()                                    # 3. 팩맨 이동
    killed = deepcopy(removeKilled())                # 4. 몬스터 시체 소멸
    copyMonster(copiedMonster)                       # 5. 몬스터 복제 완성: 1.에서 복제한 monster 다음 turn에 부화시키기

print(remainMonsters())
