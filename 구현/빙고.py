# 빙고
# https://www.acmicpc.net/problem/2578
'''
5 * 5 빙고 게임으로 사회자가 몇 번째 숫자를 외칠 때, 빙고(3개 이상)가 나오는가?
* 제한 시간 1초
'''

import sys

def input():
  return sys.stdin.readline().rstrip()

bingopan = [list(map(int, input().split())) for _ in range(5)]
bingopanList = []
calls = []
for i in range(5): 
  bingopanList += bingopan[i]
  calls += list(map(int, input().split()))

for callIdx in range(len(calls)):
  for i in range(len(bingopanList)):
    if bingopanList[i] == calls[callIdx]: 
      bingopanList[i] = -1
      break
  # check
  bingo = 0
  checkTopLeftDiagonal = 0
  checkTopRightDiagonal = 0
  for row in range(5):
    checkRow = 0
    checkCol = 0
    for col in range(5):
      if bingopanList[row * 5 + col] == -1: checkRow += 1
      if bingopanList[col * 5 + row] == -1: checkCol += 1
      if row == col and bingopanList[row * 5 + col] == -1: checkTopLeftDiagonal += 1
      if row + col == 4 and bingopanList[row * 5 + col] == -1: checkTopRightDiagonal += 1
    if checkRow == 5: bingo += 1
    if checkCol == 5: bingo += 1
  if checkTopLeftDiagonal == 5: bingo += 1
  if checkTopRightDiagonal == 5: bingo += 1
  if bingo >= 3: 
    print(callIdx + 1)
    break

'''
- 빙고판의 크기가 정해져있으므로, 한 row가 완성될 때, 한 col이 완성될 때, 각 대각선 (2개)가 완성되었는지를 확인하는 코드를 for문으로 작성할 수 있다.
- 이 때 2차원 배열을 사용할 수도 있지만, 1차원 배열을 index의 특성을 활용하였다.
'''
