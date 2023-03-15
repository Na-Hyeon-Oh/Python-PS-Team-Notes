# [B_S1] 구간 합 구하기 5
# https://www.acmicpc.net/problem/11660
'''
n * n (1 <= N <= 1,024) 크기의 표가 있을 때, (x1, y1)부터 (x2, y2)까지 합을 m번(1 <= M <= 100,000) 구하는 프로그램
* 시간 제한 1초
* 메모리 제한 256MB
'''

import sys

def input():
  return sys.stdin.readline()

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]
for i in range(n):
  rowSum = 0
  for j in range(n):
    rowSum += board[i][j]
    dp[i][j] = rowSum + (dp[i - 1][j] if i > 0 else 0)

for _ in range(m):
  x1, y1, x2, y2 = map(int, input().split())
  i1, j1, i2, j2 = x1 - 1, y1 - 1, x2 - 1, y2 - 1
  result = dp[i2][j2] - (dp[i1 - 1][j2] if i1 > 0 else 0) - (dp[i2][j1 - 1] if j1 > 0 else 0) + (dp[i1 - 1][j1 - 1] if i1 > 0 and j1 > 0 else 0)

  print(result)
