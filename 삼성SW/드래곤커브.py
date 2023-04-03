# [B_G4] 드래곤 커브
# https://www.acmicpc.net/problem/15685
'''
드래곤 커브는 시작 점, 시작 방향, 세대의 요소로 이루어져 있으며 
K(K>1) 세대 드래곤커브는 K - 1세대 커브의 끝점을 기준으로 시계 방향으로 90도 회전시키며 만들 수 있다.
100 * 100 격자 위에 1 * 1 정사각형의 네 꼭짓점이 모두 드래곤 커브의 일부인 정사각형의 개수?
* 0 <= x, y(시작 점 좌표) <= 100
* d { 0: 오른쪽, 1: 위쪽, 2: 왼쪽, 3: 아래쪽}
* 0 <= g(세대) <= 10 
* 시간 제한 1초
* 메모리 제한 512MB
'''

### i. 

# 동, 북, 서, 남
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())
curves = [list(map(int, input().split())) for _ in range(n)]      # 좌표

grid = [list(False for _ in range(101)) for _ in range(101)]     
for x, y, d, g in curves:
  curveInfo = []
  # 0세대
  nx, ny = x + dx[d], y + dy[d]
  grid[y][x], grid[ny][nx] = True, True
  curveInfo.append(d)
  x, y = nx, ny
  for i in range(1, g + 1):      # k세대
    newCurveInfo = []
    for j in range(len(curveInfo) - 1, -1, -1):
      d = (curveInfo[j] + 1) % 4            # 시계 방향으로 90도 돌렸을 때 방향
      nx, ny = x + dx[d], y + dy[d]
      grid[ny][nx] = True
      newCurveInfo.append(d)
      x, y = nx, ny
    curveInfo.extend(newCurveInfo)

result = 0
for i in range(100):            # 격자 한 칸의 모든 꼭짓점 검사
  for j in range(100):
    if (grid[i][j] == True and grid[i + 1][j] == True and grid[i][j + 1] == True and grid[i + 1][j + 1]): result += 1

print(result)



### ii. 방향과 끝점 구하기 분리

# 동, 북, 서, 남
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())
curves = [list(map(int, input().split())) for _ in range(n)]      # 좌표

grid = [list(False for _ in range(101)) for _ in range(101)]     
for x, y, d, g in curves:
  curveInfo = []
  grid[y][x] = True
  curveInfo.append(d)
  for i in range(1, g + 1):      # k세대
    for j in range(len(curveInfo) - 1, -1, -1):
      curveInfo.append((curveInfo[j] + 1) % 4)            # 시계 방향으로 90도 돌렸을 때 방향
      
  for i in range(len(curveInfo)):
    nx, ny = x + dx[curveInfo[i]], y + dy[curveInfo[i]]
    grid[ny][nx] = True
    x, y = nx, ny
      
result = 0
for i in range(100):            # 격자 한 칸의 모든 꼭짓점 검사
  for j in range(100):
    if (grid[i][j] == True and grid[i + 1][j] == True and grid[i][j + 1] == True and grid[i + 1][j + 1]): result += 1

print(result)


'''
각 방향으로 커브를 만들 때 끝지점끼리 이으므로, 가장 최근에 그린 커브부터 이전것까지 당시에 그린 커브의 방향을 활용하면 다음의 규칙성 존재
- 이동할 방향 = (이전에 그린 커브의 방향 + 1) % 4
커브 방향과 그 지점을 따로 계산한 4ms 빠른 구현 코드: https://www.acmicpc.net/source/58462467
'''
