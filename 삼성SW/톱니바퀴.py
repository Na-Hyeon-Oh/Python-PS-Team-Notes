# [B_G5] 톱니바퀴
# https://www.acmicpc.net/problem/14890
'''
8개의 톱니를 가진 톱니바퀴 4개(1 <= K <= 100)를 총 K번 회전시키려고 할 때, 회전은 한 칸씩 이루어진다.
톱니의 한 칸에는 N(0), S극(1)이 써져 있고, "회전하기 전" 서로 맞닿은 극이 다르면 톱니바퀴는 서로 다른 방향으로 회전하고 같으면 회전하지 않는다. (1: 시계 방향, -1: 반시계 방향)
회전 결과에서 네 톱니바퀴의 점수의 합?
1. 1번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 1점
2. 2번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 2점
3. 3번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 4점
4. 4번 톱니바퀴의 12시방향이 N극이면 0점, S극이면 8점
* 시간 제한 2초
* 메모리 제한 512MB
'''

def rotateSide(current, dir, isLeft):      # 기존 톱니바퀴 기준 왼쪽/오른쪽으로 회전/x
  if isLeft:
    left = current - 1
    if left < 0: return
    else:
      isDifferent = array[current][(startIdx[current] + 6) % 8] != array[left][(startIdx[left] + 2) % 8]
      if isDifferent == True:
        rotateSide(left, (-1) * dir, True)
        startIdx[left] = (startIdx[left] + dir) % 8
  else:
    right = current + 1
    if right >= 4: return
    else:
      isDifferent = array[current][(startIdx[current] + 2) % 8] != array[right][(startIdx[right] + 6) % 8]
      if isDifferent == True:
        rotateSide(right, (-1) * dir, False)
        startIdx[right] = (startIdx[right] + dir) % 8
      

array = [list(input()) for _ in range(4)]
k = int(input())
rotations = list(list(map(int, input().split())) for _ in range(k))

startIdx = [0, 0, 0, 0]                      # 12시 방향 idx
for i in range(k):
  target = rotations[i][0] - 1
  rotateDir = rotations[i][1]
  rotateSide(target, rotateDir, True)        # 왼쪽 톱니바퀴
  rotateSide(target, rotateDir, False)       # 오른쪽 톱니바퀴
  startIdx[target] = (startIdx[target] - rotateDir) % 8
  
result = 0
if array[0][startIdx[0]] == '1': result += 1
if array[1][startIdx[1]] == '1': result += 2
if array[2][startIdx[2]] == '1': result += 4
if array[3][startIdx[3]] == '1': result += 8
print(result)
