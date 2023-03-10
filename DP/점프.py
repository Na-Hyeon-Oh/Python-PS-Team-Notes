# [B_S1] 점프
# https://www.acmicpc.net/problem/1890
'''
N * N (4 <= N <= 100) 게임판에 현재 칸에서 갈 수 있는 거리인 수가 적혀 있고,
한 번 이동할 때는 오른쪽/아래쪽으로만 한 방향으로 이동해야 한다.
최좌측상단에서 최우측하단으로 이동할 수 있는 경로의 개수?
* 시간 제한 1초
* 메모리 제한 128MB
'''
# 1

import sys

def input():
  return sys.stdin.readline()

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1
for i in range(n * 2 - 2):
  for j in range(i + 1 if i < n else 2 * n - i - 1):
    nx = i - j if i < n else n - 1 - j
    ny = j if i < n else i - (n - 1) + j
    if dp[ny][nx] > 0:
      distance = board[nx][ny]
      if ny + distance < n: dp[ny + distance][nx] += dp[ny][nx]            # 아래
      if nx + distance < n: dp[ny][nx + distance] += dp[ny][nx]        # 오른쪽

print(dp[n - 1][n - 1])

# 2

import sys

def input():
  return sys.stdin.readline()

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1
for i in range(n):
  for j in range(n):
    if board[i][j] == 0 or dp[i][j] == 0: continue
    jump = board[i][j]
    if i + jump < n: dp[i + jump][j] += dp[i][j]
    if j + jump < n: dp[i][j + jump] += dp[i][j]

print(dp[-1][-1])

'''
# 1
- 오른쪽 아래로만 이동할 수 있으므로 너무 꼬아서 대각선을 이용하여야 한다고 생각함.
오른쪽 아래로 가면서 대각선 하나씩 검사하며 각 dp[i][j] 에 값이 있으면 해당 경로에서 갈 수 있는 다음 경로의 dp[a][b]에 dp[i][j] 값 추가

# 2 (

'''
