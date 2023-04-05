'''
[CT_G1] 술래 잡기
# 시뮬레이션
'''

from copy import deepcopy

global n, m, h, chaser, runners, runnerCoors
n, m, h, k = map(int, input().split())
chaser = [n // 2 + 1, n // 2 + 1, 0, True, 1, 0, 0]
runners = [[*(map(int, input().split())), 0] for _ in range(m)]
runnerCoors = [[runner[0], runner[1]] for runner in runners]
trees = [list(map(int, input().split())) for _ in range(h)]

# 우, 좌, 하, 상
dx = [[0, 0], [1, -1]]
dy = [[1, -1], [0, 0]]
# 상, 우, 하, 좌 (술래 기준)
cx = [-1, 0, 1, 0]
cy = [0, 1, 0, -1]

def inRange(x, y):
    return x > 0 and x <= n and y > 0 and y <= n

def convertToCoor(x, y):
    return x - 1, y - 1

def distance(runnerIdx):
    return abs(chaser[0] - runners[runnerIdx][0]) + abs(chaser[1] - runners[runnerIdx][1])

def runnerMove():
    global runners
    for i in range(len(runners)):
        if distance(i) <= 3:
            [x, y, dType, d] = runners[i]
            nx, ny = x + dx[dType - 1][d], y + dy[dType - 1][d]                 # 바라보고 있는 방향으로 1칸 이동한 좌표
            if inRange(nx, ny):                                                 # 격자를 벗어나지 않는 경우,
                if nx != chaser[0] or ny != chaser[1]: x, y = nx, ny            # 술래가 없는 경우에만 1칸 이동
            else:                                                               # 격자를 벗어나는 경우,
                d = (d + 1) % 2                                                 # 방향 틀기
                nx, ny = x + dx[dType - 1][d], y + dy[dType - 1][d]
                if nx != chaser[0] or ny != chaser[1]: x, y = nx, ny
            runners[i] = [x, y, dType, d]

lineCnts = [2] * (n - 2)
lineCnts.append(3)
def chaserMove():
    global n, chaser
    [x, y, d, isOuter, idx, cnt, lineCnt] = chaser
    x, y = x + cx[d], y + cy[d]
    cnt += 1
    if idx == cnt:
        if isOuter: d = (d + 1) % 4
        else: d = (d - 1) % 4
        cnt = 0 
        lineCnt += 1
    if x == 1 and y == 1: 
        isOuter, d = False, 2
        lineCnt = 0
    elif x == n // 2 + 1 and y == n // 2 + 1:
        isOuter, d = True, 0
        lineCnt = 0
    elif lineCnt == lineCnts[idx - 1]:
        idx = idx + 1 if isOuter else idx - 1
        lineCnt = 0
    chaser = [x, y, d, isOuter, idx, cnt, lineCnt]

def catch():
    global h, runners
    result = 0
    x, y, d = chaser[0], chaser[1], chaser[2]
    for _ in range(3):                 # 술래 시야(본인 포함 3칸)
        canHide = False
        for tree in trees:             # 나무로 숨기가 가능한지
            if x == tree[0] and y == tree[1]:
                canHide = True
                break
        if not canHide:                 # 불가능하면 술래잡기
            tmpRunners = deepcopy(runners)
            cnt = 0
            for j in range(len(tmpRunners)):
                if x == tmpRunners[j][0] and y == tmpRunners[j][1]: 
                    result += 1
                    runners.pop(j - cnt)
                    cnt += 1
        x, y = x + cx[d], y + cy[d]
    return result

score = 0
for t in range(1, k + 1):               # simulate
    runnerMove()                        # 도망자 turn
    chaserMove()                        # 술래 turn
    targets = catch()
    score += t * targets 
    
print(score)
