# [B_G4] 주사위 굴리기
# https://www.acmicpc.net/problem/14499
'''
N * M(1 <= N, M <= 20) 지도의 각 칸에는 정수(0~9)가 하나씩 쓰여져 있다.
주사위를 굴렸을 때, 이동한 칸에 쓰여있는 수가 0이면, 주사위의 바닥면에 쓰여 있는 수가 칸에 복사되고, 0이 아닌 경우에는 칸에 쓰여 있는 수가 주사위의 바닥면으로 복사되면서 칸에 쓰여 있는 수는 0이 된다.
주사위를 놓은 곳의 좌표(0 <= x <= N-1, 0 <= y <= M-1)와 이동시키는 명령(1 <= K(명령의 개수) <= 1,000; 동쪽 1, 서쪽 2, 북쪽 3, 남쪽 4)이 주어졌을 때, 주사위가 이동했을 때마다 상단에 쓰여 있는 값을 구하는 프로그램을 작성하시오.
* 주사위의 전개도는 다음과 같고 윗면이 1이고 동쪽을 바라보는 방향이 3인 상태로 놓여져 있다.
  2
4 1 3
  5
  6
가장 처음에는 모든 면에 0이 적혀 있다.
* 만약 주사위가 지도의 바깥으로 이동하려 한다면 해당 명령을 무시한다.
* 시간 제한 2초
* 메모리 제한 512MB
'''

# 동, 서, 북, 남
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 주사위
dice = dict()
dice[1] = [4, 3, 5, 2]              # 동, 서, 북, 남 방향으로 이동했을 때 다음 상단 idx
diceNumber = [0, 0, 0, 0, 0, 0]     # 주사위 각 idx의 값
currentTop = 1

n, m, x, y, k = map(int, input().split())
mapNumber = [list(map(int, input().split())) for _ in range(n)]
moves = list(map(int, input().split()))

for move in moves:
  x += dx[move - 1] 
  y += dy[move - 1]
  if x < 0 or x >= n or y < 0 or y >= m:       # 주사위가 바깥으로 이동하려 하는 경우
    x -= dx[move - 1] 
    y -= dy[move - 1]
    continue
  # 주사위 상단 변화
  pastTop = currentTop
  currentTop = dice[currentTop][move - 1]
  currentDiceInfo = [0, 0, 0, 0]
  match move:
    case 1:
      currentDiceInfo[1] = pastTop
      currentDiceInfo[0] = 7 - pastTop
      currentDiceInfo[2] = dice[pastTop][2]
      currentDiceInfo[3] = dice[pastTop][3]
    case 2:
      currentDiceInfo[0] = pastTop
      currentDiceInfo[1] = 7 - pastTop
      currentDiceInfo[2] = dice[pastTop][2]
      currentDiceInfo[3] = dice[pastTop][3]
    case 3:
      currentDiceInfo[3] = pastTop
      currentDiceInfo[2] = 7 - pastTop
      currentDiceInfo[0] = dice[pastTop][0]
      currentDiceInfo[1] = dice[pastTop][1]
    case 4:
      currentDiceInfo[2] = pastTop
      currentDiceInfo[3] = 7 - pastTop
      currentDiceInfo[0] = dice[pastTop][0]
      currentDiceInfo[1] = dice[pastTop][1]
  dice[currentTop] = currentDiceInfo
  # 주사위 하단 변화
  if mapNumber[x][y] != 0: 
    diceNumber[6 - currentTop] = mapNumber[x][y]
    mapNumber[x][y] = 0
  else: mapNumber[x][y] = diceNumber[6 - currentTop]
    
  print(diceNumber[currentTop - 1])

'''
<구현, 시뮬레이션>
어떤 idx의 주사위 면이 상단에 있을 때 동서남북으로 굴리면 다음 상단에 올 주사위 면 idx는 무엇일지를 dictionary로 저장하고,
주사위 각 면의 숫자는 list에 저장하여,
다음 상단에 있는 주사위 숫자를 쉽게 계산할 수 있도록 하였다.

* 다른 코드 참고: https://www.acmicpc.net/source/58216385
'''
