# 마법사 상어와 블리자드
# https://www.acmicpc.net/problem/21611
'''
N * N 격자에서 마법사 상어가 ((N+1)/2, (N+1)/2)에 위치해 있고, 
d 방향으로 s 거리만큼 떨어진 곳에 얼음을 던질 때, d 방향의 거리 s 이하의 모든 칸의 구슬은 함께 파괴된다.
구슬이 한 번 파괴되고 나면 빈 칸을 채우기 위해 구슬이 번호가 더 작은 칸(상어 쪽)으로 이동한다.
이동 후에 4개 이상 연속하는 구슬(1, 2, 3; 0: 구슬이 없음)이 있으면 구슬이 폭파하고 이동하는 것을 반복한다.
더 이상 폭발할 구슬이 없을 때, 구슬은 변화하는데, 연속하는 구슬은 하나의 그룹이 되고 이는 (그룹에 들어있는 구슬의 개수, 그룹을 이루고 있는 구슬의 번호)로 바뀐다.
이는 M번 반복된다.
1 * (폭발한 1번 구슬의 개수) + 2 * (폭발한 2번 구슬의 개수) + 3 * (폭발한 3번 구슬의 개수)를 출력하라
* 3 <= N <= 49 (N: 홀수)
* 1 <= M <= 100
* 1 <= d <= 4, 1 <= s <= (N - 1) / 2
* 제한 시간 1초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

# 상, 하, 좌, 우
# 1, 2, 3, 4
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

n, m = map(int, input().split())
ground = [list(map(int, input().split())) for _ in range(n)]
blizard = [list(map(int, input().split())) for _ in range(m)]

explodedMarbles = [0, 0, 0]
shark = int((n + 1) / 2 - 1)
for attack in blizard:
  # attack
  nx = shark
  ny = shark
  for _ in range(attack[1]):
    nx += dx[attack[0] - 1]
    ny += dy[attack[0] - 1]
    ground[ny][nx] = 0
  # explode
  # ground를 작은 번호의 판부터 리스트로 만들기
  beforeExplode = [ground[shark][shark - 1], ground[shark + 1][shark - 1]]
  dir = 3  # 우, 상, 좌, 하
  nx = shark
  ny = shark + 1
  cnt = 0  # 같은 방향으로 구슬 list에 append하는 횟수
  lineCnt = 0  # 같은 개수와 방향을 갖는 구슬들 append 횟수
  cntChangePoint = 2  # 같은 방향을 갖는 구슬들 append해야 하는 횟수
  while True:
    beforeExplode.append(ground[ny][nx])
    cnt += 1
    if cnt == cntChangePoint:
      if dir == 3: dir = 0
      elif dir == 0: dir = 2
      elif dir == 2: dir = 1
      elif dir == 1: dir = 3
      cnt = 0
      lineCnt += 1
      if cntChangePoint == n - 1:
        if lineCnt == 3: break
      elif lineCnt == 2:
        cntChangePoint += 1
        lineCnt = 0
    nx = nx + dx[dir]
    ny = ny + dy[dir]
  while 0 in beforeExplode:
    beforeExplode.remove(0)  # 0 제거 -> 구슬을 작은 번호로 밀기
  afterExplode = []
  while True:
    type = 0  # 구슬 타입
    cnt = 0  # 연속 구슬 개수
    for marbleIdx in range(len(beforeExplode)):
      if type != 0 and type != beforeExplode[marbleIdx]:
        if cnt < 4: afterExplode.extend([type for _ in range(cnt)])
        else: explodedMarbles[type - 1] += cnt
        cnt = 0
      type = beforeExplode[marbleIdx]    
      cnt += 1
      if marbleIdx == len(beforeExplode) - 1:
        if cnt < 4: afterExplode.extend([type for _ in range(cnt)])
        else: explodedMarbles[type - 1] += cnt
    if len(beforeExplode) == len(afterExplode.copy()): break
    beforeExplode = afterExplode.copy()
    afterExplode = []
  # change
  changed = []
  type = 0
  cnt = 0
  for marbleIdx in range(len(afterExplode)):
    if type != 0 and type != afterExplode[marbleIdx]:
      changed.extend([cnt, type])
      cnt = 0
    type = afterExplode[marbleIdx]
    cnt += 1
    if marbleIdx == len(afterExplode) - 1: changed.extend([cnt, type])
  # marking result on ground
  changed.extend([0 for _ in range(n * n - 1 - len(changed))])
  ground[shark][shark - 1] = changed.pop(0)
  ground[shark + 1][shark - 1] = changed.pop(0)
  dir = 3
  nx = shark
  ny = shark + 1
  cnt = 0
  lineCnt = 0
  cntChangePoint = 2
  while changed:
    ground[ny][nx] = changed.pop(0)
    cnt += 1
    if cnt == cntChangePoint:
      if dir == 3: dir = 0
      elif dir == 0: dir = 2
      elif dir == 2: dir = 1
      elif dir == 1: dir = 3
      cnt = 0
      lineCnt += 1
      if cntChangePoint == n - 1:
        if lineCnt == 3: break
      elif lineCnt == 2:
        cntChangePoint += 1
        lineCnt = 0
    nx = nx + dx[dir]
    ny = ny + dy[dir]
    
print(explodedMarbles[0] + 2 * explodedMarbles[1] + 3 * explodedMarbles[2])


''' 
explode를 위한 list를 만드는 것과 ground에 다시 저장(mark)하는 것은 같은 알고리즘을 사용한다.
- function을 사용하면 더 간단 + 2차원 배열과 1차원 배열 간 dictionary 생성 (ref. # https://kimjingo.tistory.com/171)
'''
