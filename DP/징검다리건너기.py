# [B_S1] 징검다리 건너기
# https://www.acmicpc.net/problem/21317
'''
마지막 돌 사이의 산삼을 캐기 위해 돌과 돌 사이를 점프하면서 이동할 수 있는 방법은 3가지가 있다.
1. 현재 위치에서 다음 돌로 이동하는 작은 점프
2. 1개의 돌을 건너뛰어 이동하는 큰 점프
: 1, 2 점프의 경우 돌의 번호마다 소비 에너지가 다르다.
3. 2개의 돌을 건너뛰어 이동하는 매우 큰 점프 : 단 한 번 할 수 있는 점프로 점프를 하는 돌의 번호와 상관없이 k(<= 5,000)만큼의 에너지를 소비한다.
첫 번재 돌부터 출발할 때, 산삼을 얻기 위해 필요한 에너지의 최솟값?
* 1 <= N(돌의 개수) <= 20
* 시간 제한 1초
* 메모리 제한 1024MB
'''

# i. 

import sys

def input():
  return sys.stdin.readline()

n = int(input())
energy = [list(map(int, input().split())) for _ in range(n - 1)]
k = int(input())

result = 1e8
for target in range(n):
  dp = [0] * n          # dp[i]: i까지 소비되는 에너지의 최솟값과 가장 큰 점프 횟수
  for i in range(n - 1):
    if i == target and i + 3 < n: dp[i + 3] = min(dp[i + 3] if dp[i + 3] != 0 
 else 1e8, dp[i] + k)
    if i + 1 < n: dp[i + 1] = min(dp[i + 1] if dp[i + 1] != 0 
 else 1e8, dp[i] + energy[i][0])
    if i + 2 < n: dp[i + 2] = min(dp[i + 2] if dp[i + 2] != 0 
 else 1e8, dp[i] + energy[i][1])
  result = min(result, dp[n-1])

print(result)

# ii. 

import sys

def input():
  return sys.stdin.readline()

n = int(input())
energy = [list(map(int, input().split())) for _ in range(n - 1)]
k = int(input())

dp = [[1e8, 1e8] for _ in range(n)]          # dp[i]: [매우 큰 점프를 포함하지 않는 경우의 최솟값, 포함하는 경우의 최솟값]
dp[0][0] = 0
if n > 1: dp[1][0] = energy[0][0]
if n > 2: dp[2][0] = min(dp[1][0] + energy[1][0], energy[0][1])
for i in range(3, n):
  dp[i][0] = min(dp[i - 1][0] + energy[i - 1][0], dp[i - 2][0] + energy[i - 2][1])
  dp[i][1] = min(min(dp[i - 1][1] + energy[i - 1][0], dp[i - 2][1] + energy[i - 2][1]), dp[i - 3][0] + k)         # 이중 min() => 매우 큰 점프를 하는 경우는 한 번만 

print(min(dp[n - 1][0], dp[n - 1][1]))

'''
i. 가장 큰 점프를 할 위치를 미리 정하고 그 이후 작은 점프와 큰 점프를 채우는 방식
ii. 가장 큰 점프를 포함하는 경우와 포함하지 않는 경우의 에너지 최솟값을 계속 
'''
